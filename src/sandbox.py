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


top_locations = (df_clean.groupby('location')['salary_yearly'].mean().sort_values(ascending=False).head(10).reset_index())

top_locations['salary_yearly'] = top_locations['salary_yearly'].apply(lambda x: f"${x:,.0f}")
top_locations.index = top_locations.index + 1

print(top_locations)