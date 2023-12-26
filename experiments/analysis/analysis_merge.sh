#!/bin/bash
python3 merge_alloc_discrete.py &
python3 merge_frag_discrete.py &
python3 merge_frag_ratio_discrete.py &
python3 merge_fail_pods.py &
python3 merge_price.py &
python3 merge_nodes.py &
python3 merge_time.py &
