AP Internship Tasks

This repository contains the solutions for Task 1 and Task 2 completed as part of the AP Internship Program. Both tasks focus on data analysis and visualization using Python, demonstrating skills in handling datasets, cleaning data, and extracting meaningful insights.
Overview
Task 1 covers data manipulation and exploration, while Task 2 focuses on sales data analysis. Python libraries such as Pandas and Matplotlib were used throughout for data processing and visualization.
Task	Topic	Description	Tools Used
Task 1	Data Manipulation	Performed basic data cleaning, analysis, and visualization on a dataset.	Python, Pandas, Matplotlib
Task 2	Sales Data Analysis	Combined monthly sales CSV files from 2019 into one dataset, analyzed trends, and visualized total monthly sales.	Python, Pandas, Matplotlib
Task 1 – Data Manipulation and Exploration

The objective of Task 1 was to understand how to handle and analyze structured data using Python libraries. The task involved reading data, handling missing or incorrect values, exploring data through descriptive statistics, and visualizing patterns using graphs. The output included a cleaned dataset and meaningful visualizations for interpretation.
Task 2 – Sales Data Analysis (2019)
The objective of Task 2 was to merge multiple monthly sales reports into a unified dataset and analyze business performance across different months. The dataset included twelve CSV files (January to December 2019) stored in the path “AP_intern_task/task2/data/”. The task included reading all CSV files using a loop, combining them into a single DataFrame, cleaning invalid entries, converting data types, extracting month-wise totals, and visualizing the results. The final output was a combined dataset of shape (186850, 6) and a bar graph showing total sales per month in 2019.

How to Run the Code
Clone the repository
git clone https://github.com/<your-username>/AP_intern_task.git


Navigate to the desired task folder
cd AP_intern_task/task2

Install dependencies
pip install pandas matplotlib
Run the Python script
python task2.py
Folder Structure
AP_intern_task/
│
├── task1/
│ ├── task1.py
│ ├── data/
│ └── output/
│
├── task2/
│ ├── task2.py
│ ├── data/ (contains 12 monthly sales CSV files)
│ └── output/ (contains visualizations or results)
Output Example
Task 2 produces a bar chart representing total sales per month in 2019, clearly showing which months had the highest and lowest performance.
Skills Demonstrated
Data Cleaning and Manipulation using Pandas
Data Visualization using Matplotlib
Handling multiple CSV files programmatically
Real-world data analysis workflow
Writing clean and efficient Python code
Author
Farman Ali
Computer Science Student
Pakistan
