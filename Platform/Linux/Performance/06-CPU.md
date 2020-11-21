

# CPU

- At a high level, CPU usage by process, thread, or task can be examined. 
- At a lower level, the code path within applications and the kernel can be profiled and studied. 
- At the lowest level, CPU instruction execution and cycle behavior can be studied.

## Terminology

- **Processor**: the physical chip that plugs into a socket on the system or processor board and contains one or more CPUs implemented as cores or hardware threads.
- **Core**: an independent CPU instance on a multicore processor. The use of cores is a way to scale processors, called chip-level multiprocessing (CMP).
- **Hardware thread**: a CPU architecture that supports executing multiple threads in parallel on a single core (including Intel’s Hyper-Threading Technology), where each thread is an independent CPU instance. One name for this scaling approach is **multithreading**.
- **CPU instruction**: a single CPU operation, from its instruction set. There are instructions for arithmetic operations, memory I/O, and control logic.
- **Logical CPU**: also called a virtual processor, an operating system CPU instance (a schedulable CPU entity). This may be implemented by the processor as a hardware thread (in which case it may also be called a virtual core), a core, or a single-core processor.
    - It is also sometimes called a virtual CPU; however, that term is more commonly used to refer to virtual CPU instances provided by a virtualization technology. 
- Scheduler: the kernel subsystem that assigns threads to run on CPUs.
- Run queue: a queue of runnable threads that are waiting to be serviced by CPUs. For Solaris, itis often called a dispatcher queue.
- **NUMA**: Non-Uniform Memory Access is a computer memory design used in multiprocessing, where the memory access time depends on the memory location relative to the processor. Under NUMA, a processor can access its own local memory faster than non-local memory.
- 
## CPU Run Queues

The number of software threads that are queued and ready to run is an impor- tant performance metric indicating CPU saturation.
The time spent waiting on a CPU run queue is sometimes called run-queue latency or dispatcher-queue latency.
For multiprocessor systems, the kernel typically provides a run queue for each CPU and aims to keep threads on the same run queue. This means that threads are more likely to keep running on the same CPUs, where the CPU caches have cached their data. (These caches are described as having cache warmth, and the approach to favor CPUs is called CPU affinity.) On NUMA systems, memory locality may also be improved, which also improves performance 

## Concepts

### Clock Rate

Some processors are able to vary their clock rate, increasing it to improve per- formance or decreasing it to reduce power consumption. 

Even if the CPU in your system appears to be fully uti- lized (a bottleneck), a faster clock rate may not speed up performance—it depends on what those fast CPU cycles are actually doing.

### Instruction

1. Instruction fetch
2. Instruction decode
3. Execute
4. Memory access
5. Register write-back

The last two steps are optional, depending on the instruction.

### Instruction Pipeline

The instruction pipeline is a CPU architecture that can execute multiple instruc- tions in parallel, by executing different components of different instructions at the same time.

Note:
Here the pipeline is parallel.

### Instruction Width

The instruction width describes the target number of instructions to process in parallel. Modern processors are 3-wide or 4-wide, meaning they can complete up to three or four instructions per cycle. 

### CPI, IPC

Cycles per instruction (CPI) is an important high-level metric for describing where a CPU is spending its clock cycles and for understanding the nature of CPU utili- zation. This metric may also be expressed as instructions per cycle (IPC), the inverse of CPI.

A high CPI indicates that CPUs are often stalled, typically for memory access. 

It should be noted that CPI shows the efficiency of instruction processing, but not of the instructions themselves. Consider a software change that added an inef- ficient software loop, which operates mostly on CPU registers (no stall cycles): such a change may result in a lower overall CPI, but higher CPU usage and utilization.

### Utilization

High CPU utilization may not necessarily be a problem, but rather a sign that the system is doing work. 
