# Overview
As a software engineer, I am exploring real-world job market data to strengthen my skills in data analysis, Python programming, visualization, etc. This project gives me hands-on experience with the full data science process, from cleaning and organizing data to analyzing it and presenting meaningful results. While building this software, I’m learning how to manage complex datasets, write clean and maintainable code, and uncover useful patterns from raw information.

The dataset I’m using comes from LinkedIn job postings and contains details like job titles, salaries, pay periods, locations, required skills, and much more. It’s a large dataset with over 100,000 postings, though for this project I focused on just the main postings.csv file of the 11. Here is a link to it: [Kaggle.com (LinkedIn Job Postings (2023 - 2024) Dataset)](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings)

The purpose of writing this software is to provide a tool that can answer important questions about the job market. The program is designed to be modular, so it can be expanded later to include predictive modeling, machine learning for salary predictions, and other advanced features. For more ideas about how I plan to enhance this project, see the future work section at the end.

You can watch a demo of my software here: [Software Demo Video](https://youtu.be/rizn9VMIGrw)

# Data Analysis Results

1. Which skills are most in-demand?

The analysis shows that the most in-demand skills are primarily centered around interpersonal abilities and healthcare expertise. The top five include people skills, healthcare, community outreach, patient care, and communication. This indicates that employers highly value individuals who can effectively interact with others, support community initiatives, and provide patient-centered care, reflecting strong demand in both social and medical sectors. While these soft and healthcare-related skills dominate, technical and programming skills remain relevant. For example, SQL ranks 15th, Java 19th, Python 26th, and AWS 30th, demonstrating continued demand for technology proficiency.

2. What are the top paying job titles on average (<$500,000 a year)?

When it comes to compensation, the top-paying job titles are dominated by high-level executive, medical, and technical positions. The highest-paying role is the Chief Product Officer at Slack, with an annual salary of $499,000, followed closely by specialized medical professionals such as Otorhinolaryngologists and Physician Anesthesiologists, as well as senior technical program managers and in-house counsel positions, all earning between $475,000 and $488,000. These figures highlight the premium placed on advanced expertise, leadership, and specialized knowledge.

3. What are the top paying locations on average (<$500,000 a year)?

In terms of geography, the top-paying locations are spread across the United States, with Chicago, Illinois offering the highest average salary of $475,000, followed by West Islip, NY, and Beeville, TX. Other high-paying areas include Cape Canaveral, FL, and Augusta County, VA, suggesting that both major metropolitan centers and smaller specialized regions offer lucrative opportunities, particularly in healthcare and technical industries.

# Development Environment

Refer to the requirements.txt file.

* Visual Studio Code
* Python 3.13.1
* Git / GitHub
* Matplotlib 3.10.6
* Numpy 2.3.3
* Pandas 2.3.3
* Jupyterlab 4.4.9
* Notebook 7.4.7
* Git LFS 3.7.0 — used to manage large dataset files in the repository

# Useful Websites

* [Kaggle.com (LinkedIn Job Postings (2023 - 2024) Dataset)](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings)
* [Pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html)
* [Pandas Guide](https://pandas.pydata.org/docs/user_guide/10min.html#min)
* [YouTube Pandas Tutorial](https://www.youtube.com/watch?v=EXIgjIBu4EU)
* [EDA with Pandas](https://www.kaggle.com/code/kashnitsky/topic-1-exploratory-data-analysis-with-pandas)
* [Numpy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)
* [YouTube Matplotlib Tutorial](https://www.youtube.com/watch?v=3Xc3CA655Y4)
* [Jupyter](https://jupyter.org/)

# Future Work

* Implement a machine learning model to predict salaries based on job title, location, and skills.
* Deeper analysis and data management.
* Add more visualizations and make them more interactive.
* Use the big and diverse dataset for other analysis.
* Build a user interface (UI).
* Allow users to filter and search for specific jobs, locations, or salary ranges.
* Generate automated reports or summaries from the analysis.