CREATE TABLE hr_attrition (
    Age INT,
    Attrition INT,
    BusinessTravel VARCHAR(50),
    Department VARCHAR(50),
    DistanceFromHome INT,
    Education INT,
    EducationField VARCHAR(50),
    EmployeeNumber INT,
    EnvironmentSatisfaction INT,
    Gender VARCHAR(10),
    JobInvolvement INT,
    JobLevel INT,
    JobRole VARCHAR(50),
    JobSatisfaction INT,
    MaritalStatus VARCHAR(20),
    MonthlyIncome INT,
    NumCompaniesWorked INT,
    OverTime VARCHAR(5),
    PercentSalaryHike INT,
    PerformanceRating INT,
    RelationshipSatisfaction INT,
    TotalWorkingYears INT,
    TrainingTimesLastYear INT,
    WorkLifeBalance INT,
    YearsAtCompany INT,
    YearsInCurrentRole INT,
    YearsSinceLastPromotion INT,
    YearsWithCurrManager INT
);

#1️⃣ Overall Attrition Rate
SELECT 
    ROUND(AVG(Attrition) * 100, 2) AS attrition_rate_percentage
FROM hr_attrition;

#2️⃣ Attrition by Department
SELECT 
    Department,
    ROUND(AVG(Attrition) * 100, 2) AS attrition_rate
FROM hr_attrition
GROUP BY Department
ORDER BY attrition_rate DESC;

#3️⃣ Attrition by Job Role
SELECT 
    JobRole,
    ROUND(AVG(Attrition) * 100, 2) AS attrition_rate
FROM hr_attrition
GROUP BY JobRole
ORDER BY attrition_rate DESC;

#4️⃣ Attrition by Overtime
SELECT 
    OverTime,
    ROUND(AVG(Attrition) * 100, 2) AS attrition_rate
FROM hr_attrition
GROUP BY OverTime;

#5️⃣ Income Comparison (Stayed vs Left)
SELECT 
    Attrition,
    ROUND(AVG(MonthlyIncome), 2) AS avg_monthly_income
FROM hr_attrition
GROUP BY Attrition;

#6️⃣ High-Risk Employee Segments
SELECT 
    JobRole,
    OverTime,
    ROUND(AVG(Attrition) * 100, 2) AS attrition_rate
FROM hr_attrition
GROUP BY JobRole, OverTime
HAVING attrition_rate > 25
ORDER BY attrition_rate DESC;
