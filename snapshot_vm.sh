#!/bin/bash -x
VM=$1
which python3
python3 -c "import snapshot_vm as s;s.VM=$VM;s.snapshot()"