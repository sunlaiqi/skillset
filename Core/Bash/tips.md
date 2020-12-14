
- [git related](#git-related)
  - [How to checkout a remote branch in git](#how-to-checkout-a-remote-branch-in-git)
  - [How to revert a commit on github](#how-to-revert-a-commit-on-github)
  - [Compare files with diff](#compare-files-with-diff)
  - [How to create and delete branch locally](#how-to-create-and-delete-branch-locally)
  - [Create branch and merge locally](#create-branch-and-merge-locally)
  - [Git a new branch off another branch and rebase](#git-a-new-branch-off-another-branch-and-rebase)
  - [How to sync with master repo?](#how-to-sync-with-master-repo)
  - [How to list all the changed files in git and backup](#how-to-list-all-the-changed-files-in-git-and-backup)
- [Bash scripts](#bash-scripts)
  - [Dump content of a file to a variable](#dump-content-of-a-file-to-a-variable)
  - [Check if a file exists](#check-if-a-file-exists)
  - [Check if the a file is empty](#check-if-the-a-file-is-empty)
  - [Display usage of script](#display-usage-of-script)
  - [Obtain IP mask](#obtain-ip-mask)
  - [Obtain subnet](#obtain-subnet)
  - [When to use () vs. {} in bash?](#when-to-use--vs--in-bash)
  - [FInd boot partition and erase MBR](#find-boot-partition-and-erase-mbr)
  - [How to expand variable inside single quote?](#how-to-expand-variable-inside-single-quote)
  - [How to check a user has sudo on a host](#how-to-check-a-user-has-sudo-on-a-host)
  - [Why got permission denied using source command?](#why-got-permission-denied-using-source-command)
  - [How to loop over json to modify value of each orbject in jq](#how-to-loop-over-json-to-modify-value-of-each-orbject-in-jq)
  - [Add one item to an array of strings](#add-one-item-to-an-array-of-strings)
- [jq programming](#jq-programming)
  - [Compose a json data](#compose-a-json-data)
  - [Submit json data using curl](#submit-json-data-using-curl)
  - [Use temp file and delete when exit](#use-temp-file-and-delete-when-exit)
  - [Get the list of all the keys of json](#get-the-list-of-all-the-keys-of-json)
  - [Loop over /etc/fstab using while](#loop-over-etcfstab-using-while)
- [Linux](#linux)
  - [Logical Volume Manager (LVM)](#logical-volume-manager-lvm)
  - [Erase MBR](#erase-mbr)
  - [Backup MBR with dd command](#backup-mbr-with-dd-command)
  - [How to get BIOS info from command](#how-to-get-bios-info-from-command)
  - [os-prober, update-grub, grub-install, /boot/grub/device.map](#os-prober-update-grub-grub-install-bootgrubdevicemap)
  - [How to query free DHCP ip address?](#how-to-query-free-dhcp-ip-address)
  - [Quick way to see if GRUB installed](#quick-way-to-see-if-grub-installed)
  - [Add cron job to crontab](#add-cron-job-to-crontab)
  - [Schedule a cron job](#schedule-a-cron-job)
  - [Redirect bash script output to syslog](#redirect-bash-script-output-to-syslog)
  - [Redirect bash script output to another bash script](#redirect-bash-script-output-to-another-bash-script)
  - [Suppress output from curl command](#suppress-output-from-curl-command)
  - [Embed Python in bash script](#embed-python-in-bash-script)
  - [How to find subnet and cidr by a command](#how-to-find-subnet-and-cidr-by-a-command)
  - [How to test port connectivity with telnet](#how-to-test-port-connectivity-with-telnet)
  - [Use curl to download from tftp](#use-curl-to-download-from-tftp)
  - [Find or et IP address](#find-or-et-ip-address)
  - [Read system IP address](#read-system-ip-address)
- [vscode](#vscode)
  - [remote dev using ssh](#remote-dev-using-ssh)
  - [vscode config key based auth](#vscode-config-key-based-auth)
- [Python tips](#python-tips)
  - [Split a string with multiple delimiters](#split-a-string-with-multiple-delimiters)


# git related

## How to checkout a remote branch in git
To list remote repo
`$ git remove -v`

to get branch updates from remote
```
$ git fetch
$ git checkout some_branch_name
```

## How to revert a commit on github

go to your repo and click on Pull Request. Click on "Closed" tab to list all the pull requests committed. Find the commit you want to revert and click it. Find the "revert" button and click it. It will create a new PR.

## Compare files with diff

`$ git diff HEAD helloworld.txt`
HEAD here refers to index or the local repo.
Compare the working dir with local repo:
`$ git diff HEAD [filename]`

compare the working dir with index:
`$ git diff [filename]`

compare the index with loca repo
`$ git diff -- cached [filename]`

## How to create and delete branch locally
create a branch locally
`$ git checkout -b branch_name`
push to remot repo
`$ git -u origin branch_name`
make some change and commit the changes locally
push changes to remote repo
`$ git push`

delete a branch locally
`$ git branch -a`
delete branch locally
`$ git branch -d branch_name`
delete branch on remote repo
`$ git push origin --delete branch_name`
if you already deleted the branch on github using BUI, then:
`$ git branch -d -r origin/branch_name`
or you can use the following to remove all such stale branches
`$ git remote prune origin`
with --dry-run option, report what branches will be pruned, but do not actually prune them.

`$ git fetch -p` # will fetches and prunes all origins
similar
```
$ git pull --prune
$ git remote update --prune
```

## Create branch and merge locally

1. From your project repo, bring in the changes and test
```
$ git fetch origin
$ git checkout -b branch_name origin/branch_name
$ git merge development
```
2. Merge the changes and update on remote repo
```
$ git checkout development
$ git merge --no-ff branch_name
$ git push origin development
```

## Git a new branch off another branch and rebase

Start your feature_b from feature_a, i.e.:
```
$ git checkout feature_a
$ git checkout -b feature_b
```
Whenever feature_a changes while it is waiting to get merged into master (PR submitted and in code review). You rebase feature_b on it:
... commit something onto feature_a ...
```
$ git checkout feature_b
$ git rebase feature_a
```
Finally as soon as feature_a has been merged into master, you simply get the new master and rebase feature_a onto it a last time:
```
$ git checkout master
$ git pull origin master
$ git checkout feature_b
$ git rebase --onto master feature_a feature_b
```

## How to sync with master repo?
```
$ git checkout master
$ git fetch
$ git pull
$ git checkout local_branch
$ git merge master
```
If you are ready to push your local branch to the remote repo:
```
$ git checkout master
$ git merge local_branch
$ git push origin master
```
## How to list all the changed files in git and backup

`$ git diff --name-only | xargs cp --parents -t ~/tests/bk1/`

It will keep the directory stuctures when backup



# Bash scripts

## Dump content of a file to a variable

```bash
tmpfile=$(mktemp)
trap "rm -f ${tmpfile}" EXIT
# Prune the file
>${tmpfile}
# add some data
echo "Some data" > ${tmpfile}
# dump the content 
VAR=$(< ${tmpfile})
echo ${VAR}
```

## Check if a file exists

If the file does not exist, create it.

```bash
[[ ! -f ${tmpfile} ]] && touch ${tmpfile} && echo "The file created."
```

## Check if the a file is empty

```bash
tmpfile=python.py
len=($(ls -l ${tmpfile}))
len=${len[4]}
if [[ ${len} -gt 0 ]]; then
    echo "The file is not empty"
else
    echo "The file is empty"
    exit 1
fi
```

## Display usage of script

```bash
die () { echo $@ ; exit 1; }

case $1 in 
    start)
    ...
    ;;
    stop)
        : # Do nothing
    ;;
    *) die "Usage: $0 [start|stop]"
    ;;
esac
```

## Obtain IP mask

```bash
obtain_ip_mask ()
{
    local ip_interface=$(ip r | grep default | awk '{print $5}')
    local ipaddr=$(ip r | grep -v default | head -n 1 | awk '{print $9}')
    local submask=$(ifconfig ${ip_interface} | grep -w inet | awk '{print $4}' | cut -d ":" -f 2)
    echo ${ipaddr} ${submask}
}

ip_mask=($(obtain_ip_mask))
ipaddress=${ip_mask[0]}
submask=${ip_mask[1]}
```
## Obtain subnet 

```bash
# Generate subnet/cidr from ip address and sub mask
# Usage:
# obtain_subnet ${IP} ${SUBMASK}
# Return:
#   SUBNET CIDR

obtain_subnet ()
{
    cidr=0
    new_ip=""
    OLDIFS=$IFS
    IFS=.

    for seg in $2 ; do
        while [[ ${seg} -ne 0 ]] ; do
            (( cidr += seg & 1 ))
            (( seg >>= 1 ))
        done
    done
    (( temp = cidr ))

    for subip in $1 ; do
        if [[ ${temp} -lt 8 ]] && [[ ${temp} -gt 0 ]] ; then
            (( subip >>= $((8-temp)) ))
            (( subip <<= $((8-temp)) ))
        fi
        if [[ ${#new_ip} -eq 0 ]]; then
            new_ip=${subip}
        elif [[ ${temp} -le 0 ]]; then
            new_ip=${new_ip}.0
        else
            new_ip=${new_ip}.${subip}
        fi
        (( temp -= 8 ))
    done

    IFS=$OLDIFS
    echo ${new_ip} ${cidr}
}

IP=192.168.0.1
NETMASK=255.255.255.0
SUBMASK=$(obtain_subnet ${IP} ${NETMASK})
echo ${SUBMASK}
```
Result:
```
192.168.0.0 24
```

## When to use () vs. {} in bash?

If you want the side-effects of the command list to affect your current shell, use {...}
If you want to discard any side-effects, use (...)

( list )
Placing a list of commands between parentheses causes a subshell environment to be created, and each of the commands in list to be executed in that subshell. Since the list is executed in a subshell, variable assignments do not remain in effect after the subshell completes.

{ list; }
Placing a list of commands between curly braces causes the list to be executed in the current shell context. No subshell is created. The semicolon (or newline) following list is required.

Code in '{}' is executed in the current thread/process/environment and changes are preserved, to put it more succinctly, the code is run in the current scope.
Code in '()' is run inside a separate, child process of bash that is discarded after execution. This child process is often referred to as a sub-shell and can be thought of as a new, child-like scope.



## FInd boot partition and erase MBR


```bash
BOOTDISK=$(df /boot | awk 'NR == 2 {print}' | cut -d' ' -f1 | sed 's/[0-9]//g')

DDCM="dd if=/dev/zero of=${BOOTDISK} bs=1024K count=1 conv=fsync"

${DDCM} && echo "Done!" || {echo "Can't erase MBR."; exit 1}
```


## How to expand variable inside single quote?
```bash
HOST="XXX.XXX.XXX.XXX"
echo "'"$HOST"'"
DATA_BINARY='{
    "filename" : "xxxx/xxx.txt",
    "preload" : {
        "data" : "'"$HOST"'"''
    }
}'
echo $DATA_BINARY
```

## How to check a user has sudo on a host

```bash
sudo -n -l -U $username | egrep -c -i -v "not allowed to run sudo|unknown user" > /dev/null 2>&1 
```
where
- `n` - no-interactive

## Why got permission denied using source command?

what is probably happening is that the script tries to source the file `util.sh` in the current directory and fails because it doesn't have permission to read your current directory because of sudo.
Use full path for `util.sh` to solve this issue:
```bash
BASEDIR=`dirname $0`
echo ${BASEDIR}
source ${BASEDIR}/util.sh
```
## How to loop over json to modify value of each orbject in jq

```bash
# Reduce 'size' by 8%
jq '.[].size |= . - .%8'
# If size > 100 then reduce size, otherwize, no change
jq '.'.[].size |= if .>100 then . - .%8 else . end'
# Or
jq '.'.[].size |= if (.>100) then (. - .%8) else . end'
# Convert size to string by add +
jq '.[].size |= ((. - .%8) | round | tostring + "+")'
jq '.'.[].size |= if (.>100) then ((. - .%8 | round | tostring + "+")) else . end'
```

## Add one item to an array of strings

Suppose A="aaa,bbb,ccc"
Append B="ddd" to A

```bash
A="aaa,bbb,ccc"
B="ddd"

A="${A}${A:+,}${B}"
echo ${A}
```

**Parameter Substitution**

`${parameter+alt_value}, ${parameter:+alt_value}`
If parameter set, use alt_value, else use null string.

`${parameter=default}, ${parameter:=default}`
If parameter not set, set it to default.

`${parameter-default}, ${parameter:-default}`
If parameter not set, use default.

`${parameter?err_msg}, ${parameter:?err_msg}`
If parameter set, use it, else print err_msg and abort the script with an exit status of 1.


`${#var}`
String length (number of characters in `$var`). For an array, `${#array}` is the length of the first element in the array.

`${string:position}`
Extracts substring from $string at $position.
`${string:position:length}`
Extracts $length characters of substring from $string at $position.
`${var/Pattern/Replacement}`
First match of Pattern, within var replaced with Replacement.
If Replacement is omitted, then the first match of Pattern is replaced by nothing, that is, deleted.
`${var//Pattern/Replacement}`
Global replacement. All matches of Pattern, within var replaced with Replacement.

It cuts away the first 3 characters of a (string) variable:
```bash
$ VAR="hello world"
$ echo ${VAR:3}
lo world
```
# jq programming

## Compose a json data 

```bash
MAC_ADDRESS=127.0.0.1
DATA=$(echo '""' | jq --arg mac_address ${MAC_ADDRESS} '. + $mac_address')
echo ${DATA} | jq .

DATA=$(echo '{}' | jq --arg key_name ${MAC_ADDRESS} '. + {$key_name}')
echo ${DATA} | jq .

DATA=$(echo '{}' | jq  '. + {"key_name": "1111", "key_name2": "2222"}')
echo ${DATA} | jq .

DATA=$(echo '{}' | jq  '. + {"key_name": "1111"}' | jq '. + {"key_name2": "2222"}')
echo ${DATA} | jq .

DATA=$(echo '[]' | jq --arg mac_address ${MAC_ADDRESS} '. + [$mac_address]')
echo ${DATA} | jq .

DATA=$(echo '[]' | jq '. + ["1111"]' | jq '. + ["2222"]')
echo ${DATA} | jq .
```
The result:
```
"127.0.0.1"
{
  "key_name": "127.0.0.1"
}
{
  "key_name": "1111",
  "key_name2": "2222"
}
{
  "key_name": "1111",
  "key_name2": "2222"
}
[
  "127.0.0.1"
]
[
  "1111",
  "2222"
]
```

## Submit json data using curl

There are a few ways to do this.
1 Use `-d`, usually used for single key/value update
URL is the http address.
DATA is a json string composed by, for example, like so:
```bash
DATA=$(echo '""' | jq --arg mac_address ${MAC_ADDRESS} '. + $mac_address')
curl -H "Content-Type: application/json" -X PUT ${URL} -d ${DATA}
```

2 Use `-d @-`. Usually used for json data update
But this way will use pipeline. It uses json as input instead of json string
```bash
echo ${DATA} | jq . | curl -H "Content-Type: application/json" -X PUT ${URL} -d @-
```

## Use temp file and delete when exit

```bash
tmpfile=$(mktemp)
trap "rm -f ${tmpfile}" EXIT
```

## Get the list of all the keys of json
```bash
DATA=$(echo '{}' | jq  '. + {"key_name": "1111"}' | jq '. + {"key_name2": "2222"}')
echo ${DATA} | jq .
KEYS=$(echo ${DATA} | jq 'keys | .[]')
echo ${KEYS} | jq .
```
Result:
```
{
  "key_name": "1111",
  "key_name2": "2222"
}
"key_name"
"key_name2"
```
## Loop over /etc/fstab using while

Remember `()` is a separate process. Everything in it will be gone after it exits.

```bash
DISMAP_KEYS=$(echo ${DISKMAP} | jq 'keys | .[]')
MISSING_FS='[]'
grep -v -E "^#|root|swap|tmp|boot" /etc/fstab | ( while read device dir fstype def opt1 opt2; do
    if [[  ! "${DISKMAP_KEYS}" == *"${dir}"* ]]; then
    ENTRY=$(grep -v -E "^#|root|swap|tmp|boot" /etc/fstab | grep ${dir} | sed 's/\t/    /g')
    MISSING_FS=$(echo ${MISSING_FS} | jq --arg entry "${ENTRY}" '. + [ $entry ]')
    fi
done
if [[ ${MISSING_FS} == '[]' ]]; then
    echo "No missing File System."
else
    echo "Missing FS"
    # You may need to save data into a temp file
    # becaue here () is a separate process, all the data will be gone after it exit
)
```

# Linux


## Logical Volume Manager (LVM)

LVM manages disk space using following order:
- Physical Volumes (PVs)
- Volume Groups (VGs)
- Logical Volumes (LVs)

Display PVs:
`$ sudo pvscan`

Create a VG:
`$ sudo vgcreate vgname /dev/sde1 /dev/sde2 ...`
Create LV
`$ sudo lvcreate -L 200G -n lvname vgname`
Display LV
`$ sudo lvscan`
Make file system
`$ sudo mkfs -t ext4 /dev/vgname/lvname`
(or `$ sudo mkfs.ext4 /dev/vgname/lvname`)
Create a mount point:
```
$ sudo mkdir /mnt/lvdemo
$ sudo mount /dev/vgname/lvname /mnt/lvdemo
$ sudo df -h /mnt/lvdemo
```

## Erase MBR

Understand MBR size:
446 + 64 + 2 = 512
- 446 bytes - Bootstrap
- 64 bytes - Partition table
- 2 bytes - Signature

Option #1: command to delete MBR including all partitions
delete everything.
`# dd if=/dev/zero of=/dev/sdc bs=512 count=1`
where
- if=/dev/zero - read data from /dev/zero
- of=/dev/sdc - write date to /dev/sdc
- bs=512 - read/write 512 bytes at a time
- count=1 - copy only 1 block input blocks

option #2: delete MBR only
`# dd if=/dev/zero of=/dev/sdc bs=446 count=1`

## Backup MBR with dd command
Backup:
`# dd if=/dev/sda of=/tmp/sda-mbr.bin bs=512 count=1`
Restore partition table:
`# dd if=/tmp/sda-mbr.bin of=/dev/sda bs=1 count=64 skip=446 seek=446`

## How to get BIOS info from command

`$ sudo dmidecode -t bios -q`
Or
`$ cat /sys/class/dmi/id/bios_version`


## os-prober, update-grub, grub-install, /boot/grub/device.map

os-prober will scan all disks available on the system for other OSs

`$ sudo linux-boot-prober /dev/sda1`

update-grub: program to generate GRUB's menu.lst file

If you are telling BIOS to boot from the disk that is /dev/sda, the /boot/grub/device.map should have this line in it:
`(hd0) /dev/sda`

## How to query free DHCP ip address?

## Quick way to see if GRUB installed

`# dd if/dev/sda bs=512 count=1 | xxd`

`xxd` - make a hexdump or do the reverse.

## Add cron job to crontab

`$ crontab -l | { cat; echo "0 0 0 0 0 some entry"; } | crontab -`
where
- `crontab -l` - lists the current crontab jobs
- `cat` - prints it
- `echo` - prints the new command 
- `crontab -` - adds all the printed stuff into the crontab file

## Schedule a cron job

Give crontab privilege
append the specified usernames to /etc/cron.allow
`# cat /etc/cron.allow`
create cron file for root
`# touch /var/spool/cron/root`
`# /usr/bin/crontab /var/spool/cron/root`
create a cron file for user1:
`# touch /var/spool/cron/user1`
`# /usr/bin/crontab /var/spool/cron/user1`
sechedule your job. Example, clear temp files every midnight for both users:
`# echo "0 0 * * * rm -f /tmp/root/*" >> /var/spool/cron/root`
`# echo "0 0 * * * rm -f /tmp/user1/*" >> /var/spool/cron/user1`
Validate the cron job content. You can use -u to define the username for which your wish to perform the cron action:
`# crontab -u user1 -l`
0 0 * * * rm -f /tmp/user1/*
`# crontab -u root -l`
0 0 * * * rm -f /tmp/root/*

You do not need to restart your crond service for the new changes.

## Redirect bash script output to syslog

Put the following at the top of your bash script

```
exec 1> >(logger -s -t $(basename $0)) 2>&1
```
Where:
- `exec` - is a built-in. It replaces the shell with the give command. In this case, `exec`is being used with `COMMAND` - this line is redirecting I/O for the current shell. For example, in `exec 1> >(some-command) 2>&1`, there are two redirections:
  - `1> >(some-command)` - This redirects file descriptor 1 (stdout) to the location `>(some-command)`. `>(some-command)`is a process substitution, which is a non-POSIX bash feature. `>(some-command)` returns a file descriptor that `some-commad` will use as its stdin. This is exacty the same as piping our script's stdout into `some-command`. Then we redirect file descriptor 2 (stderr) to the same location as file descriptor 1:
  - `2>&1`
- In sum, we redirect both stdout and stderr for our script to the same place: the stdin for another process, which is a command running in the background. In fact, this is the same as running the script at the command line like so:
- `$ ./some-script 2>&1 | some-command`. In this case, `some-command` is:
- `logger -s -t $(basename $0)`. This writes entries to syslog tagged `(-t)` with the filename of our script(`$(basename $0)`) and echoing them to standard error (`-s`).
- So the full line takes both stdout and stderr from our script, and redirects them to logger command, which sends them to the syslog and echoes them back to stderr.



## Redirect bash script output to another bash script
Put the following at the top of the bash script. Then all the output from this script will redirect to file `log.sh`.

```bash
> /tmp/temp_file
exec &> >(tee >(xargs -I MSG ./log.sh MSG))
```
where:
- tee - redirect both to standard out and to `xargs`
- `>()` - Output as input into pipe `()`
- `xargs -I MSG ./log.sh MSG`
  - `-I MSG` - Define MSG as a variable to accept input
  - `./log.sh MSG` - `log.sh` is the bash script that processes the output held by `MSG`

If you want to add more arguments to log.sh:
```bash
ARG="Test"
> /tmp/temp_file
exec &> >(tee >(xargs -I MSG ./log.sh ${ARG} MSG))
```
## Suppress output from curl command

```bash
curl --silent --output /dev/null http://example.com
```

## Embed Python in bash script

Calling Python from bash is easy. You simple use Python's `-` argument and pipe in your python code.
```bash
#!/bin/bash

function current_datetime () {
python3.9 - <<END
import datetime
print(datetime.datetime.now())
END
}

# Call it
current_datetime

# Call it and capture the output
DT=$(current_datetime)
echo "Current date and time : $DT"
```

## How to find subnet and cidr by a command

`$ ip r`

## How to test port connectivity with telnet

You can use the command netcat (nc) which test access to the server.(TCP)
```bash
nc -zv hostname.company.com 80
```
Use `-u` to send UDP packet
`$netcat -u host port`

Port scanning:(From port 1 to port 1000)
`$nc -zv hostname 1-1000`

Use netcat to listen on port 444
`$netcat -l 4444`

How to send files through netcat
`$ netcat -l 4444 > received_file` # on the receiving host
`$ echo "Hello, this is a file " > original_file` # on sending host
`$ netcat hostname 4444 < orginal_file` # on sending host

On the receiving end, we can anticipate a file coming over that will need to be unzipped and extracted:
`$ netcat -l 4444 | tar xzvf -`
On sending host, we want to send all the files in the folder.
`$ tar -czf - * | netcat hostname 4444`

How to use netcat as a simple web server?

```bash
while true; do printf 'HTTP/1.1 200 OK\n\n%s' "$(cat index.html)" | netcat -l 8888; done
```



## Use curl to download from tftp

`$ curl -o localfilename tftp://hostname/filename`


## Find or et IP address

Find default routing info:
`# netstat -rn`

Find the IP address:
`# hostname -I`
or 
`# ip addr show`

Linux command to display default routes
```bash
ip route show
ip r s
route -n
```
Use host and dig commands:
`# host myip.opendns.com resolver1.opendns.com`
OR
```bash
dig +short myip.opendns.com @resolver1.opendns.com
getnet hosts google.com | awk '{print $1}'
dig hostname a +short
host foo.com | grep " has address " | cut -d " " -f4
gethostip -d hostname
host google.com | awk '{print $NF}'
```

List all the net interfaces
`# ip link show`

## Read system IP address
```bash
ifconfig | grep 'inet addr:' | grep -v '127.0.0.1' | cut -d: -f2 | awk '{print $1}'
```

# vscode

## remote dev using ssh 
First install extent: Remote-SSH
Then to connect a Linux using SSH:
In vscode, from Command Palette, select "Remote-SSH: Connect to Host..."

## vscode config key based auth

Generate a separate SSH key in a different file.
macOS/Linux:
$ ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa-temote-ssh

Copy the public key to the Linux SSH host:
~/.ssh/id_rsa-remote-ssh.pub

Authorize the key on the Linux SSH host
Create a file anmed "authorized_keys" under ~/.ssh
Copy the key generated in id_rsa-remote-ssh.pub to ~/.ssh/authorized_keys on Linux SSH host.

In vscode, run "Remote-SSH: Open ofiguration File..." to config ssh....

# Python tips

## Split a string with multiple delimiters

```python
import re
line = "how to; do, in, java,   dot, com"
re.split(r'[;,\s]\s*', line) # Split with comma, semicolon and space

# ['how', 'to', 'do', 'in', 'java', 'dot', 'com']
```
