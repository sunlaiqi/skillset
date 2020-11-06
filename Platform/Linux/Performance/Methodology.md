

Methodologies can help the performance analyst approach complex systems by showing where to start and what steps to take to locate and analyze performance issues. 

## Terminology

**IOPS**: Input/output operations per second is a measure of the rate of data transfer operations. For disk I/O, IOPS refers to reads and writes per second.
**Throughput**: the rate of work performed. Especially in communications, the term is used to refer to the data rate (bytes per second or bits per second). In some contexts (e.g., databases), throughput can refer to the operation rate (operations per second or transactions per second).
**Response time**: the time for an operation to complete. This includes any time spent waiting and time spent being serviced (service time), including the time to transfer the result.
**Latency**: Latency is a measure of time an operation spends waiting to be serviced. In some contexts, it can refer to the entire time for an operation, equivalent to response time.
**Utilization**: For resources that service requests, utilization is a measure of how busy a resource is, based on how much time in a given interval it was actively performing work. For resources that provide storage, utilization may refer to the capacity that is consumed (e.g., memory utilization).
**Saturation**: the degree to which a resource has queued work it cannot service.
**Bottleneck**: In system performance, a bottleneck is a resource that limits the performance of the system. Identifying and removing systemic bottlenecks is a key activity of systems performance.
**Workload**: The input to the system or the load applied is the workload. For a database, the workload consists of the database queries and commands sent by the clients.
**Cache**: a fast storage area that can duplicate or buffer a limited amount of data, to avoid communicating directly with a slower tier of storage, thereby improving performance. For economic reasons, a cache is smaller than the slower tier.

## Concepts
### Latency
The latency is the time spent waiting before an operation is performed.
As latency is a time-based metric, various calculations are possible. Performance issues can be quantified using latency and then ranked because they are expressed using the same units (time). Predicted speedup can also be calculated, by considering when latency can be reduced or removed. Neither of these can be accurately performed using an IOPS metric, for example.
When possible, other metric types can be converted to latency or time so that they can be compared.