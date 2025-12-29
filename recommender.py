# recommender.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load and clean job dataset
def load_jobs(csv_path='monster_com-job_sample.csv'):
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=['job_title', 'job_description'])
    df = df.fillna('')
    df['combined'] = df['job_description'] + ' ' + df['job_type'] + ' ' + df['sector']
    return df


# Match jobs based on cosine similarity
def recommend_jobs(user_text, skills, jobs_df, top_n=5):
    vectorizer = TfidfVectorizer(stop_words='english')
    job_vectors = vectorizer.fit_transform(jobs_df['combined'])
    user_vector = vectorizer.transform([user_text + ' ' + ' '.join(skills)])

    similarities = cosine_similarity(user_vector, job_vectors).flatten()
    jobs_df['similarity'] = similarities
    top_matches = jobs_df.sort_values(by='similarity', ascending=False).head(top_n)

    return top_matches.reset_index(drop=True)

SKILL_DB = {
    'python', 'java', 'sql', 'excel', 'machine learning', 'deep learning',
    'data analysis', 'django', 'flask', 'react', 'html', 'css', 'javascript',
    'pandas', 'numpy', 'power bi', 'tableau', 'nlp', 'git', 'aws', 'scikit-learn',
    'keras', 'tensorflow', 'linux', 'mongodb', 'docker'
}
# Find missing skills
def detect_missing_skills(user_skills, job_desc):
    job_desc = job_desc.lower()
    job_required_skills = {skill for skill in SKILL_DB if skill in job_desc}
    user_skills_lower = set(map(str.lower, user_skills))
    missing = job_required_skills - user_skills_lower
    return list(missing)
