"""VirtualBox Snapshot Rotator.

Attributes:
    VM (String): Name of VM
"""
import subprocess
import sys

VM = None


def get_snapshot_list():
    """Get list of snapshots.

    Returns:
        List: List of VM names as String
    """
    if VM is None:
        print('Please set VM constant.')
        sys.exit(1)
    cmd = [
        'VBoxManage snapshot ' + VM + ' list'
    ]
    p = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
    stdout, stderr = p.communicate()
    if stdout:
        stdout = stdout.decode('utf-8')
    if stderr:
        stderr = stderr.decode('utf-8')
    active = False
    if stderr:
        print("stderr: " + str(stderr))
    if stdout:
        print("stdout: " + str(stdout))
        success_str = (
            "Name:"
        )
        if success_str in stdout:
            active = True
    if active:
        snapshot_lines = stdout.split('\n')
        snapshots = []
        for line in snapshot_lines:
            line_dict = line.split(' ')
            token_index = 0
            for token in line_dict:
                if token == 'Name:':
                    name = line_dict[token_index + 1]
                    snapshots.append(name)
                token_index += 1
        print('List of snapshots is - \n' + str(snapshots))
        return snapshots
    else:
        print('failed to get list of snapshots')
        return []


def snapshot():
    """Take snapshot"""
    snapshots = get_snapshot_list()
    last_snapshot_name = None
    last_snapshot_index = snapshots.__len__()
    if last_snapshot_index > 1:
        last_snapshot_name = snapshots[last_snapshot_index - 1]
        for snapshot in snapshots:
            if snapshot is not last_snapshot_name:
                print('deleting snapshot ' + snapshot)
                cmd = [
                    'VBoxManage snapshot ' + VM + ' delete ' + snapshot
                ]
                p = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True
                )
                stdout, stderr = p.communicate()
                if stdout:
                    stdout = stdout.decode('utf-8')
                if stderr:
                    stderr = stderr.decode('utf-8')
                if stderr:
                    print("stderr: " + str(stderr))
                if stdout:
                    print("stdout: " + str(stdout))
                    if '100%' in stdout:
                        print('deleted ' + snapshot + ' successfully')
    else:
        last_snapshot_index = last_snapshot_index + 2

    new_snapshot_name = None
    if last_snapshot_name is None:
        new_snapshot_name = 'Latest' + str(last_snapshot_index - 1)
    elif int(last_snapshot_name[-1]) == 1:
        new_snapshot_name = 'Latest2'
    elif int(last_snapshot_name[-1]) == 2:
        new_snapshot_name = 'Latest1'

    cmd = [
        'VBoxManage snapshot ' + VM + ' take ' + new_snapshot_name
    ]
    p = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
    stdout, stderr = p.communicate()
    if stdout:
        stdout = stdout.decode('utf-8')
    if stderr:
        stderr = stderr.decode('utf-8')
    if stderr:
        print("stderr: " + str(stderr))
    if stdout:
        print("stdout: " + str(stdout))
        if '100%' in stdout:
            print('created new snapshot called ' + new_snapshot_name + ', successfully')
