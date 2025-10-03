import pandas as pd

df = pd.read_csv("../data/linkedin-job-postings/postings.csv")

df['med_salary'] = df['med_salary'].fillna((df['min_salary'] + df['max_salary']) / 2)

df_clean = df.dropna(subset=['title', 'location', 'med_salary', 'pay_period'])
df_clean = df_clean.copy()

def normalize_salary(row):
    if row['pay_period'] == 'Hourly':
        return row['med_salary'] * 40 * 52   
    elif row['pay_period'] == 'Monthly':
        return row['med_salary'] * 12        
    else:  
        return row['med_salary']

df_clean['salary_yearly'] = df_clean.apply(normalize_salary, axis=1)
df_clean = df_clean[df_clean['salary_yearly'] < 500_000]

top_titles = (df_clean.groupby('title')['salary_yearly'].mean().sort_values(ascending=False).head(10).reset_index())

top_titles['salary_yearly'] = top_titles['salary_yearly'].apply(lambda x: f"${x:,.0f}")
top_titles.index = top_titles.index + 1

print(top_titles)