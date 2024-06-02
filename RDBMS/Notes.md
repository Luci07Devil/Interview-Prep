## Choosing between a **relational database** and a **NoSQL database**

### Relational Database

1. **Structure**:
   - Relational databases store data in related tables with a fixed schema.
   - Each table represents a specific type of data (e.g., customers, orders) with columns defining attributes (e.g., name, email, address).

2. **Query Language**:
   - Relational databases use **Structured Query Language (SQL)** for data manipulation.
   - SQL allows complex queries, joins, and transactions.

3. **Consistency**:
   - Relational databases provide **ACID guarantees** (Atomicity, Consistency, Isolation, Durability).
   - Ensures data integrity and accuracy.

4. **Use Cases**:
   - Ideal for scenarios where data precision matters, such as financial transactions, inventory management, and complex relationships.

## NoSQL Database

1. **Flexibility**:
   - NoSQL databases are non-relational and offer flexibility.
   - They handle unstructured or semi-structured data efficiently.

2. **Scalability**:
   - NoSQL databases excel in scalability.
   - Easily handle large volumes of data and high read/write loads.

3. **Ease of Use**:
   - NoSQL databases are simpler to set up and manage.
   - Well-suited for rapid development and prototyping.

4. **Availability and Resilience**:
   - NoSQL databases are designed for high availability and fault tolerance.
   - Distributed architecture ensures resilience.

## Considerations for Choosing:

1. **Data Model**:
   - If your data has a well-defined schema and complex relationships, consider a relational database.
   - If your data is dynamic, schema-less, or hierarchical, NoSQL may be a better fit.

2. **Scalability Requirements**:
   - If you anticipate rapid growth or need horizontal scalability, NoSQL databases are preferable.
   - Relational databases can scale vertically but have limitations.

3. **Development Speed**:
   - NoSQL databases allow faster development due to their flexible schema.
   - Relational databases may require more upfront design.

4. **Consistency vs. Flexibility**:
   - Choose based on your priority: data consistency (relational) or flexibility (NoSQL).

## `RANK()`, `ROW_NUMBER()`, and `DENSE_RANK()` functions in SQL.

### RANK()
The `RANK()` function assigns a rank to each row within a result set based on the values of one or more columns. When there are ties (i.e., multiple rows with the same value), `RANK()` assigns the same rank to those tied rows and then skips the next rank. For example:

```sql
SELECT SALARY, RANK() OVER (ORDER BY SALARY) AS RANK
FROM Employee;
```

Output:
```
SALARY | RANK
1000   | 1
1500   | 2
1500   | 2
2000   | 4
2200   | 5
2500   | 6
2500   | 6
2500   | 6
3000   | 9
```

In the above example, the second and third rows have the same salary of 1500, so they both get a rank of 2. The next rank (3) is skipped.

### ROW_NUMBER()
The `ROW_NUMBER()` function generates a unique, incremental number for each row in the result set, regardless of duplicates. It does not handle ties; each row receives a distinct number:

```sql
SELECT SALARY, ROW_NUMBER() OVER (ORDER BY SALARY) AS ROW_NUM
FROM Employee;
```

Output:
```
SALARY | ROW_NUM
1000   | 1
1500   | 2
1500   | 3
2000   | 4
2200   | 5
2500   | 6
2500   | 7
2500   | 8
3000   | 9
```

### DENSE_RANK()
The `DENSE_RANK()` function also assigns a rank to each row based on column values. However, it handles ties differently. When there are ties, it assigns the same rank to tied rows and continues the rank count without skipping any numbers:

```sql
SELECT SALARY, DENSE_RANK() OVER (ORDER BY SALARY) AS DENSE_RANK
FROM Employee;
```

Output:
```
SALARY | DENSE_RANK
1000   | 1
1500   | 2
1500   | 2
2000   | 3
2200   | 4
2500   | 5
2500   | 5
2500   | 5
3000   | 6
```

In this example, the second and third rows (with salary 1500) both receive a rank of 2, and the next rank (3) is not skipped.

Choose the appropriate function based on your requirements:
- Use `DENSE_RANK()` when you want consecutive ranks even in the presence of ties (e.g., reporting winners with first, second, and third places).
- Use `RANK()` when you want to skip ranks for tied rows (e.g., no second or third place).
- Use `ROW_NUMBER()` when you need a unique number for each row, regardless of duplicates¹²³⁴.

## List of Window Functions
####Ranking Functions
* row_number()
* rank()
* dense_rank()
#### Distribution Functions
* percent_rank()
* cume_dist()
#### Analytic Functions
* lead()
* lag()
* ntile()
* first_value()
* last_value()
* nth_value()
#### Aggregate Functions
* avg()
* count()
* max()
* min()
* sum()
