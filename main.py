
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("covid_sample_data.csv", parse_dates=["Date"])
df.sort_values("Date", inplace=True)

# -----------------------------
# Compute Metrics
# -----------------------------

# Daily Growth Rate
df["Daily_Growth_Rate (%)"] = df["Confirmed"].pct_change() * 100

# Case Fatality Rate (CFR)
df["CFR (%)"] = (df["Deaths"] / df["Confirmed"]) * 100

# -----------------------------
# Exploratory Data Analysis
# -----------------------------

print("\nSummary Statistics:")
print(df.describe())

# -----------------------------
# Visualization 1: Confirmed Cases Over Time
# -----------------------------
plt.figure()
plt.plot(df["Date"], df["Confirmed"])
plt.title("COVID-19 Confirmed Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("line_chart_confirmed_cases.png")
plt.close()

# -----------------------------
# Visualization 2: Death Distribution (Bar Chart)
# -----------------------------
plt.figure()
plt.bar(df["Date"][-30:], df["Deaths"][-30:])
plt.title("Last 30 Days Death Count")
plt.xlabel("Date")
plt.ylabel("Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_chart_deaths.png")
plt.close()

# -----------------------------
# Visualization 3: Case Distribution (Pie Chart - Latest Data)
# -----------------------------
latest = df.iloc[-1]
labels = ["Confirmed", "Recovered", "Deaths"]
sizes = [latest["Confirmed"], latest["Recovered"], latest["Deaths"]]

plt.figure()
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Case Distribution (Latest Date)")
plt.savefig("pie_chart_distribution.png")
plt.close()

print("\nAnalysis Complete. Charts saved successfully.")
