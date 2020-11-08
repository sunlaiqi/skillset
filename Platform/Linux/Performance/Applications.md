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


