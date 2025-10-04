import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
#                 LINKEDIN JOB DATA ANALYSIS
# ==========================================================
# This script performs:
#   1. Data cleaning and salary normalization
#   2. Skill extraction and frequency analysis
#   3. Salary insights by job title and location
#   4. Visualization of top in-demand skills
# ==========================================================


# -------------------------
# Load & Clean Salary Data
# -------------------------
def load_data(file_path):
    """
    Load and clean salary data from a CSV file.

    Steps:
      - Fill missing median salaries using avg(min, max)
      - Normalize all salaries to yearly values
      - Remove incomplete rows and extreme outliers
    """

    # Load dataset into DataFrame
    df = pd.read_csv(file_path)

    # Fill missing median salaries with average of min and max
    df['med_salary'] = df['med_salary'].fillna((df['min_salary'] + df['max_salary']) / 2)

    # Drop rows missing key info
    df_clean = df.dropna(subset=['title', 'location', 'med_salary', 'pay_period'])
    df_clean = df_clean.copy()

    # Normalize salaries to yearly
    def normalize_salary(row):
        if row['pay_period'] == 'Hourly':
            return row['med_salary'] * 40 * 52   # Assume 40 hrs a week times by 52 weeks in a year
        elif row['pay_period'] == 'Monthly':
            return row['med_salary'] * 12        # 12 months a year
        else:  
            return row['med_salary']
        
    # Apply normalization across dataset
    df_clean['salary_yearly'] = df_clean.apply(normalize_salary, axis=1)

    # Remove extreme outliers over $500k a year
    df_clean = df_clean[df_clean['salary_yearly'] < 500_000]

    return df_clean

# -------------------------
# Top Skills Analysis
# -------------------------
def get_top_skills(df, n=30):
    """
    Extract and count the most common skills from job postings.

    Steps:
      - Clean skill text field
      - Split skills into separate rows
      - Normalize skill names (lowercase, trim, etc.)
      - Remove irrelevant terms and merge similar skills
      - Count unique jobs mentioning each skill
    """

    # Remove boilerplate text from skills column
    df['skills_clean'] = df['skills_desc'].str.replace(r'This position requires the following skills:\s*', '', regex=True)

    # Split skills while keeping job_id
    df_exploded = (df[['job_id', 'skills_clean']].dropna().assign(skill=lambda x: x['skills_clean'].str.split(',')).explode('skill'))

    df_exploded['skill'] = df_exploded['skill'].str.strip().str.lower()

    # Remove irrelevant words
    irrelevant = ['color', 'religion', 'age', 'national origin', 'sexual orientation', 'sex', 'disability', 'gender identity']
    df_exploded = df_exploded[~df_exploded['skill'].isin(irrelevant)]

    # Merge similar skills
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

    # Avoid double-counting, so one skill per job posting
    df_unique = df_exploded.drop_duplicates(subset=['job_id', 'skill_clean'])

    # Count postings per skill
    top_skills = df_unique['skill_clean'].value_counts().head(n).reset_index()
    top_skills.columns = ['skill', 'count']
    top_skills.index = top_skills.index + 1

    return top_skills

def plot_top_skills(top_skills):
    """
    Visualize the most in-demand skills as a horizontal bar chart.
    """
    plt.figure(figsize=(10, 6))
    plt.barh(top_skills['skill'], top_skills['count'], color='skyblue')
    plt.gca().invert_yaxis()  # largest at top
    plt.title("Top In-Demand Skills", fontsize=14, weight='bold')
    plt.xlabel("Number of Postings")
    plt.tight_layout()
    plt.show()

# -------------------------
# Salary Analysis
# -------------------------
def get_highest_paying_titles(df, n=10):
    """
    Compute the top n job titles based on average annual salary.
    """

    top_titles = (df.groupby('title')['salary_yearly'].mean().sort_values(ascending=False).head(n). reset_index())

    # Format salary values for readability
    top_titles['salary_yearly'] = top_titles['salary_yearly'].apply(lambda x: f"${x:,.0f}")
    top_titles.index = top_titles.index + 1

    return top_titles

def get_highest_paying_locations(df, n=10):
    """
    Compute the top n locations based on average annual salary.
    """

    top_locations = (df.groupby('location')['salary_yearly'].mean().sort_values(ascending=False).head(n).reset_index())

    top_locations['salary_yearly'] = top_locations['salary_yearly'].apply(lambda x: f"${x:,.0f}")
    top_locations.index = top_locations.index + 1

    return top_locations

# -------------------------
# Main Program
# -------------------------
def main():
    """
    Main entry point for job posting analysis.

    Steps:
      1. Load raw and cleaned datasets
      2. Identify most in-demand skills
      3. Find top-paying job titles
      4. Find top-paying locations
      5. Visualize results
    """

    # Raw dataset for skills analysis
    raw_df = pd.read_csv("../data/linkedin-job-postings/postings.csv")

    # Cleaned dataset for salary analysis
    clean_df = load_data("../data/linkedin-job-postings/postings.csv")

    # Q1: Which skills are most in-demand?
    print("\n--- Top In-Demand Skills ---")
    top_skills = get_top_skills(raw_df)
    print(top_skills)
    plot_top_skills(top_skills)

    # Q2: What are the top paying job titles on average?
    print("\n--- Top Paying Job Titles ---")
    top_titles = get_highest_paying_titles(clean_df)
    print(top_titles)

    # Q3: What are the top paying locations on average?
    print("\n--- Top Paying Locations ---")
    top_locations = get_highest_paying_locations(clean_df)
    print(top_locations)

# Run program
if __name__ == "__main__":
    main()
    
