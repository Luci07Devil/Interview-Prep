# Amazon Redshift

Amazon Redshift is a fully managed data warehousing service provided by Amazon Web Services (AWS). It is designed for analyzing large datasets using SQL queries. Here are the key points you need to know:

## Query Execution Plan (EXPLAIN)

Redshift provides a powerful feature called **EXPLAIN**, which allows you to understand how it will interpret a query before actually running it. The EXPLAIN command generates an execution plan, estimating the query's complexity, data processing requirements, and data movement involved.

### Syntax

```sql
EXPLAIN [VERBOSE] query;
```

- `VERBOSE`: Displays the full query plan instead of just a summary.
- `query`: The SQL statement you want to explain (can be a SELECT, INSERT, CREATE TABLE AS, UPDATE, or DELETE statement).

### Execution Steps

The execution plan breaks down query execution into a sequence of steps and table operations. Here are some common steps:

1. **SCAN (Sequential Scan)**:
   - Scans an entire table sequentially from beginning to end.
   - Evaluates query constraints (e.g., WHERE clause).
   - Used for SELECT, INSERT, UPDATE, and DELETE statements.

2. **JOINS**:
   - Redshift uses different join operators based on table design and query attributes.
   - Examples:
     - **Nested Loop Join**: Least optimal, mainly for cross-joins (Cartesian products) and some inequality joins.
     - **Hash Join**: Used for inner joins and left/right outer joins. Typically faster than nested loop join.
     - **Merge Join**: Also used for inner and outer joins (for distributed and sorted join tables).

3. **Subquery Scan**:
   - Used for UNION queries.

4. **Query Planning and Execution**:
   - Redshift estimates resource costs (relative unit costs) to choose the best query plan.
   - Factors include schema, statistics, and temporary table creation time.

# Amazon Redshift Features

Amazon Redshift is a powerful cloud data warehouse that combines scalability, performance, and ease of management. Let's explore its features:

1. **Column-Oriented Databases**:
   - Redshift stores data in a columnar format, which improves query performance by minimizing I/O operations during data retrieval.
   - Columnar storage allows efficient compression and better data organization.

2. **End-to-End Data Encryption**:
   - Security is a top priority for Redshift.
   - It provides encryption for data at rest and in transit, ensuring your sensitive information remains protected.

3. **Massively Parallel Processing (MPP) Architecture**:
   - Redshift leverages MPP to distribute query execution across multiple nodes.
   - This parallel processing enables fast query performance, especially for large datasets.

4. **Cost-Effective**:
   - Redshift offers competitive pricing, allowing you to achieve the best price-performance ratio.
   - You pay only for the resources you use, and the separation of compute and storage (RA3 instances) further optimizes costs.

5. **Scalability**:
   - Whether you have gigabytes or exabytes of data, Redshift scales seamlessly.
   - It handles growing data volumes and concurrent users efficiently.

6. **Zero-ETL Approach**:
   - Break down data silos by integrating Redshift with other AWS services.
   - Redshift supports interoperability with Amazon S3 data lakes, Amazon Aurora, Amazon RDS, and more.
   - No need for complex ETL pipelines; data is ingested automatically or accessed in place.

7. **Comprehensive Analytics & ML**:
   - Execute SQL queries, build dashboards, and create AI/Gen-AI applications.
   - Use Redshift's Query Editor for collaborative data analysis.
   - Leverage Amazon Redshift ML to build, train, and deploy machine learning models directly within the warehouse.

8. **Secure Data Collaboration**:
   - Share data securely across AWS regions, teams, and third-party data warehouses.
   - No data movement or copying required.
   - Governed by AWS Lake Formation for centralized control.

9. **Fault Tolerance**:
   - Redshift's multi-AZ deployments deliver 99.99% SLAs.
   - Minimize disruptions and ensure high availability for your analytics workloads.

10. **Result Caching**:
    - Redshift intelligently caches query results to improve performance for frequently executed queries.

## Interleaved Sort Keys

An interleaved sort key is an alternative to the more common compound sort key. Here are the key points:

1. **Equal Weight for Columns**:
   - Unlike compound sort keys, which prioritize the order of columns, interleaved sort keys give **equal weight** to each column (or subset of columns) included in the sort key.
   - This means that query predicates can use **any subset** of the columns in the sort key, in **any order**.

2. **Query Flexibility**:
   - Interleaved sort keys are beneficial when there's **no dominant column** in your queries.
   - If your queries involve various combinations of filter conditions across different columns, an interleaved sort key can improve query performance.

3. **Example**:
   - Suppose you have a table storing sales data with columns like `product_id`, `sales_date`, `region`, and `quantity`.
   - An interleaved sort key on all these columns would allow efficient filtering based on any combination of these attributes.

4. **Considerations**:
   - Interleaved sort keys are **not always optimal**; they work well in specific scenarios.
   - Regularly perform **VACUUM REINDEX** on interleaved tables, as it analyzes the sort keys and can take longer than VACUUM FULL.
   - The sort and merge operation for interleaved tables might be more resource-intensive than for compound sort keys.

## **compound** and **interleaved** sort keys in **Amazon Redshift**:

1. **Compound Sort Key**:
   - A compound sort key is more efficient when query predicates use a **prefix**, which is a subset of the sort key columns in order.
   - In other words, if your queries often filter data based on the leftmost columns of the sort key, a compound sort key is a good choice.
   - The compound sort key organizes data hierarchically, with the first column having the most significant impact on sorting.
   - For example, if you have a compound sort key on columns `(A, B, C)`, queries filtering on `A` will benefit the most, followed by those filtering on `(A, B)`, and so on.
   - Use the `COMPOUND` keyword when defining your sort key¹.

2. **Interleaved Sort Key**:
   - An interleaved sort key gives **equal weight** to each column in the sort key.
   - Unlike the compound sort key, where the leftmost columns dominate, an interleaved sort key allows any subset of the columns to be used in query predicates, in any order.
   - If your queries don't consistently filter on a specific prefix of the sort key, an interleaved sort key might be more suitable.
   - However, keep in mind that interleaved sort keys can be less efficient for certain types of queries.
   - An interleaved sort key can use a maximum of **eight columns**.
   - Note that `VACUUM REINDEX` might take longer for interleaved tables due to additional analysis of the interleaved sort keys¹.

3. **Choosing Between Compound and Interleaved**:
   - **Compound**:
     - Recommended when you regularly update your tables with `INSERT`, `UPDATE`, or `DELETE` operations.
     - Provides better performance for queries that filter on a specific prefix of the sort key.
   - **Interleaved**:
     - Useful when there's no dominant column in your queries.
     - Allows flexibility in query predicates by considering any subset of the columns in the sort key.
     - Be cautious with interleaved sort keys for very large tables or complex queries.

Remember to use the `EXPLAIN` command to understand the impact of your chosen sort key on query performance. You can also query the `SVV_TABLE_INFO` system view to view the sort keys for a table¹. 

## SYSTEM TABLES IN REDSHIFT
In **Amazon Redshift**, system tables and views provide valuable information about how the system is functioning.

1. **SVV Views (System Views with References to Transient STV Tables)**:
   - SVV views contain information about database objects and their references to transient STV (System Table Virtual) tables.
   - These views provide details about various aspects of the system, including metadata, query execution, and session information.
   - Examples of SVV views:
     - `SVV_TABLE_INFO`: Contains information about tables in the database.
     - `SVV_COLUMNS`: Provides details about columns in tables.
     - `SVV_BLOCKLIST`: Shows blocked queries.
     - `SVV_TRANSACTIONS`: Displays transaction details.
     - ...and more.

2. **SYS Views (Used for Query and Workload Monitoring)**:
   - SYS views are specifically used to monitor query and workload usage for provisioned clusters and serverless workgroups.
   - They help track query performance, resource utilization, and overall system health.
   - Examples of SYS views:
     - `SYS_QUERY`: Contains information about executed queries.
     - `SYS_WLM_QUERY`: Provides details about workload management (WLM) queries.
     - `SYS_SESSION`: Displays session-level information.
     - ...and others related to monitoring.

3. **STL Views (History of System Logs)**:
   - STL views are generated from logs that have been persisted to disk, providing a historical record of system activity.
   - These views include details about query execution, execution states, and resource usage.
   - Examples of STL views:
     - `STL_QUERY`: Contains query execution history.
     - `STL_SCAN`: Shows details about table scans.
     - `STL_LOAD_ERRORS`: Displays load errors.
     - ...and more.

4. **STV Tables (Virtual Snapshots of Current System Data)**:
   - STV tables are virtual system tables based on transient in-memory data.
   - They contain snapshots of the current system state and are not persisted to disk-based logs or regular tables.
   - Examples of STV tables:
     - `STV_BLOCKLIST`: Contains blocked queries.
     - `STV_INFLIGHT`: Shows currently executing queries.
     - `STV_LOCKS`: Displays lock information.
     - ...and others related to real-time system status.

5. **SVCS Views (Details About Queries on Scaling Clusters)**:
   - SVCS views provide information about queries on both the main and concurrency scaling clusters.
   - Useful for understanding query distribution across different cluster nodes.

6. **SVL Views (Details About Queries on Main Clusters)**:
   - SVL views provide details about queries executed on the main clusters.
   - Includes information about query execution, resource usage, and query plans.

Remember that system tables and views do not follow the same consistency model as regular tables. 
When querying them, be aware of this difference, especially for STV tables and SVV views. 
For example, transient values may lead to unexpected results.

## Amazon Redshift Cluster

Amazon Redshift is a powerful **data warehousing service** that allows users to easily store, manage, and analyze large amounts of data in the cloud. 
An Amazon Redshift cluster is the fundamental building block of your data warehouse. It consists of **nodes**, which are organized into a cohesive group. Let's break down the essential components:

1. **Leader Node**:
   - The **leader node** plays a central role in query processing.
   - It receives queries from client applications, parses them, and develops query execution plans.
   - The leader node then coordinates the parallel execution of these plans with the compute nodes (discussed next).
   - Finally, it aggregates the intermediate results from compute nodes and returns the final results to the client applications.

2. **Compute Nodes**:
   - Compute nodes are the workhorses of the cluster.
   - Each cluster has one or more compute nodes.
   - These nodes run the query execution plans and transmit data among themselves to serve queries.
   - Compute nodes process data in parallel, enabling high-speed query performance.
   - Intermediate results are sent back to the leader node for aggregation before being returned to the client applications.

3. **Choosing Node Types**:
   - When creating a cluster, you specify the **node type**.
   - The node type determines CPU, RAM, storage capacity, and storage drive type for each node.
   - Amazon Redshift offers various node types (e.g., RA3, DC2) to accommodate different workloads.
   - **RA3 nodes with managed storage** allow you to optimize your data warehouse by scaling compute and storage independently.
   - Size your RA3 cluster based on the amount of data you process daily.

4. **Cluster Configuration**:
   - When launching a cluster, consider factors like data size, query characteristics, and expected growth.
   - You can use the **sizing calculator** in the Amazon Redshift console to get recommendations based on your workload.
   - Clusters using RA3 node types are launched in a **virtual private cloud (VPC)**.

5. **Monitoring and Management**:
   - Monitor your cluster using **Amazon CloudWatch** and custom alarms.
   - Consider using serverless solutions (e.g., AWS Lambda) for advanced monitoring.
   - Manage clusters programmatically using the **Amazon Redshift API** or SDK libraries.

## Redshift Cluster Creation

To create your own Amazon Redshift cluster, follow these steps:

1. **Launch a Cluster**:
   - Use the Amazon Redshift console to create a cluster.
   - Specify the node type, VPC settings, and other configuration options.
   - Get recommendations based on your workload.

2. **Load Data**:
   - Load your data into the cluster using COPY commands or other methods.
   - Amazon Redshift supports various data formats (CSV, Parquet, JSON, etc.).

3. **Query Your Data**:
   - Write SQL queries to analyze your data.
   - Leverage the power of parallel processing and optimized storage.

Remember that Amazon Redshift clusters are designed for scalability, performance, and ease of management. 
Whether you're handling large-scale analytics or building data-driven applications, Redshift clusters provide the foundation for efficient data processing in the cloud¹².

## Amazon Redshift Node Types

An Amazon Redshift data warehouse consists of computing resources organized into a group called a **cluster**. 
Each cluster runs an Amazon Redshift engine and contains one or more databases. 
The core components of an Amazon Redshift cluster are the **leader node** and the **compute nodes**¹.

### 1. Leader Node
- The **leader node** is responsible for:
  - Receiving queries from client applications.
  - Parsing queries and developing query execution plans.
  - Coordinating parallel execution of query plans with compute nodes.
  - Aggregating intermediate results from compute nodes.
  - Returning final query results to client applications.

### 2. Compute Nodes
- Compute nodes run query execution plans and transmit data among themselves to serve queries.
- They execute query tasks in parallel.
- Intermediate results are sent back to the leader node for aggregation before being returned to client applications.

### Node Types
Amazon Redshift offers different node types to accommodate various workloads. Here are the key node types:

1. **Dense Compute Nodes (DC2)**
   - Best for performance-intensive workloads.
   - Equipped with solid-state disk drives (SSD).
   - Suitable for scenarios where fast query execution is critical.

2. **Dense Storage Nodes (DS2)**
   - Ideal for large data workloads.
   - Come with hard disk drives (HDD).
   - Designed to handle large volumes of data efficiently.

3. **RA3 Nodes**
   - RA3 nodes with managed storage allow you to optimize your data warehouse.
   - You can scale compute and pay for managed storage independently.
   - Choose the number of nodes based on performance requirements and pay only for the storage you use.
   - Size your RA3 cluster based on the daily data processing needs.

Remember to select the appropriate node type based on your workload requirements, data size, and expected growth.
When creating a cluster, you can use the sizing calculator to get recommendations based on your data and query characteristics¹.
