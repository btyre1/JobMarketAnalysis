import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):

    df = pd.read_csv(file_path)
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

    return df_clean

def get_top_skills(n=30):

    df = pd.read_csv("../data/linkedin-job-postings/postings.csv")

    df['skills_clean'] = df['skills_desc'].str.replace(r'This position requires the following skills:\s*', '', regex=True)

    skills_series = df['skills_clean'].dropna().str.split(',').explode().str.strip()
    skills_series = skills_series.str.lower()

    irrelevant = ['color', 'religion', 'age', 'national origin', 'sexual orientation', 'sex', 'disability']

    skills_series = skills_series[~skills_series.isin(irrelevant)]

    skills_series = skills_series.replace({
        'verbal / written communication': 'communication',
        'csr / volunteer coordination': 'volunteer coordination',
        'elder care': 'healthcare',
    })

    top_skills = skills_series.value_counts().head(n).reset_index()
    top_skills.index = top_skills.index + 1

    return top_skills

def get_highest_paying_titles(df, n=10):

        top_titles = (df.groupby('title')['salary_yearly'].mean().sort_values(ascending=False).head(n).reset_index())

        top_titles['salary_yearly'] = top_titles['salary_yearly'].apply(lambda x: f"${x:,.0f}")
        top_titles.index = top_titles.index + 1

        return top_titles

def get_highest_paying_locations(df, n=10):

        top_locations = (df.groupby('location')['salary_yearly'].mean().sort_values(ascending=False).head(n).reset_index())

        top_locations['salary_yearly'] = top_locations['salary_yearly'].apply(lambda x: f"${x:,.0f}")
        top_locations.index = top_locations.index + 1

        return top_locations

def main():

    clean_df = load_data("../data/linkedin-job-postings/postings.csv")

    # Q1: Which skills are most in-demand?
    print("\n--- Top In-Demand Skills ---")
    skills = get_top_skills()
    print(skills)

    # Q2: What are the top paying job titles on average?
    print("\n--- Top Paying Job Titles ---")
    titles = get_highest_paying_titles(clean_df)
    print(titles)

    # Q3: What are the top paying locations on average?
    print("\n--- Top Paying Locations ---")
    locations = get_highest_paying_locations(clean_df)
    print(locations)

if __name__ == "__main__":
    main()
    
