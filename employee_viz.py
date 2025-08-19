import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpld3
import numpy as np

# Your email for verification
email = "24f2004977@ds.study.iitm.ac.in"

# Seed for reproducibility
np.random.seed(42)

# Generate synthetic data for 100 employees
departments = ["Marketing", "Sales", "Engineering", "HR", "Finance", "Operations"]
regions = ["Europe", "North America", "Asia", "Africa", "Middle East"]
employee_ids = [f"EMP{i:03d}" for i in range(1, 101)]

df = pd.DataFrame({
    "employee_id": employee_ids,
    "department": np.random.choice(departments, size=100),
    "region": np.random.choice(regions, size=100),
    "performance_score": np.round(np.random.uniform(70, 95, 100), 2),
    "years_experience": np.random.randint(1, 15, 100),
    "satisfaction_rating": np.round(np.random.uniform(3.0, 5.0, 100), 1)
})

# Count Marketing employees
marketing_count = df[df["department"] == "Marketing"].shape[0]
print(f"Number of employees in Marketing: {marketing_count}")

# Create histogram of departments
plt.figure(figsize=(8,6))
sns.countplot(data=df, x="department", palette="Set2")
plt.title("Distribution of Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

# Save interactive HTML
html_str = mpld3.fig_to_html(plt.gcf())
with open("employee_histogram.html", "w") as f:
    f.write(html_str)

plt.close()
