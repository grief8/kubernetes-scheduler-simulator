import sys
import yaml
import pandas as pd
from pathlib import Path


OUTPUT_DIR_DEFAULT =  '/home/fabing/projects/kubernetes-scheduler-simulator/data/node_yaml'
MILLI = 1000


def generate_pod_yaml(workload_name='paib-pod-10',
                      limits={'cpu': '6000m'}):
    pod_template = """
    apiVersion: v1
    kind: Node
    metadata:
        labels:
            alibabacloud.com/gpu-card-model: P100
            beta.kubernetes.io/os: linux
            kubernetes.io/hostname: openb-node-0000
            kubernetes.io/os: linux
        name: openb-node-0000
    status:
        allocatable:
            alibabacloud.com/gpu-count: '2'
            alibabacloud.com/gpu-milli: '2000'
            cpu: 64000m
            memory: 262144Mi
            pods: '1001'
        capacity:
            alibabacloud.com/gpu-count: '2'
            alibabacloud.com/gpu-milli: '2000'
            cpu: 64000m
            memory: 262144Mi
            pods: '1001'
    """
    workload_yaml = yaml.safe_load(pod_template)
    workload_yaml['metadata']['name'] = workload_name
    workload_yaml['metadata']['labels']['kubernetes.io/hostname'] = workload_name
    workload_yaml['status']['allocatable']['cpu'] = limits['cpu']
    workload_yaml['status']['capacity']['cpu'] = limits['cpu']
    workload_yaml['status']['allocatable']['memory'] = limits['memory']
    workload_yaml['status']['capacity']['memory'] = limits['memory']

    return workload_yaml


def output_pod(dfp, outfile='pod.yaml', node_select=False):
    num_pod = len(dfp)
    for index, row in dfp.iterrows():
        if 'sn' in row: 
            workload_name = row['sn']
        elif 'job_id' in row:
            workload_name = f"job-{row['job_id']:04}" # float is not allowed
        else:
            exit("neither sn nor job_id in row")
           
        container_requests = {}
        if 'cpu_milli' in row:
            if row['cpu_milli'] < 80000:
                continue
            container_requests['cpu'] = "%dm" % (row['cpu_milli'])
        elif 'cpu' in row:
            container_requests['cpu'] = "%dm" % (row['cpu'] * MILLI)
        elif 'num_cpu' in row:
            container_requests['num_cpu'] = "%dm" % (row['num_cpu'] * MILLI)
        else:
            exit("neither cpu_milli nor cpu in row")
        if 'memory_mib' in row:
            if row['memory_mib'] < 300000:
                continue
            container_requests['memory'] = "%dMi" % row['memory_mib']
        container_limits = container_requests.copy()
        
        pod_yaml = generate_pod_yaml(workload_name=workload_name, limits=container_limits)

        if index == 0:
            with open(outfile, 'w') as file:
                yaml.dump(pod_yaml, file)
        else:
            with open(outfile, 'a') as file:
                file.writelines(['\n---\n\n'])
                yaml.dump(pod_yaml, file)
                
                
if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(0)
    pod_csv_file = Path(sys.argv[1])
    if not pod_csv_file.exists():
        exit(f"CSV File: {pod_csv_file} does not exist")
    
    dfp = pd.read_csv(pod_csv_file, dtype={'gpu_index': str})
    if 'gpu_spec' in dfp:
        dfp.gpu_spec = dfp.gpu_spec.fillna('')
    
    output_dir = pod_csv_file.stem # .csv to ""
    if len(output_dir) <= 0:
        output_dir_path = Path(OUTPUT_DIR_DEFAULT)
    else:
        output_dir_path = Path(output_dir)
    output_dir_path.mkdir(exist_ok=True)

    pod_yaml_file = output_dir_path / (pod_csv_file.stem + '.yaml') # .csv to .yaml
    output_pod(dfp, pod_yaml_file, node_select=False)
    print("OUTPUT: %s (len: %d)" % (pod_yaml_file, len(dfp)))

