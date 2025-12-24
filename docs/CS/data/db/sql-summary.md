## 📚 SQL 语法主要分类

SQL 语句通常可以分为以下三大类：

| 分类 | 英文全称 | 简称 | 主要功能 |
| :--- | :--- | :--- | :--- |
| **数据定义语言** | Data Definition Language | **DDL** | 用于定义和管理数据库对象的结构（如表、索引、视图等）。 |
| **数据操作语言** | Data Manipulation Language | **DML** | 用于操作数据库中的数据，包括查询、插入、更新和删除。 |
| **数据控制语言** | Data Control Language | **DCL** | 用于控制数据库用户的权限和事务。 |

---

## 💻 核心 SQL 语法语句

### 1. 数据定义语言 (DDL)

用于定义数据库的结构和对象。

| 语句 | 目的 | 示例（简略） |
| :--- | :--- | :--- |
| **CREATE** | 创建新的数据库对象（如表、数据库、视图、索引）。 | `CREATE TABLE table_name (column1 datatype, ...);` |
| **ALTER** | 修改现有数据库对象的结构。 | `ALTER TABLE table_name ADD column_name datatype;` |
| **DROP** | 永久删除数据库对象。 | `DROP TABLE table_name;` |
| **TRUNCATE** | 快速删除表中的所有数据（保留表结构）。 | `TRUNCATE TABLE table_name;` |

### 2. 数据操作语言 (DML)

用于管理和操作数据库中的实际数据。

| 语句 | 目的 | 核心子句/关键字 |
| :--- | :--- | :--- |
| **SELECT** | **查询**数据（从一个或多个表中检索数据）。 | `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `JOIN` |
| **INSERT** | **插入**新数据（向表中添加新的行）。 | `INTO`, `VALUES` |
| **UPDATE** | **更新**现有数据（修改表中的行记录）。 | `SET`, `WHERE` |
| **DELETE** | **删除**数据（从表中删除行记录）。 | `FROM`, `WHERE` |

#### **✨ SELECT 语句的关键子句**

`SELECT` 是最复杂和最常用的语句，其常见子句和执行顺序如下：

| 子句 | 目的 |
| :--- | :--- |
| **FROM** | 指定要查询的数据表。 |
| **JOIN** | 连接两个或多个表（如 `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`）。 |
| **WHERE** | 过滤行记录，只返回符合特定条件的行。 |
| **GROUP BY** | 将结果集按照一个或多个列进行分组。 |
| **HAVING** | 过滤 `GROUP BY` 后的分组（通常配合聚合函数）。 |
| **ORDER BY** | 对结果集进行排序（升序 `ASC` 或降序 `DESC`）。 |
| **LIMIT / OFFSET** | 限制返回的行数或指定从哪一行开始返回（数据库系统之间略有不同）。 |
| **DISTINCT** | 用于返回唯一不同的值。 |

### 3. 数据控制语言 (DCL) 和事务控制语言 (TCL)

用于管理权限和确保数据完整性。

| 语句 | 目的 | 分类 |
| :--- | :--- | :--- |
| **GRANT** | 授予用户或角色执行特定操作的权限。 | DCL |
| **REVOKE** | 撤销已授予的权限。 | DCL |
| **COMMIT** | 永久保存事务中所做的所有更改。 | TCL |
| **ROLLBACK** | 撤销自上次 `COMMIT` 以来事务中所做的所有更改。 | TCL |
| **SAVEPOINT** | 在事务中设置一个临时标记点，以便在需要时可以回滚到该点。 | TCL |

### 4. 其他重要语法要素

* **约束 (Constraints):** 用于规定表中的数据规则，确保数据的准确性和完整性。
    * `PRIMARY KEY`（主键）
    * `FOREIGN KEY`（外键）
    * `NOT NULL`（非空）
    * `UNIQUE`（唯一）
    * `CHECK`（检查条件）
    * `DEFAULT`（默认值）
* **聚合函数 (Aggregate Functions):** 对一组值执行计算，并返回单个值。
    * `COUNT()`（计数）
    * `SUM()`（求和）
    * `AVG()`（求平均）
    * `MAX()`（最大值）
    * `MIN()`（最小值）
* **表达式 (Expressions) 和 谓词 (Predicates):** 用于在语句中进行计算和条件判断。
    * **算术表达式**（如 `+`, `-`, `*`, `/`）
    * **比较谓词**（如 `=`, `>`, `<`, `!=`, `BETWEEN`, `LIKE`, `IN`, `IS NULL`）
    * **逻辑谓词**（如 `AND`, `OR`, `NOT`）

好的，我们来通过一个经典的**客户与订单**的例子，深入理解并举例讲解主键约束和外键约束，并解释每个语句的含义。

## 🔑 主键约束 (PRIMARY KEY) 示例

主键用于**唯一标识**表中的每一行记录。它确保了数据的完整性和快速检索。

### 示例：创建 `Customers`（客户）表

我们创建一个 `Customers` 表，并定义 `CustomerID` 为主键。

```sql
CREATE TABLE Customers (
    CustomerID INT NOT NULL PRIMARY KEY, -- 主键约束：必须非空且唯一
    LastName VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255),
    Email VARCHAR(255) UNIQUE -- 额外添加 UNIQUE 约束
);
```

#### 语句解释：

| 语句部分 | 含义 | 约束/作用 |
| :--- | :--- | :--- |
| `CustomerID INT` | 创建一个名为 `CustomerID` 的整数（INT）列。 | 数据类型定义。 |
| `NOT NULL` | 确保 `CustomerID` 字段在插入数据时**必须**有值。 | 非空约束。 |
| `PRIMARY KEY` | 将 `CustomerID` 列指定为该表的**主键**。 | **主键约束**：自动保证该列的数值是唯一的且非空。 |
| `LastName VARCHAR(255) NOT NULL` | 创建一个最大长度为 255 的字符串列，且不允许为空。 | 非空约束。 |
| `Email VARCHAR(255) UNIQUE` | 创建一个字符串列，并确保所有邮箱值都是**唯一的**。 | 唯一约束（与主键类似，但可以接受一个 NULL 值）。 |

#### 主键的作用：

1.  **唯一性**：任何两个客户不能拥有相同的 `CustomerID`。
2.  **非空性**：插入客户记录时，`CustomerID` 必须提供。

-----

## 🔗 外键约束 (FOREIGN KEY) 示例

外键用于在两个表之间建立**链接**，以确保数据的**引用完整性**。外键列引用另一个表（通常是主表）的**主键**。

### 示例：创建 `Orders`（订单）表

我们创建一个 `Orders` 表，它需要引用 `Customers` 表，以知道每个订单属于哪个客户。

```sql
CREATE TABLE Orders (
    OrderID INT NOT NULL PRIMARY KEY,
    OrderDate DATE,
    OrderAmount DECIMAL(10, 2),
    
    -- Foreign Key 约束定义
    CustomerID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) 
    ON DELETE CASCADE -- 级联操作
);
```

#### 语句解释：

| 语句部分 | 含义 | 约束/作用 |
| :--- | :--- | :--- |
| `OrderID INT NOT NULL PRIMARY KEY` | 定义 `OrderID` 为订单表的主键。 | 主键约束。 |
| `CustomerID INT` | 创建一个名为 `CustomerID` 的整数列。 | 这是一个普通列，但它将作为外键。 |
| `FOREIGN KEY (CustomerID)` | **声明** `Orders` 表中的 `CustomerID` 列是一个**外键**。 | 外键定义。 |
| `REFERENCES Customers(CustomerID)` | 指定这个外键引用 `Customers` 表中的 `CustomerID` **主键**。 | 建立两个表之间的关系。 |
| `ON DELETE CASCADE` | 这是一个**级联操作**：如果 `Customers` 表中某个客户的记录被删除，那么 `Orders` 表中所有引用该客户的订单记录也将**自动被删除**。 | 确保引用完整性的行为。 |

#### 外键的作用：

1.  **引用完整性**：您不能在 `Orders` 表中插入一个 `CustomerID`，除非该 `CustomerID` **已经存在于** `Customers` 表中。这防止了“孤儿”订单的出现。
2.  **数据一致性**：通过 `ON DELETE CASCADE` 等级联操作，保证父表数据变动时，子表数据同步更新，维护数据的一致性。
