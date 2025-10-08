Apexcify Internship Tasks

This repository contains the solutions for Task 1 and Task 2 completed as part of the Apexcify Internship Program.
Both tasks demonstrate the use of Python, Pandas, and Matplotlib for data analysis and visualization.

Overview
Task	Topic	Description	Tools Used
Task 1	Student Grades Analysis	Loaded a CSV file of student scores, calculated averages, and identified the top-performing student.	Python, Pandas
Task 2	Monthly Sales Visualization	Combined 12 monthly sales CSV files from 2019, analyzed total sales per month, and visualized trends.	Python, Pandas, Matplotlib
Task 1 – Student Grades Analysis

Objective:
Analyze students’ performance across three subjects (Math, English, Science).

Steps Performed:

Loaded the dataset using Pandas.

Calculated each student’s average score using mean(axis=1).

Identified the student with the highest average score.

Displayed summary statistics using .describe().

Sample Columns:
Name | Math | English | Science

Output Example:

Top Student: Ali Khan — Average Score: 94.33

Task 2 – Monthly Sales Visualization

Objective:
Combine and analyze monthly sales data for 2019 and visualize the sales trend.

Steps Performed:

Read 12 monthly CSV files from the data folder using a loop.

Combined them into a single DataFrame using pd.concat().

Cleaned and formatted the data by converting Order Date to datetime.

Extracted the month and calculated total monthly sales.

Plotted a line chart showing the sales trend.

Sample Columns:
Order ID | Product | Quantity Ordered | Price Each | Order Date | Purchase Address

Output Visualization:
A line chart representing total monthly sales across 2019.

How to Run

Clone the repository:

git clone https://github.com/FarmanAli108/Apexcify_Intern_Tasks.git
cd Apexcify_Intern_Tasks


Install dependencies:

pip install pandas matplotlib


Run each task:

python task1/task1.py
python task2/task2.py

Folder Structure
Apexcify_Intern_Tasks/
│
├── task1/
│   ├── task1.py
│   ├── student_grades.csv
│
├── task2/
│   ├── task2.py
│   ├── Sales_January_2019.csv
│   ├── ...
│
└── README.md
Author

Farman Ali
Intern at Apexcify
GitHub Profile
