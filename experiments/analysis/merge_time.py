import os
import pandas as pd
from pathlib import Path

RESULTDIR="analysis_results"
DATADIR="data"

filepath = os.path.abspath(__file__)
root = Path(filepath).parents[1] # 0524
data = root / DATADIR
analysis = Path(filepath).parent # 0830
resultDir = analysis / RESULTDIR
node_path = '/home/fabing/projects/kubernetes-scheduler-simulator/data/csv/openb_node_list_all_node.csv'


def exit_and_save_to_csv(dflist):
    dfo = pd.concat(dflist)
    resultDir.mkdir(exist_ok=True)
    csvfile = resultDir / 'analysis_time_discrete.csv'
    dfo.to_csv(csvfile)
    print("%d rows saved to: %s" % (len(dfo), csvfile))
    exit()

def calculate_total_capcity(nodes_path, price_path):
    price_df = pd.read_csv(price_path)
    cpu = 0
    mem = 0
    used_nodes = 0
    with open(nodes_path, 'r') as f:
        line = f.readline()
        line = line.replace(r'\n', '')
        line = line.split(r',')
        for sn in line:
            sn = sn.strip()
            try:
                cpu_cost = price_df.loc[price_df['sn'] == sn, 'cpu_milli']
                mem_cost = price_df.loc[price_df['sn'] == sn, 'memory_mib']
                cpu += cpu_cost.values[0]
                mem += mem_cost.values[0]
                used_nodes += 1
            except IndexError:
                print(f"No match found for sn: {sn}")
    return cpu, mem, used_nodes

fileDirs = sorted([x for x in data.iterdir() if x.is_dir()])
dflist = []
for fdir in fileDirs:
    policyDirs = sorted([x for x in fdir.iterdir() if x.is_dir()])
    for pdir in policyDirs:            
        tuneDirs = sorted([x for x in pdir.iterdir() if x.is_dir()])
        for tdir in tuneDirs:
            seedDirs = sorted([x for x in tdir.iterdir() if x.is_dir()])
            avg_cpu = []
            avg_mem = []
            avg_used_nodes = []
            all_real = []
            for sdir in seedDirs:
                afile = fdir / pdir / tdir / sdir / 'analysis_price.csv'
                bfile = fdir / pdir / tdir / sdir / 'analysis_time.csv'
                print(afile)
                if not afile.is_file():
                    continue
                try:
                    cpu, mem, un = calculate_total_capcity(afile, node_path)
                    avg_cpu.append(cpu)
                    avg_mem.append(mem)
                    avg_used_nodes.append(un)
                    all_real.append(bfile)
                except Exception as e:
                    exit("ERROR file: %s\n%s" % (afile, e))
            dfn = dict()
            dfn['workload'] = fdir.name
            dfn['sc_policy'] = pdir.name
            dfn['tune'] = tdir.name
            dfn['cpu'] = sum(avg_cpu) / len(avg_cpu)
            dfn['mem'] = sum(avg_mem) / len(avg_mem)
            dfn['used_nodes'] = sum(avg_used_nodes) / len(avg_used_nodes)
            dfn['real'] = all_real
            dfo = pd.DataFrame(dfn, index=[len(dflist)]).set_index(["workload", "sc_policy", "tune"])
            dflist.append(dfo)
            

exit_and_save_to_csv(dflist)