
# smart toothbrush

# system requirements

- both batch and stream processing
- fault tolerance
- exactly-once consistency
- big data
- ingestion statistics need to be locally available to return after a job is completed
- iterate through 2 streams together to correctly translate ticks to UNIX timestamps (only stream #2 has the timestamps)

---

# stream computation framework: ❓

[Spark vs Flink?](https://data-flair.training/blogs/comparison-apache-flink-vs-apache-spark/)

Flink ✅

- Lightweight, which results in maintaining **high throughput** rates and provide **strong consistency guarantees** at the same time.
- Uses streams for all workloads & batch is just a finite set of streamed data
- In-memory computing; task/job state is locally available
- Provides distributed processing

Spark

- Recovers lost work and delivers exactly-once semantics out of the box with no extra code or configuration.
- Not sufficient for large streams of live data - high latency

# [computation framework: flink](https://data-flair.training/blogs/flink-tutorial/)

---

# cloud storage system: ❓

requirements:

- NoSQL Database
- index by device/toothbrush id & timestamps
- efficient batch write
- high scale
- high performance search

choices:

- MongoDB
- HBase in the Hadoop ecosystem ✅

# [cloud storage system: HBase](http://data-flair.training/blogs/hbase-tutorial-beginners-guide/)

---