import pandas as pd

raw_df = pd.read_csv("../data/linkedin-job-postings/postings.csv")

def get_top_skills(df, n=30):

    # Clean up skills text
    df['skills_clean'] = df['skills_desc'].str.replace(
        r'This position requires the following skills:\s*', '', regex=True
    )

    # Split skills while keeping job_id
    df_exploded = (
        df[['job_id', 'skills_clean']]
        .dropna()
        .assign(skill=lambda x: x['skills_clean'].str.split(','))
        .explode('skill')
    )
    df_exploded['skill'] = df_exploded['skill'].str.strip().str.lower()

    # Remove irrelevant words
    irrelevant = [
        'color', 'religion', 'age', 'national origin',
        'sexual orientation', 'sex', 'disability', 'gender identity'
    ]
    df_exploded = df_exploded[~df_exploded['skill'].isin(irrelevant)]

    # Combine similar skills
    df_exploded['skill_clean'] = df_exploded['skill'].replace({
        'verbal / written communication': 'communication',
        'csr / volunteer coordination': 'volunteer coordination',
        'relationship building': 'people skills',
        'networking': 'people skills',
        'marketing & communications (mar/com)': 'marketing',
        'hospice care': 'healthcare',
        'elder care': 'patient care',
        'contact lenses': 'optometry',
        'glaucoma': 'optometry',
        'ocular disease': 'optometry',
        'cataracts': 'optometry',
        'eye exams': 'optometry',
        'cataract': 'optometry',
        'low vision': 'optometry',
        'eyewear': 'optometry',
        'diabetes': 'healthcare',
        'vision': 'optometry'
    })

    # ✅ Deduplicate so each job_id only counts once per skill
    df_unique = df_exploded.drop_duplicates(subset=['job_id', 'skill_clean'])

    # Count postings per skill
    top_skills = df_unique['skill_clean'].value_counts().head(n).reset_index()
    top_skills.columns = ['skill', 'count']
    top_skills.index = top_skills.index + 1

    return top_skills

def get_top_skill(df, n=30):

    # Clean up skills text
    df['skills_clean'] = df['skills_desc'].str.replace(r'This position requires the following skills:\s*', '', regex=True)

     # Split skills while keeping job_id
    df_exploded = (df[['job_id', 'skills_clean']].dropna().assign(skill=lambda x: x['skills_clean'].str.split(',')).explode('skill'))
    df_exploded['skill'] = df_exploded['skill'].str.strip().str.lower()

    # Remove irrelevant words
    irrelevant = ['color', 'religion', 'age', 'national origin', 'sexual orientation', 'sex', 'disability', 'gender identity']
    df_exploded = df_exploded[~df_exploded['skill'].isin(irrelevant)]

    # Combine similar skills
    df_exploded['skill_clean'] = df_exploded['skill'].replace({
        'verbal / written communication': 'communication',
        'csr / volunteer coordination': 'volunteer coordination',
        'relationship building': 'people skills',
        'networking': 'people skills',
        'marketing & communications (mar/com)': 'marketing',
        'hospice care': 'healthcare',
        'elder care': 'patient care',
        'contact lenses': 'optometry',
        'glaucoma': 'optometry',
        'ocular disease': 'optometry',
        'cataracts': 'optometry',
        'eye exams': 'optometry',
        'cataract': 'optometry',
        'low vision': 'optometry',
        'eyewear': 'optometry',
        'diabetes': 'healthcare',
        'vision': 'optometry'
    })

    # Deduplicate so each job_id only counts once per skill
    df_unique = df_exploded.drop_duplicates(subset=['job_id', 'skill_clean'])

    # Count postings per skill
    top_skills = df_unique['skill_clean'].value_counts().head(n).reset_index()
    top_skills.columns = ['skill', 'count']
    top_skills.index = top_skills.index + 1

    return top_skills

skills = get_top_skill(raw_df)
print(skills)

