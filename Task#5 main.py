# SECTION 1 — Launch Your Project
#================================

# Banner
print("=" * 42)
print(" Langflow — Open Source Project")
print(" Project Lead : Tamim")
print("=" * 42)
print() 

# Tuple (Project Info)
# --------------------

project = ("Langflow", "1.8", 2024, "Python", "Tamim")

print("Name :", project[0])
print("Version :", project[1])
print("Started :", project[2])
print("Language :", project[3])
print("Lead :", project[4])

print("First 3 fields :", project[0:3])

print("Language count :", project.count("Python"))
print("Language index :", project.index("Python"))

# project[0] = "Test"
# TypeError: tuple does not support item assignment
# Reason: Tuples are immutable (cannot be changed)

print("-" * 42)

# Contributors Input
# ------------------

contributors = []

for i in range(4):
    print(f"\nEnter details for Contributor {i+1}")
    
    name = input("Name: ").strip().title()
    role = input("Role (e.g., Senior Dev, Junior Dev, Backend Dev): ").strip().title()
    language = input("Language (e.g., Python, Java, C++): ").strip().title()
    commits = int(input("Commits: "))
    country = input("Country: ").strip().title()
    
    contributor = {
        "name": name,
        "role": role,
        "language": language,
        "commits": commits,
        "country": country
    }
    
    contributors.append(contributor)

# Names List Operations
# ----------------------

names = []

for c in contributors:
    names.append(c["name"])

names.sort()
print("\nSorted names :", names)

print("Last name :", names[-1])
print("First two :", names[:2])

# Dictionary Operations
# ----------------------

for c in contributors:
    c.update({"status": "Active"})

print("Contributor 1 status :", contributors[0].get("status"))

backup = contributors[0].copy()
print("Backup :", backup)


# SECTION 2 — Issues & Analysis
#================================

issues = []

for i in range(5):
    print(f"\nEnter details for Issue {i+1}")
    
    issue_id = input("ID: ")
    title = input("Title: ").strip().title()
    issue_type = input("Type (Bug/Feature): ").strip().title()
    priority = input("Priority (Critical/High/Medium/Low): ").strip().title()
    reporter = input("Reporter: ").strip().title()
    status = input("Status (Open/In Progress/Resolved): ").strip().title()
    
    issue = {
        "id": issue_id,
        "title": title,
        "type": issue_type,
        "priority": priority,
        "reporter": reporter,
        "status": status
    }
    
    issues.append(issue)


# List Operations
# ----------------

open_count = 0
for issue in issues:
    if issue["status"] == "Open":
        open_count += 1

print("Open issues :", open_count)

issues[0]["priority"] = "Critical"
print("First issue → priority updated to Critical.")

print("Last two issues :", issues[-2:])
print()


# Set Operations
# ---------------

print("\n--- Set Operations ---")

reporters = set()
for issue in issues:
    reporters.add(issue["reporter"])

tech_stack = set()
for c in contributors:
    tech_stack.add(c["language"])

tech_stack.add("Go")
tech_stack.discard("Rust")

print("reporters :", reporters)
print("tech_stack :", tech_stack)

print("union :", reporters.union(tech_stack))
print("intersection :", reporters.intersection(tech_stack))
print("difference :", reporters.difference(tech_stack))

priorities = set()
for issue in issues:
    priorities.add(issue["priority"])

if "Critical" in priorities:
    print("Critical present : YES — flag for immediate review.")
else:
    print("Critical present : NO")


# Dictionary Operations
# ----------------------

print("\n--- Dictionary Operations ---")

priority_count = {}
for issue in issues:
    p = issue["priority"]
    if p in priority_count:
        priority_count[p] += 1
    else:
        priority_count[p] = 1

print("priority keys :", priority_count.keys())
print("priority values :", priority_count.values())

for k, v in priority_count.items():
    print(k, ":", v)

status_groups = {}
for issue in issues:
    status = issue["status"]
    title = issue["title"]
    
    if status not in status_groups:
        status_groups[status] = []
    
    status_groups[status].append(title)

for status, titles in status_groups.items():
    print(status, ":", titles)

reporter_count = {}
for issue in issues:
    r = issue["reporter"]
    if r in reporter_count:
        reporter_count[r] += 1
    else:
        reporter_count[r] = 1

top_reporter = None
max_count = 0

for r, count in reporter_count.items():
    if count > max_count:
        max_count = count
        top_reporter = r

print("Top reporter :", top_reporter, f"({max_count} issues)")

removed = issues[0].pop("type")
print("After pop('type') :", issues[0])


# SECTION 3 - Files & Reporting
# ================================

print("\n File & Reporting Section\n")

import os

project_name=project[0].lower().replace(" ", "_")

if not os.path.exists(project_name):
    os.mkdir(project_name)
    print("Folder created:",project_name)
else:
    print("Folder already exists:",project_name)

report_path = os.path.join(project_name,"project_report.txt")
csv_path = os.path.join(project_name,"issues.csv")

print("Files in folder: ",os.listdir(project_name))

# Write Files
# ------------

try:
    with open(report_path,"w") as f:
        f.write(f"{'=' * 42}\n")
        f.write(f"{project[0]} - PROJECT REPORT\n")
        f.write(f"{'=' * 42}\n")

        f.write("Project Info:\n")
        f.write(f"Name: {project[0]}\nVersion: {project[1]}\nYear: {project[2]}\n\n")

        f.write("Contributors:\n")
        for c in contributors:
            f.write(f"{c}\n")
        
        f.write("\nIssues:\n")
        for issue in issues:
            f.write(f"{issue}\n")
        
        f.write("\nAnalysis:\n")
        f.write(f"Top Reporter: {top_reporter} ({max_count})\n")

except IOError:
     print("Error writing report file.")


try:
    with open(csv_path, "w") as f:
        f.write("id,title,priority,reporter,status\n")
        
        for issue in issues:
            f.write(f"{issue['id']},{issue['title']},{issue['priority']},{issue['reporter']},{issue['status']}\n")
            
except IOError:
    print("Error writing CSV file.")


# Reading Files
# --------------

print("\n--- Reading Files ---\n")

try:
    with open(report_path, "r") as f:
        print("--- read() ---")
        print(f.read())
except FileNotFoundError:
    print("File not found.")

try:
    with open(report_path, "r") as f:
        print("--- readline() ---")
        print("Line 1 :", f.readline().strip())
        print("Line 2 :", f.readline().strip())
except FileNotFoundError:
    print("File not found.")

try:
    with open(report_path, "r") as f:
        lines = f.readlines()
        print("--- readlines() ---")
        print("Total lines :", len(lines))
        
        count = 0
        for line in lines:
            if "Critical" in line or "High" in line:
                count += 1
        
        print("Critical/High lines :", count)
        
except FileNotFoundError:
    print("File not found.")


# Final Summary
# ---------------
print("=" * 42)
print(f"{project[0]} — FINAL SUMMARY")
print("=" * 42)
print()

print(f"Project : {project[0]} Version : {project[1]} Lead : {project[4]}")
print(f"Contributors : {len(contributors)} Names : {names}")
print(f"Tech Stack : {tech_stack}")
print(f"Issues : {len(issues)} Open : {open_count} Reporters : {len(reporters)}")
print(f"Top Reporter : {top_reporter} ({max_count} issues)")

for k, v in priority_count.items():
    print(f"{k}:{v}", end=" ")
print()

print(f"Report : {report_path}")
print(f"CSV : {csv_path}")

print("=" * 42)
print(f"{project[0]} complete. Thank you for contributing to open source!")
print("=" * 42)



# FINAL PART — URGENT ISSUES
# ===============================
print("\nUrgent Issue Section\n")

# List comprehension
# -------------------
urgent = [issue["title"] for issue in issues if issue["priority"] in ("Critical", "High")]

print("Urgent issues :", urgent)
print("Total urgent :", len(urgent))

# Append to file
# --------------

try:
    with open(report_path, "a") as f:
        f.write(f"{'=' * 42}\n")
        f.write("URGENT ISSUES\n")
        f.write(f"{'=' * 42}\n")
        
        for title in urgent:
            f.write(f"{title}\n")
            
except IOError:
    print("Error appending to file.")

# Read last 6 lines
# ------------------

try:
    with open(report_path, "r") as f:
        lines = f.readlines()
        
        print("\n--- Last 6 lines ---")
        for line in lines[-6:]:
            print(line.strip())
            
except FileNotFoundError:
    print("File not found.")