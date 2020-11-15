Some additional insights into what our interviewers are assessing during your interview.

# CODING
* Can you code in some language, do you understand data structures and algorithms,

* Are you writing code defensively and do you know how a program interacts with a system.

## 5 Tips to Focus On

### Algorithmic complexity (basics of big O notation), 

### Opening and reading files, 

- Files on most modern file systems are composed of three main parts:

    **Header**: metadata about the contents of the file (file name, size, type, and so on)
    **Data**: contents of the file as written by the creator or editor
    **End of file (EOF)**: special character that indicates the end of the file

- Line Ending
    ASA standard states that line endings should use the sequence of the Carriage Return (CR or \r) and the Line Feed (LF or \n) characters (CR+LF or \r\n). The ISO standard however allowed for either the CR+LF characters or just the LF character.
    Windows uses the CR+LF characters to indicate a new line, while Unix and the newer Mac versions use just the LF character. 
- Character Encodings
    Another common problem that you may face is the encoding of the byte data. An encoding is a translation from byte data to human readable characters. 
- There are three different categories of file objects:
    Text files
    Buffered binary files
    Raw binary files
    - buffered binary file:
        A buffered binary file type is used for reading and writing binary files.
        ```python
        open('abc.txt', 'rb')
        open('abc.txt', 'wb')
        ```
        'rb' or 'wb'	Open in binary mode (read/write using byte data)
    - raw file:
        generally used as a low-level building-block for binary and text streams.
        ```python
        file = open('abc.txt', 'rb', buffering=0)
        type(file)
        <class '_io.FileIO'>
        ```
- Reading and Writing Opened Files

    Method	| What It Does
    --------|-------------
    .read(size=-1)	| This reads from the file based on the number of size bytes. If no argument is passed or None or -1 is passed, then the entire file is read.
    .readline(size=-1)	| This reads at most size number of characters from the line. This continues to the end of the line and then wraps back around. If no argument is passed or None or -1 is passed, then the entire line (or rest of the line) is read.
    .readlines()	| This reads the remaining lines from the file object and returns them as a list.

- Working With Bytes
    ```python
    >>> with open('dog_breeds.txt', 'rb') as reader:
    >>>     print(reader.readline())
    b'Pug\n'
    ```
- Tips and Tricks



### data structures (hash tables), 

### scaling issues (size larger than memory, etc). 


###  Great to know things like Arrays, Linked Lists and Strings. 

[Python Linked List](https://realpython.com/linked-lists-python/)

- Performance Comparison: Lists vs Linked Lists

        In Python, however, lists are dynamic arrays. That means that the memory usage of 
        both lists and linked lists is very similar.

- How to create a linked list:

    ```python
        class LinkedList:
            def __init__(self):
                self.head = None
            
            def __repl__(self):
                node = self.head
                nodes = []
                while node is not None:
                    nodes.append(node.data):
                    node = node.next
                nodes.append("None")
                return " ->".join(nodes)
    ```

    The only information you need to store for a linked list is where the list starts (the head of the list). Next, create another class to represent each node of the linked list:

    ```python {.line-numbers .highlight=4}
        class Node:
            def __init__(self, data):
                self.data = data
                self.next = None
            
            def __repl__(self):
                return self.data
    ```

- To traverse a linked list: 
    ```python
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    ```
- to move to next node: 

        node = node.next
- Insert at the beginning:

        node.next = self.head
        self.head = node
- Insert at the end:

    ```python
        def add_last(self, node):
            if not self.head:
                self.head = node
                return
            for current_node in self:
                pass
            current_node.next = node
    ```

- Inserting Between Two Nodes:

    ```python

        def add_after(self, target_node_data, new_node):
            if not self.head:
                raise Exception("List is empty")

            for node in self:
                if node.data == target_node_data:
                    new_node.next = node.next
                    node.next = new_node
                    return

            raise Exception("Node with data '%s' not found" % target_node_data)

    
        def add_before(self, target_node_data, new_node):
            if not self.head:
                raise Exception("List is empty")

            if self.head.data == target_node_data:
                return self.add_first(new_node)

            prev_node = self.head
            for node in self:
                if node.data == target_node_data:
                    prev_node.next = new_node
                    new_node.next = node
                    return
                prev_node = node

            raise Exception("Node with data '%s' not found" % target_node_data)
        ```

- How to Remove a Node:

    ```python
        def remove_node(self, target_node_data):
            if not self.head:
                raise Exception("List is empty")

            if self.head.data == target_node_data:
                self.head = self.head.next
                return

            previous_node = self.head
            for node in self:
                if node.data == target_node_data:
                    previous_node.next = node.next
                    return
                previous_node = node

            raise Exception("Node with data '%s' not found" % target_node_data)
    ```

- Doubly Linked List:

    ```python
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.previous = None
    ```
- Circular Linked Lists

    Circular linked lists are a type of linked list in which the last node points back to the head of the list instead of pointing to None. This is what makes them circular. Circular linked lists have quite a few interesting use cases:
    - Going around each player’s turn in a multiplayer game
    - Managing the application life cycle of a given operating system
    - Implementing a Fibonacci heap

    In terms of implementation, circular linked lists are very similar to singly linked list. The only difference is that you can define the starting point when you traverse the list:

    ```python
    class CircularLinkedList:
        def __init__(self):
            self.head = None

        def traverse(self, starting_point=None):
            if starting_point is None:
                starting_point = self.head
            node = starting_point
            while node is not None and (node.next != starting_point):
                yield node
                node = node.next
            yield node

        def print_list(self, starting_point=None):
            nodes = []
            for node in self.traverse(starting_point):
                nodes.append(str(node))
            print(" -> ".join(nodes))
    ```

- collections.deque

    - implemented in doubly linked list
            from collections import deque

            >>> deque()
            deque([])
            >>> deque(['a','b','c'])
            deque(['a', 'b', 'c'])

            >>> deque('abc')
            deque(['a', 'b', 'c'])

            >>> deque([{'data': 'a'}, {'data': 'b'}])
            deque([{'data': 'a'}, {'data': 'b'}])



### Data manipulation, 

- str.find(sub[, start[, end]] )

        The find() method returns the index of first occurrence of the substring (if found). If not found, 
        it returns -1.

- regular expression
    http://evc-cit.info/comsc020/python-regex-tutorial/#

        The pattern is a string preceded by the letter r, which tells Python to interpet the string as a 
        regular expression.

    - Matching any single character: dot "."
            re.search(r'e.t', string)
    - Matching classes of characters: “any one of a certain series of characters”
            re.seerch(r'b[aeiou]t', string)
        
        There are abbreviations for establishing a series of letters: [a-f] is the same as [abcdef]; [A-Gm-p] is the same as [ABCDEFGmnop]; [0-9] matches a single digit (same as [0123456789]).

        You may also complement (negate) a class; the next two patterns will look for the letter e followed by anything except a vowel, followed by the letter t; or any character except a capital letter:

        >r'e[^aeiou]t'
        >r'[^A-Z]'

    - There are some classes that are so useful that Python provides quick and easy abbrevations:

        Abbreviation   | Means	                            | Same as 
        ------------   | ---------| -------
        | \d	        |  a digit                  | [0-9]         |
        \w      |a “word” character; uppercase letter, lowercase letter, digit, or underscore	|[A-Za-z0-9_]
        \s	    |a whitespace character (blank, new line, tab)  |	[ \r\t\n]
        And their complements:
        Abbreviation   | Means	                            | Same as 
        ------------   | ---------| -------
        \D	    |a non-digit	|   [^0-9]
        \W	    |a non-word character	|   [^A-Za-z0-9_]
        \S	    |a non-whitespace character	| [^ \r\t\n]

        Thus, this pattern: **\d\d\d-\d\d-\d\d\d\d** matches a Social Security number; again, you’ll see a shorter way later on.

    - Anchors

        The up-arrow ^ matches the beginning of a line, and the dollar sign `$` matches the end of a line. Thus, `^[A-Z]` matches a capital letter at the beginning of the line. A pattern `\d$` matches a digit at the end of a line.

        The other two anchors are `\b` and `\B`, which stand for a “**word** boundary” and “non-word boundary”. For example, if you want to find the word `met` at the beginning of **a word**, we write the pattern `r'\bmet'`. `r'ing\b'` will match `Hiking is fun and Reading, writing, and arithmetic`. Finally,the pattern `r'\bhat\b'` matches only the `The hat is red` but not `That is the question or she hates anchovies or the shattered glass`.
        
        While `\b` is used to find the breakpoint between words and non-words, `\B` finds pairs of letters or nonletters; `\Bmet` and `ing\b` match the opposite examples of the preceding paragraph; `\Bhat\B` matches only the `shattered glass`.

    - Repetition

        Pattern	| Matches
        ------- | -------
        r'b[aeiou]{2}t'	| b followed by two vowels, followed by t
        r'A\d{3,}'	| The letter A followed by 3 or more digits
        r'[A-Z]{,5}'	| Zero to five capital letters
        r'\w{3,7}'	| Three to seven “word” characters

        This lets you rewrite the social security number pattern match as r'\d{3}-\d{2}-\d{4}'
        
        There are three repetitions that are so common that Python has special symbols for them: 
        - `*` means “zero or more,” 
        - `+` means “one or more,” and 
        - `?` means “zero or one.”   
        
        `r'^\w+,?\s*[A-Z]$'` explained:
            - `^` starting at the beginning of the string,
            - `\w+` look for one or more word characters
            - `,?` followed by an optional comma (zero or one commas)
            - `\s*` zero or more spaces
            - `[A-Z]` and a capital letter
            - `$` which must be at the end of the string.

    - Grouping¶
        Put the comma, whitespace, and initial into a unit with parentheses as a group.
        `r'^\w+(,?\s*[A-Z])?$'`
    - Modifiers
        If you want a pattern match to be case-insenstive, add the `flags=re.I` to the search() call.
    - Advanced Pattern Matching
        The return value from `search()` is not a boolean; it is a matching object
        The `found.group(0)` method calls contains everything matched by the entire pattern. `found.group(1)` contains the part of the string that the first set of grouping parentheses matched–the last name, and `found.group(2)` contains the part of the string matched by the second set of grouping parentheses–the comma and initial, if any. If the pattern had more groups of parentheses, you would use `.group(3)`, `.group(4)`, and so forth.
    - Finding All Occurrences
        The re.search() method finds only the first occurrence of a pattern within a string. If you want to find all the matches in a string, use re.findall(), which returns a list of matched substrings. (Unlike re.search(), which returns match objects.) 

        ```python
        import re
        message = 'Insert tabs B3, D-7, and C6 into slot A9.'
        result = re.findall(r'([A-Z]-?\d)', message)
        if result:
            for item in result:
                print(item)
        else:
            print('findall() did not find any matches to the pattern.')
        ```

### handling input / output, 

raw_input() in Python 2 reads input from the keyboard and returns it. raw_input() in Python 2 behaves just like input() in Python 3

- Keyword Arguments to print()
    - The `sep=Keyword` Argument
    Adding the keyword argument `sep=<str>` causes objects to be separated by the string <str> instead of the default single space
    - The `end=Keyword` Argument
    The keyword argument `end=<str>` causes output to be terminated by <str> instead of the default newline
    - Output Stream Keyword Arguments
        print() accepts two additional keyword arguments, both of which affect handling of the output stream:

        `file=<stream>`: By default, print() sends its output to a default stream called sys.stdout, which is usually equivalent to the console. The `file=<stream>` argument causes output to be sent to an alternate stream designated by `<stream>` instead.

        `flush=True`: Ordinarily, print() buffers its output and only writes to the output stream intermittently. `flush=True` specifies that the output stream is forcibly flushed with each print().

### automating tasks, 

### interfacing with external systems / processes, etc. 

The questions can be a real problem, or something contrived to use these skills.
Pay attention to edge/corners cases, bad inputs, failures, exceptions, check for bugs, if you are unsure how far to go, just ask the interviewer.
It's important that the code can run. In production you are dealing with real time incidents that need to be taken care of during the time.
Behaviorally, ask clarifying questions, walk through your solution out loud and help the interviewer understand your thought process.


## Interview Question:

### Question 1
Given a 1TB file of serialized 4 byte integers, and 2GB of ram, sort the integers into a resulting 1TB file. 

Answer:
Any kind of comparison based sorting would be expensive here as it results in runtime complexity of `O(nlogn)`  where n is 256 billion (GB) integers (1TB/4). There are only 4 billion (GB) possible integers which means there are lot of **duplicates**. We could use hashes or array with index being the integer and value being the number of times that integer is repeated.
```
1B = 2^3
1KB = 2^10 Bytes
1MB = 2^20 Bytes
1GB = 2^30 = 1 Billion Bytes
1TB = 2^40 Bytes
1TB / 4 = 2^38 = 256 GB = 256 Billion
4 bytes => 2^32 = 4GB
```

We have 2^31 (2GB) RAM and in the worst case there could be only one integer repeated 256 billion times. 
For this, we will need 64bit integer (8 bytes) to store the count. This will reduce the size of our array to 
2^28 indices. We could divide the 4 billion integers into 16 ranges, each covering 2^28 integers.
 
In the first pass over the file, we will consider the integers between 1-256m (2^28) to fill the array. Increment 
the count of the index whenever it is hit. At the end of the pass, pass through the array and for all non-zero 
valued array indices write down the index count number of times. 
 
Now, do the second pass over the file, consider integers between 256m-512m. Do the same as above.
Third pass 512m-768m, so on until we cover up to 4billion integers. Total of 16 passes thru the file.
 
At the end of it, we have a sorted file.

The whole process is like this:
1. Create an array(list) with size 2^28 to hold the 256M unique 4 bytes integers. The keys will be 0 ~ 2^28.
2. Loop over the file using lazy function `generator` to update the array.
3. Write the array back to a file named sortedfile
4. Resume from step 1 but increase the keys with 2^28 
5. Totally there are 8 loops to go over all the 4 GB unique integers (or keys)
6. Finally we have sorted file

How to use generator (lazy iterator) expression to save memory? 
```python
# Initialize dict
new_dict = dict.fromkeys(range(2**28), 0)
fd = open('filename','rb')
for i in range(8):
    new_dict = dict.fromkeys(range(i*2**28, (i+1)*2**28),0)
    for piece in read_in_chunks(fd)

def read_in_chunks(file_object, chunk_size=4):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


with open("Notes.txt") as f:
    for piece in read_in_chunks(f):
        process_data(piece)

# Another option would be to use iter and a helper function:

f = open('Notes.txt')
def read1k():
    return f.read(4)

for piece in iter(read1k, ''):
    process_data(piece)
```


# SYSTEMS

Can you troubleshoot and debug a system, understand how to identify and overcome performance bottlenecks, and understand the relationship between the system and user.

5 Tips to Focus On

## Understanding how to assess and reason about resource utilization (things like memory, IO, CPU) 

## How deeply can you go into Linux internals

##  Understanding signals, command line etc.

### Processes

- init 
    Each child process is started by parent process. When linux starts, it runs a single program, **init**, with process `#1`. This is OS process manager, and it's the prime ancestor of all processes. Then, other system processes are started by init or by other processes started by **init**. The login procedure is one of the example. The init starts the **getty** program once for each terminal that we can use to log in, and it is shown in the **ps** as below:
    ```
    3812 tty1     Ss+    0:00 /sbin/mingetty tty1
    ```
    The **getty** processes wait for activity at the terminal, prompt the user with the login prompt, and then pass control to the login program, which sets up the user environment, and starts a shell. When the user shell exits, **init** starts another **getty** process.

- System calls
    A **system call** is a controlled entry point into the kernel, allowing a process to request that the kernel perform some action for the process.

- Process Scheduling
    Tho OS determines the priority of a process based on a nice value and on the behavior of the program. Program that run for long periods without pausing generally get lower priorities. Programs that pause get rewarded. This helps keep a program that interacts with the user responsive; while it is waiting for some input from the user, the system increases its priority, so that when it's ready to resume, it has a high priority.
    A niceness of -20 is the highest priority and 19 or 20 is the lowest priority. The default niceness for processes is inherited from its parent process, usually 0.
    But we can set the nice value using `nice` and adjust it using `renice`. The `nice` command increases the nice value of a process by 10, giving it a lower priority. Only the superuser (root) may set the niceness to a smaller (higher priority) value. On Linux it is possible to change `/etc/security/limits.conf` to allow other users or groups to set low nice values.

    Here we can see that the myTest.sh program is running with a default nice value 0. If it had been started with the following command:
    ```
    $ nice ./myTest.sh &
    ```
    it would have been allocated a nice value of +10.

    We have another way of doing it:

    ```
    $ renice 10 12681
    12681: old priority 0, new priority 10
    ```
- exec() system call
    An `exec` function replaces the current process with a new process specified by the path or file argument. We can use `exec` to hand off execution of our program to another.
    The exec functions are more efficient than system because the original program will no longer be running after the new one is started.

- fork() system call
    The key point to understanding `fork()` is to realize that after it has completed its work, two processes exist, and, in each process, execution continues from the point where `fork()` returns.
    The **fork()** called once but returns **twice**!
    Linux will make an exact copy of the parent's address space and give it to the child. Therefore, the parent and child processes have separate address spaces. Therefore, the new process is almost identical to the original, and executing the same code. However, the child process has its own data space, environment, and file descriptor. So, combined with the **exec()** functions, **fork()** is what we need to create a new process.
    The **fork()** returns a process ID, PID so that we can distinguish the two processes via the value returned from fork(). For the parent, `fork()` returns the process ID of the newly created child. This is useful because the parent may create, and thus need to track, several children (by `wait()` call). For the child, `fork()` returns 0. If necessary, the child can obtain its own process ID using **getpid()**, and the process ID of its parent using **getppid()**.
- wait() system call
    The primary role of `wait()` is to synchronization with children.


### Signals
- List signals 
    ```
    $ kill -l
    ```
- Send signals
    ```
    $ kill -signal pid
    ```
    Here signal is either the number or name of the signal to deliver and pid is the process ID that the signal should be sent to. For Example:
    ```
    $ kill -1 1001
    ```
    The above command sends the `HUP` or `hang-up` signal to the program that is running with process ID 1001. To send a kill signal to the same process, use the following command:
    ```
    $ kill -9 1001
    ```
- Trapping signals
    ```
    $ trap "rm -f $WORKDIR/work1$$ $WORKDIR/dataout$$; exit" 2
    ```
    From the point in the shell program that this trap is executed, the two files `work1$$` and `dataout$$` will be automatically removed if signal number 2 is received by the program.

    ```
    tempfile="$(mktemp)"
    trap "{ rm -f $tempfile; }" EXIT
    ```

- Ignoring Signals
    If the command listed for trap is null, the specified signal will be ignored when received. For example, the command :
    ```
    $ trap '' 2
    ```

## Distributed systems concepts like CAP theorem and containerization 
    - aka how things are practically running in production.

In theoretical computer science, the CAP theorem, also named Brewer's theorem after computer scientist Eric Brewer, states that it is impossible for a distributed data store to simultaneously provide more than two out of the following three guarantees:

- **Consistency**: Every read receives the most recent write or an error
- **Availability**: Every request receives a (non-error) response, without the guarantee that it contains the most recent write
- **Partition tolerance**: The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes. 

When a network partition failure happens should we decide to

- Cancel the operation and thus decrease the availability but ensure consistency
- Proceed with the operation and thus provide availability but risk inconsistency

The CAP theorem implies that in the presence of a network partition, one has to choose between consistency and availability. Note that consistency as defined in the CAP theorem is quite different from the consistency guaranteed in ACID database transactions.

## Behaviorally, the goal of this interview is to test your depth and breadth 
    - it's important to be clear where your expertise starts and ends so we can understand your knowledge.

## Performance Monitoring Tools

- uptime - load average
    If load > # of CPUs, it may mean CPU saturation.

- top - system and per-process interval summary
    When we use `top` to diagnose load, the basic steps are to examine the top output to identify what **resources** we are running out of (CPU, RAM, disk I/O). Once we have figured that out, we can try to identify what **processes** are consuming those resources the most.

    %CPU is summed across all CPUs  
    Descriptions for the top display:

    ```
    %Cpu(s): 10.7 us,  2.9 sy,  0.0 ni, 85.7 id,  0.5 wa,  0.0 hi,  0.2 si,  0.0 st
    ```
    This line shows CPU state percentages based on the interval since the last refresh.

    **us, user** user cpu time (or) % CPU time spent in user space, time running un-niced user processes.

    **sy, system** system cpu time (or) % CPU time spent in kernel space. This is the amount of time that the CPU spent running the kernel. The amount of time spent in the kernel should be **as low as possible**. This number can peak much higher, especially when there is a lot of I/O happening.

    **ni, nice** time running niced user processes.
    The niceness level ranges from -20 (most favorable scheduling) to 19 (least favorable). By default processes on Linux are started with a niceness of 0.
    A "niced" process is one with a positive nice value. So if the processor's nice value is high, that means it is working with some low priority processes. So this indicator is useful when we see high CPU utilization and we are afraid that this high load will have bad effect on our system:
    - High CPU utilization with high nice value: Nothing to worry, not so important tasks doing there job, important processes will easily get CPU time if they need. This situation is not a real bottleneck.
    - High CPU utilization with low nice value: Something to worry because the CPU is stressed with important processes so these or new processes will have to wait. This situation is a real bottleneck.

    **id, idle** time spent in the kernel idle handler.
    If the CPU is spending a more time in the other states then something is probably wrong, and may need trouble shooting.

    **wa, IO-wait** time waiting for I/O completion.
    'wa' is the measure of time over a given period that a CPU spent idle because all runnable tasks were waiting for a IO operation to be fulfilled.

    **hi** time spent servicing hardware interrupts.
    Since these can happen very frequently, and since they essentially block the current CPU while they are running, kernel hardware interrupt handlers are written to be as fast and simple as possible.
    On a system where no processes have been niced then the number will be 0.
    Hardware interrupts are physical interrupts sent to the CPU from various peripherals like disks and network interfaces. Software interrupts come from processes running on the system. A hardware interrupt will actually cause the CPU to stop what it is doing and go handle the interrupt. A software interrupt doesn't occur at the CPU level, but rather at the kernel level.

    **si** time spent servicing software interrupts.
    This represents the time spent in softirqs.

    **st** time stolen from this vm by the hypervisor.
    This represents "steal time", and it is only relevant in virtualized environments. It represents time when the real CPU was not available to the current virtual machine - it was "stolen" from that VM by the hypervisor (either to run another VM, or for its own needs).
    This number tells how long the virtual CPU has spent waiting for the hypervisor to service another virtual CPU running on a different virtual machine. Since in the real-world these virtual processors are sharing the same physical processor(s) then there will be times when the virtual machine wanted to run but the hypervisor scheduled another virtual machine instead.


    ### Here are some of the trouble shootings:

    - **High user mode CPU usage** - If a system suddenly jumps from having spare CPU cycles to running flat out high, then the first thing to check is the amount of time the CPU spends running user space processes. If this is high, then it probably means that a process has gone crazy and is eating up all the CPU time.
    Using the top command we will be able to see which process is to blame and **restart the service** or **kill the process**.

    - **High kernel CPU usage** - Sometimes this is acceptable. For example, a program that does lots of console I/O can cause the kernel usage to spike. However if it remains higher for long periods of time, then it could be an indication that something isn't right.
    A possible cause of such spikes could be a problem with a **driver/kernel module**.

    - **High niced value CPU usage** - If the amount of time the CPU is spending running processes with a niced priority value jumps, then it means that someone has started some intensive CPU jobs on the system, but they have niced the task.
    If the niceness level is greater than zero, then the user has been courteous enough lower to the priority of the process and therefore avoid a CPU overload. There is probably little that needs to be done in this case, other than maybe find out who has started the process.
    But if the niceness level is less than 0, then we will need to investigate what is happening and who is responsible, as such a task could easily cripple the responsiveness of the system.

    - **High waiting on I/O** This means that there are some intensive I/O tasks running on the system that don't use up much CPU time. If this number is high for anything other than short bursts, then it means that either the I/O performed by the task is very inefficient, or the data is being transferred to a very slow device, or there is a potential problem with a hard disk that is taking a long time to process reads & writes.

    - **High interrupt processing** This could be an indication of a broken peripheral that is causing lots of hardware interrupts or of a process that is issuing lots of software interrupts.

    - **Large stolen time** Basically, this means that the host system running the hypervisor is too busy. If possible, check the other virtual machines running on the hypervisor, and/or migrate our virtual machine to another host.

    When we have a **slow server**, one of the first values we should look at is I/O wait so we can rule out disk I/O. If I/O wait is low, then we can look at the idle percentage. If I/O wait is high, then the next step is to diagnose what is causing high disk I/O.

    If I/O wait and idle times are low, then we will likely see a high user time percentage, so we must diagnose what is causing high user time. If the I/O wait is low and the idle percentage is high, we then know any sluggishness is not because of CPU resources, and we will have to start troubleshooting elsewhere.
    This might mean looking for **network** problems, or in the case of a web server, looking at **slow queries** to MySQL, for instance.

- ps - process status listing
    ```
    $ ps -ef f
    ```
    Note "f" displays ASCII art process hierarchy (forest).
    To get the top 5 cpu eating process:
    ```
    $ ps -eo pcpu,pid,user | sort -k1 -r | head -6  
    ```

- vmstat
    The vmstat tool provides information about memory, swap utilization, IO wait, and system activity. It is particularly useful for diagnosing I/O-related issues.

    Usage : vmstat [interval [count]]
    ```
    vmstat 1 20
    ```
    The most salient information produced by this command is the wa column, which is the final column in most implementations. This field displays the amount of time the CPU spends waiting for IO operations to complete.

    If this number is consistently and considerably higher than 0, we might consider taking measures to address the IO usage.

    **Procs**:
    **r**: The number of processes waiting for run time.
    **b**: The number of processes in uninterruptible sleep.

    **Memory**
    **swpd**: the amount of virtual memory used.
    **free**: the amount of idle memory.
    **buff**: the amount of memory used as buffers.
    **cache**: the amount of memory used as cache.
    **inact**: the amount of inactive memory. (-a option)
    **active**: the amount of active memory. (-a option)

    **Swap**
    **si**: Amount of memory swapped in from disk (/s).
    **so**: Amount of memory swapped to disk (/s).

    **IO**
    **bi**: Blocks received from a block device (blocks/s).
    **bo**: Blocks sent to a block device (blocks/s).

    **System**
    **in**: The number of interrupts per second, including the clock.
    **cs**: The number of context switches per second.

    **CPU**
    These are percentages of total CPU time.
    **us**: Time spent running non-kernel code. (user time, including nice time).
    **sy**: Time spent running kernel code. (system time).
    **id**: Time spent idle. Prior to Linux 2.5.41, this includes IO-wait time.
    **wa**: Time spent waiting for IO. Prior to Linux 2.5.41, included in idle.
    **st**: Time stolen from a virtual machine. Prior to Linux 2.6.11, unknown.

- iostat - Block I/O disk utilization
    To monitor disk read/write rates of individual disks, we can use iostat. This tool allows us to monitor I/O statistics for each device or partition. Using iostat command, we can find out disk utilization and monitor system input/output device loading by observing the time the physical disks are active in relation to their average transfer rates.  

    To use this tool, we need to run sysstat package.
    Syntax for disk utilization report looks like this:
    ```
    iostat -d -x interval count
    ```
    where:

    **-d** : Display the device utilization report (d == disk)
    **-x** : Display extended statistics including disk utilization
    **interval** : It is time period in seconds between two samples. iostat 2 will give data at each 2 seconds interval.
    **count** : It is the number of times the data is needed. iostat 2 5 will give data at 2 seconds interval 5 times.

    The following values from the iostat output are the major ones:

    **r/s **: The number of read requests per second. See if a hard disk reports consistently high reads
    **w/s** : The number of write requests per second. See if a hard disk reports consistently high writes
    **svctm** : The average service time (in milliseconds) for I/O requests that were issued to the device.
    **%util** : Percentage of CPU time during which I/O requests were issued to the device (bandwidth utilization for the device). Device saturation occurs when this value is close to 100%.

- mpstat - multi-processor statistics, per-CPU
    We may want to look for unbalanced workloads, hot CPUs:
    ```
    $ mpstat -P ALL 1
    ```
- free
    The m option displays all data in MBs. 
    ```
    $ free -m
    ```
- sar - system activity report
    sar -P ALL 1 2 displays real time CPU usage for ALL cores every 1 second for 2 times (broken down by all cores).
    ```
    $ sar -P ALL 1 2
    ```
    sar -P 1 1 2 displays real time CPU usage for core number 1, every 1 second for 2 times.
    ```
    $ sar -P 1 1 2
    ```
    sar -n DEV 1 1 displays network devices vital statistics for eth0, eth1, etc. every 1 second for 1 times.
    ```
    $ sar -n DEV 1 1
    ```

- strace
    The strace is the tool that helps in debugging issues by tracing system calls executed by a program.
    ```
    # Slow the target command and print details for each syscall:
    strace command

    # Slow the target PID and print details for each syscall:
    strace -p PID

    # Slow the target PID and any newly created child process, printing syscall details:
    strace -fp PID

    # Slow the target PID and record syscalls, printing a summary:
    strace -cp PID

    # Slow the target PID and trace open() syscalls only:
    strace -eopen -p PID

    # Slow the target PID and trace open() and stat() syscalls only:
    strace -eopen,stat -p PID

    # Slow the target PID and trace connect() and accept() syscalls only:
    strace -econnect,accept -p PID

    # Slow the target command and see what other programs it launches (slow them too!):
    strace -qfeexecve command

    # Slow the target PID and print time-since-epoch with (distorted) microsecond resolution:
    strace -ttt -p PID

    # Slow the target PID and print syscall durations with (distorted) microsecond resolution:
    strace -T -p PID
    ```

    Another method is to use the -e option to select the events to be traced. For example, we can use the following command to trace open() and close() system calls:
    ```
    $ strace -e trace=open,close date
    ```

- dmesg

    The dmesg command displays all messages from the kernel ring buffer which is a data structure that records messages related to the operation of the kernel. A ring buffer is a special kind of buffer that is always a constant size, removing the oldest messages when new messages come in.

    We can use **dmesg** command to check why a process was killed. That happens if the process was consuming too much memory, and the kernel "**Out of Memory**" (OOM) killer will automatically kill the offending process.

- ab (Apache Bench)
    ApacheBench (ab) is a single-threaded command line computer program for measuring the performance of HTTP web servers. Though it was designed to test the Apache HTTP Server, it is generic enough to test any web server.

    Here is a typical command to do performance test making 100 requests with concurrency 10 to the example.com server.
    ```
    $ ab -n 100 -c 10 https://www.example.com/
    ```

## Linux tips 

- tee
    We frequently face the situation where a command runs on a root shell but redirection runs on a shell of a normal user.

    ```
    $ sudo echo "deb http://pkg.jenkins-ci.org/debian binary/" >>  /etc/apt/sources.list.d/jenkins.list (not working)
    $ echo "deb http://pkg.jenkins-ci.org/debian binary/" | sudo  tee -a /etc/apt/sources.list.d/jenkins.list
    $ echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list
    $ echo "/dev/sdf   /mnt/data-store ext3 defaults,noatime 1 2" | sudo  tee -a /etc/fstab
    ```
- awk
    The syntax looks like this:
    ```
    awk '/search_pattern/ { action_to_take_on_matches; another_action; }' file_to_parse
    ```
    like cat command:
    ```
    $ awk '{print}' /etc/fstab
    ```
    like grep command:
    ```
    $ awk '/UUID/' /etc/fstab
    $ awk '/^UUID/' /etc/fstab
    # print the first column, $0 is the entire line
    $ awk '/^UUID/ {print $1;}' /etc/fstab 
    # print 2nd (PID), 4 (MEM) and 11th (COMMAND) columns
    $ echo [PID]  [MEM]  [PATH] &&  ps aux | awk '{print $2, $4, $11}'
    ```
    How to get "192.168.*.*" from the output of "ifconfig" command?
    ```
    $ ifconfig | grep 'inet ' | egrep -v '172|127' | awk '{print $2}' | awk -F':' '{print $2}'
    # Or
    $ ifconfig |grep Mask | egrep -v '172|127' | awk '{print $2}' |cut -d: -f2
    ```
- tr
    We can use tr for translating, or deleting, or squeezing repeated characters. It will read from STDIN and write to STDOUT.

    ```
    $ tr a-z A-Z
    $ tr '()' '{}'
    $ tr '()' '{}' < ok1 > ok2
    $ tr " " "\n" < myfile.txt | grep zero 
    ```
- sed 
    A stream editor, we can use it to replacing a string with another either in-place or to a new file.
    We can in-place (via the option '-i') replace '-' with ':'
    ```
    $ sed -i 's/-/:/g' t.txt 
    # backup the old file as t.txt.bak
    $ sed -i .bak 's/-/:/g' t.txt
    # create another file
    $ sed 's/:/-/g' t.txt > tnew.txt 
    # In place deleting the last of a file
    $ sed -i '$ d' a.txt 
    # add 'line ' at the beginning of each line
    $ sed -i 's/^/line /g' t.txt
    # add '#' from line 1 to 10 at the beginning of each line
    $ sed -i '1,10{s/^/#/}' variables.tf
    # print from line 3 to 7
    $ sed -n 3,5p t.txt
    ```

- cut
    the option -f specifies which field we want to extract
    the option -d specifies what is the field delimiter
    ```
    $ cut -f1 -d':' /etc/passwd
    # or
    $ cut -f1 -d: /etc/passwd
    ```

- tac
    tac (which is "cat" backwards) outputs in reverse:

- watch
    We can execute a command periodically using watch command.
    By default watch command uses 2 second interval, we can change it using -n option. The following example executes df -h command every 10 seconds.
    ```
    $ watch -n 10 df -h
    ```

- Symbolic link (soft link) : ln -s
    ```
    $ ln -s target target-alias
    ```
- uptime - load average
    From left to right, these numbers show us the average load over the last 1 minute, the last 5 minutes, and the last 15 minutes.
    

    ```
    $ uptime
    16:48:25 up 32 min,  2 users,  load average: 0.58, 1.13, 2.46

    Assuming 1 cpu machine, it means:
    load average over the last 1 minute: 0.58 => The CPU idled for 42% of the time
    load average over the last 5 minutes: 1.13 => .13 processes were waiting for the CPU
    load average over the last 15 minutes: 2.46 => On average, 1.46 processes were waiting for the CPU

    if the machine has 2 CPUs
    load average over the last 1 minute: 0.58 => The CPU idled for 142% of the time
    load average over the last 5 minutes: 1.13 => .87 processes were waiting for the CPU
    load average over the last 15 minutes: 2.46 => On average, 0.46 processes were waiting for the CPU
    ```
- What is inode?
    **inode** is a "database" of all file information that tells about file structure. The inode of each file uses a pointer to point to the specific file, directory or object. The pointer is a unique number which usually is referred to as the inode number.
    ```
    $ ls -i myfile
    19147527 myfile
    ```
    To get more information that just the inode number, we can use the "stat" command:
    ```
    $ stat myfile
    ```
    To check inode count:
    ```
    $ df -i
    ```

- How to use 'dd' command?
    By default, dd reads from stdin and writes to stdout, but these can be changed by using the if (input file) and of (output file) options.
    We often use dd to simulate CPU load by filling a file with random content:
    ```
    $ dd if=/dev/urandom of=500MBfile bs=1M count=500
    ```
    For this, /dev/urandom will supply random numbers, which will be generated by the kernel. This will lead to an increased load on the CPU (sy - system time). 
    As a high IO read load example, a large file (such as an ISO file) will be read and written to /dev/null using dd:
    ```
    $ dd if=bigfile.iso of=/dev/null bs=1M
    ```

- Check if a file has been modified
    "%Y" should display "Time of last data modification as seconds since Epoch"
    ```
    $ stat -c %Y a.txt
    1487890881

    $ touch a.txt

    $ stat -c %Y a.txt
    1487890975

    $ stat -c %Y a.txt
    1487890975
    ```

- killing processes
    ```
    $ sudo killall nginx
    $ sudo pkill -u username
    ```