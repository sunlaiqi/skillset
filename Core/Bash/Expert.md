- [Shell tricks](#shell-tricks)
  - [pkg-config](#pkg-config)
  - [Export variable for single command](#export-variable-for-single-command)
- [Standard Output](#standard-output)
  - [Process substitution and pipe](#process-substitution-and-pipe)
    - [Definition](#definition)
    - [Explained](#explained)
    - [Applications](#applications)
  - [Explain the bash command “`exec > >(tee $LOG_FILE) 2>&1`”](#explain-the-bash-command-exec--tee-log_file-21)
  - [output without the default newline](#output-without-the-default-newline)
  - [Redirect error to file](#redirect-error-to-file)
  - [Throwing Output Away](#throwing-output-away)
  - [Skipping a Header in a File](#skipping-a-header-in-a-file)
  - [Saving or Grouping Output from Several Commands](#saving-or-grouping-output-from-several-commands)
  - [Keeping Files Safe from Accidental Overwriting](#keeping-files-safe-from-accidental-overwriting)
- [Standard Input](#standard-input)
  - [Keeping Your Data with Your Script](#keeping-your-data-with-your-script)
  - [Indenting Here-Documents](#indenting-here-documents)
  - [Getting User Input](#getting-user-input)
- [Executing Commands](#executing-commands)
  - [Running Several Commands in Sequence](#running-several-commands-in-sequence)
  - [Running Long Jobs Unattended](#running-long-jobs-unattended)
  - [Running All Scripts in a Directory](#running-all-scripts-in-a-directory)
- [Basic Scripting: Shell Variables](#basic-scripting-shell-variables)
  - [Getting the Absolute Value of a Number](#getting-the-absolute-value-of-a-number)
  - [Using bash for basename](#using-bash-for-basename)
  - [Using Alternate Values for Comma Separated Values](#using-alternate-values-for-comma-separated-values)
  - [Using Array Variables](#using-array-variables)
  - [Converting Between Upper- and Lowercase ??](#converting-between-upper--and-lowercase-)
  - [Converting to Camel Case ??](#converting-to-camel-case-)
- [Shell Logic and Arithmetic](#shell-logic-and-arithmetic)
  - [Doing Arithmetic in Your Shell Script](#doing-arithmetic-in-your-shell-script)
  - [Testing with Pattern Matches](#testing-with-pattern-matches)
- [Additional Features for Scripting](#additional-features-for-scripting)
  - [“Daemon-izing” Your Script](#daemon-izing-your-script)
  - [Avoiding Aliases and Functions](#avoiding-aliases-and-functions)
- [Advanced Scripting](#advanced-scripting)
  - [Finding bash Portably for `#!`](#finding-bash-portably-for-)
  - [Setting a POSIX $PATH](#setting-a-posix-path)
  - [Developing Portable Shell Scripts](#developing-portable-shell-scripts)
  - [Using for Loops Portably](#using-for-loops-portably)
  - [Using bash Net-Redirection ?](#using-bash-net-redirection-)
  - [Finding My IP Address](#finding-my-ip-address)
  - [Redirecting Output for the Life of a Script](#redirecting-output-for-the-life-of-a-script)
  - [Logging to syslog from Your Script](#logging-to-syslog-from-your-script)
- [Configuring and Customizing bash](#configuring-and-customizing-bash)
- [Housekeeping and Administrative Tasks](#housekeeping-and-administrative-tasks)
  - [Recovering Disconnected Sessions Using screen](#recovering-disconnected-sessions-using-screen)
  - [Sharing a Single bash Session](#sharing-a-single-bash-session)
  - [Logging an Entire Session or Batch Job](#logging-an-entire-session-or-batch-job)
  - [Counting Differences in Files](#counting-differences-in-files)
  - [Using sudo on a Group of Commands](#using-sudo-on-a-group-of-commands)
  - [Numbering Lines](#numbering-lines)
- [Working Faster by Typing Less](#working-faster-by-typing-less)
  - [Reusing Arguments](#reusing-arguments)
- [Tips and Traps: Common Goofs for Novices](#tips-and-traps-common-goofs-for-novices)
  - [Forgetting to Set Execute Permissions](#forgetting-to-set-execute-permissions)
  - [Fixing “No such file or directory” Errors](#fixing-no-such-file-or-directory-errors)
  - [Forgetting that Pattern Matching Alphabetizes](#forgetting-that-pattern-matching-alphabetizes)
  - [Making Your Terminal Sane Again Problem](#making-your-terminal-sane-again-problem)
  - [Deleting Files Using an Empty Variable Problem](#deleting-files-using-an-empty-variable-problem)
  - [Testing bash Script Syntax](#testing-bash-script-syntax)
  - [Debugging Scripts](#debugging-scripts)
  - [Confusing Shell Wildcards and Regular Expressions Problem](#confusing-shell-wildcards-and-regular-expressions-problem)


**Excerpt from Shell Cookbook**

# Shell tricks

## pkg-config

`pkg-config` is a helper tool used when compiling applications and libraries. It helps you insert the correct compiler options on the command line so an application can use 
```
gcc -o test test.c `pkg-config --libs --cflags glib-2.0` 
```
for instance, rather than hard-coding values on where to find `glib` (or other libraries). It is language-agnostic, so it can be used for defining the location of documentation tools, for instance.

For example, on my PC, typing these two commands on the command line: 
```
pkg-config --libs gsl libxml-2.0 
pkg-config --cflags gsl libxml-2.0 
```
gives me these two lines of output: 
```
-lgsl -lgslcblas -lm -lxml2 
-I/usr/include/libxml2 
```

## Export variable for single command

You can export a variable for a single command by putting the assignment just before the command. The env command lists the environment variables it knows about, so when you run the following: 
```
$ PANTS=kakhi env | grep PANTS
```

Using this form sets and exports the given variables for one line only. 
After you try this on the command line, try running env | grep PANTS again to verify that PANTS is no longer an exported variable. 
Feel free to specify as many variables as you’d like: 
```
PANTS=kakhi PLANTS="ficus fern" env | grep 'P.*NTS' 
```

# Standard Output 

## Process substitution and pipe

### Definition

**Process substitution** is supported on systems that support named pipes (FIFOs) or the `/dev/fd` method of naming open files. It takes the form of `<(list)` or `>(list)`. The process list is run with its input or output connected to a FIFO or some file in `/dev/fd`. The name of this file is passed as an argument to the current command as the result of the expansion. If the `>(list)` form is used, writing to the file will provide input for list. If the `<(list)` form is used, the file passed as an argument should be read to obtain the output of list.

When available, process substitution is performed simultaneously with parameter and variable expansion, command substitution, and arithmetic expansion.

In other words, and from a practical point of view, you can use an expression like the following
```
<(commands)
```
as a file name for other commands requiring a file as a parameter. Or you can use redirection for such a file:
```
while read line; do something; done < <(commands)
```

Process substitution is not a POSIX compliant feature and so it may have to be enabled via:
```
set +o posix
```

### Explained

A good way to grok the difference between them is to do a little experimenting on the command line. In spite of the visual similarity in use of the < character, it does something very different than a redirect or pipe.

Let's use the date command for testing.
```
$ date | cat
Thu Jul 21 12:39:18 EEST 2011
```
This is a pointless example but it shows that cat accepted the output of date on STDIN and spit it back out. The same results can be achieved by process substitution:
```
$ cat <(date)
Thu Jul 21 12:40:53 EEST 2011
```
However what just happened behind the scenes was different. Instead of being given a STDIN stream, cat was actually passed the name of a file that it needed to go open and read. You can see this step by using echo instead of cat.
```
$ echo <(date)
/dev/fd/63
```
When cat received the file name, it read the file's content for us. On the other hand, echo just showed us the file's name that it was passed. This difference becomes more obvious if you add more substitutions:
```
$ cat <(date) <(date) <(date)
Thu Jul 21 12:44:45 EEST 2011
Thu Jul 21 12:44:45 EEST 2011
Thu Jul 21 12:44:45 EEST 2011

$ echo <(date) <(date) <(date)
/dev/fd/63 /dev/fd/62 /dev/fd/61
```

It is possible to combine process substitution (which generates a file) and input redirection (which connects a file to STDIN):
```
$ cat < <(date)
Thu Jul 21 12:46:22 EEST 2011
```
It looks pretty much the same but this time cat was passed STDIN stream instead of a file name. You can see this by trying it with echo:
```
$ echo < <(date)
<blank>
```
Since echo doesn't read STDIN and no argument was passed, we get nothing.

- Pipes and input redirects shove content onto the STDIN stream. 
- Process substitution runs the commands, saves their output to a special temporary file and then passes that file name in place of the command. 
  - Whatever command you are using treats it as a file name. Note that the file created is not a regular file but a named pipe that gets removed automatically once it is no longer needed.

### Applications

Here are three things you can do with process substitution that are impossible otherwise.

**Multiple process inputs**
```
diff <(cd /foo/bar/; ls) <(cd /foo/baz; ls)
```
There simply is no way to do this with pipes.

**Preserving STDIN**

Say you have the following:
```bash
curl -o - http://example.com/script.sh
   #/bin/bash
   read LINE
   echo "You said ${LINE}!"
```

And you want to run it directly. The following fails miserably. Bash is already using STDIN to read the script, so other input is impossible.
```
curl -o - http://example.com/script.sh | bash 
```
But this way works perfectly.
```
bash <(curl -o - http://example.com/script.sh)
```

**Outbound process substitution**

Also note that process substitution works the other way too. So you can do something like this:
```
(ls /proc/*/exe >/dev/null) 2> >(sed -n \
  '/Permission denied/ s/.*\(\/proc.*\):.*/\1/p' > denied.txt )
```
That's a bit of a convoluted example, but it sends stdout to /dev/null, while piping `stderr` to a `sed` script to extract the names of the files for which a "Permission denied" error was displayed, and then sends THOSE results to a file.

Note that the first command and the stdout redirection is in parentheses (subshell) so that only the result of THAT command gets sent to /dev/null and it doesn't mess with the rest of the line.



## Explain the bash command “`exec > >(tee $LOG_FILE) 2>&1`”

Same result:
```
exec &> >(tee "$LOG_FILE")
```
`>(...)` starts the process `...` and returns a file representing its **standard input**.

Using the syntax, `<(program)` for capturing output and `>(program)` for feeding input, we can pass data just one record at a time. It is more powerful than command substitution (backticks, or `$( )`) because it **substitutes for a filename**, not text. Therefore **anywhere a file is normally specified we can substitute a program's standard output or input** (although process substitution on input is not all that common). This is particularly useful where a program does not use standard streams for what you want.
```bash
exec > >(tee $LOG_FILE) 2>&1
```
is correct, that space is critical.

So, the `exec >` part changes file descriptor 1 (the default), also known as stdout or standard output, to refer to "whatever comes next", in this case it is the process substitution, although normally it would be a filename.

`2>&1` redirect file descriptor 2, stderr or standard error to refer to the same place as file descriptor 1 (if you omit the & you end-up with a file called 1).

Once you have done that, then you have changed the current process's standard output, so output from the commands which follow go to that tee process.

## output without the default newline

Using `printf` it’s easy—just leave off the ending `\n` in your format string: 
```
$ printf "%s %s" next prompt 
next prompt$
```

With echo, use the `-n` option: 
```
$ echo -n prompt 
prompt$ 
```
To use these escape sequences, you must invoke echo with the `-e` option. 
One of echo’s escape sequences is `\c`, which doesn’t print a character, but rather inhibits printing the ending newline. 
Thus, here’s a third solution: 
```
$ echo -e 'hi\c' 
hi$ 
```

## Redirect error to file

capture all the output and error messages to a single file? 

Preferred:     

```bash
both >& outfile
#or: 
both &> outfile
```
or older and slightly more verbose (but also more portable): 
```bash
both > outfile 2>&1
```

**Discussion**

- `&>` and `>&` are shortcuts that simply send both STDOUT and STDERR to the same place—exactly what we want to do. 
- In the third example, the 1 appears to be used as the target of the redirection, but the `>&` says to interpret the 1 as a **file descriptor** instead of a filename. 
  - In fact, the `2>&1` is a **single entity—no spaces allowed—indicating** that standard error (`2`) will be redirected (`>`) to a file descriptor (`&`) that follows (`1`). 
  - The `2>&` all has to appear together without spaces; otherwise the 2 would look just like another argument, and 
  - the `&` actually means something completely different when it appears by itself. (It has to do with running the command in the background.) 
- If you want to have error messages (i.e., STDERR) included in the redirection, specify that redirection after redirecting STDERR, like this: 
  ```bash
  ls >> /tmp/ls.out 2>&1 
  ```
- As of bash version 4 you can combine both of those redirections in one: 
  ```bash
  ls &>> /tmp/ls.out
  ```
  which will redirect both STDERR and STDOUT and append them to the specified file. 
  Just remember that the **ampersand** must come first and no spacing is allowed between the three characters. 

## Throwing Output Away 

Redirect the output to `/dev/null` as shown in these examples: 
```
find / -name myfile -print 2> /dev/null 
```
or: 
```
Noisy > /dev/null 2>&1
```

## Skipping a Header in a File 

Folloiwng command won't display the first line of file `lines`.
```
$ tail -n +2 lines 
Line 2
Line 3
Line 4 
Line 5 
$ 
```

`tail -n +3` won't display the first two lines in file `lines`.

- An argument to tail, of the format `-n` number (or just `-number`), will specify a line offset relative to the end of the file. 
  - So, `tail -n 10` file shows the last 10 lines of file, which also happens to be the default if you don’t specify anything. 
- Specifying a number starting with a plus sign (`+`) indicates an offset relative to the top of the file. 
  - Thus, `tail -n +1` file gives you the entire file, `tail -n +2` skips the first line, and so on. 

For `head` command:
```
head -n -2 filename
```
Will display first `(total_line - 2)` lines 

## Saving or Grouping Output from Several Commands 

Use braces (`{ }`) to group these commands together; then redirection applies to the output from all commands in the group. For example: 
```
{ pwd; ls; cd ../elsewhere; pwd; ls; } > /tmp/all.out 
```
Alternatively, you could use parentheses, `()`, to tell bash to run the commands in a **subshell**, then redirect the output of the entire subshell’s execution. For example: 
```
(pwd; ls; cd ../elsewhere; pwd; ls) > /tmp/all.out 
```

## Keeping Files Safe from Accidental Overwriting 


Tell the shell to be more careful, as follows: 
```
set -o noclobber 
```
If you decide you don’t want to be so careful after all, then turn the option off: 
```
set +o noclobber
```

But,
Use `>|` to redirect your output. Even if `noclobber` is set, bash ignores its setting and overwrites the file. 

# Standard Input 

## Keeping Your Data with Your Script 

Use **a here-document** with the `<<` characters, redirecting the text from the command line rather than from a file. When put into a shell script, the script file then contains the data along with the script. 
Here’s an example of a shell script in a file we call `ext`: 
```bash
$ cat ext
#
# here is a "here" document #
grep $1 <<EOF
mike  x.123 
joe  x.234
sue  x.555
pete x.818
sara x.822
bill x.919
EOF
$ 
```

## Indenting Here-Documents 

Use `<<-`, and then you can use tab characters (only!) at the beginning of lines to indent this portion of your shell script

## Getting User Input 
Use the read statement: 
```
read 
or: 	read -p "answer me this " ANSWER 
or: 	read -t 3 -p "answer quickly: " ANSWER 
or: 	read PRE MID POST
```

**Prompting for a Password** 
Use the read command to read the user’s input, but with a special option to turn off echoing: 
```bash
read -s -p "password: " PASSWD 
printf "%b" "\n" 
```


# Executing Commands 

## Running Several Commands in Sequence 

If you want to run each program regardless of whether the preceding ones fail, separate them with semicolons: 
```
long ; medium ; short
```
If you only want to run the next program if the preceding program worked, and all the programs correctly set exit codes, separate them with double ampersands: 
```    
long && medium && short
```

Running Several Commands All at Once 
```
$ long & medium & short 
```

## Running Long Jobs Unattended 

If you want to run a job in the background and expect to exit the shell before the job completes, then you need to `nohup` the job: 
```
$ nohup long &nohup
: appending output to `nohup.out' 
$
```

## Running All Scripts in a Directory 
```bash
for SCRIPT in /path/to/scripts/dir/* 
do 	
    if [ -f "$SCRIPT" -a -x "$SCRIPT" ] 
	then 		
        $SCRIPT 	
    fi 
done 
```

# Basic Scripting: Shell Variables 


## Getting the Absolute Value of a Number
bash doesn’t seem to have an absolute value function. Use string manipulation: 
```bash
${MYVAR#-}
```

## Using bash for basename 

Yes, bash can strip the directory path from a shell variable string and leave just the last part of the path (the filename). Where you may want to write: 
```bash
FILE=$(basename $FULLPATHTOFILE) 
```
instead you need only write: 
```bash
FILE=${FULLPATHTOFILE##*/} 
```

**Using bash for dirname** 
```bash
DIR=${MYPATHTOFILE%/*} 
```

## Using Alternate Values for Comma Separated Values 

You want to make a list of values separated by commas, but you don’t want a leading or trailing comma. If you write `LIST="${LIST},${NEWVAL}"` inside a loop to build up the list, then the first time (when LIST is null) you’ll end up with a leading comma. You could special-case the initialization of LIST so that it gets the first element before entering the loop, but if that’s not practical, or to avoid duplicate code (for getting a new value), you can instead use the `${:+}` syntax in bash: 
```bash
LIST="${LIST}${LIST:+,}${NEWVAL}"
```

## Using Array Variables 

Arrays are easy to initialize if you know the values as you write the script. The format is simple: 
`MYRA=(first second third home)` Each element of the array is a separate word in the list enclosed in parentheses. 

Then you can refer to each this way: 
```bash
echo runners on ${MYRA[0]} and ${MYRA[2]} 
```
This output is the result: 
```bash
runners on first and third
```

## Converting Between Upper- and Lowercase ??

As of bash 4.0 there are a few operators to do case conversion when referencing a variable name. If `$FN` is the variable in which you put a filename (i.e., string) that you want converted to lowercase, 
- then `${FN,,}` will return that string in all lowercase. 
- Similarly, `${FN^^}` will return the string in all uppercase. 
- There is even the `${FN~~}` operator to swap case

## Converting to Camel Case ??

Use a combination of an array and case conversion substitution: 
```bash
while read TXT 
do 
	RA=($TXT) # must be ($ not $( 
	echo ${RA[@]^} 
done 
```

# Shell Logic and Arithmetic

## Doing Arithmetic in Your Shell Script 
Use `$(( ))` or `let` for integer arithmetic expressions. For example: 
```bash
COUNT=$((COUNT + 5 + MAX * 2)) 
let COUNT+='5+MAX*2'
```

- Spaces are not needed, nor are they prohibited around operators and arguments (though `**` must be together) within a `$(( ))` expression. 
- But you must not have spaces around the equals sign, as with any bash variable assignment. Also, be sure to quote `let` expressions since the `let` statement is a bash builtin and its arguments will undergo word expansion. 
```bash
echo $(( X+=5 , Y*=3 ))
let X+=5  Y*=3
```
These both work: 
```
let i=2+2
let "i = 2 + 2"
```

## Testing with Pattern Matches 
Use the double-bracket compound statement in an if statement to enable shell-style pattern matches on the righthand side of the equality operator: 
```bash
if [[ "${MYFILENAME}" == *.jpg ]] 
```

Grouping symbols for extended pattern matching:
```
@(...)  Only one occurence
*(...)  Zero or more occurences
+(...)  One or more occurences
?(...)  Zero or one occurence
!(...)  Not this, but anything else
```

Matches are case-sensitive, but you may use `shopt -s nocasematch` (in bash versions 3.1+) to change that. This option affects case and `[[` commands. 

shopt is a shell builtin command to set and unset (remove) various Bash shell options. To see current settings, type:
```bash
shopt
```

# Additional Features for Scripting 

## “Daemon-izing” Your Script 

Sometimes you want a script to run as a daemon, in the background and never ending. 
Use the following to invoke your script, run it in the background, and still allow yourself to log out: 
```bash
nohup mydaemonscript 0<&-1>/dev/null 2>&1 & 
```
or:
```bash 
nohup mydaemonscript >>/var/log/myadmin.log 2>&1 <&- &
```

You need to close the controlling TTY (terminal), which is connected in three ways to your (or any) job: 
- via standard input (STDIN), 
- standard output (STDOUT), and 
- standard error (STDERR). 

We can close STDOUT and STDERR by pointing them at another file—typically either a logfile, so that you can retrieve their output at a later time, or the file `/dev/null` to throw away all their output. We use the redirecting operator `>` to do this. 

But what about STDIN? The cleanest way to deal with STDIN is to close the file descriptor. The bash syntax to do that is like a redirect, but with a dash for the filename `(0<&- or <&-)`. 

We use the `nohup` command so that the script is run without being interrupted by a hangup signal when we log off. 

## Avoiding Aliases and Functions 

Here are some examples: 
```bash
$ alias echo='echo ~~~' 
$ echo test 
~~~ test 
$ \echo test 
test 
$ builtin echo test 
test 
$ type echo
echo is aliased to `echo ~~~' 
$ unalias echo 
$ type echo 
echo is a shell builtin 
```

# Advanced Scripting 

## Finding bash Portably for `#!` 

You need to run a bash script on several machines, but bash is not always in the same place 
Use the `/usr/bin/env` command in the shebang line, as in `#!/usr/bin/env bash`. 

`env’s` purpose is to “run a program in a modified environment,” but since it will search the path for the command it is given to run, it works very well for this use. 

Therefore, our advice is to omit the - when using env for portability, and to hardcode the interpreter and trailing - when security is critical. 

## Setting a POSIX $PATH 

You are on a machine that provides older or proprietary tools (e.g., Solaris) and you need to set your path so that you get POSIX-compliant tools. 
Use the **getconf** utility: 
```bash
PATH=$(PATH=/bin:/usr/bin getconf PATH) 
```
`getconf` reports various system configuration variables, so you can use it to set a default path. However, unless getconf itself is a builtin, you will need a minimal path to find it, hence the `PATH=/bin:/usr/bin` part of the solution. 

## Developing Portable Shell Scripts 

You are writing a shell script that will need to run on multiple versions of multiple Unix or POSIX operating systems. 

First, try using the `command` builtin with its `-p` option to find the POSIX version of program. For example, in `/usr/xpg4` or `/usr/xpg6` on Solaris: 
```bash
command -p program args 
```

`command -p` uses a default path that is guaranteed to find all of the POSIX-standard utilities. 

## Using for Loops Portably 

You need to do a `for` loop but want it to work on older versions of bash.
This method is portable back to bash 2.04+: 
```bash
$ for ((i=0; i<10; i++)); do echo $i; done 
```

There are nicer ways of writing this loop in newer versions of bash, but they are not backward compatible. As of bash 3.0+ you can use the syntax `for {x..y}`, as in: 
```bash
$ for i in {1..10}; do echo $i; done 
```
If your system has the `seq` command, you could also do this: 
```bash
$ for i in $(seq 1 10); do echo $i; done 
```

## Using bash Net-Redirection ?
You need to send or receive very simple network traffic but you do not have a tool such as Netcat installed. 
If you have bash version 2.04+ compiled with ``--enable-net-redirections`` (default), you can use bash itself. 
```bash
$ exec 3<> /dev/tcp/checkip.dyndns.org/80 
$ echo -e "GET / HTTP/1.0\n" >&3
$ cat <&3
```

```
root@laimeet:/tmp# exec 3<> /dev/tcp/checkip.dyndns.org/80 
root@laimeet:/tmp# echo -e "GET / HTTP/1.0\n" >&3
root@laimeet:/tmp# cat <&3
HTTP/1.1 200 OK
Content-Type: text/html
Server: DynDNS-CheckIP/1.0.1
Connection: close
Cache-Control: no-cache
Pragma: no-cache
Content-Length: 104

<html><head><title>Current IP Check</title></head><body>Current IP Address: 47.105.79.16</body></html>
root@laimeet:/tmp# 
```

## Finding My IP Address 

You need to know the IP address of the machine you are running on. 
First, you can parse output from `ifconfig` to look for IP addresses. 
Second, you can get your hostname and resolve it back to an IP address. 
Use at your own risk and test well: 
```bash
host $(hostname)
```
Third, you may be more interested in your host’s external, routable address than its internal RFC 1918 address. 
```bash
$  wget -qO - http://ipinfo.io/ 
$  wget -qO - http://ipinfo.io/ip/ 
$ lynx -dump http://ipinfo.io/ip/ 
$ curl whatismyip.akamai.com 
$ curl http://checkip.amazonaws.com 
```

## Redirecting Output for the Life of a Script 

You’d like to **redirect output for an entire script**, and you’d rather not have to edit every `echo` or `printf` statement. 
Use a little-known feature of the `exec` command to redirect STDOUT or STDERR:
```bash
# Optional, save the "old" STDERR 
exec 3>&2
# Redirect any output to STDERR to an error logfile instead 
exec 2> /path/to/error_log 

# Script with "globally" redirected STDERR goes here  

# Turn off redirect by reverting STDERR and closing FH3
exec 2>&3- 
```

Usually exec replaces the running shell with the command supplied in its arguments, destroying the original shell. However, if no command is given, it can manipulate redirection in the current shell. You are not limited to redirecting STDOUT or STDERR, but they are the most common targets for redirection in this case.

## Logging to syslog from Your Script 

Use logger, Netcat, or bash’s built-in network redirection features.

logger is installed by default on most systems and is an easy way to send messages to the local syslog service:
```bash
$ logger -p local0.notice -t ${0##*/}[$$] test message
```
However, it does not send syslog to remote hosts by itself. If you need to do that, you can use bash: 
```bash
# Netcat
$ echo "<133>${0##*/}[$$]: Test syslog message from Netcat" | nc -w1 -u loghost 514

# bash
$ echo "<133>${0##*/}[$$]: Test syslog message from bash" \
  > /dev/udp/loghost.example.com/514
```

# Configuring and Customizing bash

# Housekeeping and Administrative Tasks

## Recovering Disconnected Sessions Using screen

Problem
You run long processes over SSH, perhaps over the WAN, and when you get disconnected you lose a lot of work. Or perhaps you started a long job from work, but need to go home and be able to check on the job later; you could run your process using `nohup`, but then you won’t be able to reattach to it when your connection comes back or you get home.

Solution
Install and use GNU `screen`.


## Sharing a Single bash Session 

Problem
You need to share a single bash session for training or troubleshooting purposes, and there are too many people for “over the shoulder” to work. Or you need to help some‐ one who’s located somewhere else, and you need to share a session across a network.

Solution
Use GNU screen in multiuser mode. 


## Logging an Entire Session or Batch Job 

Problem
You need to capture all the output from an entire session or a long batch job.

Solution
There are many ways to solve this problem, depending on your needs and environ‐ ment.
The simplest solution is to turn on logging to memory or disk in your terminal pro‐ gram. The problems with that are that your terminal program may not allow it, and when it gets disconnected you lose your log.
The next simplest solution is to modify the job to log itself, or redirect the entire thing to tee or a file. For example, one of the following might work:
```bash
    long_noisy_job >& log_file
    long_noisy_job 2>&1 | tee log_file
    ( long_noisy_job ) >& log_file
    ( long_noisy_job ) 2>&1 | tee log_file
```
The problems here are that you may not be able to modify the job, or the job itself may do something that precludes these solutions (e.g., if it requires user input, it could get stuck asking for the input before the prompt is actually displayed). 

The third solution is to use an interesting program called `script` that exists for this very purpose, and its probably already on your system. You run `script`, and it logs everything that happens to the logfile (called a `typescript`) you’ve given it, which is OK if you want to log the entire session—just start `script`, then run your job. But if you only want to capture part of the session, there is no way to have your code start script, run something to log it, then stop script again. 

Our final solution uses the terminal multiplexer screen. With screen, you can turn whole session logging on or off from inside your script. Once you are already running screen, do the following in your script:
```bash
# Set a logfile and turn on logging
screen -X logfile /path/to/logfile && screen -X log on

# Your commands here

# Turn logging back off
screen -X logfile 1 # Set buffer to 1 sec
sleep 3 # Wait to avoid file truncation... 
screen -X log off
```

## Counting Differences in Files 

Problem
You have two files and need to know about how many differences exist between them.

Solution
Count the hunks (i.e., sections of changed data) in diff’s output:
```bash
$ diff -C0 original_file modified_file | grep -c "^\*\*\*\*\*"
2
$ diff -C0 original_file modified_file
*** original_file Fri Nov 24 12:48:35 2006 --- modified_file Fri Nov 24 12:48:43 2006 ***************
*** 1 ****
! This is original_file, and this line is different. --- 1 ---
! This is modified_file, and this line is different. ***************
*** 6 ****
! But this one is different.
--- 6 ---
! But this 1 is different.
```

If you only need to know whether the files are different and not how many differences there are, use `cmp`. It will exit at the first difference, which can save time on large files. Like diff, it is silent if the files are identical, but it reports the location of the first difference if not:
```
$ cmp original_file modified_file
original_file modified_file differ: char 9, line 1
```

## Using sudo on a Group of Commands 

Problem
You are running as a regular user and need to sudo several commands at once, or you need to use redirection that applies to the commands and not to sudo.

Solution
Use `sudo` to run a subshell in which you may group your commands and use pipelines and redirection:
```bash    
sudo bash -c 'command1 && command2 || command3'
```

If you try something like`sudo command1 && command2 || command3` you’ll find that `command2` and `command3` are running as you, not as root. That’s because sudo’s influence only extends to the **first command** and your shell is doing the rest. 

Note the use of the `-c` argument to bash, which causes it to just execute the given commands and exit. Without that you will just end up running a new interactive root shell, which is probably not what you wanted. 

## Numbering Lines 

Problem
You need to number the lines of a text file for reference or for use as an example.

Solution
Note that our sample file named lines has a trailing blank line:
```bash
$ i=0; while IFS= read -r line; do (( i++ )); echo "$i $line"; done < lines 
1 Line 1
2 Line 2
3
4 Line 4
5 Line 5
6
```

Or a useful use of cat:
```bash
$ cat -n lines 
1 Line 1 
2 Line 2
3
4 Line 4
5 Line 5
6

$ cat -b lines 
1 Line 1 
2 Line 2 
3 Line 4 
4 Line 5
```


# Working Faster by Typing Less 


## Reusing Arguments 
Reusing the last command is easy with `!!`, but you don’t always want the whole command. How can you reuse just the last argument? 
- Use `!$` to indicate the last argument of the preceding command. 
- Use `!:1` for the first argument on the command line, `!:2` for the second, and so on. 


# Tips and Traps: Common Goofs for Novices 

## Forgetting to Set Execute Permissions 

You’ve got your script all written and want to try it out, but when you go to run the script you get an error message: 
```
$ ./my.script
bash: ./my.script: Permission denied 
$ 
```
You have two choices. 
- First, you could invoke bash and give it the name of the script as a parameter: 
```bash
bash my.script 
```
- Or second (and better still), you could set execute permissions on the script so that you can run it directly: 
```bash
chmod a+x my.script 
./my.script 
```

## Fixing “No such file or directory” Errors 

Try running the script using bash explicitly: 
```bash
bash ./busted 
```

- If it works, you have some kind of permissions error, or a typo in your shebang line. 
- If you get a bunch more errors, you probably have the wrong line endings. This can happen if you’ve edited the file on Windows (perhaps via Samba), or if you’ve simply copied the file around. 
- If you run the `file` command on your suspect script, it can tell you if your line endings are wrong. It may say something like this: 
```bash
$ file ./busted
./busted: Bourne-Again shell script, ASCII text executable, with CRLF line terminators
$ 
```
To fix it, try the `dos2unix` program if you have it 

## Forgetting that Pattern Matching Alphabetizes 
 
bash will alphabetize the data in a pattern match: 
```bash
$ echo x.[ba] 
x.a x.b
$ 
```

Even though you specified `b` then `a` in the square brackets, when the pattern matching is done and the results found, they will be **alphabetized** before being given to the command to execute. That means that you don’t want to do this: 
```bash
mv x.[ba] 
```
thinking that it will expand to: 
```bash
mv x.b x.a 
```
Rather, it will expand to: 
```bash
mv x.a x.b 
```
since bash alpha-sorts the results before putting them in the command line, which is exactly the opposite of what you intended! 
However, if you use `braces` to enumerate your different values, it will keep them in the specified order. This will do what you intended and not change the order: 
```bash
mv x.{b,a} 
```

## Making Your Terminal Sane Again Problem 
You have aborted an SSH session and now you can’t see what you are typing. Or perhaps you accidentally displayed a binary file and your terminal window is now full of gibberish. 

Solution Type `stty sane` and then press the Enter key, even if you can’t see what you are typing, to restore sane terminal settings. You may want to hit Enter a few times first, to make sure you don’t have anything else on your input line before you start typing the stty command. If you do this a lot, you might consider creating an alias that’s easier to type blind

## Deleting Files Using an Empty Variable Problem 

You have a variable that you think contains a list of files to delete, perhaps to clean up after your script. But in fact, the variable is **empty** and Bad Things happen. 

Never do: 

```bash
rm -rf $files_to_delete 
```

Never, ever, ever do:
```bash
rm -rf /$files_to_delete 
```

Use this instead: 
```bash
[ -n "$files_to_delete" ] && rm -rf $files_to_delete 
```

The solution is easy. 
- First, make sure that there is some value in the variable you’re using, and 
- second, never precede that variable with a `/`.

## Testing bash Script Syntax 

You are editing a bash script and want to make sure that your syntax is correct. Use the `-n` argument to bash to test syntax often, ideally after every save, and certainly before committing any changes to a revision control system: 
```bash
$ bash -n my_script
$ echo 'echo "Broken line' >> my_script 
$ bash -n my_script
my_script: line 4: unexpected EOF while looking for matching `"' 
my_script: line 5: syntax error: unexpected end of file 
```

## Debugging Scripts 

You can’t figure out what’s happening in your script and why it doesn’t work as expected. 

- Add s`et -x` to the top of the script when you run it, or 
- use `set -x` to turn on `xtrace` before a troublesome spot and `set +x` to turn it off after. 
- You may also wish to experiment with the `$PS4` prompt. `xtrace` also works on the interactive command line. 

## Confusing Shell Wildcards and Regular Expressions Problem

- Regular expression syntax is only used with the **=~** comparison operator in bash. 
- All of the other expressions in bash use shell pattern matching. 
