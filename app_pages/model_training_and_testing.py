# app_pages/model_training_and_testing.py
import streamlit as st

from src.model_training import plot_feature_importance, load_or_train_model
from src.model_testing import recommend_price


def page_model_training_and_testing_body():
    tuned_rf_model, X, le_level, le_subject, scaler = load_or_train_model()

    st.title("Model Training and Testing")

    st.header("Feature Importance")
    if st.button("Plot Feature Importance"):
        plot_feature_importance(tuned_rf_model, X)

    st.header("Test Model with Sample Data")
    subscribers = st.number_input("Number of Subscribers", min_value=0, value=1000)
    reviews = st.number_input("Number of Reviews", min_value=0, value=60)
    lectures = st.number_input("Number of Lectures", min_value=0, value=30)
    duration = st.number_input("Content Duration (hours)", min_value=0.0, value=20.0)
    level = st.selectbox("Course Level", le_level.classes_)
    subject = st.selectbox("Course Subject", le_subject.classes_)

    if st.button("Recommend Price"):
        recommended_price = recommend_price(subscribers, reviews, lectures, duration, level, subject, le_level,
                                            le_subject, scaler, tuned_rf_model)
        st.markdown(
            f"""
            <div style="background-color: #d4edda; padding: 10px; border-radius: 5px;">
                <h3 style="color: #155724;">Based on Our Model, the Recommended Price is 
                    <span style="font-weight: bold; color: #155724;">${recommended_price[0]:.2f}</span>
                </h3>
            </div>
            """,
            unsafe_allow_html=True
        )