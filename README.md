# Course Cost Analyzer

This project focuses on the Udemy Courses Dataset, where I developed a predictive model for course pricing. Using Python, Streamlit, and machine learning, I created an interactive application to explore the dataset and predict key course metrics. The app is deployed on Heroku, providing a practical tool for developers and educators to analyze course attributes and trends effectively.

[Course Cost Analyzer](https://course-cost-analyzer-4dbdeb80a36e.herokuapp.com)

---

## Table of Contents

1. [Dataset Overview](#dataset-overview)
2. [Business Requirements](#business-requirements)
3. [Methods and Tools](#methods-and-tools)
4. [Project Structure](#project-structure)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Model Training](#model-training)
8. [Model Testing](#model-testing)
9. [Deployment](#deployment)
10. [Dashboard Design](#dashboard-design)
11. [Credits and References](#credits-and-references)

---

## Dataset Overview

The dataset, sourced from Kaggle, contains records of Udemy courses. It includes attributes like price, subject, level, number of subscribers, reviews, lectures, and content duration. The dataset allows us to explore patterns, correlations, and trends in online education.

[Dataset Link](https://www.kaggle.com/datasets/andrewmvd/udemy-courses)

### Key Features:
| Column               | Description                                             |
|----------------------|---------------------------------------------------------|
| `course_id`          | Unique identifier for each course                       |
| `course_title`       | Title of the course                                     |
| `is_paid`            | Whether the course is free or paid                      |
| `price`              | Course price in USD                                     |
| `num_subscribers`    | Number of users subscribed to the course                |
| `num_reviews`        | Number of reviews for the course                        |
| `num_lectures`       | Number of lectures in the course                        |
| `content_duration`   | Total hours of course content                           |
| `subject`            | Subject category of the course (e.g., Business, Music)  |
| `level`              | Course difficulty level (e.g., Beginner, Advanced)      |
| `published_timestamp`| Date when the course was published                      |

---

## Business Requirements

1. **Optimize Course Pricing for Revenue Growth.**
   - Develop a strategy to adjust course prices while maintaining a competitive edge in the market.

2. **Identify Best-Performing Courses for Marketing Campaigns.**
   - Analyze and rank courses based on popularity metrics to feature in promotional activities.

3. **Enhance Course Engagement and Retention.**
   - Explore and optimize course attributes (e.g., number of lectures, content duration) to improve student experience and satisfaction.

---

## Methods and Tools

### Key Libraries:
- **Pandas**: Data cleaning and manipulation.
- **NumPy**: Numerical computations.
- **Matplotlib/Seaborn**: Visualization tools.
- **Scikit-learn**: Machine learning pipeline and model building.
- **Streamlit**: Interactive dashboard development.
- **Feature-engine**: Model building.

---

## Project Structure

```
Course-Cost-Analyzer/
├── jupyter_notebooks/
│   ├── 1. Data_Cleaning.ipynb
│   ├── 2. Exploratory_Data_Analysis.ipynb
│   ├── 3. Feature_Engineering.ipynb
│   ├── 4. Model_Training.ipynb
│   ├── 5. Model_Evaluation.ipynb
│   ├── 6. Model_Deployment.ipynb
│   └── 7. ML_Modeling_and_Evaluation2.ipynb
├── src/
│   ├── model_training.py
│   ├── model_testing.py
│   └── app.py
├── outputs/
│   ├── datasets/
│   │   └── cleaned/
│   │       └── cleanedDataset.csv
│   └── model/
│       ├── tuned_rf_model.pkl
│       ├── X.pkl
│       ├── le_level.pkl
│       ├── le_subject.pkl
│       └── scaler.pkl
├── app_pages/
│   ├── model_training_and_testing.py
│   ├── multipage.py
│   └── summary.py
├── README.md
├── requirements.txt
└── Procfile
```

---

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/hirakhan95/course-cost-analyzer
   cd Course-Cost-Analyzer
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

---

## Usage

### Running the Application

1. **Start the Streamlit application:**
   ```sh
   streamlit run src/app.py
   ```

2. **Open your browser and navigate to:**
   ```
   http://localhost:8501
   ```

### Jupyter Notebooks

- **Data Cleaning:** `jupyter_notebooks/1. Data_Cleaning.ipynb`
- **Exploratory Data Analysis:** `jupyter_notebooks/2. Exploratory_Data_Analysis.ipynb`
- **Feature Engineering:** `jupyter_notebooks/3. Feature_Engineering.ipynb`
- **Model Training:** `jupyter_notebooks/4. Model_Training.ipynb`
- **Model Evaluation:** `jupyter_notebooks/5. Model_Evaluation.ipynb`
- **Model Deployment:** `jupyter_notebooks/6. Model_Deployment.ipynb`
- **ML Modeling and Evaluation:** `jupyter_notebooks/7. ML_Modeling_and_Evaluation2.ipynb`

---

## Model Training

The `src/model_training.py` script handles the training of the RandomForestRegressor model. It includes feature engineering, model training, and saving the trained model and associated objects.

### Key Functions:

- **load_or_train_model():**
  - Loads a pre-trained model and associated objects if they exist.
  - If not, performs feature engineering, trains the model, and saves the objects.

- **plot_feature_importance(model, X):**
  - Plots the feature importance of the trained model.

---

## Model Testing

The `src/model_testing.py` script includes the function to recommend a course price based on various input features.

### Key Functions:

- **recommend_price(subscribers, reviews, lectures, duration, level, subject, le_level, le_subject, scaler, model):**
  - Recommends a price for a course based on input features.

---

## Deployment

### Steps to Deploy on Heroku:

1. **Prepare environment:**
   - Create a `requirements.txt` and `Procfile`.

2. **Push to GitHub:**
   - Commit changes to a branch linked to Heroku.

3. **Deploy:**
   - Set up Heroku application and push the branch.

---

## Dashboard Design

The dashboard is designed using Streamlit and consists of the following pages:

1. **Summary Page:**
   - Provides an overview of the project, including a summary of the dataset and key project terms.
   - Displays the business requirements and project goals.

2. **Model Training and Testing Page:**
   - Allows users to train the model or load a pre-trained model.
   - Displays feature importance of the trained model.
   - Provides an interface to test the model with sample data and get price recommendations.

### Summary Page

The summary page (`app_pages/summary.py`) includes:
- A project summary with key terms and jargon.
- Information about the dataset and its attributes.
- Business requirements and project goals.

### Model Training and Testing Page

The model training and testing page (`app_pages/model_training_and_testing.py`) includes:
- A button to plot feature importance of the trained model.
- Input fields for testing the model with sample data (number of subscribers, reviews, lectures, content duration, course level, and subject).
- A button to recommend a price based on the input features.

### MultiPage Class

The `MultiPage` class (`app_pages/multipage.py`) is used to generate multiple Streamlit pages using an object-oriented approach. It includes:
- Initialization of the application with a specified name and configuration.
- Methods to add pages to the application.
- A method to run the application and display the selected page from the sidebar menu.

---

## Credits and References

- **Kaggle Dataset:** [Udemy Courses Dataset](https://www.kaggle.com/datasets/andrewmvd/udemy-courses)
- **Libraries:** Pandas, NumPy, Matplotlib, Scikit-learn, Streamlit
- **Inspiration:** Data Science projects on Kaggle and Streamlit documentation.
- **Stackoverflow:** For bugs and errors.
```
