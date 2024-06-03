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

## Triggers in RDBMS

**Triggers** are special types of stored procedures that automatically execute in response to specific events occurring in a database. These events are typically related to changes made to a table's data, such as insertions, updates, or deletions. Triggers play a crucial role in maintaining data integrity and enforcing business rules within the database.

### Types of Triggers

1. **AFTER INSERT Trigger**:
   - Activated after data is inserted into a table.
   - Useful for performing actions after new records are added.
   - Example: Suppose we have an `Orders` table, and we want to update the `OrderCount` in another table after each new order is placed.

2. **AFTER UPDATE Trigger**:
   - Activated after data in a table is modified (updated).
   - Useful for handling post-update tasks.
   - Example: Updating a `LastModified` timestamp whenever an employee's record is updated.

3. **AFTER DELETE Trigger**:
   - Activated after data is deleted or removed from a table.
   - Useful for maintaining historical records or logging deletions.
   - Example: Archiving deleted records in an `EmployeeArchive` table.

4. **BEFORE INSERT Trigger**:
   - Activated before data is inserted into a table.
   - Useful for enforcing pre-insert conditions or validations.
   - Example: Ensuring that an employee's age is at least 25 years before adding their record.

5. **BEFORE UPDATE Trigger**:
   - Activated before data in a table is modified.
   - Useful for enforcing business rules or constraints before updates.
   - Example: Preventing salary updates beyond a certain limit.

6. **BEFORE DELETE Trigger**:
   - Activated before data is deleted from a table.
   - Useful for cascading deletions or additional checks.
   - Example: Checking if an employee can be deleted based on their role.

### Examples

1. **Age Validation Trigger**:
   ```sql
   CREATE TRIGGER CheckAge
   BEFORE INSERT ON Employees
   FOR EACH ROW
   BEGIN
       IF NEW.Age < 25 THEN
           SIGNAL SQLSTATE '45000'
           SET MESSAGE_TEXT = 'ERROR: AGE MUST BE AT LEAST 25 YEARS!';
       END IF;
   END;
   ```
   Explanation: This trigger ensures that no employee younger than 25 can be inserted into the `Employees` table.

2. **Backup Trigger**:
   ```sql
   CREATE TABLE EmployeeBackup (
       EmployeeNo INT,
       EmployeeName VARCHAR(40),
       Job VARCHAR(40),
       HireDate DATE,
       Salary INT,
       PRIMARY KEY (EmployeeNo)
   );

   CREATE TRIGGER Backup
   BEFORE DELETE ON Employees
   FOR EACH ROW
   BEGIN
       INSERT INTO EmployeeBackup
       VALUES (OLD.EmployeeNo, OLD.EmployeeName, OLD.Job, OLD.HireDate, OLD.Salary);
   END;
   ```
   Explanation: The `Backup` trigger creates a backup record in the `EmployeeBackup` table before deleting an employee from the main table.

3. **Counting Inserted Tuples Trigger**:
   ```sql
   DECLARE Count INT;
   SET Count = 0;

   CREATE TRIGGER CountTuples
   AFTER INSERT ON Employees
   FOR EACH ROW
   BEGIN
       SET Count = Count + 1;
   END;
   ```
   Explanation: This trigger keeps track of the number of new tuples inserted using each `INSERT` statement.

## **Nested triggers**

**Nested triggers** in **SQL Server** refer to triggers that are fired as a result of the execution of other triggers.

1. **Types of Triggers**:
   - **AFTER Triggers**: These execute after a **DML** (Data Manipulation Language) or **DDL** (Data Definition Language) operation (e.g., **INSERT**, **UPDATE**, **DELETE**, **CREATE**, **ALTER**, **DROP**).
   - **INSTEAD OF Triggers**: These execute in place of a DML or DDL operation.
   - **Nested Triggers**: These are triggered by other triggers, creating a chain of trigger execution.

2. **How Nested Triggers Work**:
   - Suppose we want to ensure that no one can directly insert data into the `CarLog` table. Instead, we want to insert a subset of data from the `Car` table into `CarLog`.
   - To achieve this, we'll create two triggers:
     - **First Trigger (CarLog)**: Prevents direct insertion into `CarLog`.
     - **Second Trigger (Car)**: Inserts data into `CarLog` after inserting data into `Car`.
   - Here's an example:

```sql
-- First Trigger (CarLog)
CREATE TRIGGER PreventCarLogInsert
ON CarLog
INSTEAD OF INSERT
AS
BEGIN
    RAISEERROR('Direct insertion into CarLog is not allowed.', 16, 1);
END;

-- Second Trigger (Car)
CREATE TRIGGER InsertIntoCarLog
ON Car
AFTER INSERT
AS
BEGIN
    INSERT INTO CarLog (CarId, CarName)
    SELECT CarId, Name
    FROM inserted;
END;
```

3. **Explanation**:
   - The **`PreventCarLogInsert`** trigger prevents direct inserts into `CarLog`.
   - The **`InsertIntoCarLog`** trigger fires after an insert into `Car`. It selects relevant data from the **`inserted`** pseudo-table (which contains newly inserted rows) and inserts it into `CarLog`.

Remember that while nested triggers can be powerful, they should be used judiciously. 
Incorrect usage can lead to problems. Always ensure proper backups before implementing triggers¹².

## Performance impact of using **nested triggers** in **SQL Server**

1. **Recompilations and Execution Plans**:
   - **Nested triggers** can lead to excessive recompilations. Each time a trigger fires, SQL Server recompiles the trigger code, which can be resource-intensive.
   - If you include calls to other objects (such as stored procedures or functions) within a trigger, it may result in frequent recompilations and inefficient execution plans being cached².

2. **Parameter Sniffing**:
   - When executing stored procedures or functions from inside a trigger, you might encounter **parameter sniffing** issues.
   - Parameter sniffing occurs when SQL Server generates an execution plan based on the first set of parameters passed to a stored procedure or function. If subsequent executions use different parameter values, the cached plan may not be optimal.
   - Consider using local variables within the trigger to avoid parameter sniffing problems².

3. **Performance Bottlenecks**:
   - Triggers execute within the same transaction as the original operation (e.g., **INSERT**, **UPDATE**, or **DELETE**).
   - If a trigger performs resource-intensive tasks (such as complex calculations, data validation, or logging), it can slow down the entire transaction.
   - Be cautious about the logic and complexity of trigger code to prevent performance bottlenecks.

4. **Avoid Recursive Triggers**:
   - Recursive triggers occur when a trigger fires another trigger, creating a chain of execution.
   - While nested triggers are allowed, excessive recursion can lead to poor performance and unexpected behavior.
   - Set proper conditions to prevent infinite loops caused by recursive triggers.

5. **Consider Alternatives**:
   - Evaluate whether triggers are the best solution for your requirements.
   - Sometimes, alternative approaches (such as using stored procedures or application-level logic) can achieve the same goals without the overhead of triggers.

## Advantages of using nested triggers:

1. **Automated Auditing**:
   - **Nested triggers** allow you to create more robust auditing solutions.
   - By using the `deleted` table inside a trigger, you can build an audit trail that captures data changes (insertions, updates, or deletions) and store them in an audit table.
   - This ensures that you have a historical record of all modifications made to your data¹.

2. **Batch Data Validation**:
   - Triggers are useful when you need to validate data in batches rather than row by row.
   - Within a trigger's code, you have access to the `inserted` and `deleted` tables, which hold copies of data that will be stored (in the `inserted` table) or removed (in the `deleted` table) from the main table.
   - This batch processing capability is valuable for complex validation scenarios¹.

3. **Referential Integrity Across Databases**:
   - SQL Server doesn't allow direct creation of constraints between objects in different databases.
   - However, by using triggers, you can simulate referential integrity across databases.
   - For example, you can enforce foreign key relationships between tables in separate databases using triggers¹.

4. **Ensuring Consistent Events**:
   - Triggers ensure that specific events always happen when data is inserted, updated, or deleted.
   - This is crucial when dealing with complex default values for columns or when modifying data in other related tables.
   - Triggers guarantee consistency across related data entities¹.

5. **Recursion and Self-Referencing Constraints**:
   - Nested triggers allow recursion, which means a trigger on a table can perform an action that causes another instance of the same trigger to fire.
   - This is useful for solving self-referencing relations (constraints to itself) within the database schema¹.

6. **CLR Triggers and External Code**:
   - You can use **Common Language Runtime (CLR)** triggers to incorporate external code written in .NET languages.
   - CLR triggers allow you to bind triggers to methods in .NET assemblies, extending the trigger functionality beyond T-SQL.
   - This flexibility enables you to perform custom actions using external libraries or business logic¹.

## **Nested triggers** - limitations and considerations

1. **Performance Impact**:
   - **Nested triggers** can lead to performance bottlenecks.
   - Each trigger execution involves additional processing, which can impact system response times.
   - Frequent recompilations due to nested triggers can affect query performance¹.

2. **Recompilations and Execution Plans**:
   - Triggers are recompiled each time they fire, which can be resource-intensive.
   - Excessive recompilations may occur if triggers are nested, affecting overall performance.
   - Properly manage triggers to avoid unnecessary recompilations¹.

3. **Transaction Behavior**:
   - Triggers execute within the same transaction as the original operation (e.g., **INSERT**, **UPDATE**, or **DELETE**).
   - If a nested trigger fails, the entire transaction is rolled back, affecting data consistency.
   - Be cautious about complex logic within triggers to prevent unintended rollbacks⁴.

4. **Parameter Sniffing**:
   - Nested triggers can lead to **parameter sniffing** issues.
   - Parameter sniffing occurs when cached execution plans are based on specific parameter values.
   - Consider using local variables within triggers to avoid parameter sniffing problems¹.

5. **Avoid Recursive Triggers**:
   - Recursive triggers occur when a trigger fires another trigger, creating a loop.
   - Excessive recursion can lead to poor performance and unexpected behavior.
   - Set proper conditions to prevent infinite loops caused by recursive triggers¹.

6. **Maintenance Complexity**:
   - Managing nested triggers can become complex.
   - Debugging and maintaining code with multiple layers of triggers may be challenging.
   - Document your trigger logic thoroughly to ease future maintenance¹.

## Difference between **Row Level Triggers** and **Statement Level Triggers**

### Row Level Triggers
- **Activation Frequency**: Row level triggers execute **once for each row** in a transaction.
- **Purpose**: They are specifically used for **data auditing** purposes.
- **Example**: If you're inserting 1500 rows into a table, a row level trigger would execute **1500 times** (once for each row).

### Statement Level Triggers
- **Activation Frequency**: Statement level triggers execute **only once** for each single transaction, regardless of the number of rows affected.
- **Purpose**: They are used for enforcing **additional security** on the transactions performed on the table.
- **Example**: If you're inserting 1500 rows into a table, a statement level trigger would execute **only once**.

In summary, row level triggers focus on individual rows, while statement level triggers operate at the transaction level.

## LINKS
> https://learnsql.com/blog/sql-window-functions-cheat-sheet/
> https://learnsql.com/blog/sql-join-cheat-sheet/
> https://learnsql.com/blog/sql-basics-cheat-sheet/
> https://learnsql.com/blog/standard-sql-functions-cheat-sheet/
> https://learnsql.com/blog/sql-for-data-analysis-cheat-sheet/
