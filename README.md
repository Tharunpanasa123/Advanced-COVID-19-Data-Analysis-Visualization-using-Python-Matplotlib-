# 📊 Advanced COVID-19 Data Analysis & Visualization using Python

## 📌 Project Overview

This project performs time-series analysis on COVID-19 data using Python to understand infection trends, growth patterns, and mortality impact. The analysis includes key metric computation and insightful data visualizations to support data-driven understanding of pandemic progression.

## 🎯 Objectives

* Perform Exploratory Data Analysis (EDA) on COVID-19 time-series data
* Calculate Daily Growth Rate to analyze spread trends
* Compute Case Fatality Rate (CFR) to evaluate mortality impact
* Create meaningful visualizations for trend and distribution analysis

## 🛠️ Technologies Used

* **Python** -Programming Language
* **Pandas** – Data manipulation & time-series analysis
* **NumPy** – Numerical computations
* **Matplotlib** – Data visualization

## 📂 Project Structure

Advanced_COVID19_Data_Analysis/
│── main.py
│── covid_sample_data.csv
│── requirements.txt
│── README.md

## 📈 Key Analytical Metrics

### 1️⃣ Daily Growth Rate

Measures the percentage increase in confirmed cases compared to the previous day.

[
Daily\ Growth\ Rate = \frac{Current\ Day\ Cases - Previous\ Day\ Cases}{Previous\ Day\ Cases} \times 100
]

### 2️⃣ Case Fatality Rate (CFR)

Indicates the proportion of deaths among confirmed cases.

[
CFR = \frac{Total\ Deaths}{Total\ Confirmed\ Cases} \times 100
]

## 📊 Visualizations Generated

* 📈 Line Chart – Confirmed Cases Over Time
* 📊 Bar Chart – Death Count (Last 30 Days)
* 🥧 Pie Chart – Case Distribution (Latest Date)

All charts are automatically saved as PNG files after execution.

## ▶️ How to Run the Project

### Step 1: Install Dependencies

**bash**
pip install -r requirements.txt

### Step 2: Execute the Script

**bash**
python main.py

## 📌 Output

* Summary statistics printed in terminal
* Three visualization image files generated in the project directory

## 🚀 Skills Demonstrated

* Time-Series Data Analysis
* Exploratory Data Analysis (EDA)
* Statistical Metric Computation
* Data Visualization & Communication
* Python-based Analytical Programming

## 📎 Future Improvements

* Integration with real-world datasets (Johns Hopkins / WHO)
* 7-day rolling average analysis
* Trend forecasting models
* Interactive dashboards (Streamlit / Plotly)

👤 Author

PANASA THARUN KUMAR

Aspiring Data Analyst

