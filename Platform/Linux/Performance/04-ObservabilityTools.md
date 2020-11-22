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
