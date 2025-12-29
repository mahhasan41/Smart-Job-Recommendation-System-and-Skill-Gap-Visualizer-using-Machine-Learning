# 🎯 SkillMatch - Job Recommendation System

A machine learning-powered job recommendation system that analyzes resumes, matches candidates with suitable job positions, and provides skill gap analysis. Built with Streamlit, scikit-learn, and spaCy.

## ✨ Features

- **Resume Parser**: Automatically extracts information from PDF resumes (name, email, phone, skills)
- **Job Recommendation Engine**: Uses TF-IDF vectorization and cosine similarity to match candidates with jobs
- **User Authentication**: Secure login and registration system with MySQL database
- **Skill Gap Analysis**: Identifies missing skills based on job requirements
- **Interactive Visualizations**: Match score charts and missing skills display
- **Job Search**: Filter jobs by location, skills, and experience level

## 🛠️ Technologies Used

- **Python 3.8+**
- **Streamlit** - Web framework for UI
- **scikit-learn** - Machine learning (TF-IDF, cosine similarity)
- **pandas** - Data manipulation
- **spaCy** - Natural Language Processing
- **pdfplumber** - PDF text extraction
- **pymysql** - MySQL database connection
- **matplotlib** - Data visualization

## 📋 Prerequisites

- Python 3.8 or higher
- MySQL Server installed and running
- pip package manager

## 🚀 Installation

### 1. Clone or Download the Project

```bash
cd "c:\Users\GLOBAL TECHNOLOGY\PycharmProjects\Machine Learning"
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download spaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

### 4. Dataset link: https://www.kaggle.com/datasets/PromptCloudHQ/us-jobs-on-monstercom


## 🗄️ Database Setup

### 1. Create MySQL Database

Open MySQL command line or workbench and run:

```sql
CREATE DATABASE resume_system;
USE resume_system;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 2. Configure Database Connection

Edit `config.py` with your MySQL credentials:

```python
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",              # Your MySQL username
        password="your_password",  # Your MySQL password
        database="resume_system"
    )
```

## 📂 Project Structure

```
Machine Learning/
├── app.py                          # Standalone job recommender demo
├── main.py                         # Main application with authentication
├── auth.py                         # User authentication logic
├── config.py                       # Database configuration
├── resume_parser.py                # PDF resume parsing
├── recommender.py                  # Job recommendation engine
├── visualizer.py                   # Data visualization components
├── check.py                        # API connection test (Adzuna)
├── monster_com-job_sample.csv      # Job dataset
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 🎮 How to Run

### Option 1: Run Complete Application (with Authentication)

```bash
streamlit run main.py
```

This starts the full application with:
- User registration and login
- Resume upload and parsing
- Job recommendations
- Skill gap analysis
- Visualization

**Default URL**: http://localhost:8501

### Option 2: Run Simple Job Recommender (No Authentication)

```bash
streamlit run app.py
```

This is a lightweight version without authentication, ideal for quick testing.

## 📖 Usage Guide

### 1. **Register/Login**
   - Create a new account or login with existing credentials
   - User data is stored securely in MySQL database

### 2. **Upload Resume**
   - Upload your resume in PDF format
   - The system automatically extracts:
     - Name
     - Email
     - Phone number
     - Skills

### 3. **Complete Your Profile**
   - Review and edit extracted skills
   - Add experience summary
   - Specify preferred job location
   - Enter job interests/keywords

### 4. **Get Job Recommendations**
   - Click "Find Matching Jobs"
   - View top 5 matching jobs with similarity scores
   - See detailed job descriptions and requirements

### 5. **Analyze Skills**
   - View match score visualization
   - Identify missing skills for top jobs
   - Get recommendations for skill development

## 🔧 Configuration

### Job Dataset
The system uses `monster_com-job_sample.csv`. You can replace it with your own dataset with these columns:
- `job_title`
- `job_description`
- `location`
- `job_type`
- `sector`
- `page_url` (optional)

### Skill Database
Edit the `SKILL_SET` in `resume_parser.py` and `SKILL_DB` in `recommender.py` to customize recognized skills:

```python
SKILL_SET = {
    'python', 'java', 'sql', 'excel', 'machine learning',
    'deep learning', 'data analysis', 'django', 'flask',
    # Add more skills...
}
```


## 🐛 Troubleshooting

### Database Connection Error
- Ensure MySQL server is running
- Verify credentials in `config.py`
- Check if database `resume_system` exists

### spaCy Model Not Found
```bash
python -m spacy download en_core_web_sm
```

### Port Already in Use
```bash
streamlit run main.py --server.port 8502
```

### CSV File Not Found
Ensure `monster_com-job_sample.csv` is in the project root directory.

## 📊 How It Works

1. **Resume Parsing**: Uses pdfplumber to extract text and spaCy NER to identify entities
2. **Feature Extraction**: TF-IDF vectorization converts text to numerical features
3. **Similarity Calculation**: Cosine similarity measures match between user profile and jobs
4. **Ranking**: Jobs sorted by similarity score, top matches displayed
5. **Skill Analysis**: Compares user skills with job requirements to identify gaps

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements.

## 📝 License

This project is open source and available for educational purposes.

## 👥 Author

Md. Mahmudol Hasan
