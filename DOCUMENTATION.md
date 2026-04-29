# 📚 Documentation

##  Introduction

Langflow is a Python-based console application that simulates a simple open-source project management system.
The program collects structured data, performs basic analysis, and generates reports using core Python concepts.

---

###  Project Information (Tuple)

Project details such as name, version, year, language, and lead are stored in a tuple.

**Reason for usage:**

* The data is fixed and should not be modified
* Tuple ensures immutability and data safety

**Implementation highlights:**

* Access using indexing (`project[0]`)
* Slicing (`project[0:3]`)
* Built-in methods like `count()` and `index()`

---

###  Contributors (List of Dictionaries)

Contributor data is stored as a list of dictionaries.

**Structure:**
Each contributor contains:

* name, role, language, commits, country

**Reason for usage:**

* List allows storing multiple contributors
* Dictionary provides structured key-value representation

**Operations performed:**

* Adding contributors using `append()`
* Extracting names into a separate list
* Sorting names using `sort()`
* Updating data using `update()`
* Creating backup using `copy()`

---

###  Issues (List of Dictionaries)

Issue data is also stored as a list of dictionaries.

**Structure:**
Each issue contains:

* id, title, type, priority, reporter, status

**Reason for usage:**

* Consistent structure for handling multiple records
* Easy iteration and modification

**Operations performed:**

* Counting open issues using conditions
* Updating values (`issues[0]["priority"]`)
* Accessing subsets using slicing (`issues[-2:]`)

---

##  Data Processing

###  Loops and Conditions

Used for:

* Filtering issues (e.g., status = Open)
* Counting occurrences
* Identifying urgent issues

---

###  Set Operations

Sets are used to store unique values.

**Examples:**

* Unique reporters
* Unique programming languages

**Operations:**

* `add()`, `discard()`
* `union()`, `intersection()`, `difference()`

**Reason for usage:**

* Automatically removes duplicates
* Efficient comparison between datasets

---

###  Dictionary-Based Analysis

Dictionaries are used for aggregation and grouping.

**Implemented features:**

* Counting issues by priority
* Grouping issues by status
* Finding top reporter using frequency count

**Reason for usage:**

* Efficient for counting and grouping operations

---

###  List Comprehension

Used to extract urgent issues (Critical and High priority).

**Reason for usage:**

* More concise and readable than traditional loops

---

##  File Handling

###  Directory Management

* Creates a folder using the `os` module
* Ensures organized storage of output files

---

###  File Writing

Two files are generated:

* `project_report.txt` → detailed project report
* `issues.csv` → structured issue data

**Concepts used:**

* Writing formatted text
* Writing structured CSV data

---

###  File Reading

Different methods are demonstrated:

* `read()` → reads full content
* `readline()` → reads line by line
* `readlines()` → reads all lines into a list

Additional processing:

* Counting lines containing "Critical" or "High"

---

###  File Appending

* Urgent issues are appended to the report file
* Demonstrates extending existing data without overwriting

---

##  Program Flow

1. Initialize project data
2. Collect contributor information
3. Process contributor data (sorting, updating)
4. Collect issue data
5. Perform analysis (counting, grouping, filtering)
6. Generate report and CSV files
7. Read and verify file contents
8. Append urgent issues
9. Display final summary

---





