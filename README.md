# VirtualBox Snapshot Rotator

A python script for rotating on premise Oracle Virtual Box Snapshots.


## Limitations
- VM pauses the live system during snapshots
- Script is hardcoded to retain two snapshots
- This shell script was not tested. I ran the py file directly from a jenkins CI job scheduler. So the py file is known to work.

## Motivation
I needed a cheap way to have on premise snapshots.
I no longer need this script since i now have a more elaborate backup strategy that minimises live downtime.
I hope this helps people that need something quick and that works.
Great for small coding projects on a development environment!

## Installation
### Unix
Check VirtualBox user of the vm installation. Make sure your script can execute it.
```
ls -lrtah ./virtualbox/TomDevCodingMachine
drwx------  8 vboxuser    vboxuser    4.0K Sep 17 21:30 TomDevCodingMachine
sudo chmod 100 /home/vboxuser/snapshot_vm.sh
sudo chmod 100 /home/vboxuser/snapshot_vm.py
sudo chown vboxuser:vboxuser snapshot_vm.*
```
Open crontab
```sudo vi /etc/crontab```
Enter schedule. Example below is a snapshot every hour.
```* */1   * * *   vboxuser   /home/vboxuser/snapshot_vm.sh TomDevCodingMachine```
### Windows
Sorry.
