import pandas as pd

def main():

    df = pd.read_csv("../data/linkedin-job-postings/postings.csv")

    def display_top_skills():

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

        top_skills = skills_series.value_counts().head(30).reset_index()
        top_skills.index = top_skills.index + 1

        print(top_skills)

    def display_highest_paying_titles():
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
        
    def display_highest_paying_locations():
        pass



    display_top_skills()
    display_highest_paying_titles()

if __name__ == "__main__":
    main()
    
