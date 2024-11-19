# src/model_training.py
import pandas as pd
import joblib
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor

# Paths to save/load the objects
MODEL_PATH = 'outputs/model/tuned_rf_model.pkl'
X_PATH = 'outputs/model/X.pkl'
LE_LEVEL_PATH = 'outputs/model/le_level.pkl'
LE_SUBJECT_PATH = 'outputs/model/le_subject.pkl'
SCALER_PATH = 'outputs/model/scaler.pkl'


def load_or_train_model():
    try:
        # Load the objects if they exist
        tuned_rf_model = joblib.load(MODEL_PATH)
        X = joblib.load(X_PATH)
        le_level = joblib.load(LE_LEVEL_PATH)
        le_subject = joblib.load(LE_SUBJECT_PATH)
        scaler = joblib.load(SCALER_PATH)
    except FileNotFoundError:
        # If not, perform feature engineering and train the model
        df = pd.read_csv('outputs/datasets/cleaned/cleanedDataset.csv')  # Load your dataset

        # Feature engineering steps
        df['review_subscriber_ratio'] = df['num_reviews'] / df['num_subscribers']
        df['course_popularity'] = df['num_subscribers'] * df['num_reviews']
        df['lectures_to_duration'] = df['num_lectures'] / df['content_duration']

        features = ['num_subscribers', 'num_reviews', 'num_lectures', 'content_duration',
                    'review_subscriber_ratio', 'course_popularity', 'lectures_to_duration', 'price']
        X = df[features]

        le_level = LabelEncoder()
        le_subject = LabelEncoder()
        X['level'] = le_level.fit_transform(df['level'])
        X['subject'] = le_subject.fit_transform(df['subject'])

        scaler = StandardScaler()
        X[features] = scaler.fit_transform(X[features])

        y = X['price']
        X.drop(['price'], axis=1, inplace=True)

        # Using tuned hyper parameter
        tuned_rf_model = RandomForestRegressor(
            max_depth=10,
            min_samples_leaf=4,
            min_samples_split=10,
            n_estimators=200,
            random_state=42
        )
        tuned_rf_model.fit(X, y)

        # Save the objects
        joblib.dump(tuned_rf_model, MODEL_PATH)
        joblib.dump(X, X_PATH)
        joblib.dump(le_level, LE_LEVEL_PATH)
        joblib.dump(le_subject, LE_SUBJECT_PATH)
        joblib.dump(scaler, SCALER_PATH)

    return tuned_rf_model, X, le_level, le_subject, scaler