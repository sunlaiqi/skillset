- [7 Job Control](#7-job-control)
  - [7.1 Job Control Basics](#71-job-control-basics)
  - [7.2 Job Control Builtins](#72-job-control-builtins)
    - [bg](#bg)
    - [fg](#fg)
    - [jobs](#jobs)
    - [kill](#kill)
    - [wait](#wait)
    - [disown](#disown)
    - [suspend](#suspend)
  - [7.3 Job Control Variables](#73-job-control-variables)
    - [auto_resume](#auto_resume)


# 7 Job Control

## 7.1 Job Control Basics

Job control refers to the ability to selectively stop (suspend) the execution of processes and continue (resume) their execution at a later point. A user typically employs this facility via an interactive interface supplied jointly by the operating system kernel’s terminal driver and Bash.

The shell associates a job with each pipeline. 
- It keeps a table of currently executing jobs, which may be listed with the `jobs` command. 
- When Bash starts a job asynchronously, it prints a line that looks like:
```
[1] 25647
```
indicating that this job is job number 1 and that the process ID of the last process in the pipeline associated with this job is 25647. 
- All of the processes in a single pipeline are members of the same job. 
- Bash uses the job abstraction as the basis for job control.

To facilitate the implementation of the user interface to job control, the operating system maintains the notion of **a current terminal process group ID**. 
- Members of this process group (processes whose process group ID is equal to the current terminal process group ID) receive keyboard-generated signals such as SIGINT. 
  - These processes are said to be in the foreground. 
- Background processes are those whose process group ID differs from the terminal’s; 
  - such processes are immune to keyboard-generated signals. 
- Only foreground processes are allowed to read from or, if the user so specifies with `stty tostop`, write to the terminal. 
- Background processes which attempt to read from (write to when `stty tostop` is in effect) the terminal are sent a SIGTTIN (SIGTTOU) signal by the kernel’s terminal driver, which, unless caught, suspends the process.

If the operating system on which Bash is running supports job control, Bash contains facilities to use it. 
- Typing the suspend character (typically ‘^Z’, Control-Z) while a process is running causes that process to be stopped and returns control to Bash. 
- Typing the delayed suspend character (typically ‘^Y’, Control-Y) causes the process to be stopped when it attempts to read input from the terminal, and control to be returned to Bash. 
- The user then manipulates the state of this job, 
  - using the `bg` command to continue it in the background, 
  - the `fg` command to continue it in the foreground, 
  - or the `kill` command to kill it. 
- A ‘^Z’ takes effect immediately, and has the additional side effect of causing pending output and typeahead to be discarded.

There are a number of ways to refer to a job in the shell. The character ‘%’ introduces a job specification (jobspec).

- Job number `n` may be referred to as ‘%n’. 
- The symbols ‘%%’ and ‘%+’ refer to the shell’s notion of the current job, which is the last job stopped while it was in the foreground or started in the background. 
- A single ‘%’ (with no accompanying job specification) also refers to the current job. 
- The previous job may be referenced using ‘%-’. 
- If there is only a single job, ‘%+’ and ‘%-’ can both be used to refer to that job. 
- In output pertaining to jobs (e.g., the output of the jobs command), the current job is always flagged with a ‘+’, and the previous job with a ‘-’.

A job may also be referred to using a prefix of the name used to start it, or using a substring that appears in its command line. 
- For example, ‘%ce’ refers to a stopped job whose command name begins with ‘ce’. 
- Using ‘%?ce’, on the other hand, refers to any job containing the string ‘ce’ in its command line. 
- If the prefix or substring matches more than one job, Bash reports an error.

Simply naming a job can be used to bring it into the foreground: 
- ‘%1’ is a synonym for ‘fg %1’, bringing job 1 from the background into the foreground. 
- Similarly, ‘%1 &’ resumes job 1 in the background, equivalent to ‘bg %1’

The shell learns immediately whenever a job changes state. 
- Normally, Bash waits until it is about to print a prompt before reporting changes in a job’s status so as to not interrupt any other output. 
- If the `-b` option to the `set` builtin is enabled, Bash reports such changes immediately. 
- Any trap on SIGCHLD is executed for each child process that exits.

- If an attempt to exit Bash is made while jobs are stopped, (or running, if the `checkjobs` option is enabled – see The Shopt Builtin), the shell prints a warning message, 
- and if the `checkjobs` option is enabled, lists the jobs and their statuses. 
- The `jobs` command may then be used to inspect their status. 
- If a second attempt to exit is made without an intervening command, Bash does not print another warning, and any stopped jobs are terminated.

- When the shell is waiting for a job or process using the `wait` builtin, and job control is enabled, `wait` will return when the job changes state. 
  - The `-f` option causes `wait` to wait until the job or process terminates before returning.

## 7.2 Job Control Builtins

### bg

```bash
bg [jobspec …]
```

Resume each suspended job jobspec in the background, as if it had been started with ‘&’. 
- If jobspec is not supplied, the current job is used. 
- The return status is zero unless it is run when job control is not enabled, or, when run with job control enabled, any jobspec was not found or specifies a job that was started without job control.

### fg

```bash
fg [jobspec]
```

Resume the job jobspec in the foreground and make it the current job. 
- If jobspec is not supplied, the current job is used. 
- The return status is that of the command placed into the foreground, or non-zero if run when job control is disabled or, when run with job control enabled, jobspec does not specify a valid job or jobspec specifies a job that was started without job control.

### jobs

```bash
jobs [-lnprs] [jobspec]
jobs -x command [arguments]
```

The first form lists the active jobs. The options have the following meanings:

`-l`
List process IDs in addition to the normal information.

`-n`
Display information only about jobs that have changed status since the user was last notified of their status.

`-p`
List only the process ID of the job’s process group leader.

`-r`
Display only running jobs.

`-s`
Display only stopped jobs.

If jobspec is given, output is restricted to information about that job. If jobspec is not supplied, the status of all jobs is listed.

If the `-x` option is supplied, jobs replaces any jobspec found in command or arguments with the corresponding process group ID, and executes command, passing it arguments, returning its exit status.

### kill

```bash
kill [-s sigspec] [-n signum] [-sigspec] jobspec or pid
kill -l|-L [exit_status]
```

Send a signal specified by sigspec or signum to the process named by job specification jobspec or process ID pid. 
- sigspec is either a case-insensitive signal name such as SIGINT (with or without the SIG prefix) or a signal number; signum is a signal number. 
- If sigspec and signum are not present, SIGTERM is used. 
- The `-l` option lists the signal names. 
- If any arguments are supplied when `-l` is given, the names of the signals corresponding to the arguments are listed, and the return status is zero. 
- `exit_status` is a number specifying a signal number or the exit status of a process terminated by a signal. 
- The `-L` option is equivalent to `-l`. 
- The return status is zero if at least one signal was successfully sent, or non-zero if an error occurs or an invalid option is encountered.

### wait

```bash
wait [-fn] [-p varname] [jobspec or pid …]
```

Wait until the child process specified by each process ID pid or job specification jobspec exits and return the exit status of the last command waited for. 
- If a job spec is given, all processes in the job are waited for. 
- If no arguments are given, wait waits for all running background jobs and the last-executed process substitution, if its process id is the same as `$!`, and the return status is zero. 
- If the `-n` option is supplied, `wait` waits for a single job from the list of pids or jobspecs or, if no arguments are supplied, any job, to complete and returns its exit status. 
- If none of the supplied arguments is a child of the shell, or if no arguments are supplied and the shell has no unwaited-for children, the exit status is 127. 
- If the `-p` option is supplied, the process or job identifier of the job for which the exit status is returned is assigned to the variable `varname` named by the option argument. 
  - The variable will be unset initially, before any assignment. 
  - This is useful only when the `-n` option is supplied. 
- Supplying the `-f` option, when job control is enabled, forces `wait` to wait for each pid or jobspec to terminate before returning its status, intead of returning when it changes status. 
- If neither jobspec nor pid specifies an active child process of the shell, the return status is 127.

### disown

```bash
disown [-ar] [-h] [jobspec … | pid … ]
```

- Without options, remove each jobspec from the table of active jobs. 
- If the `-h` option is given, the job is not removed from the table, but is marked so that SIGHUP is not sent to the job if the shell receives a SIGHUP. 
- If jobspec is not present, and neither the `-a` nor the `-r` option is supplied, the current job is used. 
- If no jobspec is supplied, 
  - the `-a` option means to remove or mark all jobs; 
  - the `-r` option without a jobspec argument restricts operation to running jobs.

### suspend

```bash
suspend [-f]
```

Suspend the execution of this shell until it receives a SIGCONT signal. 
- A login shell cannot be suspended; 
  - the `-f` option can be used to override this and force the suspension.

When job control is not active, the `kill` and `wait` builtins do not accept jobspec arguments. They must be supplied process IDs.

## 7.3 Job Control Variables

### auto_resume

This variable controls how the shell interacts with the user and job control. 
- If this variable exists then single word simple commands without redirections are treated as candidates for resumption of an existing job. 
- There is no ambiguity allowed; if there is more than one job beginning with the string typed, then the most recently accessed job will be selected. 
- The name of a stopped job, in this context, is the command line used to start it. 
- If this variable is set to the value ‘exact’, the string supplied must match the name of a stopped job exactly; 
- if set to ‘substring’, the string supplied needs to match a substring of the name of a stopped job. 
- The ‘substring’ value provides functionality analogous to the ‘%?’ job ID. 
- If set to any other value, the supplied string must be a prefix of a stopped job’s name; this provides functionality analogous to the ‘%’ job ID.












