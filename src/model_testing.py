import pandas as pd


def recommend_price(subscribers, reviews, lectures, duration, level, subject, le_level, le_subject, scaler, model):
    level_encoded = le_level.transform([level])[0]
    subject_encoded = le_subject.transform([subject])[0]

    input_data = pd.DataFrame({
        'num_subscribers': [subscribers],
        'num_reviews': [reviews],
        'num_lectures': [lectures],
        'content_duration': [duration],
        'price': 20,
        'review_subscriber_ratio': [reviews / subscribers],
        'course_popularity': [subscribers * reviews],
        'lectures_to_duration': [lectures / duration],
        'level': [level_encoded],
        'subject': [subject_encoded],
    })

    features = ['num_subscribers', 'num_reviews', 'num_lectures', 'content_duration',
                'review_subscriber_ratio', 'course_popularity', 'lectures_to_duration', 'price']
    input_data_scaled = input_data.copy()
    input_data_scaled[features] = scaler.transform(input_data[features])
    input_data_scaled.drop(['price'], axis=1, inplace=True)

    predicted_price = model.predict(input_data_scaled)

    output_data_unscaled = input_data_scaled.copy()
    output_data_unscaled['price'] = predicted_price[0]
    output_data_unscaled[features] = scaler.inverse_transform(output_data_unscaled[features])

    return output_data_unscaled['price']
