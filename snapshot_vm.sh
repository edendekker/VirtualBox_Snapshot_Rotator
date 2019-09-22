#!/bin/bash -x
VM=$1
which python3
CMD="import snapshot_vm as s;s.VM='"$VM"';s.snapshot()"
python3 -c $CMD
