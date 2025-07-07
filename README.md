# E-Commerce Sales Analysis
## 🌟 Objective
The goal is to investigate and summarize data to uncover patterns, identify anomalies, and understand the relationships between variables. This involves summarizing the main characteristics of the data, such as its type and distribution, examines  individual variables to understand their distributions, identify outliers that may require further investigation, trends, and other meaningful patterns, and assess data quality, and  investigates relationships between variables, looking for correlations and potential dependencies.

## 📖 Overview
This dataset focuses on Target's operations in Brazil, covering 100,000 orders placed between 2016 and 2018. It includes detailed information on order status, pricing, payment and shipping performance, customer locations, product attributes, and customer reviews. Analyzing this dataset offers valuable insights, revealing details about order processing, pricing strategies, payment and shipping efficiency, customer demographics, product characteristics, and customer satisfaction. This comprehensive dataset is a valuable resource for understanding various business aspects and enhancing strategic decision-making.

## 💻 Techniques & Technology
- Data Exploration
- Descriptive Statistics
- Data Processing/Cleaning
- Data Visualization
- Python
- MySQL
- Pandas, Numpy
- Matplotlib, Seaborn
- Jupyter

## 🚀 Getting Started
# [📎](csv_mysql_importer.py)CSV to MySQL Importer
A Python utility for automated bulk import of CSV files into MySQL database tables with intelligent data type mapping and error handling.

## Table of Contents
1. [Overview](#overview)
2. [Feature Highlights](#feature-highlights)
3. [Prerequisites](#prerequisites)
4. [Configuration](#configuration)
5. [Usage Examples](#usage-examples)
6. [Code Structure](#code-structure)
7. [Data Type Mapping](#data-type-mapping)
8. [Quick Start Checklist](#quick-start-checklist)
9. [Conclusion](#conclusion)

## Overview
This utility automates the process of importing multiple CSV files into a MySQL database. It intelligently creates database tables with appropriate data types, handles missing values, and provides debugging information for data quality assessment. The script is specifically designed for e-commerce data import scenarios but can be adapted for various data import requirements.

## Feature Highlights
- **Automated Table Creation**: Dynamically generates CREATE TABLE statements based on CSV column structure
- **Intelligent Data Type Mapping**: Automatically maps pandas data types to appropriate MySQL data types
- **Null Value Handling**: Properly converts NaN values to SQL NULL for database compatibility
- **Column Name Sanitization**: Automatically cleans column names to be MySQL-compatible
- **Batch Processing**: Efficiently processes multiple CSV files in a single execution
- **Transaction Management**: Commits data per table to ensure data integrity
- **Debug Information**: Provides detailed logging for data quality assessment

## Prerequisites
### System Requirements
- Python 3.7+
- MySQL Server 5.7+ or MySQL 8.0+

### Python Dependencies
```bash
pip install pandas mysql-connector-python
```

### Database Setup
- MySQL server running and accessible
- Database created (default: `ecommerce`)
- User with appropriate privileges (INSERT, CREATE TABLE)

## Configuration
### Database Connection
Modify the connection parameters in the script:

```python
conn = mysql.connector.connect(
    host='localhost',        # MySQL server host
    user='root',            # MySQL username
    password='password',    # MySQL password
    database='ecommerce'    # Target database name
)
```

### File Configuration
Update the CSV files list and folder path:

```python
# CSV files and corresponding table names
csv_files = [
    ('customers.csv', 'customers'),
    ('orders.csv', 'orders'),
    # Add more files as needed
]

# Update folder path to your CSV location
folder_path = 'C:/Users/harsh/OneDrive/Desktop/E-commerce sales'
```

## Usage Examples
### Basic Execution
```bash
python file.py
```

### Expected Output
```
Processing customers.csv
NaN values before replacement:
column1    0
column2    5
column3    0
dtype: int64

Processing orders.csv
NaN values before replacement:
...
```

### Customizing for New Data
```python
# Example: Adding new CSV files
csv_files = [
    ('inventory.csv', 'inventory'),
    ('reviews.csv', 'product_reviews'),
    ('categories.csv', 'product_categories')
]
```

## Code Structure
### Main Components
#### 1. Configuration Section
- Database connection parameters
- CSV file definitions
- Folder path specification

#### 2. Data Type Mapping Function
```python
def get_sql_type(dtype):
    # Maps pandas dtypes to MySQL types
```

#### 3. Processing Loop
- Iterates through each CSV file
- Performs data cleaning and validation
- Creates tables and inserts data

#### 4. Error Handling
- NaN value conversion
- Column name sanitization
- Transaction management

### Key Functions

| Function | Purpose |
|----------|---------|
| `get_sql_type()` | Maps pandas data types to MySQL equivalents |
| `pd.read_csv()` | Loads CSV data into DataFrame |
| `df.where()` | Handles NaN to None conversion |
| `cursor.execute()` | Executes SQL statements |

## Data Type Mapping
The script uses intelligent data type mapping to ensure optimal database performance:

| Pandas Data Type | MySQL Data Type | Use Case |
|------------------|-----------------|----------|
| `int64`, `int32` | `BIGINT` | Integer values, IDs |
| `float64`, `float32` | `FLOAT` | Decimal numbers, prices |
| `bool` | `BOOLEAN` | True/False values |
| `datetime64` | `DATETIME` | Date and time stamps |
| `object`, `string` | `TEXT` | String data, descriptions |

### Column Name Sanitization
The script automatically converts column names to MySQL-compatible format:
- Spaces → Underscores (`Customer Name` → `Customer_Name`)
- Hyphens → Underscores (`order-id` → `order_id`)
- Periods → Underscores (`price.usd` → `price_usd`)

## Quick Start Checklist
### Pre-Execution
- [✅] MySQL server is running and accessible
- [✅] Target database exists
- [✅] Python dependencies installed (`pandas`, `mysql-connector-python`)
- [✅] CSV files are in the specified folder
- [✅] Database connection parameters updated

### Configuration
- [✅] Update `folder_path` to your CSV location
- [✅] Modify `csv_files` list with your file names and desired table names
- [✅] Verify database connection parameters
- [✅] Ensure MySQL user has CREATE and INSERT privileges

### Execution
- [✅] Run the script: `python file.py`
- [✅] Monitor console output for processing status
- [✅] Verify data import in MySQL database
- [✅] Check for any error messages or warnings

### Post-Execution Verification
- [✅] Connect to MySQL and verify table creation
- [✅] Check row counts match CSV file records
- [✅] Validate data types and NULL value handling
- [✅] Review debug output for data quality issues

## Conclusion
This CSV to MySQL importer provides a robust, automated solution for bulk data import operations. Its intelligent data type mapping and error handling capabilities make it suitable for production environments while maintaining simplicity for quick data migration tasks.

The script's modular design allows for easy customization and extension, making it adaptable to various data import scenarios beyond the default e-commerce use case. Regular monitoring of the debug output ensures data quality and helps identify potential issues early in the import process.

For production use, consider adding additional error handling, logging mechanisms, and performance optimizations based on your specific data volume and requirements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
