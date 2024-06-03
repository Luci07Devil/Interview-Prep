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

## ACID Properties in DBMS

1. **Atomicity**:
   - **Definition**: Atomicity ensures that either the entire transaction takes place at once or doesn't happen at all. There is no midway—transactions do not occur partially.
   - **Operations**:
     - **Abort**: If a transaction aborts, changes made to the database are not visible.
     - **Commit**: If a transaction commits, changes made are visible.
   - **Example**: Consider a transaction transferring 100 units from account X to account Y. If the transaction fails after deducting from X but before adding to Y, the database becomes inconsistent. Thus, transactions must execute entirely to maintain correctness¹.

2. **Consistency**:
   - **Definition**: Consistency ensures that integrity constraints are maintained, making the database consistent before and after the transaction.
   - **Example**: Suppose the total amount before the transaction is 700 (500 in X and 200 in Y). After the transaction, it should remain consistent (400 in X and 300 in Y). Inconsistency occurs if T1 completes but T2 fails, leaving the database in an incomplete state¹.

3. **Isolation**:
   - **Definition**: Isolation ensures that multiple transactions can occur concurrently without affecting the database's consistency.
   - **Behavior**:
     - Changes within a transaction are not visible to other transactions until committed.
     - Execution of concurrent transactions results in a state equivalent to serial execution.
   - **Example**: Let X = 500, Y = 500. If two transactions (T and T'') read and update X and Y concurrently, proper isolation prevents inconsistencies¹.

4. **Durability**:
   - **Definition**: Durability ensures that once a transaction completes, updates and modifications are stored in and written to disk. They persist even after system failures.
   - **Guarantee**: Even if the system crashes, committed changes remain intact.
   - **Example**: After a successful transaction, the database remains durable, safeguarding data integrity¹.

ACID properties provide a robust foundation for reliable transaction processing in DBMS. 
They ensure that each transaction acts as a single unit, produces consistent results, operates independently, and persists its updates⁵.

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

## Most commonly used SQL aggregate functions

1. **`AVG(column_name)`**:
   - Returns the average value of a numeric column.
   - Example: Calculate the average salary from an "Employees" table: `SELECT AVG(Salary) FROM Employees;`

2. **`COUNT(column_name | *)`**:
   - Returns the number of rows in a table or the number of non-null values in a specified column.
   - Example: Count the total number of orders in an "Orders" table: `SELECT COUNT(*) FROM Orders;`

3. **`MAX(column_name)`**:
   - Returns the maximum value within the selected column.
   - Example: Find the highest product price from a "Products" table: `SELECT MAX(Price) FROM Products;`

4. **`MIN(column_name)`**:
   - Returns the minimum value within the selected column.
   - Example: Retrieve the lowest temperature from a "Weather" table: `SELECT MIN(Temperature) FROM Weather;`

5. **`SUM(column_name)`**:
   - Returns the sum of all values in a numeric column.
   - Example: Calculate the total revenue from an "Invoices" table: `SELECT SUM(TotalAmount) FROM Invoices;`

## SQL string functions

1. **`ASCII(string)`**:
   - Returns the ASCII value of the first character in the input string.
   - Example: `SELECT ASCII('A'); -- Returns 65`

2. **`CHAR(index)`**:
   - Returns the character corresponding to the specified ASCII value.
   - Example: `SELECT CHAR(65); -- Returns 'A'`

3. **`CHARINDEX(substring, string)`**:
   - Returns the starting position of a substring within a string.
   - Example: `SELECT CHARINDEX('world', 'Hello, world!'); -- Returns 8`

4. **`CONCAT(string1, string2, ...)`**:
   - Concatenates two or more strings.
   - Example: `SELECT CONCAT('Hello', ' ', 'World'); -- Returns 'Hello World'`

5. **`LEFT(string, length)`**:
   - Returns the leftmost characters of a string up to the specified length.
   - Example: `SELECT LEFT('Hello', 3); -- Returns 'Hel'`

6. **`LEN(string)`**:
   - Returns the length (number of characters) of a string.
   - Example: `SELECT LEN('Hello'); -- Returns 5`

7. **`LOWER(string)`**:
   - Converts a string to lowercase.
   - Example: `SELECT LOWER('Hello'); -- Returns 'hello'`

8. **`REPLACE(string, old_substring, new_substring)`**:
   - Replaces occurrences of a substring with another substring.
   - Example: `SELECT REPLACE('Hello, world!', 'world', 'universe'); -- Returns 'Hello, universe!'`

9. **`RIGHT(string, length)`**:
   - Returns the rightmost characters of a string up to the specified length.
   - Example: `SELECT RIGHT('Hello', 2); -- Returns 'lo'`

10. **`TRIM(string)`**:
    - Removes leading and trailing spaces from a string.
    - Example: `SELECT TRIM('   Hello   '); -- Returns 'Hello'`

11. **`UPPER(string)`**:
    - Converts a string to uppercase.
    - Example: `SELECT UPPER('Hello'); -- Returns 'HELLO'`

# Indexes in Relational Databases (RDBMS)

Indexes play a crucial role in optimizing query performance within relational databases.

## What Are Database Indexes?

A database index is an additional data structure created on top of the data in a table. When you specify an index over a table and a column (or set of columns), it creates an additional data search structure associated with that table. The primary purpose of an index is to improve query performance by speeding up data retrieval. However, this efficiency comes at the cost of additional storage space to hold the index data structure and pointers to the actual data.

## Implicit Index vs. Composite Index in RDBMS

## 1. Implicit Index

### Description
An implicit index is automatically created by the database system to support primary key constraints or unique constraints. It is tied to a specific column (or set of columns) and ensures data uniqueness.

### Characteristics
- **Single Column**: Implicit indexes are associated with a single column.
- **Automatically Created**: When you define a primary key or unique constraint, the database system generates an implicit index.
- **Hidden from Users**: Users don't explicitly create or manage implicit indexes; they are maintained by the database engine.

### Use Cases
- **Primary Key Constraint**: The primary key enforces uniqueness and identifies each row uniquely within a table.
- **Unique Constraint**: Ensures that values in the indexed column(s) are unique across rows.

### Example

```sql
-- Implicit index for primary key
CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    UserName VARCHAR(50)
);
```

## 2. Composite Index

### Description
A composite index (also known as a multi-column index) involves multiple columns. It combines the values from these columns into a single index entry.

### Characteristics
- **Multiple Columns**: Composite indexes span two or more columns.
- **Explicitly Created**: Users define composite indexes based on specific query requirements.
- **Order Matters**: The order of columns matters; the index is built using the specified column order.

### Use Cases
- **Query Optimization**: Composite indexes improve query performance for WHERE clauses involving multiple columns.
- **Covering Index**: A well-designed composite index can cover all columns needed for a query, avoiding additional lookups.

### Example

```sql
-- Composite index for efficient search by (City, Country)
CREATE INDEX IX_Location ON Customers (City, Country);
```

## Types of Indexes

### 1. **B-Tree Index (Nonclustered Index)**

- **Description**: The B-Tree index is the most common type of index. It organizes data in a balanced tree structure, allowing efficient range queries and equality searches.
- **When to Use**:
  - For columns with high cardinality (many distinct values).
  - For equality searches (e.g., WHERE clause with = operator).
  - For range queries (e.g., BETWEEN, >, <).

### 2. **Bitmap Index**

- **Description**: A bitmap index uses bitmaps to represent the presence or absence of values for each row in the table. It's efficient for low-cardinality columns (few distinct values).
- **When to Use**:
  - For columns with few distinct values (e.g., gender, status).
  - Not suitable for frequently updated tables.

### 3. **Hash Index**

- **Description**: Hash indexes use a hash function to map keys to specific locations in memory. They work well for equality searches but not for range queries.
- **When to Use**:
  - For exact match lookups (e.g., primary key columns).
  - Not suitable for range queries.

### 4. **Clustered Index**

- **Description**: Unlike other indexes, a clustered index determines the physical order of rows in a table. Each table can have only one clustered index.
- **When to Use**:
  - For columns frequently used in range queries.
  - When you want to physically order the data based on a specific column.

### 5. **Full-Text Index**

- **Description**: Full-text indexes enable efficient text-based searches within large text columns (e.g., articles, descriptions).
- **When to Use**:
  - For searching natural language content.
  - Not suitable for small tables or non-text columns.

### 6. **Spatial Index**

- **Description**: Spatial indexes optimize spatial data (e.g., geographic coordinates, polygons). They support spatial queries like distance-based searches.
- **When to Use**:
  - For geographical or geometric data.
  - When performing spatial queries.

## How to Create an Index

To create an index, use the following general syntax (specific syntax may vary by RDBMS):

```sql
CREATE INDEX index_name ON table_name (column_name_1, column_name_2, ...);
```

For example:

```sql
CREATE INDEX IX_CustomerName ON Customer (FirstName, LastName);
```

LINKS
> https://learnsql.com/blog/sql-window-functions-cheat-sheet/
> https://learnsql.com/blog/sql-join-cheat-sheet/
> https://learnsql.com/blog/sql-basics-cheat-sheet/
> https://learnsql.com/blog/standard-sql-functions-cheat-sheet/
> https://learnsql.com/blog/sql-for-data-analysis-cheat-sheet/
> 
