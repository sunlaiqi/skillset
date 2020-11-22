- [Observability Tools](#observability-tools)
  - [Tool Types](#tool-types)
    - [Counters](#counters)
    - [Tracing](#tracing)
    - [Profiling](#profiling)
    - [Monitoring (sar)](#monitoring-sar)
  - [Observability Sources](#observability-sources)
    - [/proc](#proc)
    - [/sys](#sys)
    - [Other Observability Sources](#other-observability-sources)
  - [DTrace](#dtrace)
    - [Probes](#probes)
    - [D Language](#d-language)
    - [Overheads](#overheads)
  - [perf](#perf)
    - [SystemTap](#systemtap)
    - [perf](#perf-1)
    - [Other Tools](#other-tools)
    - [Visualizations](#visualizations)
  - [Experimentation](#experimentation)
    - [Ad Hoc](#ad-hoc)
    - [SysBench](#sysbench)
  - [Tuning](#tuning)
    - [Compiler Options](#compiler-options)
    - [Scheduling Priority and Class](#scheduling-priority-and-class)
    - [Scheduler Options](#scheduler-options)
    - [Process Binding](#process-binding)
    - [Exclusive CPU Sets](#exclusive-cpu-sets)
    - [Resource Controls](#resource-controls)
    - [Processor Options (BIOS Tuning)](#processor-options-bios-tuning)

# Observability Tools

With the addition of tracing frameworks, especially dynamic tracing, everything can now be observed, and virtually any activity can be observed directly. 

## Tool Types

Performance observability tools can be categorized as providing system-wide or per-process observability, and most are based on either counters or tracing.

![Tool Types](Images/ToolTypes.png)

### Counters

Kernels maintain various statistics, called counters, for counting events. They are usually implemented as unsigned integers that are incremented when events occur. For example, there are counters for the number of network packets received, disk I/O issued, and system calls performed.


Counters are considered “free” to use since they are enabled by default and maintained continually by the kernel. The only additional cost when using them is the act of reading their values from user- land (which should be negligible). 

### Tracing

Tracing collects per-event data for analysis. Tracing frameworks are not typically enabled by default, since tracing incurs CPU overhead to capture the data and can require significant storage to save it.

Logging, including the system log, can be thought of as low-frequency tracing that is enabled by default. Logging includes per-event data, although usually only for infrequent events such as errors and warnings.

### Profiling

Profiling characterizes the target by collecting a set of samples or snapshots of its behavior. CPU usage is a common example, where samples are taken of the program counter or stack trace to characterize the code paths that are consuming CPU cycles. These samples are usually collected at a fixed rate, such as 100 or 1,000 Hz (cycles per second) across all CPUs. Profiling tools, or profilers, sometimes vary this rate slightly to avoid sampling in lockstep with target activity, which could lead to over- or undercounting.

### Monitoring (sar)

sar(1) is counter-based and has an agent that executes at scheduled times (via cron) to record the state of system counters. 

## Observability Sources


Type    | Linux 
---     | ---
Per-process counters    | /proc
System-wide counters    | /proc, /sys
Device driver and debug info    | /sys
Per-process tracing | ptrace, uprobes
CPU performance counters    | perf_event
Network tracing | libpcap
Per-thread latency metircs  | delay accounting
System-wide tracing | tracepoints, kprobes, ftrace

### /proc

/proc is dynamically created by the kernel and is not backed by storage devices (it runs in- memory). It is mostly read-only, providing statistics for observability tools. Some files are writeable, for controlling process and kernel behavior.

The file system type for /proc on Linux is “proc”.

Various files are provided in /proc for per-process statistics. 

Those related to per-process performance observability include
- limits: in-effect resource limits
- maps: mapped memory regions
- sched: various CPU scheduler statistics
- schedstat: CPU runtime, latency, and time slices
- smaps: mapped memory regions with usage statistics
- stat: process status and statistics, including total CPU and memory usage 
- statm: memory usage summary in units of pages
- status: stat and statm information, human-readable
- task: directory of per-task statistics

Linux has also extended /proc to include system-wide statistics, contained in these additional files
and directories:
$ cd /proc; ls -Fd [a-z]*

System-wide files related to performance observability include
- cpuinfo: physical processor information, including every virtual CPU, model name, clock speed, and cache sizes.
- diskstats: disk I/O statistics for all disk devices
- interrupts: interrupt counters per CPU
- loadavg: load averages
- meminfo: system memory usage breakdowns
- net/dev: network interface statistics
- net/tcp: active TCP socket information
- schedstat: system-wide CPU scheduler statistics
- self: a symlink to the current process ID directory, for convenience 
- slabinfo: kernel slab allocator cache statistics
- stat: a summary of kernel and system resource statistics: CPUs, disks, paging, swap, processes
- zoneinfo: memory zone information

These are read by system-wide tools. /proc files are usually text formatted, allowing them to be read easily from the command line and processed by shell scripting tools. 

### /sys

Linux provides a sysfs file system, mounted on /sys, which was introduced with the 2.6 kernel to provide a directory-based structure for kernel statistics. This differs from /proc, which has evolved over time and had various system statistics added to the top-level directory. sysfs was originally designed to provide device driver statistics but has been extended to include any statistic type.


The /sys file system typically has tens of thousands of statistics in read-only files, as well as many writeable files for changing kernel state. For example, CPUs can be set to online or offline by writing “1” or “0” to a file named “online.” As with reading statistics, setting state can be performed by using text strings at the command line (echo 1 > filename), rather than a binary interface.

### Other Observability Sources

CPU performance counters: These are programmable hardware registers that provide low- level performance information, including CPU cycle counts, instruction counts, stall cycles, and so on. On Linux they are accessed via the perf_events interface and the perf_event_open() syscall and are consumed by tools including perf(1). 

Per-process tracing: This traces user-level software events, such as syscalls and function calls. It is usually expensive to perform, slowing the target. On Linux there is the ptrace() syscall for controlling process tracing, which is used by strace(1) for tracing syscalls. Linux also has uprobes for user-level dynamic tracing. 

Kernel tracing: On Linux, tracepoints provide static kernel probes (originally kernel makers), and kprobes provide dynamic probes. Both of these are used by tracing tools such as ftrace, perf(1), DTrace, and SystemTap. 

Network sniffing: These interfaces provide a way to capture packets from network devices for detailed investigations into packet and protocol performance. On Linux, sniffing is provided via the libpcap library and /proc/net/dev and is consumed by the tcpdump(8) tool.

Process accounting: This dates back to mainframes and the need to bill departments and users for their computer usage, based on the execution and runtime of processes. 

System calls: Some system or library calls may be available to provide some performance metrics. These include getrusage(), a function call for processes to get their own resource usage statistics, including user- and system-time, faults, messages, and context switches.

More:

Linux: I/O accounting, blktrace, timer_stats, lockstat, debugfs

## DTrace

DTrace is an observability framework that includes a programming language and a tool. This section summarizes DTrace basics, including dynamic and static tracing, probes, providers, D, actions, variables, one-liners, and scripting. 

DTrace can observe all user- and kernel-level code via instrumentation points called probes. When probes are hit, arbitrary actions may be performed in its D language. Actions can include counting events, recording timestamps, performing calculations, printing values, and summarizing data. These actions can be performed in real time, while tracing is still enabled.

A key difference of DTrace from other tracing frameworks (e.g., syscall tracing) is that DTrace is designed to be production-safe, with minimized performance overhead. One way it does this is by use of per-CPU kernel buffers, which improve memory locality, reduce cache coherency overheads, and can remove the need for synchronization locks. These buffers are also used to pass data to user-land at a gentle rate (by default, once per second), minimizing context switches. DTrace also provides a set of actions that can summarize and filter data in-kernel, which also reduces data overheads.

DTrace supports both static and dynamic tracing, each providing complementary functionality. Static probes have a documented and stable interface, and dynamic probes allow virtually unlimited observability as needed.

### Probes

DTrace probes are named with a four-tuple:
```
provider:module:function:name
```
### D Language

The D language is awk-like and can be used in one-liners or scripts (the same as awk). DTrace statements have the form.
```
probe_description /predicate/ { action }
```
The action is a series of optional semicolon-delimited statements that are executed when the probe fires. The predicate is an optional filtering expression.

For example, the statement
```
proc:::exec-success /execname == "httpd"/ { trace(pid); }
```
traces the exec-success probe from the proc provider and performs the printing action trace(pid) if the process name is equal to "httpd". 

### Overheads

As has been mentioned, DTrace minimizes instrumentation overhead by use of per-CPU kernel buffers and in-kernel aggregation summaries. By default, it also passes data from kernel-space to user-space at a gentle asynchronous rate of once per second. It has various other features that reduce overhead and improve safety, including a routine whereby it will abort tracing if it detects that the system may have become unresponsive.

The overhead cost of performing tracing is relative to the frequency of traces and the actions they perform. Tracing block device I/O is typically so infrequent (1,000 I/O per second or less) that the overheads are negligible. On the other hand, tracing network I/O, when packet rates can reach millions per second, can cause significant overhead.]

The action also comes at a cost. For example, I frequently sample kernel stacks at a rate of 997 Hz across all CPUs (using stack()) without a noticeable overhead. Sampling user-level stacks is more involved (using ustack()), for which I typically reduce the rate to 97 Hz.

There are also overheads when saving data into variables, especially associative arrays. While the use of DTrace typically comes without noticeable overhead, you do need to be aware that it is possible, and to use some caution.

##  perf

**Linux Performance Events (LPE)**, perf for short, has been evolving to support a wide range of performance observability activities. While it doesn’t currently have the real-time programmatic capabilities of DTrace or SystemTap, it can perform static and dynamic tracing (based on tracepoints, kprobes, and uprobes), as well as profiling. It can also inspect stack traces, local variables, and data types. Since it is part of the mainline kernel, it may be the easiest to use (if it is already there) and may provide enough observability to answer many of your questions.

Some of the tracing overheads from perf(1) should be similar to those of DTrace. In typical use, DTrace programs are written to summarize data in-kernel (aggregations), which perf(1) does not currently do. With perf(1), data is passed to the user level for post-processing (it has a scripting framework to help), which can cause significant additional overhead when tracing frequent events.

**Kernel Profiling**
DTrace can be used to identify what the kernel is doing.

***One-Liners***
Sample kernel stacks at 997 Hz:
```
dtrace -n 'profile-997 /arg0/ { @[stack()] = count(); }'
```
The most frequent stack is printed last.

**User Profiling**
CPU time spent in user mode can be profiled similarly to the kernel. The following one-liner matches on user-level code by checking on arg1 (user PC) and also matches processes named "mysqld" (MySQL database):
```
# dtrace -n 'profile-97 /arg1 && execname == "mysqld"/ { @[ustack()] = count(); }'
dtrace: description 'profile-97 ' matched 1 probe
```

Sample user stacks at 97 Hz, for PID 123:
```
dtrace -n 'profile-97 /arg1 && pid == 123/ { @[ustack()] = count(); }'
```
Sample user stacks at 97 Hz, for all processes named "sshd":
```
dtrace -n 'profile-97 /arg1 && execname == "sshd"/ { @[ustack()] = count(); }'
```

**Function Tracing**

While profiling can show the total CPU time consumed by functions, it doesn’t show the runtime distribution of those function calls. This can be determined by using tracing and the vtimestamp built-in—a high-resolution timestamp that increments only when the current thread is on-CPU. A function’s CPU time can be measured by tracing its entry and return and calculating the vtimestamp delta.

**CPU Cross Calls**

Excessive CPU cross calls can reduce performance due to their CPU consumption.
```
# dtrace -n 'sysinfo:::xcalls { @[stack()] = count(); }'
```
**Interrupts**
DTrace allows interrupts to be traced and examined.

**Scheduler Tracing**
The scheduler provider (sched) provides probes for tracing operations of the kernel CPU scheduler. 

sched Provider Probes 

Probe       | Description
------------|-----------------------------------------------
on-cpu      | The current thread begins execution on-CPU.
off-cpu     | The current thread is about to end execution on-CPU.
remain-cpu  | The scheduler has decided to continue running the current thread.
enqueue     | A thread is being enqueued to a run queue (examine it via args[]).
dequeue     | A thread is being dequeued from a run queue (examine it via args[]).
preempt     | The current thread is about to be preempted by another.

Since many of these fire in thread context, the curthread built-in refers to the thread in question, and thread-local variables can be used.

### SystemTap

SystemTap can also be used on Linux systems for tracing of scheduler events. 

### perf

A collection of tools for profiling and tracing, now called Linux Performance Events (LPE)

perf Subcommands

Command     | Description
------------|------------------------------------------------------------
annotate    | Read perf.data (created by perf record) and display annotated code.
diff        | Read two perf.data files and display the differential profile.
evlist      | List the event names in a perf.data file.
inject      | Filter to augment the events stream with additional information.
kmem        | Tool to trace/measure kernel memory (slab) properties.
kvm         | Tool to trace/measure kvm guest OS.
list        | List all symbolic event types.
lock        | Analyze lock events.
probe       | Define new dynamic tracepoints.
record      | Run a command and record its profile into perf.data.
report      | Read perf.data (created by perf record) and display the profile.
sched       | Tool to trace/measure scheduler properties (latencies).
script      | Read perf.data (created by perf record) and display trace output.
stat        | Run a command and gather performance counter statistics.
timechart   | Tool to visualize total system behavior during a workload.
top         | System profiling tool.


**System Profiling**
perf(1) can be used to profile CPU call paths, summarizing where CPU time is spent in both kernel- and user-space. This is performed by the record command, which captures samples at regular intervals to a perf.data file. A report com- mand is then used to view the file.
```
# perf record -a -g -F 997 sleep 10
...
# perf report --stdio
```
All CPUs (-a) are sampled with call stacks (-g) at 997 Hz (-F 997) for 10 s (sleep 10). The --stdio option is used to print all the out- put, instead of operating in interactive mode.
These kernel and process `symbols` are available only if their debuginfo files are available; otherwise hex addresses are shown.
perf(1) operates by programming an overflow interrupt for the CPU cycle counter. Since the cycle rate varies on modern processors, a “scaled” counter is used that remains constant.

**Process Profiling**
The fol- lowing command executes the command and creates the perf.data file:
```
# perf record -g command 
```

**Scheduler Latency**
The sched command records and reports scheduler statistics.
```
# perf sched record sleep 10
...
# perf sched latency
```
Scheduler events are frequent, so this type of tracing incurs CPU and storage overhead.
An advantage of the DTrace model of in-kernel filtering and aggregation: it can summarize data while tracing and pass only the summary to user-space, minimiz- ing overhead. 
               
**stat**
The stat command provides a high-level summary of CPU cycle behavior based on CPC.
```
$ perf stat gzip file1
```
The statistics include the cycle and instruction count, and the IPC (inverse of CPI). This is an extremely useful high-level metric for determining the types of cycles occurring and how many of them are stall cycles.

The following lists other counters that can be examined:
```
# perf list
```
Look for both “Hardware event” and “Hardware cache event.” 

These events can be specified using –e.
```
$ perf stat -e instructions,cycles,L1-dcache-load-misses,LLC-load-misses,dTLB-load- misses gzip file1
```

- **L1-dcache-load-misses**: Level 1 data cache load misses. This gives you a measure of the memory load caused by the application, after some loads have been returned from the Level 1 cache. It can be compared with other L1 event counters to determine cache hit rate.
- **LLC-load-misses**: Last level cache load misses. After the last level, this accesses main memory, and so this is a measure of main memory load. The difference between this and L1-dcache-load-misses gives an idea (other counters are needed for completeness) of the effectiveness of the CPU caches beyond Level 1.
- **dTLB-load-misses**: Data translation lookaside buffer misses. This shows the effectiveness of the MMU to cache page mappings for the workload and can measure the size of the memory workload (working set).

**Software Tracing**
`perf record -e` can be used with various software instrumentation points for tracing activity of the kernel scheduler. These include software events and trace-point events (static probes), as listed by `perf list`. 

The following example uses the context switch software event to trace when applications leave the CPU and collects call stacks for 10 s:
```
# perf record -f -g -a -e context-switches sleep 10
...
# perf report --stdio
```

More information can be found using the sched tracepoint events. Kernel sched- uler functions can also be traced directly using dynamic tracepoints (dynamic trac- ing).

### Other Tools

- **oprofile**: the original CPU profiling tool by John Levon.
- **htop**: includes ASCII bar charts for CPU usage and has a more powerful interactive interface than the original top(1).
- **atop**: includes many more system-wide statistics and uses process accounting to catch the presence of short-lived processes.
- **/proc/cpuinfo**: This can be read to see processor details, including clock speed and feature flags.
- **getdelays.c**: This is an example of delay accounting observability and includes CPU scheduler latency per process. 
- **valgrind**: a memory debugging and profiling toolkit. It contains call-grind, a tool to trace function calls and gather a call graph, which can be visualized using kcachegrind; and cachegrind for analysis of hardware cache usage by a given program.

### Visualizations

## Experimentation

When using these tools, it’s a good idea to leave mpstat(1) continually run- ning to confirm CPU usage and parallelism.

### Ad Hoc
This creates a single-threaded workload that is CPU-bound (“hot on one CPU”):
```
# while :; do :; done &
```

### SysBench

The SysBench system benchmark suite has a simple CPU benchmark tool that cal- culates prime numbers. For example:
```
# sysbench --num-threads=8 --test=cpu --cpu-max-prime=100000 run
```
This executed eight threads, with a maximum prime number of 100,000. The run-time was 30.4 s, which can be used for comparison with the results from other sys- tems or configurations.

## Tuning

For CPUs, the biggest performance wins are typically those that eliminate unnec- essary work, which is an effective form of tuning.

### Compiler Options
Compile for 64-bit instead of 32-bit
Select a level of optimizations.

### Scheduling Priority and Class
The range is from -20 to +19. For example:
```
$ nice -n 19 command
```
To change the priority of an already running process, use renice(1).
chrt(1) command can show and set the scheduling priority directly, and the scheduling policy. The scheduling priority can also be set directly using the setpriority() syscall, and the priority and scheduling policy can be set using the sched_setscheduler() syscall.

### Scheduler Options

Example Linux Scheduler Config Option

Option                          | Default|  Description
--------------------------------|--------|------------------------------
CONFIG_CGROUP_SCHED             |y       |  allows tasks to be grouped, allocating CPU time on a group basis
CONFIG_FAIR_GROUP_SCHED         |y       |  allows CFS tasks to be grouped
CONFIG_RT_GROUP_SCHED           |y       |  allows real-time tasks to be grouped
CONFIG_SCHED_AUTOGROUP          | y      |  automatically identifies and creates task groups (e.g., build jobs)
CONFIG_SCHED_SMT                |y      | hyperthreading support
CONFIG_SCHED_MC                 |y      | multicore support
CONFIG_HZ                       |1,000  | sets kernel clock rate (timer interrupt)                      
CONFIG_NO_HZ                    |y      | tickless kernel behavior
CONFIG_SCHED_HRTICK             |y      | use high-resolution timers
CONFIG_PREEMPT                  |n      | full kernel preemption (exception of spin lock regions and interrupts)
CONFIG_PREEMPT_NONE             |n      | no preemption
CONFIG_PREEMPT_VOLUNTARY        |y      | preemption at voluntary kernel code points


Some Linux kernels provide additional tunables (e.g., in /proc/sys/sched).

### Process Binding

A process may be bound to one or more CPUs, which may increase its performance by improving cache warmth and memory locality.
On Linux, this is performed using the taskset(1) command, which can use a CPU mask or ranges to set CPU affinity. For example:
```
$ taskset -pc 7-10 10790
pid 10790's current affinity list: 0-15 
pid 10790's new affinity list: 7-10
```

### Exclusive CPU Sets

Linux provides cpusets, which allow CPUs to be grouped and processes assigned to them.
```
# mkdir /dev/cpuset
# mount -t cpuset cpuset /dev/cpuset 
# cd /dev/cpuset
# mkdir prodset               # create a cpuset called "prodset"
# cd prodset
# echo 7-10 > cpus            # assign CPUs 7-10
# echo 1 > cpu_exclusive      # make prodset exclusive
# echo 1159 > tasks           # assign PID 1159 to prodset
```

### Resource Controls
Apart from associating processes with whole CPUs, modern operating systems pro- vide resource controls for fine-grained allocation of CPU usage.

For Linux, there are container groups (`cgroups`), which can also control resource usage by processes or groups of processes. CPU usage can be controlled using shares, and the CFS scheduler allows fixed limits to be imposed (CPU band-width), in terms of allocating microseconds of CPU cycles per interval. 

### Processor Options (BIOS Tuning)

Processors typically provide settings to enable, disable, and tune processor-level features. On x86 systems, these are typically accessed via the BIOS settings menu at boot time.
The settings usually provide maximum performance by default and don’t need to be adjusted. The most common reason I adjust these today is to disable Intel Turbo Boost, so that CPU benchmarks execute with a consistent clock rate (bearing in mind that, for production use, Turbo Boost should be enabled for slightly faster performance).