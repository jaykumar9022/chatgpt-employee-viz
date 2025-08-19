import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpld3
import random

# Verification email
email = "24f2004977@ds.study.iitm.ac.in"

# -----------------------------
# 1. Generate sample dataset
# -----------------------------
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

# -----------------------------
# 2. Calculate Marketing count
# -----------------------------
marketing_count = df[df['department'] == "Marketing"].shape[0]
print(f"Marketing department count: {marketing_count}")

# -----------------------------
# 3. Create histogram
# -----------------------------
plt.figure(figsize=(10,6))
df['department'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribution of Employees by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.text(-0.5, -3, f"Verification Email: {email}", fontsize=10, color='gray')

# -----------------------------
# 4. Embed Python code in HTML
# -----------------------------
python_code = '''import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpld3
import random

email = "24f2004977@ds.study.iitm.ac.in"

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
marketing_count = df[df['department'] == "Marketing"].shape[0]
print(f"Marketing department count: {marketing_count}")

plt.figure(figsize=(10,6))
df['department'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribution of Employees by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.text(-0.5, -3, f"Verification Email: {email}", fontsize=10, color='gray')
'''

# -----------------------------
# 5. Save interactive HTML
# -----------------------------
html_file = "employee_histogram.html"
with open(html_file, "w") as f:
    # Embed email in HTML comment
    f.write(f"<!-- {email} -->\n")
    # Embed Python code as preformatted text
    f.write(f"<pre>{python_code}</pre>\n")
    # Embed mpld3 interactive figure
    f.write(mpld3.fig_to_html(plt.gcf()))

print(f"HTML file saved with embedded Python code and plot: {html_file}")
