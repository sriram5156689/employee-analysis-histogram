import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io, base64

# ----------------------------
# Generate synthetic dataset
# ----------------------------
# 100 employees across regions & departments
import numpy as np
np.random.seed(42)

departments = ["Marketing", "Sales", "IT", "Finance", "HR", "Operations"]
regions = ["North", "South", "East", "West"]

data = {
    "EmployeeID": range(1, 101),
    "Department": np.random.choice(departments, 100),
    "Region": np.random.choice(regions, 100),
    "PerformanceScore": np.random.randint(50, 100, 100)
}

df = pd.DataFrame(data)

# ----------------------------
# Frequency count for Marketing
# ----------------------------
marketing_count = (df["Department"] == "Marketing").sum()
print("Frequency count for Marketing department:", marketing_count)

# ----------------------------
# Plot histogram of departments
# ----------------------------
plt.figure(figsize=(8,6))
sns.countplot(data=df, x="Department", palette="viridis")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Employee Count")

# Save chart to buffer
buf = io.BytesIO()
plt.savefig(buf, format="png")
buf.seek(0)
img_base64 = base64.b64encode(buf.read()).decode("utf-8")
plt.close()

# ----------------------------
# Save HTML with email + chart
# ----------------------------
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Employee Performance Analysis</title>
</head>
<body>
    <h1>Department Frequency Analysis</h1>
    <p><b>Marketing Department Count:</b> {marketing_count}</p>
    <img src="data:image/png;base64,{img_base64}" alt="Department Histogram">

    <!-- Student Email for Verification: 23f2002842@ds.study.iitm.ac.in -->
</body>
</html>
"""

with open("employee_analysis.html", "w") as f:
    f.write(html_content)

print("✅ employee_analysis.html has been generated successfully.")
