import pandas as pd

df = pd.read_csv("../data/linkedin-job-postings/postings.csv")

# Fill missing median salaries row-wise
df['med_salary'] = df.apply(
    lambda row: row['med_salary'] if pd.notna(row['med_salary']) else (row['min_salary'] + row['max_salary']) / 2,
    axis=1
)

# Drop rows missing important info
df_clean = df.dropna(subset=['title', 'location', 'med_salary', 'pay_period']).copy()

# Normalize salaries to yearly
def normalize_salary(row):
    if row['pay_period'] == 'Hourly':
        return row['med_salary'] * 40 * 52
    elif row['pay_period'] == 'Monthly':
        return row['med_salary'] * 12
    else:
        return row['med_salary']

df_clean['salary_yearly'] = df_clean.apply(normalize_salary, axis=1)

# Remove zero or unrealistic salaries
df_clean = df_clean[df_clean['salary_yearly'] > 0]

# Top 20 job titles by average yearly salary
avg_salary_title = (
    df_clean.groupby('title')['salary_yearly']
    .mean()
    .sort_values(ascending=False)
    .head(20)
)

print(avg_salary_title)

