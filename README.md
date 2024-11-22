# Course Cost Analyzer

This project focuses on the Udemy Courses Dataset, where I developed a predictive model for course pricing. Using Python, Streamlit and machine learning, I created an interactive application to explore the dataset and predict key course metrics. The app is deployed on Heroku, providing a practical tool for developers and educators to analyze course attributes and trends effectively.

[Course Cost Analyzer](https://course-cost-analyzer-4dbdeb80a36e.herokuapp.com//)

---

## Dataset Overview

The dataset, sourced from Kaggle, contains records of Udemy courses. It includes attributes like price, subject, level, number of subscribers, reviews, lectures, and content duration. The dataset allows us to explore patterns, correlations, and trends in online education.

[Dataset Link](https://www.kaggle.com/datasets/andrewmvd/udemy-courses)

### Key Features:
| Column           | Description                                             |
|-------------------|---------------------------------------------------------|
| `course_id`       | Unique identifier for each course                       |
| `course_title`    | Title of the course                                     |
| `is_paid`         | Whether the course is free or paid                      |
| `price`           | Course price in USD                                     |
| `num_subscribers` | Number of users subscribed to the course                |
| `num_reviews`     | Number of reviews for the course                        |
| `num_lectures`    | Number of lectures in the course                        |
| `content_duration`| Total hours of course content                           |
| `subject`         | Subject category of the course (e.g., Business, Music) |
| `level`           | Course difficulty level (e.g., Beginner, Advanced)     |
| `published_timestamp` | Date when the course was published                |

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


## Deployment

### Steps to Deploy on Heroku:
1. **Prepare environment**: Create a `requirements.txt` and `Procfile`.
2. **Push to GitHub**: Commit changes to a branch linked to Heroku.
3. **Deploy**: Set up Heroku application and push the branch.

---


## Credits and References

- **Kaggle Dataset**: [Udemy Courses Dataset](https://www.kaggle.com/datasets/andrewmvd/udemy-courses)
- **Libraries**: Pandas, NumPy, Matplotlib, Scikit-learn, Streamlit
- **Inspiration**: Data Science projects on kaggle and Streamlit documentation.
- **Stackoverflow**: For bugs and errors.
