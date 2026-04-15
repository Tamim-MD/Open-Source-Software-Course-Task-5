# 📚 Documentation

##  Introduction
Langflow is a simple Python console project that simulates an open-source project system.  
It allows users to manage contributors, track issues, and generate reports.

---

## ⚙️ Project Structure

The project has 3 main sections:

### 1. Project & Contributors
- Stores project info using a tuple
- Takes input for 4 contributors
- Each contributor includes:
  - Name
  - Role
  - Language
  - Commits
  - Country

---

### 2. Issues & Analysis
- Takes input for 5 issues
- Each issue includes:
  - ID
  - Title
  - Type (Bug/Feature)
  - Priority (Critical/High/Medium/Low)
  - Reporter
  - Status (Open/In Progress/Resolved)

#### Analysis Done:
- Count open issues
- Find top reporter
- Group issues by status
- Count priorities
- Identify urgent issues (Critical/High)

---

### 3. File Handling
Creates a folder and saves:

- `project_report.txt` → full project report  
- `issues.csv` → issue data in CSV format  

Also demonstrates:
- Writing files
- Reading files (`read`, `readline`, `readlines`)
- Appending data

---

##  Concepts Used
- Tuple (project info)
- List (contributors, issues)
- Dictionary (data storage)
- Set (unique values)
- File handling (read/write)
- Basic loops and conditions

---

##  How It Works
1. Run the program
2. Enter contributor details
3. Enter issue details
4. Program processes data
5. Files are generated automatically
6. Final summary is shown

---

##  Notes
- Input must be correct (numbers for commits)
- Runs in terminal (no GUI)
- Data is stored only in generated files

---

##  Future Improvements
- Add menu system
- Use database instead of files
- Build web version
- Add search and filters

---
