


## Log vs Cache (ZFS)

􏱾 Log: A log vdev is for ZFS Intent Log (ZIL). The ZIL increases the write per- formance on ZFS. Only dynamic stripe and mirrored vdev configurations are supported for this vdev type.
􏱾 Cache: A cache vdev is used to speed up random reads from a RAID-Z-configured pool. Its intended use is for read-heavy workloads. There is no redundancy support at this point for this vdev type. If there is a read error, then ZFS will read from the original storage pool.

Log usually is for writing and cache is usually for reading.??
