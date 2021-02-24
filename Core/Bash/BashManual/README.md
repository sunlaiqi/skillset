

Bash Reference Manual

Chet Ramey, Case Western Reserve University Brian Fox, Free Software Foundation

Reference Documentation for Bash Edition 5.1, for Bash Version 5.1. December 2020


How to find info about a command?

```
$ type command
```
Find out the type of the command, builtin? or external command.
```
nobody@primary:~$ type uname
uname is /usr/bin/uname
nobody@primary:~$ type cd
cd is a shell builtin
nobody@primary:~$ type ls
ls is aliased to `ls --color=auto'
nobody@primary:~$ 
```

If no man page for a command, use help.
```
$ help command
```

```
command -V command
```






