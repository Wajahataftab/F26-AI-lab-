# Artificial Intelligence (Lab) - Lab Manual 01

* **Student Name:** Wajahat Aftab
* **Student ID:** SU92-BSSEM-S25-002
* **Class:** BSSEM-4A
* **Instructor:** Sir. Rasikh Ali

---

## 📌 Problem Statement
The purpose of this lab is to study selected milestones in AI history, implement a small rule-based decision program, and compare a conversational-style answer with a decision made using explicit rules. This work is a historical and testing exercise and does not train a machine learning model[cite: 1].

### Objectives:
* Prepare a chronological timeline with sources[cite: 1].
* Add two transport (eligibility) conditions to scholarship examples and test four cases[cite: 1].
* Show a disagreement between a fixed rule decision and a fluent but incomplete answer, and discuss limitations, edge cases, and responsible use[cite: 1].

---

## ⏳ AI Milestone Timeline

| Year | Milestone | Key Impact | Source |
| :--- | :--- | :--- | :--- |
| **1950** | Turing Test[cite: 1] | Machine intelligence test propose hua[cite: 1] | Turing (1950)[cite: 1] |
| **1956** | Dartmouth Conference[cite: 1] | AI research field ki bunyad rakhi gayi[cite: 1] | McCarthy et al. (1955)[cite: 1] |
| **1958** | Perceptron[cite: 1] | Early neural network model bana[cite: 1] | Rosenblatt (1958)[cite: 1] |
| **1974–80** | 1st AI Winter[cite: 1] | Hype aur high expectations ke wajha se funding ruki[cite: 1] | Lighthill (1973) / Stanford AI100[cite: 1] |
| **1980–90** | 2nd AI Winter[cite: 1] | Expensive expert systems ke fail hone par interest ghata[cite: 1] | Crevier (1993) / Stanford AI100[cite: 1] |
| **2012** | AlexNet[cite: 1] | Deep learning aur GPU se ImageNet breakdown hua[cite: 1] | Krizheveky et al. (2012)[cite: 1] |

---

## ⚙️ Rule-Based Implementation & Test Cases

The program checks four explicit conditions[cite: 1]:
1. **Score** $\ge 70$ (retained condition)[cite: 1]
2. **Documents** are complete (retained condition)[cite: 1]
3. **Attendance** $\ge 75\%$ (new condition 1)[cite: 1]
4. **Disciplinary cases** $= 0$ (new condition 2)[cite: 1]

### Test Cases Table:
| Test Case | Input | Expected | Actual | Reason |
| :--- | :--- | :--- | :--- | :--- |
| **Normal Pass**[cite: 1] | Score 80, Docs OK, Att. 85%, Disc. 0[cite: 1] | PASS[cite: 1] | PASS[cite: 1] | All eligibility criteria met[cite: 1]. |
| **Attendance Fail**[cite: 1] | Score 80, Docs OK, Att. 70%, Disc. 0[cite: 1] | FAIL[cite: 1] | FAIL[cite: 1] | Attendance is below 75%[cite: 1]. |
| **Disciplinary Fail**[cite: 1] | Score 80, Docs OK, Att. 85%, Disc. 1[cite: 1] | FAIL[cite: 1] | FAIL[cite: 1] | Disciplinary cases must be 0[cite: 1]. |
| **Score Boundary**[cite: 1] | Score 70, Docs OK, Att. 75%, Disc. 0[cite: 1] | PASS[cite: 1] | PASS[cite: 1] | Minimum required score (70) met[cite: 1]. |

---

## 📊 Scholarship Disagreement Table

| Item | Observation |
| :--- | :--- |
| **Input**[cite: 1] | Score 85; documents complete; attendance 60%; disciplinary cases 0[cite: 1]. |
| **Rule-based result**[cite: 1] | FAIL — attendance is below the assumed 75% minimum[cite: 1]. |
| **Conversational-style answer**[cite: 1] | "The student should qualify because the score is high."[cite: 1] |
| **Agreement**[cite: 1] | No. The conversational-style answer implies PASS while rules return FAIL[cite: 1]. |
| **Likely cause**[cite: 1] | The response pays attention to one positive factor and overlooks another required condition[cite: 1]. |
| **Proposed improvement**[cite: 1] | Check every condition, show the reason for each decision, and test results against fixed examples[cite: 1]. |

---

## 🚀 Running the Files

From a terminal opened in the `lab1` folder, run the following scripts[cite: 1]:
```bash
python lab1_rules.py
python lab1_compare.py