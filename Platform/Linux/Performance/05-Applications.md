- [Applications](#applications)
  - [Application Basics](#application-basics)
    - [Objectives](#objectives)
    - [Optimize the Common Case](#optimize-the-common-case)
  - [Application Performance Techniques](#application-performance-techniques)
    - [Selecting an I/O Size](#selecting-an-io-size)
    - [Caching](#caching)
    - [Buffering](#buffering)
    - [Polling](#polling)
    - [Concurrency and Parallelism](#concurrency-and-parallelism)
    - [Non-Blocking I/O](#non-blocking-io)
    - [Processor Binding](#processor-binding)
  - [Programming Languages](#programming-languages)
    - [Compiled Languages](#compiled-languages)
      - [Compiler Optimizations](#compiler-optimizations)
    - [Interpreted Languages](#interpreted-languages)
    - [Virtual Machines](#virtual-machines)
    - [Garbage Collection](#garbage-collection)
  - [Methodology and Analysis](#methodology-and-analysis)
    - [Thread State Analysis](#thread-state-analysis)
    - [CPU Profiling](#cpu-profiling)
    - [Syscall Analysis](#syscall-analysis)
    - [I/O Profiling](#io-profiling)
    - [Workload Characterization](#workload-characterization)
    - [USE Method](#use-method)
    - [Drill-Down Analysis](#drill-down-analysis)
    - [Lock Analysis](#lock-analysis)
    - [Static Performance Tuning](#static-performance-tuning)

# Applications

Performance is best tuned closest to where the work is performed: in the applications. 

## Application Basics

Before diving into application performance, you should familiarize yourself with the role of the application, its basic characteristics, and its ecosystem in the industry.

### Objectives

A performance goal provides direction for your performance analysis work and helps you select which activities to perform.

The goal may be
- Latency: a low application response time
- Throughput: a high application operation rate or data transfer rate 
- Resource utilization: efficiency for a given application workload

Once a goal has been chosen, you can work on the limiters for that goal. For latency, the limiter may be disk or network I/O; for throughput, it may be CPU usage. 

### Optimize the Common Case

One way to efficiently improve application performance is to find the most common code path for the production workload and begin by improving that. If the application is CPU-bound, that may mean the code paths that are frequently on-CPU. If the application is I/O-bound, you should be looking at the code paths that frequently lead to I/O. 

## Application Performance Techniques

### Selecting an I/O Size

Costs associated with performing I/O can include initializing buffers, making a system call, context switching, allocating kernel metadata, checking process privileges and limits, mapping addresses to devices, executing kernel and driver code to deliver the I/O, and, finally, freeing metadata and buffers. “Initialization tax” is paid for small and large I/O alike. For efficiency, the more data transferred by each I/O, the better.

Increasing the I/O size is a common strategy used by applications to improve throughput.

There’s a downside when the application doesn’t need larger I/O sizes. A database performing 8 Kbyte random reads may run more slowly with a 128 Kbyte I/O size, as 120 Kbytes of data transfer is wasted. This introduces I/O latency, which can be lowered by selecting a smaller I/O size that more closely matches what the application is requesting. Unnecessarily larger I/O sizes can also waste cache space.

### Caching

An important aspect of the cache is how it manages integrity, so that lookups do not return stale data. This is called cache coherency and can be expensive to perform—ideally not more so than the benefit the cache provides.
While caches improve read performance, their storage is often used as buffers to improve write performance.

### Buffering

To improve write performance, data may be coalesced in a buffer before being sent to the next level. This increases the I/O size and efficiency of the operation. Depending on the type of writes, it may also increase write latency, as the first write to a buffer waits for subsequent writes before being sent.

A ring buffer (or circular buffer) is a type of fixed buffer that can be used for continuous transfer between components, which act upon the buffer asynchronously. 

### Polling

Polling is a technique in which the system waits for an event to occur by checking the status of the event in a loop, with pauses between checks. 

poll() System Call
There is a poll() syscall to check for the status of file descriptors, which serves a similar function to polling, although it is event-based so it doesn’t suffer the performance cost of polling.

The poll() interface supports multiple file descriptors as an array, which requires the application to scan the array when events occur to find the related file descriptors. This scanning is O(n), whose overhead can become a performance problem at scale. A different interface is available: on Linux it is epoll(), which can avoid the scan and therefore be O(1).

### Concurrency and Parallelism

For a multiprocessor system, multiple threads (or the equivalent tasks) are more efficient and are therefore the preferred approach.

**Synchronization Primitives**

Synchronization primitives police access to memory, similarly to the way traffic lights regulate access to an intersection. And, like traffic lights, they halt the flow of traffic, causing wait time (latency). The three commonly used types are
- **Mutex (MUTually EXclusive) locks**: Only the holder of the lock can operate. Others block and wait off-CPU.
- **Spin locks**: Spin locks allow the holder to operate, while others requiring the lock spin on- CPU in a tight loop, checking for the lock to be released. While these can provide low-latency access—the blocked thread never leaves CPU and is ready to run in a matter of cycles once the lock is available—they also waste CPU resources while threads spin, waiting.
- **RW locks**: Reader/writer locks ensure integrity by allowing either multiple readers, or one writer only and no readers.

**Hash Tables**

A hash table of locks can be used to employ the optimum number of locks for a large number of data structures. 

A hash table of locks is an in-between solution and is suitable when lock contention is expected to be light. A fixed number of locks are created, and a hashing algorithm is used to select which lock is used for which data structure. This avoids the creation and destruction cost with the data structure and also avoids the problem of having only a single lock.

Ideally, the number of hash table buckets should be equal to or greater than the CPU count, for the potential of maximum parallelism. 

This situation is called false sharing and is commonly solved by padding hash locks with unused bytes so that only one lock exists in each cache line in memory.

### Non-Blocking I/O

The Unix process life cycle shows processes blocking and entering the sleep state during I/O. 

The non-blocking I/O model issues I/O asynchronously, without blocking the current thread, which can then perform other work.

### Processor Binding

For NUMA environments, it can be advantageous for a process or thread to remain running on a single CPU and to run on the same CPU as it did previously after performing I/O. This can improve the memory locality of the application, reducing the cycles for memory I/O and improving overall application performance. Operating systems are well aware of this and are designed to keep application threads on the same CPUs (CPU affinity).

Some applications force this behavior by binding themselves to CPUs. This can significantly improve performance for some systems. 

Be especially careful about the risks of CPU binding when there are other tenants or applications running on the same system. When a server is shared by other tenant applications that are also binding, there can be conflicts and scheduler latency as the bound CPUs are busy with other tenants, even though other CPUs are idle.

## Programming Languages

For example, high CPU usage may be identified as a result of garbage collection (GC), and then fixed via some commonly used tunables. Or it may be caused by a code path that can be found as a known bug in a bug database and fixed by upgrading the software version (this happens a lot).

### Compiled Languages

Compilers can improve performance by use of compiler optimizations—routines that optimize the choice and placement of CPU instructions.

#### Compiler Optimizations

The gcc(1) compiler provides a range from 0 to 3, where 3 uses the largest number of optimizations. gcc(1) can be queried to show which optimizations it uses for different levels. For example:
```
$ gcc -Q -O3 --help=optimizers
```
Should performance issues arise, it may be tempting to simply recompile the application with a reduced optimization level (from –O3 to –O2, for example), in the hope that any debugging needs could then be met. This turns out not to be simple: the changes to the compiler output can be massive and important, and they can affect the behavior of the issue you were originally trying to analyze.

### Interpreted Languages

Unless observability tools are provided, performance analysis of interpreted languages can be difficult. CPU profiling can show the operation of the interpreter—including parsing, translating, and performing actions—but it may not show the original program function names, leaving essential program context a mystery.

Depending on the interpreter, program context may be easy to fetch indirectly (e.g., dynamic tracing of the parser). Often these programs are studied by simply adding print statements and timestamps.

### Virtual Machines

The bytecode is compiled from the original program and then interpreted by the language virtual machine, which translates it to machine code. The Java HotSpot Virtual Machine supports JIT compilation, which compiles bytecode to machine code ahead of time, so that during execution the native machine code can be executed. This provides the performance advantages of compiled code, together with the portability of a virtual machine.

Virtual machines are typically the most difficult of the language types to observe. By the time the program is executing on-CPU, multiple stages of compilation or interpretation may have passed, and information about the original program may not be readily available. Performance analysis usually focuses on the toolset provided with the language virtual machine, many of which provide DTrace probes, and on third-party tools.

### Garbage Collection

While this makes programs easier to write, there can be disadvantages:
- Memory growth: There is less control of the application’s memory usage, which may grow when objects are not identified automatically as eligible to be freed. 

- CPU cost: GC will typically run intermittently and involves searching or scanning objects in memory. This consumes CPU resources, reducing what is available to the application for short periods. 

- Latency outliers: Application execution may be paused while GC executes, causing occasional application responses with high latency. 

GC is a common target for performance tuning, to reduce CPU cost and occurrence of latency outliers.

If tuning is not effective, the problem may be the application creating too much garbage, or leaking references. 

## Methodology and Analysis

**Application Performance Methodologies**

Methodology | Type
---     | ---
Thread state analysis   | observational analysis
CPU profiling   | observational analysis
Syscall analysis    | observational analysis
I/O profiling   | observational analysis
Workload characterization   | observational analysis, capacity planning
USE method  | observational analysis
Drill-down analysis | observational analysis
Lock analysis   | observational analysis
Static performance turning  | observational analysis, tuning

### Thread State Analysis

The goal is to identify at a high level where application threads are spending their time, which solves some issues immediately and directs the investigation of others. This is done by dividing each application’s thread time into a number of meaningful states.

**Two State**

At a minimum, there are two thread states:
- **On-CPU**: executing
- **Off-CPU**: waiting for a turn on-CPU, or for I/O, locks, paging, work, and so on

If time is largely spent on-CPU, CPU profiling can usually explain this quickly. This is the case for many performance issues, so spending time measuring other states may not be necessary.
If time is found to be spent off-CPU, various other methodologies can be used, although without a better starting point this can be time-consuming.

**Six State**

Here is an expanded list, this time using six thread states (and a different naming scheme), which gives better starting points for the off-CPU cases:

- **Executing**: on-CPU
- **Runnable**: and waiting for a turn on-CPU
- **Anonymous paging**: runnable, but blocked waiting for anonymous 
- **page-ins Sleeping**: waiting for I/O, including network, block, and data/text 
- **page-ins Lock**: waiting to acquire a synchronization lock (waiting on someone else) 
- **Idle**: waiting for work

These have been selected as a minimal and useful set; you may wish to add more states to your list. For example, the executing state may be split into user- and kernel-mode execution, and the sleeping state can be divided based on the target. 

Once you’ve established in which of the first five states the threads are spending their time, you can investigate them further:
- **Executing**: Check whether this is user- or kernel-mode time and the reason for CPU consumption by using profiling. Profiling can determine which code paths are consuming CPU and for how long, which can include time spent spinning on locks. 

- **Runnable**: Spending time in this state means the application needs more CPU resources. 

- **Anonymous paging**: A lack of available main memory for the application can cause anonymous paging and delays. 

- **Sleeping**: Analyze the resource on which the application is blocked. 

- **Lock**: Identify the lock, the thread holding it, and the reason why the holder held it for so long. The reason may be that the holder was blocked on another lock, which requires further unwinding. 

When you see large sleeping and lock state times, remember to drill down a little to check if this is really idle time.

**Linux**

The time spent **executing** is not hard to determine: top(1) reports this as %CPU. 

**Runnabl**e is tracked by the kernel `schedstats` feature and is exposed via `/proc/*/schedstat`. The `perf sched` tool can also provide metrics for understanding time spent runnable and waiting.

Time waiting for **anonymous paging** (in Linux, swapping) can be measured by the *kernel delay accounting* feature, provided it is enabled. It provides separate states for swapping and for time blocked during memory reclaim (also related to memory pressure). There isn’t a commonly used tool to expose these states; however, the kernel documentation contains an example program to do this: `getdelays.c`. Another approach is to use tracing tools such as `DTrace` or `SystemTap`.

Time blocked in the **sleeping** state can be loosely estimated using other tools, for example, `pidstat -d` to determine if a process is performing disk I/O, and probably sleeping. Delay and other I/O accounting features, if they are enabled, do provide time blocked on block I/O, which can also be observed using `iotop(1)`. Other reasons for blocking can be investigated using tracing tools such as `DTrace` or `SystemTap`. The application may also have instrumentation, or instrumentation can be added, to track time performing explicit I/O (disk and network).

If the application is stuck in the sleeping state for very long intervals (seconds), you can try `pstack(1)` to determine why. This takes a single snapshot of the threads and their user stack traces, which should include the sleeping threads and the reason they are sleeping. Be warned, however: `pstack(1`) may briefly pause the target while it does this, so use with caution.

**S** can be investigated using tracing tools.

### CPU Profiling

Use `Dtrace` or `perf(1)` for CPU profiling.

The intent is to determine why an application is consuming CPU resources. An effective technique is to sample the on-CPU user-level stack trace and coalesce the results. The stack traces shows the code path taken, which can reveal both high- and low-level reasons for the application consuming CPU.

Sampling stack traces can generate many thousands of lines of output to examine, even when summarizing the output to print only unique stacks. One way to understand the profile quickly is to visualize it using flame graphs.

Apart from sampling the stack trace, the currently running function alone can be sampled. In some cases this is sufficient to identify why the application is using the CPU and produces much less output, making it quicker to read and understand. 

It can also be useful to study the caller of the currently running function, which some profiling software (including DTrace) can easily do.

### Syscall Analysis

It can be useful, and sometimes more practical, to study these based on system call execution:

- **Executing**: on-CPU (user mode)
- **Syscalls**: time during a system call (kernel mode running or waiting)

The syscall time includes I/O, locks, and other syscall types.

The intent is to find out where syscall time is spent, including the type of syscall and the reason it is called.

**Breakpoint Tracing**

The traditional style of syscall tracing involves setting breakpoints for syscall entry and return. These are invasive, and for applications with high syscall rates their performance may be worsened by an order of magnitude.

**strace**

On Linux, this is performed using the strace(1) command. For example:
```
$ strace -ttt -T -p 1884
```
The options used were (see the man page for all)
- **-ttt**: prints the first column of time-since-epoch, in units of seconds with microsecond resolution.
- **-T**: prints the last field (<time>), which is the duration of the system call, in units of seconds with microsecond resolution.
- **-p PID**: trace this process ID. A command can also be specified so that strace(1) launches and traces it.

This form of strace(1) prints a line of output per syscall. The -c option can be used to summarize system call activity:
```
$ strace -c -p 1884
```

The output includes

- time: percentage showing where system CPU time was spent 
- seconds: total system CPU time, in seconds
- usecs/call: average system CPU time per call, in microseconds 
- calls: number of system calls during strace(1)
- syscall: system call name

Following example shows how `strace ` samples output `dd` command.
```bash
$ strace -c dd if=/dev/zero of=/dev/null bs=1k count=5000k
```

**Buffered Tracing**

With buffered tracing, instrumentation data can be buffered in-kernel while the target program continues to execute. This differs from breakpoint tracing, which interrupts the target program for each tracepoint.

DTrace provides both buffered tracing and aggregations to reduce tracing overhead and allows custom programs to be written for syscall analysis. 

### I/O Profiling

This can be done using DTrace, examining the user-level stack traces for system calls.

For example, this one-liner traces PostgreSQL read() syscalls, gathers the user-level stack trace, and aggregates them:
```bash
# dtrace -n 'syscall::read:entry /execname == "postgres"/ { @[ustack()] = count(); }'
```

### Workload Characterization

The application applies work to system resources—CPUs, memory, file system, disk, and network— as well as to the operating system via system calls. All of these can be studied using the workload characterization methodology. 
In addition, the workload sent to the application can be studied. 

### USE Method

If you can find a functional diagram showing the internal components of an application, consider the utilization, saturation, and error metrics for each software resource and see what makes sense.

For example, the application may use a pool of worker threads to process requests, with a queue for requests waiting their turn. Treating this as a resource, the three metrics could then be defined in this way:
- **Utilization**: average number of threads busy processing requests during an interval, as a percentage of the total threads. For example, 50% would mean that, on average, half the threads were busy working on requests.
- **Saturation**: average length of the request queue during an interval. This shows how many requests have backed up waiting for a worker thread.
- **Errors**: requests denied or failed for any reason.

Your task is then to find how these metrics can be measured.

For a different example, consider file descriptors. The system may impose a limit, such that these are a finite resource. The three metrics could be as follows:
- **Utilization**: number of in-use file descriptors, as a percentage of the limit.
- **Saturation**: depends on the OS behavior: if threads block waiting for file descriptor allocation, this can be the number of blocked threads waiting for this resource.
- **Errors**: allocation error, such as EFILE, “Too many open files.”

### Drill-Down Analysis

For applications, drill-down analysis can begin with examining the operations the application serves and then drilling down into application internals to see how it is performing them. For I/O, this drill- down analysis can enter system libraries, syscalls, and the kernel.

There are also specific tools for investigating library calls: ltrace(1) on Linux.

### Lock Analysis

For multithreaded applications, locks can become a bottleneck, inhibiting parallelism and scalability. They can be analyzed by
- Checking for contention
- Checking for excessive hold times

The first identifies whether there is a problem now. Excessive hold times are not necessarily a problem, but they may be in the future, with more parallel load. For each, try to identify the name of the lock (if it exists) and the code path that led to using it.

While there are special-purpose tools for lock analysis, you can sometimes solve issues from CPU profiling alone. For spin locks, contention shows up as CPU usage and can easily be identified using CPU profiling of stack traces. For adaptive mutex locks, contention often involves some spinning, which can also be identified by CPU profiling of stack traces. In that case, be aware that the CPU profile gives only a part of the story, as threads may have blocked and slept while waiting for the locks. 

Tracing of kernel- or user-level locks does add overhead. These particular tools are based on DTrace, which minimizes this overhead as much as possible. Alternatively, as described earlier, CPU profiling at a fixed rate (e.g., 97 Hz) will identify many (but not all) lock issues, without the perevent tracing overhead.

### Static Performance Tuning

Static performance tuning focuses on issues of the configured environment. For application performance, examine the following aspects of the static configuration:
- What version of the application is running? Are there newer versions? Do their release notes mention performance improvements?
- What known performance issues are there with the application? Is there a bug database that can be searched?
- How is the application configured?
- If it was configured or tuned differently from the defaults, what was the reason? (Was it based on measurements and analysis, or guesswork?)
- Does the application employ a cache of objects? How is it sized?
- Does the application run concurrently? How is that configured (e.g., thread pool sizing)?
- Is the application running in a special mode? (For example, debug mode may have been enabled and be reducing performance.)
- What system libraries does the application use? What versions are they?
What memory allocator does the application use?
- Is the application configured to use large pages for its heap?
- Is the application compiled? What version of the compiler? What compiler options and optimizations? 64-bit?
- Has the application encountered an error, and is it now running in a degraded mode?
- Are there system-imposed limits or resource controls for CPU, memory, file system, disk, or network usage? (These are common with cloud computing.)

Answering these questions may reveal configuration choices that have been overlooked.