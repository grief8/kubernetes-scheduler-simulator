# 
# Usage: python3 generate_run_scripts.py > run_scripts.sh


DATE = "2023_uniform" # Used as the folder name under experiments/ to hold all log results. To avoid collision of repeated experiments, may change date or append _v1, _v2, etc.
REMARK = "Artifacts"
REPEAT = 1 # Number of repetitive experiments.
FILELIST = [
    "data/fabing_uniform_050_1_1", "data/fabing_uniform_050_2_1", "data/fabing_uniform_050_2_2", "data/fabing_uniform_050_3_1", "data/fabing_uniform_050_3_2",
    "data/fabing_uniform_050_3_3", "data/fabing_uniform_050_5_1", "data/fabing_uniform_050_5_2", "data/fabing_uniform_050_5_3", "data/fabing_uniform_050_5_4",
    "data/fabing_uniform_050_5_5", "data/fabing_uniform_050_10_1", "data/fabing_uniform_050_10_2", "data/fabing_uniform_050_10_3", "data/fabing_uniform_050_10_4",
    "data/fabing_uniform_050_10_5", "data/fabing_uniform_050_10_6", "data/fabing_uniform_050_10_7", "data/fabing_uniform_050_10_8", "data/fabing_uniform_050_10_9",
    "data/fabing_uniform_050_10_10", "data/fabing_uniform_050_15_1", "data/fabing_uniform_050_15_2", "data/fabing_uniform_050_15_3", "data/fabing_uniform_050_15_4",
    "data/fabing_uniform_050_15_5", "data/fabing_uniform_050_15_6", "data/fabing_uniform_050_15_7", "data/fabing_uniform_050_15_8", "data/fabing_uniform_050_15_9",
    "data/fabing_uniform_050_15_10", "data/fabing_uniform_050_15_11", "data/fabing_uniform_050_15_12", "data/fabing_uniform_050_15_13", "data/fabing_uniform_050_15_14",
    "data/fabing_uniform_050_15_15", "data/fabing_uniform_050_20_1", "data/fabing_uniform_050_20_2", "data/fabing_uniform_050_20_3", "data/fabing_uniform_050_20_4",
    "data/fabing_uniform_050_20_5", "data/fabing_uniform_050_20_6", "data/fabing_uniform_050_20_7", "data/fabing_uniform_050_20_8", "data/fabing_uniform_050_20_9",
    "data/fabing_uniform_050_20_10", "data/fabing_uniform_050_20_11", "data/fabing_uniform_050_20_12", "data/fabing_uniform_050_20_13", "data/fabing_uniform_050_20_14",
    "data/fabing_uniform_050_20_15", 
    "data/fabing_uniform_100_1_1", "data/fabing_uniform_100_2_1", "data/fabing_uniform_100_2_2", "data/fabing_uniform_100_3_1",
    "data/fabing_uniform_100_3_2", "data/fabing_uniform_100_3_3", "data/fabing_uniform_100_5_1", "data/fabing_uniform_100_5_2", "data/fabing_uniform_100_5_3",
    "data/fabing_uniform_100_5_4", "data/fabing_uniform_100_5_5", "data/fabing_uniform_100_10_1", "data/fabing_uniform_100_10_2", "data/fabing_uniform_100_10_3",
    "data/fabing_uniform_100_10_4", "data/fabing_uniform_100_10_5", "data/fabing_uniform_100_10_6", "data/fabing_uniform_100_10_7", "data/fabing_uniform_100_10_8",
    "data/fabing_uniform_100_10_9", "data/fabing_uniform_100_10_10", "data/fabing_uniform_100_15_1", "data/fabing_uniform_100_15_2", "data/fabing_uniform_100_15_3",
    "data/fabing_uniform_100_15_4", "data/fabing_uniform_100_15_5", "data/fabing_uniform_100_15_6", "data/fabing_uniform_100_15_7", "data/fabing_uniform_100_15_8",
    "data/fabing_uniform_100_15_9", "data/fabing_uniform_100_15_10", "data/fabing_uniform_100_15_11", "data/fabing_uniform_100_15_12", "data/fabing_uniform_100_15_13",
    "data/fabing_uniform_100_15_14", "data/fabing_uniform_100_15_15", "data/fabing_uniform_100_20_1", "data/fabing_uniform_100_20_2", "data/fabing_uniform_100_20_3",
    "data/fabing_uniform_100_20_4", "data/fabing_uniform_100_20_5", "data/fabing_uniform_100_20_6", "data/fabing_uniform_100_20_7", "data/fabing_uniform_100_20_8",
    "data/fabing_uniform_100_20_9", "data/fabing_uniform_100_20_10", "data/fabing_uniform_100_20_11", "data/fabing_uniform_100_20_12", "data/fabing_uniform_100_20_13",
    "data/fabing_uniform_100_20_14", "data/fabing_uniform_100_20_15", "data/fabing_uniform_100_20_16", "data/fabing_uniform_100_20_17", "data/fabing_uniform_100_20_18",
    "data/fabing_uniform_100_20_19", "data/fabing_uniform_100_20_20", 
    "data/fabing_uniform_200_1_1", "data/fabing_uniform_200_2_1", "data/fabing_uniform_200_2_2",
    "data/fabing_uniform_200_3_1", "data/fabing_uniform_200_3_2", "data/fabing_uniform_200_3_3", "data/fabing_uniform_200_5_1", "data/fabing_uniform_200_5_2",
    "data/fabing_uniform_200_5_3", "data/fabing_uniform_200_5_4", "data/fabing_uniform_200_5_5", "data/fabing_uniform_200_10_1", "data/fabing_uniform_200_10_2",
    "data/fabing_uniform_200_10_3", "data/fabing_uniform_200_10_4", "data/fabing_uniform_200_10_5", "data/fabing_uniform_200_10_6", "data/fabing_uniform_200_10_7",
    "data/fabing_uniform_200_10_8", "data/fabing_uniform_200_10_9", "data/fabing_uniform_200_10_10", "data/fabing_uniform_200_15_1", "data/fabing_uniform_200_15_2",
    "data/fabing_uniform_200_15_3", "data/fabing_uniform_200_15_4", "data/fabing_uniform_200_15_5", "data/fabing_uniform_200_15_6", "data/fabing_uniform_200_15_7",
    "data/fabing_uniform_200_15_8", "data/fabing_uniform_200_15_9", "data/fabing_uniform_200_15_10", "data/fabing_uniform_200_15_11", "data/fabing_uniform_200_15_12",
    "data/fabing_uniform_200_15_13", "data/fabing_uniform_200_15_14", "data/fabing_uniform_200_15_15", "data/fabing_uniform_200_20_1", "data/fabing_uniform_200_20_2",
    "data/fabing_uniform_200_20_3", "data/fabing_uniform_200_20_4", "data/fabing_uniform_200_20_5", "data/fabing_uniform_200_20_6", "data/fabing_uniform_200_20_7",
    "data/fabing_uniform_200_20_8", "data/fabing_uniform_200_20_9", "data/fabing_uniform_200_20_10", "data/fabing_uniform_200_20_11", "data/fabing_uniform_200_20_12",
    "data/fabing_uniform_200_20_13", "data/fabing_uniform_200_20_14", "data/fabing_uniform_200_20_15", "data/fabing_uniform_200_20_16", "data/fabing_uniform_200_20_17",
    "data/fabing_uniform_200_20_18", "data/fabing_uniform_200_20_19", "data/fabing_uniform_200_20_20", 
    "data/fabing_uniform_250_1_1", "data/fabing_uniform_250_2_1",
    "data/fabing_uniform_250_2_2", "data/fabing_uniform_250_3_1", "data/fabing_uniform_250_3_2", "data/fabing_uniform_250_3_3", "data/fabing_uniform_250_5_1",
    "data/fabing_uniform_250_5_2", "data/fabing_uniform_250_5_3", "data/fabing_uniform_250_5_4", "data/fabing_uniform_250_5_5", "data/fabing_uniform_250_10_1",
    "data/fabing_uniform_250_10_2", "data/fabing_uniform_250_10_3", "data/fabing_uniform_250_10_4", "data/fabing_uniform_250_10_5", "data/fabing_uniform_250_10_6",
    "data/fabing_uniform_250_10_7", "data/fabing_uniform_250_10_8", "data/fabing_uniform_250_10_9", "data/fabing_uniform_250_10_10", "data/fabing_uniform_250_15_1",
    "data/fabing_uniform_250_15_2", "data/fabing_uniform_250_15_3", "data/fabing_uniform_250_15_4", "data/fabing_uniform_250_15_5", "data/fabing_uniform_250_15_6",
    "data/fabing_uniform_250_15_7", "data/fabing_uniform_250_15_8", "data/fabing_uniform_250_15_9", "data/fabing_uniform_250_15_10", "data/fabing_uniform_250_15_11",
    "data/fabing_uniform_250_15_12", "data/fabing_uniform_250_15_13", "data/fabing_uniform_250_15_14", "data/fabing_uniform_250_15_15", "data/fabing_uniform_250_20_1",
    "data/fabing_uniform_250_20_2", "data/fabing_uniform_250_20_3", "data/fabing_uniform_250_20_4", "data/fabing_uniform_250_20_5", "data/fabing_uniform_250_20_6",
    "data/fabing_uniform_250_20_7", "data/fabing_uniform_250_20_8", "data/fabing_uniform_250_20_9", "data/fabing_uniform_250_20_10", "data/fabing_uniform_250_20_11",
    "data/fabing_uniform_250_20_12", "data/fabing_uniform_250_20_13", "data/fabing_uniform_250_20_14", "data/fabing_uniform_250_20_15", "data/fabing_uniform_250_20_16",
    "data/fabing_uniform_250_20_17", "data/fabing_uniform_250_20_18", "data/fabing_uniform_250_20_19", "data/fabing_uniform_250_20_20", 
    "data/fabing_uniform_300_1_1",
    "data/fabing_uniform_300_2_1", "data/fabing_uniform_300_2_2", "data/fabing_uniform_300_3_1", "data/fabing_uniform_300_3_2", "data/fabing_uniform_300_3_3",
    "data/fabing_uniform_300_5_1", "data/fabing_uniform_300_5_2", "data/fabing_uniform_300_5_3", "data/fabing_uniform_300_5_4", "data/fabing_uniform_300_5_5",
    "data/fabing_uniform_300_10_1", "data/fabing_uniform_300_10_2", "data/fabing_uniform_300_10_3", "data/fabing_uniform_300_10_4", "data/fabing_uniform_300_10_5",
    "data/fabing_uniform_300_10_6", "data/fabing_uniform_300_10_7", "data/fabing_uniform_300_10_8", "data/fabing_uniform_300_10_9", "data/fabing_uniform_300_10_10",
    "data/fabing_uniform_300_15_1", "data/fabing_uniform_300_15_2", "data/fabing_uniform_300_15_3", "data/fabing_uniform_300_15_4", "data/fabing_uniform_300_15_5",
    "data/fabing_uniform_300_15_6", "data/fabing_uniform_300_15_7", "data/fabing_uniform_300_15_8", "data/fabing_uniform_300_15_9", "data/fabing_uniform_300_15_10",
    "data/fabing_uniform_300_15_11", "data/fabing_uniform_300_15_12", "data/fabing_uniform_300_15_13", "data/fabing_uniform_300_15_14", "data/fabing_uniform_300_15_15",
    "data/fabing_uniform_300_20_1", "data/fabing_uniform_300_20_2", "data/fabing_uniform_300_20_3", "data/fabing_uniform_300_20_4", "data/fabing_uniform_300_20_5",
    "data/fabing_uniform_300_20_6", "data/fabing_uniform_300_20_7", "data/fabing_uniform_300_20_8", "data/fabing_uniform_300_20_9", "data/fabing_uniform_300_20_10",
    "data/fabing_uniform_300_20_11", "data/fabing_uniform_300_20_12", "data/fabing_uniform_300_20_13", "data/fabing_uniform_300_20_14", "data/fabing_uniform_300_20_15",
    "data/fabing_uniform_300_20_16", "data/fabing_uniform_300_20_17", "data/fabing_uniform_300_20_18", "data/fabing_uniform_300_20_19", "data/fabing_uniform_300_20_20"
]


AllMethodList = [
    ["05", "BestFit", "<none>", "<none>", "<none>"]
]

AllMethodDict = {}
for item in AllMethodList:
    AllMethodDict[item[0]] = item

#####################################################################
#####################################################################
#####################################################################

MethodList = AllMethodList.copy()

MethodList = [
    ["05", "BestFit", "<none>", "<none>", "<none>"]
]

def get_dir_name_from_method(method_input):
    if len(method_input) != 5:
        print("[ERROR] get_dir_name_from_method: len(method) == 5, including id, policy, gsm, dem, nm")
        return "default_name"
    id, policy, gsm, dem, nm = method_input
    gsm = policy if gsm == "<self>" else gsm # no need to adjust, except that <self> is not allowed in bash. generate_config_and_run will recover the policy's full name
    dir_name = "%s-%s" % (id, policy)
    suffix = ""
    suffix += '_%s' % gsm if gsm != "<none>" else ''
    suffix += '_%s' % dem if dem != "<none>" else ''
    suffix += '_%s' % nm if nm != "<none>" else ''
    return dir_name # + suffix

def get_method_from_policy_id_list(id_list):
    if type(id_list) == list:
        return [AllMethodDict.get("%02d" % id, None) if type(id)==int else AllMethodDict.get("%s" % id, None) for id in id_list]
    else:
        return [AllMethodDict.get("%02d" % id_list, None) if type(id)==int else AllMethodDict.get("%s" % id_list, None)]

def get_dir_name_from_policy_id_list(id_list):
    return [get_dir_name_from_method(x) for x in get_method_from_policy_id_list(id_list)]

###########################################################
###########################################################
###########################################################

def generate_run_scripts(asyncc=True, parallel=16):
    DateAndRemark = DATE + "-" + REMARK.replace(' ', "_").replace('(',"_").replace(')',"_")
    numJobs=0
    if asyncc:
        print('#!/bin/bash\n# screen -dmS sim-%s bash -c "bash run_scripts_%s.sh"\n' % (DateAndRemark, DATE[-4:]))
    else:
        print('#!/bin/bash\n# cat run_scripts_%s.sh | while read i; do printf "%%q\\n" "$i"; done | xargs --max-procs=16 -I CMD bash -c CMD\n' % (DATE[-4:]))
    for tune_ratio in [1.3]:
        tune_seed_end = 42 + REPEAT if REPEAT >= 1 else 43
        for tune_seed in range(42, tune_seed_end, 1):
            for file in FILELIST:
                filename = file.split('/')[-1]
                for id, policy, gsm, dem, nm in MethodList:  # GpuSelMethod, DimExtMethod, NormMethod
                    dir_name = get_dir_name_from_method([id, policy, gsm, dem, nm])
                    gsm = policy if gsm == "<self>" else gsm
                    OUTPUT_YAML = False
                    SHUFFLE_POD = False
                    outstr = "# %s, %s, %s, %s, %s @ %s\n" % (id, policy, gsm, dem, nm, filename)
                    outstr += 'EXPDIR="experiments/%s/%s/%s/%s/%s' % (DATE, filename, dir_name, tune_ratio, tune_seed)
                    outstr += '" && mkdir -p ${EXPDIR} && touch "${EXPDIR}/terminal.out" && '
                    outstr += 'python3 scripts/generate_config_and_run.py -d "${EXPDIR}" '
                    outstr += '-e -b '
                    outstr += '-f %s ' % file
                    outstr += '-%s 1000 ' % policy
                    outstr += '-gpusel %s ' % gsm if gsm != "<none>" else ''
                    outstr += '-dimext %s ' % dem if dem != "<none>" else ''
                    outstr += '-norm %s ' % nm if nm != "<none>" else ''
                    outstr += '-tune %s ' % '0'
                    outstr += '-tuneseed %s ' % '0'
                    outstr += "--shuffle-pod=true " if SHUFFLE_POD else ""
                    outstr += '-y "${EXPDIR}/snapshot/yaml" ' if OUTPUT_YAML else ""
                    outstr += '-z "${EXPDIR}/snapshot/ds01" '
                    outstr += '| tee -a "${EXPDIR}/terminal.out" '
                    outstr += '&& python3 scripts/analysis.py -f -g ${EXPDIR} '
                    outstr += '| tee -a "${EXPDIR}/terminal.out" '
                    if asyncc:
                        outstr += " &"
                    print(outstr + "\n")

                    numJobs += 1
                    if asyncc and (numJobs % parallel == 0):
                        print("date & wait\n")  # force them to sync
    if asyncc:
        print("wait && date")

if __name__=='__main__':
    # generate_run_scripts(asyncc=True)
    #: $ bash run_scripts.txt
    generate_run_scripts(asyncc=False)
    #: $ cat run_scripts.txt | while read i; do printf "%q\n" "$i"; done | xargs --max-procs=16 -I CMD bash -c CMD

