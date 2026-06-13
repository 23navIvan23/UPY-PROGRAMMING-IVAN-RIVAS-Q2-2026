# UPY — Academic Project Report
**Course:** Programming  
**Student:** Ivan Rivas (Matrícula: 2509214)  
**Assignment:** Classwork #08 - Numerical Integration  
**Date:** June 12, 2026  

---

## 1. Introduction & Objective
The goal of this project is to build an interactive numerical integration tool using Python. The program calculates the area under a curve for a mathematical function given by the user. It divides the interval into $n = 1000$ subintervals and uses four different geometric methods: Left, Right, and Midpoint Riemann Sums, and the Trapezoidal Rule. 

The project workflow uses Git for local version control and GitHub for cloud deployment.

---

## 2. Program Architecture & Variables
The code perfectly preserves the logic and variables created during our classroom session. It is divided into three main blocks:

* **`# INPUT`**: Asks the user for the limits (`a`, `b`), the mathematical function (`f_x`), and the selection string (`method`).
* **`# PROCESS`**: Checks if the user typed `"pi"` and resolves any math operation (like `pi/2`) using string replacement and `eval()`. It sets $n = 1000$, calculates the step width (`h`), initializes the tracking counters (`area`, `shift`, `constant`, `variable`), and runs the integration loops.
* **`# DISPLAY`**: Prints the final calculated area on the console screen.

---

## 3. Project Evidences

### A. Git Tracking Verification (`git --version`)
This screenshot shows that the local Git engine is successfully installed and tracking changes in the system terminal:

![Git Version Verification](Classwork-08-Numerical-Integration/git_version.png)

### B. Algorithm Control Flow Diagram (`Flowchart.png`)
The systematic flowchart maps the logic of the application, including the code loop boundaries, variable offsets, and geometric methods:

![Flowchart Logic Layout](Classwork-08-Numerical-Integration/Flowchart.png)

### C. Cloud Storage Deployment (GitHub)
This capture shows the final folder structure on the GitHub remote repository containing all required files:

![GitHub Cloud Repository](Classwork-08-Numerical-Integration/github_repo_capture.png)

---

## 4. AI Use Declaration
AI Use Declaration: I used generative AI (Gemini) to fully transcribe our functional classroom interactive numerical integration script into a standardized plain-English pseudocode format (PPP.txt) following the class rules, structure the step-by-step logic nodes required to construct the Flowchart.png deliverable, and organize this markdown repository report layout.