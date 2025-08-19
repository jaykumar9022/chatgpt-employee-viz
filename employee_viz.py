import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpld3
import random

# ✅ Verification email
email = "24f2004977@ds.study.iitm.ac.in"

# 1️⃣ Generate random employee data for 100 employees
np.random.seed(42)
departments = ["Marketing", "Operations", "Finance", "HR", "IT", "Sales"]
regions = ["Europe", "North America", "Africa", "Asia", "Middle East"]

data = {
    "employee_id": [f"EMP{str(i+1).zfill(3)}" for i in range(100)],
    "department": [random.choice(departments) for _ in range(100)],
    "region": [random.choice(regions) for _ in range(100)],
    "performance_score": np.round(np.random.uniform(60, 100, 100), 2),
    "years_experience": np.random.randint(1, 15, 100),
    "satisfaction_rating": np.round(np.random.uniform(1, 5, 100), 1)
}

df = pd.DataFrame(data)

# 2️⃣ Calculate Marketing department count
marketing_count = df[df['department'] == "Marketing"].shape[0]
print(f"Marketing department count: {marketing_count}")

# 3️⃣ Create histogram of departments
plt.figure(figsize=(10,6))
df['department'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribution of Employees by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')

# 4️⃣ Add verification email to figure
plt.text(0, -3, f"Verification Email: {email}", fontsize=10, color='gray')

# 5️⃣ Save interactive HTML using mpld3
html_file = "employee_histogram.html"
with open(html_file, "w") as f:
    # Embed email for verification
    f.write(f"<!-- {email} -->\n")
    f.write(mpld3.fig_to_html(plt.gcf()))

print(f"HTML file saved: {html_file}")
