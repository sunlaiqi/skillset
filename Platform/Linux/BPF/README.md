
“In Linux, the main features that containers are based on are namespaces and cgroups. Namespaces are the components that isolate tasks from one another. In a sense, when you’re inside a namespace, you experience the operating system like there were no other tasks running on the computer. Cgroups are the components that provide resource management. From an operational point of view, they give you fine-grained control over any resource usage, such as CPU, disk I/O, network, and so on. ”

“The kernel is an evented system, which means that all work is described and executed based on events. Opening files is a kind of event, executing an arbitrary instruction by a CPU is an event, receiving a network packet is an event, and so on. Berkeley Packet Filter (BPF) is a subsystem in the kernel that can inspect those new sources of information. BPF allows you to write programs that are safely executed when the kernel triggers any event. BPF gives you strong safety guarantees to prevent you from injecting system crashes and malicious behavior in those programs. BPF is enabling a new wave of tools to help system developers observe and work with these new platforms.”

# BPF’s History

In 1992, Steven McCanne and Van Jacobson wrote the paper “The BSD Packet Filter: A New Architecture for User-Level Packet Capture.” 
Packet filters have a specific purpose: to provide applications that monitor the system’s network with direct information from the kernel. With this information, applications could decide what to do with those packets. 

BPF introduced two big innovations in packet filtering:
- A new virtual machine (VM) designed to work efficiently with register-based CPUs. (BPF VM or BPM interpreter)
- The usage of per-application buffers that could filter packets without copying all the packet information. This minimized the amount of data BPF required to make decisions.

In early 2014, Alexei Starovoitov introduced the extended BPF (eBPF) implementation. This new design was optimized for modern hardware.
BPF became a top-level kernel subsystem, and it stopped being limited to the networking stack. BPF programs began to look more like kernel modules, with a big emphasis on safety and stability. Unlike kernel modules, BPF programs don’t require you to recompile your kernel, and they are guaranteed to complete without crashing.
“The BPF verifier added these required safety guarantees.

With the changes to make BPF accessible from user-space, the kernel developers also added a new system call (syscall), bpf. 

# Architecture

BPF is a highly advanced VM, running code instructions in an isolated environment. In a sense, you can think of BPF like how you think about the Java Virtual Machine (JVM), a specialized program that runs machine code compiled from a high-level programming language. Compilers like LLVM, and GNU Compiler Collection (GCC) in the near future, provide support for BPF, allowing you to compile C code into BPF instructions. After your code is compiled, BPF uses a verifier to ensure that the program is safe to run by the kernel. It prevents you from running code that might compromise your system by crashing the kernel. If your code is safe, the BPF program will be loaded in the kernel. The Linux kernel also incorporates a just-in-time (JIT) compiler for BPF instructions. The JIT will transform the BPF bytecode into machine code directly after the program is verified, avoiding this overhead on execution time.

One interesting aspect of this architecture is that you don’t need to restart your system to load BPF programs; you can load them on demand, and you can also write your own init scripts that load BPF programs when your system starts.

Before the kernel runs any BPF program, it needs to know which execution point the program is attached to. There are multiple attachment points in the kernel, and the list is growing. The execution points are defined by the BPF program types. When you choose an execution point, the kernel also makes available specific function helpers that you can use to work with the data that your program receives, making execution points and BPF programs tightly coupled.

The final component in BPF’s architecture is responsible for sharing data between the kernel and user-space. This component is called a BPF map. BPF maps are bidirectional structures to share data. This means that you can write and read them from both sides, the kernel and user-space. There are several types of structures, from simple arrays and hash maps to specialized maps, that allow you to save entire BPF programs in them.
