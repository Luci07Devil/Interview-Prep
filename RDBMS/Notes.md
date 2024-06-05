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

**ACID properties** in **Relational Database Management Systems (RDBMS)** are fundamental principles that ensure reliable and predictable transactional behavior. They stand for:

1. **Atomicity**: Transactions are either fully completed or fully rolled back, ensuring all-or-nothing execution.
2. **Consistency**: Transactions maintain the database's integrity by transitioning from one consistent state to another.
3. **Isolation**: Transactions occur independently, without interfering with each other, preventing data anomalies.
4. **Durability**: Once committed, changes persist even after system failures or crashes¹²³⁴⁵.

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

## To address the "lost update" problem
database systems employ various techniques to ensure data consistency and prevent concurrent transactions from interfering with each other. Here are some strategies:

1. **Locking Mechanisms**:
   - **Exclusive Locks**: When a transaction modifies a record, it acquires an exclusive lock on that record. Other transactions must wait until the lock is released.
   - **Shared Locks**: Transactions reading data acquire shared locks. Exclusive locks are only granted when no shared locks exist.
   - **Drawback**: Lock contention can lead to performance issues.

2. **Isolation Levels**:
   - Specify the level of isolation between concurrent transactions.
   - Common levels:
     - **Read Uncommitted**: No locks; dirty reads possible.
     - **Read Committed**: Locks acquired during read; no dirty reads.
     - **Repeatable Read**: Locks acquired during read and held until the end of the transaction.
     - **Serializable**: Strongest isolation; prevents anomalies.
   - **Drawback**: Higher isolation levels may impact performance.

3. **Timestamp-Based Concurrency Control**:
   - Assign timestamps to transactions.
   - Ensure that transactions with earlier timestamps execute first.
   - Prevents lost updates by enforcing a chronological order.
   - **Drawback**: Requires a reliable timestamp mechanism.

4. **Optimistic Concurrency Control**:
   - Transactions read data without acquiring locks.
   - Before committing, check if any other transaction modified the same data.
   - If conflicts occur, handle them (e.g., retry or abort).
   - **Drawback**: Requires additional checks during commit.

5. **Multi-Version Concurrency Control (MVCC)**:
   - Maintain multiple versions of data.
   - Each transaction sees a consistent snapshot based on its start time.
   - Avoids lost updates by allowing concurrent reads and writes.
   - **Drawback**: Increased storage overhead.

Remember, the choice of method depends on the specific use case, workload, and system requirements. 😊

## TABLES & RELATIVE TERMS
In a **Relational Database Management System (RDBMS)**, tables play a crucial role in organizing and storing data.

1. **Table**:
   - A table is a collection of data elements organized in rows and columns.
   - It represents a set of related data.
   - Each row in a table is called a **tuple**, **record**, or **row**.
   - Example: Consider an "Employee" table with columns like ID, Name, Age, and Salary¹.

2. **Tuple (Record or Row)**:
   - A single entry in a table.
   - Represents a specific set of related data.
   - For instance, the "Employee" table has multiple tuples, each corresponding to an employee.

3. **Attribute**:
   - A table consists of several records (rows), and each record can be broken down into smaller parts of data known as attributes.
   - Attributes correspond to the columns in the table.
   - Example: In the "Employee" table, the attributes are ID, Name, Age, and Salary.

4. **Attribute Domain**:
   - When defining an attribute in a relation (table), we specify the type of values it can hold.
   - For instance, the "Name" attribute holds employee names, and saving an address there would violate the relational database model.

5. **Relation Schema**:
   - Describes the structure of a relation (table).
   - Includes the relation's name, attributes, and their names and types.

6. **Relation Key**:
   - An attribute that uniquely identifies a particular tuple (row) in a relation.
   - For example, in the "Employee" table, the ID attribute can be used as a key to fetch data for each employee.

## NORMALIZATION
#### Types of **database normalization** in **Relational Database Management Systems (RDBMS)**:

1. **First Normal Form (1NF)**:
   - Criteria:
     - Each cell must hold only one value (atomicity).
     - A primary key uniquely identifies each row.
     - No duplicated rows or columns.
   - Example:
     Consider a table with student data:
     ```
     Student ID | Name       | Courses
     ---------------------------------
     1          | John Smith | Math, History
     2          | Maria G.   | Biology
     ```
     Normalize by splitting the "Courses" column into separate rows.

2. **Second Normal Form (2NF)**:
   - Criteria:
     - Must be in 1NF.
     - Non-key attributes depend entirely on the primary key.
   - Example:
     Separate student-course relationships:
     ```
     Student ID | Course ID
     -----------------------
     1          | Math
     1          | History
     2          | Biology
     ```

3. **Third Normal Form (3NF)**:
   - Criteria:
     - Must be in 2NF.
     - Non-key attributes depend only on the primary key.
   - Example:
     Separate teacher information:
     ```
     Course ID | Teacher
     -------------------
     Math      | Prof. A
     History   | Prof. B
     Biology   | Prof. C
     ```

## Apply **database normalization** in practice. 
Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity.

1. **Understand Your Data**:
   - Begin with a rough idea of the data you want to store.
   - Identify the entities (e.g., students, courses) and their relationships.

2. **Start with Unnormalized Data**:
   - Consider an example student database:
     ```
     Student ID | Student Name | Fees Paid | Course Name | Class 1 | Class 2 | Class 3
     1          | John Smith   | 200       | Economics  | Economics | Biology | -
     2          | Maria Griffin| 500       | Comp Sci   | Biology  | -       | -
     ```

3. **Apply Normalization Rules**:
   - Normalize to achieve efficiency, accuracy, and prevent anomalies.
   - Follow the normal forms (1NF, 2NF, 3NF, etc.).

4. **First Normal Form (1NF)**:
   - Ensure each cell holds only one value (atomicity).
   - Create separate rows for repeating groups (e.g., classes).

5. **Second Normal Form (2NF)**:
   - Non-key attributes depend entirely on the primary key.
   - Separate student-course relationships:
     ```
     Student ID | Course ID
     -----------------------
     1          | Economics
     1          | Biology
     2          | Biology
     ```

6. **Third Normal Form (3NF)**:
   - Non-key attributes depend only on the primary key.
   - Separate teacher information:
     ```
     Course ID | Teacher
     -------------------
     Economics | Prof. A
     Biology   | Prof. B
     ```

7. **Beyond 3NF**:
   - Additional normal forms (e.g., Boyce-Codd Normal Form) address complex scenarios.

## PARTITIONING

Partitioning in an RDBMS is a technique used to divide a large database table into smaller, more manageable pieces called **partitions**. 
By doing so, the RDBMS can process data more efficiently by accessing only the relevant partitions instead of scanning the entire table. 
There are several types of partitioning:

1. **Range Partitioning**: In this method, the table is partitioned based on a range of values in a specific column. For example, if a table is partitioned by date, each partition could contain data for a specific date range.

2. **List Partitioning**: Here, the table is partitioned based on a specific list of values in a column. For instance, if a table is partitioned by country, each partition could contain data for a specific list of countries.

3. **Hash Partitioning**: This approach involves partitioning the table based on a hash function applied to a specific column. For example, if a table is partitioned by customer ID, each partition could be assigned based on the hash value of the customer ID.

4. **Composite Partitioning**: In composite partitioning, a table is partitioned using a combination of partitioning techniques. For instance, a table could be range partitioned by date and then list partitioned by region within each date range.

**Example of Range Partitioning**:
Suppose we have a table called "sales" that contains sales data for a company. The table has columns like `id`, `date`, `customer_id`, `product_id`, and `amount`. To improve query performance, we could range partition the table by date. For example, we could create partitions for each quarter of the year:

```sql
CREATE TABLE sales (
    id INT,
    date DATE,
    customer_id INT,
    product_id INT,
    amount DECIMAL(10,2)
) PARTITION BY RANGE(YEAR(date)*100 + QUARTER(date)) (
    PARTITION p1 VALUES LESS THAN (201601),
    PARTITION p2 VALUES LESS THAN (201604),
    PARTITION p3 VALUES LESS THAN (201607),
    PARTITION p4 VALUES LESS THAN (201610),
    PARTITION p5 VALUES LESS THAN (201701)
);
```

In this example, the table is partitioned by the year and quarter of the `date` column, with each partition containing data for a specific quarter of the year.

**Example of List Partitioning**:
Consider a table called "customers" with columns `id`, `name`, and `country`. To improve query performance, we could list partition the table by country. For instance:

```sql
CREATE TABLE customers (
    id INT,
    name VARCHAR(50),
    country VARCHAR(50)
) PARTITION BY LIST(country) (
    PARTITION p1 VALUES IN ('USA', 'Canada'),
    PARTITION p2 VALUES IN ('Mexico', 'Brazil'),
    PARTITION p3 VALUES IN ('France', 'Germany'),
    PARTITION p4 VALUES IN ('UK', 'Italy'),
    PARTITION p5 VALUES IN ('Japan', 'China')
);
```

In this example, the table is partitioned by the `country` column, with each partition containing data for specific countries¹².

## **Hash partitioning** 
**Hash Partitioning** is a technique used to divide a table into partitions based on a hash function applied to a specific column. 
Unlike range or list partitioning, where data is grouped by specific values or ranges, hash partitioning distributes data uniformly across partitions using a hashing algorithm. Here's how it works:

1. **Hash Function**:
   - You choose a column (the **partitioning key**) that will be used for hashing.
   - The hash function generates a hash value for each row based on the partitioning key.
   - The hash value determines which partition the row belongs to.

2. **Example**:
   - Suppose we have a table called "Citizenship" with an `Identity Number` column (like a Social Security number).
   - Hash partitioning is suitable when this column doesn't fit well into range or list partitions.
   - We'll create a hash-partitioned table with four partitions:
     ```sql
     CREATE TABLE Citizenship (
         IdentityNumber VARCHAR(20),
         Name VARCHAR(50),
         Address VARCHAR(100)
     ) PARTITION BY HASH (IdentityNumber) PARTITIONS 4;
     ```
   - The data will be distributed across the partitions based on the hash value of the `IdentityNumber`.

3. **Considerations**:
   - Hash partitioning creates a fixed number of partitions (specified by `PARTITIONS`).
   - It's useful for distributing data evenly and achieving load balancing.
   - However, it doesn't guarantee specific ranges or values in partitions.

Remember that hash partitioning is ideal when other methods (range, list) don't suit your data distribution. Feel free to ask if you need further clarification! 😊👍

Choosing a suitable column for partitioning depends on your specific use case and data distribution. Here are some considerations:

1. **Cardinality**:
   - Choose a column with high cardinality (many distinct values). This ensures that partitions are evenly distributed.
   - Examples: `customer_id`, `product_code`, or `order_number`.

2. **Query Patterns**:
   - Consider the most common queries. Partition by a column frequently used in WHERE clauses or JOIN conditions.
   - For sales data, partitioning by `date` or `region` might be beneficial.

3. **Data Distribution**:
   - Analyze data distribution. If certain values dominate, partitioning by that column may not evenly distribute data.
   - Avoid partitioning by low-cardinality columns (e.g., boolean flags).

4. **Size and Growth**:
   - Partition large tables to manage growth. Choose a column related to data volume.
   - For example, partitioning by date can help manage historical data growth.

5. **Maintenance Impact**:
   - Consider maintenance tasks (index rebuilds, archiving). Partitioning affects these operations.
   - Choose a column that minimizes maintenance overhead.

# Slowly Changing Dimensions (SCD) and Their Types

In modern data analytics, organizations utilize data warehouses to store vast amounts of historical data, ensuring data analysts can easily access critical information. While most attributes or dimensions of data in a warehouse remain static, certain dimensions like customer addresses, product specifications, or employee designations evolve over time. These evolving dimensions are also known as **Slowly Changing Dimensions (SCDs)** in data science. SCDs help businesses retain their original records while also tracking changes over time, maintaining the integrity of data warehouses and ensuring that insights derived from stored data account for its slowly evolving nature¹.

## Dimensions and Measures in Data Science
- **Dimensions**: Qualitative values such as names, dates, or geographical data. They categorize, segment, and reveal essential details in data. For example, sales data can include dimensions like Region, Product Type, or Time Period.
- **Measures**: Numeric or quantitative values within the scope of dimensions. These metrics (e.g., Total Sales, Profit Margin, or Number of Units Sold) provide statistical information for data-driven decision-making¹.

## Slowly Changing Dimensions (SCD) Types
1. **Type 0 SCD (Fixed Dimension)**:
   - No changes allowed; dimension remains constant.
   - Example: A reference table containing country codes.
2. **Type 1 SCD (Overwriting)**:
   - Update the record directly; no historical values are retained.
   - Example: Employee salary updates.
3. **Type 2 SCD (Row Versioning)**:
   - Track changes as version records with flags, active dates, and other metadata.
   - Example: Customer address changes.
4. **Type 3 SCD (Previous Value Column)**:
   - Add a new column to show the previous value.
   - Example: Product price changes.
5. **Type 4 SCD (History Table)**:
   - Maintain a separate history table for changes.
   - Example: Employee promotions.
6. **Type 6 SCD (Hybrid)**:
   - Combines aspects of other types (e.g., Type 1 and Type 2).
   - Example: Product category changes²⁴.

## **Data Lake** and **Data Warehouse**:

1. **Data Lake**:
    - **Definition**: A data lake is a centralized repository that ingests and stores large volumes of data in its original form. It can accommodate all types of data from any source, including structured (like database tables), semi-structured (such as XML files), and unstructured (like images or audio files).
    - **Storage Approach**: Data lakes store data without sacrificing fidelity, allowing raw, cleansed, and curated data to coexist.
    - **Use Cases**:
        - **Big Data Analytics**: Data lakes power big data analytics, machine learning, and predictive analytics.
        - **Scalable Architecture**: They provide core data consistency across various applications.
        - **Flexible Data Types**: Data lakes handle diverse data types without predefined schemas.
    - **Example Use Case**:
        - *Streaming Media*: Subscription-based streaming companies analyze customer behavior data to improve recommendation algorithms.
    - **Key Point**: Data lakes hold raw, unstructured data and support big data analytics and machine learning¹³.

2. **Data Warehouse**:
    - **Definition**: A data warehouse is designed to be a repository for structured data that has been treated and transformed with a specific purpose in mind. It's optimized for efficient querying and reporting.
    - **Structured Data**: Data warehouses store data that is already structured (e.g., cleaned, transformed) for specific business intelligence needs.
    - **Use Cases**:
        - **Business Intelligence**: Data warehouses enable efficient querying and reporting for business insights.
        - **Structured Data Storage**: They organize data into predefined schemas.
    - **Example Use Case**:
        - *Finance*: Investment firms use structured market data for efficient portfolio risk management.
    - **Key Point**: Data warehouses are repositories for structured data, while data lakes hold data of all structure types, including raw and unprocessed data²⁴.

In summary, data lakes accommodate diverse data types, while data warehouses focus on structured data for specific analytical purposes. 
They serve different needs and can complement each other in a comprehensive data architecture. 

## Examples - **Data Lakes** and **Data Warehouses**:

1. **Data Lake Examples**:
    - **Streaming Media**: Subscription-based streaming companies collect and process insights on customer behavior using data lakes. They can improve their recommendation algorithms based on this data.
    - **Finance**: Investment firms use real-time market data stored in data lakes to efficiently manage portfolio risks.
    - **Healthcare**: Hospitals rely on big data from data lakes to streamline patient pathways, leading to better outcomes and reduced costs of care¹³.

2. **Data Warehouse Examples**:
    - **Amazon Redshift on S3 (Amazon Spectrum)**: A classic data warehouse integrated with a data lake.
    - **Azure Synapse on ADLS**: Another example of a data warehouse combined with a data lake.
    - **Google Big Query on Google Cloud Storage**: A data warehouse solution tightly coupled with a storage system.
    - **Snowflake on External S3**: A data warehouse leveraging external storage for efficient querying².

Remember, while a data lake holds raw and unprocessed data, a data warehouse stores structured data for specific analytical purposes.

## Different types of tables in a database management system (DBMS):

1. **Base Tables**:
   - These hold persistent data and are the primary tables where data is stored.
   - Base tables are used for regular data storage and retrieval.
   - For example, an "Employee" table storing employee records.

2. **Temporary Tables**:
   - Temporary tables are used for temporary data storage during a session or a specific task.
   - They exist only for a limited duration and are automatically dropped when the session ends.
   - Two types:
     - **Local Temporary Tables**: Visible only within the current session and deleted when the session closes.
     - **Global Temporary Tables**: Visible to all sessions until the session that created them disconnects⁷.
   - Useful for intermediate results, staging, or one-off tasks.

3. **Dimensional Tables**:
   - Commonly used in data warehousing and business intelligence.
   - Represent dimensions (attributes) of data, such as time, geography, or product categories.
   - Often used in star schema or snowflake schema designs.
   - Examples: "Time Dimension," "Product Dimension."

4. **Fact Tables**:
   - Also part of data warehousing.
   - Store quantitative data (facts) related to business transactions or events.
   - Fact tables are associated with dimension tables.
   - Examples: "Sales Fact Table," "Inventory Fact Table."

## Different types of database schemas in the context of Database Management Systems (DBMS):

1. **Physical Database Schema**:
   - The physical schema defines how data is stored physically in storage systems, such as files and indices. It includes the actual code or syntax needed to create the database structure.
   - Database administrators decide where and how to store data within different storage blocks.
   - Example: Deciding which data goes into which disk block or file.
   - ¹

2. **Logical Database Schema**:
   - The logical schema defines logical constraints applied to stored data. It describes tables, views, entity relationships, and integrity constraints.
   - It specifies how data is organized in tables and how attributes within a table are connected.
   - Example: Designing tables, defining relationships between them, and ensuring data quality through integrity constraints.
   - ¹

3. **View Database Schema**:
   - The view-level design allows end-users to interact with the database without needing to understand the underlying data storage mechanisms.
   - Views provide an interface for users to query and manipulate data.
   - Example: Creating a view that combines data from multiple tables for reporting purposes.
   - ¹

Remember that these schema types serve different purposes and play essential roles in database design and management.

## LOGICAL DATABASE SCHRMA
The **logical database schema** defines the comprehensive logical structure of a database, including detailed data types, keys, field lengths, validation rules, views, indexes, explicit table relationships, joins, and normalization¹. Here are some common types of logical database schemas:

1. **Flat Model**:
   - In this simple schema, data is stored in a single table without any relationships.
   - It's suitable for small datasets with minimal complexity.

2. **Hierarchical Model**:
   - Data is organized in a tree-like structure with parent-child relationships.
   - Commonly used in file systems and XML databases.

3. **Network Model**:
   - Similar to the hierarchical model but allows multiple parent-child relationships.
   - Used in some legacy databases.

4. **Relational Model**:
   - The most widely used schema type.
   - Organizes data into tables with rows and columns.
   - Relationships are defined through keys (e.g., primary keys, foreign keys).

5. **Star Schema**:
   - Commonly used in data warehouses.
   - Central fact table surrounded by dimension tables.
   - Simplifies complex queries for reporting and analytics.

6. **Snowflake Schema**:
   - An extension of the star schema.
   - Dimension tables are normalized into multiple related tables.
   - Reduces data redundancy but can be more complex to query.

## LINKS
> https://learnsql.com/blog/sql-window-functions-cheat-sheet/
> https://learnsql.com/blog/sql-join-cheat-sheet/
> https://learnsql.com/blog/sql-basics-cheat-sheet/
> https://learnsql.com/blog/standard-sql-functions-cheat-sheet/
> https://learnsql.com/blog/sql-for-data-analysis-cheat-sheet/
