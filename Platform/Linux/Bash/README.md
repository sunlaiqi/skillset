- [Various ways to obtain ip address](#various-ways-to-obtain-ip-address)
- [Find files and remove duplicate files](#find-files-and-remove-duplicate-files)


# Various ways to obtain ip address 

Obtain remote host ip address:

You can use `getent`, which comes with glibc (so you almost certainly have it on Linux). This resolves using gethostbyaddr/gethostbyname2, and so also will check `/etc/hosts/NIS/etc`.
`dig` with the +short argument (queries DNS servers directly, does not look at `/etc/hosts/NSS/etc`)

If `dig +short` is unavailable, any one of the following should work. All of these query DNS directly and ignore other means of resolution:
```
host unix.stackexchange.com | awk '/has address/ { print $4 }'
nslookup unix.stackexchange.com | awk '/^Address: / { print $2 }'
dig unix.stackexchange.com | awk '/^;; ANSWER SECTION:$/ { getline ; print $5 }'
```
If you want to only print one IP, then add the exit command to awk's workflow.
```
dig +short unix.stackexchange.com | awk '{ print ; exit }'
getent hosts unix.stackexchange.com | awk '{ print $1 ; exit }'
host unix.stackexchange.com | awk '/has address/ { print $4 ; exit }'
nslookup unix.stackexchange.com | awk '/^Address: / { print $2 ; exit }'
dig unix.stackexchange.com | awk '/^;; ANSWER SECTION:$/ { getline ; print $5 ; exit }'
```

```
# getent hosts google.com | awk '{print $1}'
93.46.8.90
# dig +short unix.stackexchange.com
151.101.1.69
151.101.193.69
151.101.129.69
151.101.65.69
# dig www.google.com a +short
104.244.43.57
# host google.com|grep " has address "|cut -d" " -f4
216.58.199.110

# gethostip -d hostname

```

To get public IP address of your host:
```
$ curl -4 ifconfig.co
68.227.12.xxx
$ curl ifconfig.me/ip
68.227.12.xxx
```

For Linux: to get local ip address
```
# ip route get 1 | head -1|awk '{print $7}'
# hostname --ip-address
# hostname -i
# hostname -I
```

I guess it would create a strange dependency for your script... (**Very slow**)
```
ping -q -c 1 -t 1 your_host_here | grep PING | sed -e "s/).*//" | sed -e "s/.*(//"
```
works without dependencies on other systems (and for hosts specified in /etc/hosts)

Here is a slight variation of the ping approach that takes "unknown host" into account (by piping through stderr) and uses tr to avoid the use of sed regexps:
```
ping -c1 -t1 -W0 www.example.com 2>&1 | tr -d '():' | awk '/^PING/{print $3}'
```
In case it's important to capture the exit value, then the following will work (although less elegant):
```
ping -c1 -t1 -W0 www.example.com &>/dev/null && ping -c1 -t1 -W0 www.example.com 2>&1 | tr -d '():' | awk '/^PING/{print $3}'
```

# Find files and remove duplicate files

Find all the pdf files, compare them with the files in one folder and then remove all those duplicate files in the folder.
```bash
find ./ -iname "*.pdf" -exec mv '{}' ../Books/ \;

find ./ -iname "*.pdf" -exec basename '{}' \; 

cat dupfile -exec mv '{}' ../duplicate \;

# Find the files in bookfile.txt but not in pdffile.txt
grep -v -f pdffile.txt bookfile.txt > difffile.txt

for file in `cat ../difffile.txt`; do mv "$file" ../Doc-bk/; done
# above will have problem with space

while read -r file; do mv "$file" /path/of/destination ; done < ../difffile.txt

while read -r file; do rm "file" ; done < ../pdffile.txt
```