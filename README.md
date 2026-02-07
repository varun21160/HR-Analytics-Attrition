# HR Attrition & Employee Performance Analysis Dashboard

## 📌 Project Overview
This project analyzes employee attrition and performance using real-world HR data, and delivers actionable insights through an interactive Power BI dashboard. The purpose is to help HR teams identify turnover drivers and make data-driven retention decisions.

---

## 🛠 Tools & Technologies Used
- **Python** – Data cleaning, exploratory analysis (Pandas, Matplotlib, Seaborn)
- **SQL (SQLite)** – Business queries for aggregated insights
- **Power BI** – Interactive dashboard visualization
- **GitHub** – Source code and project documentation

---

## 📊 Key KPIs
This dashboard highlights the following key performance indicators:
- **Total Employees**
- **Attrition Rate (%)**
- **Attrition Count**
- **Employees Working Overtime (%)**

---

## 🔍 Key Insights
The analysis reveals the following:
- 🧑‍💼 **Sales roles exhibit the highest attrition risk**
- ⏱ **Employees working overtime have significantly higher attrition**
- 📉 **Attrition is highest among early-tenure employees**
- 😊 **Job satisfaction strongly impacts employee retention**

These insights can help HR teams target retention strategies more effectively.

---

## 📁 Project Structure

HR-Analytics-Attrition/
│
├── data/
│ └── cleaned_hr_attrition.csv
│
├── notebooks/
│ └── hr_attrition_analysis.py
│
├── sql/
│ └── hr_attrition_queries.sql
│
├── Power BI/
│ └── HR_Attrition_Dashboard.pbix
│
├── images/
│ └── dashboard.png
│
└── README.md



---

## 📈 Dashboard Preview
Below is a preview of the final Power BI dashboard:

![HR Attrition Dashboard](images/dashboard.png)

---

## ▶ How to View the Dashboard

**Option 1. Download and open in Power BI Desktop**
1. Download `powerbi/HR_Attrition_Dashboard.pbix`
2. Open it in **Power BI Desktop**
3. Use the slicers to interact with the visuals

> *This method allows you to explore all dashboard features interactively.*

**Option 2. View static dashboard previews**
- Screenshots are included in the `images/` folder for quick reference.

---

## 📎 How to Run the Code

### Python EDA
1. Open `notebooks/hr_attrition_analysis.py`
2. Run with your preferred Python environment (Jupyter, VS Code, etc.)
3. Make sure required libraries are installed:
pandas
numpy
matplotlib
seaborn


### SQL Queries
- The file `sql/hr_attrition_queries.sql` contains all business analytics queries used during analysis.

---

## 📍 Data Source
IBM HR Analytics Employee Attrition dataset from Kaggle  
(Used to derive insights and build the dashboard.)

---

## 🚀 Outcome
This project demonstrates a complete HR analytics workflow, combining data preparation, exploratory analysis, SQL querying, and dashboard visualization to derive actionable business insights.

---

## 🧠 License
This repository is open to public use. Feel free to explore and learn from it!
