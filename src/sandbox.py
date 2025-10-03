import pandas as pd

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

display_top_skills()