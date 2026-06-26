# Classwork #10 – School Management System

## Course Information

**Course:** Programming  
**Degree:** Data and Artificial Intelligence Engineering  
**University:** Universidad Politécnica de Yucatán (UPY)  
**Instructor:** Dr. Jorge J. Pedrozo Romero

---

## Objective

Develop a Python program that simulates a basic School Management System with three different user roles:

- Student
- Teacher
- Coordinator

The program implements authentication, role-based access, grade management, and reporting using only the programming concepts covered during the course.

---

## Repository Structure

```
Classwork-10-School-Management-System/
│
├── PPP.txt
├── Flowchart.png
├── school_management_system.py
└── README.md
```

---

## Features

### Login

- Unlimited login attempts.
- Username and password validation.
- Role-based access.

### Student

- Displays the student's report card.
- Shows every subject and its grade.
- Displays:
  - Approved subjects
  - Pending subjects

### Teacher

- Displays all students.
- Allows selecting a student.
- Allows selecting a subject.
- Allows editing grades.
- Confirmation before saving changes.
- Navigation options:
  - **Yes** → Save changes.
  - **No** → Enter another grade.
  - **Back** → Return to subject selection.
  - **Exit** → Close the teacher session.

### Coordinator

Read-only report including:

- Teachers
- Subjects
- Students
- Complete grades table
- Failed grades highlighted
- Summary of failed subjects per student

---

## Programming Concepts Used

- Variables
- Dictionaries
- Tuples
- Sets
- Loops (`while`)
- Conditional statements (`if`, `elif`, `else`)
- Input / Output
- Data validation

---

## Requirements

- Python 3.x
- Compatible with **Thonny IDE**

---

## How to Run

Run the program using:

```bash
python school_management_system.py
```

or execute it directly from **Thonny**.

---

## AI Usage Declaration

This project was developed by the student with assistance from **OpenAI ChatGPT**.

Artificial Intelligence was used as a support tool for:

- Planning the program structure.
- Reviewing and improving the program logic.
- Generating pseudocode (PPP).
- Designing the flowchart.
- Improving code readability.
- Identifying and correcting programming errors.
- Writing project documentation.

All implementation decisions, testing, customization, and final validation were performed by the student.

---

## Author

**Iván Fernando Rivas Suárez**

Data and Artificial Intelligence Engineering

Universidad Politécnica de Yucatán

## Version History

### v1.0
- Initial implementation.

### v1.1
- Added teacher confirmation menu.
- Added Back and Exit navigation.
- Improved coordinator report.
- Added failed grade highlighting.
- Improved user experience.
