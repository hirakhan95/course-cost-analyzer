from app_pages.multipage import MultiPage

# Load pages scripts
from app_pages.summary import page_summary_body
from app_pages.eda import page_eda_body
from app_pages.bi_case_study_1 import page_bi_case_study_1
from app_pages.bi_case_study_2 import page_bi_case_study_2
from app_pages.bi_case_study_3 import page_bi_case_study_3
from app_pages.analysis import analysis
from app_pages.model_training_and_testing import page_model_training_and_testing_body  # New page import

app = MultiPage(app_name="Udemy Courses Analysis")

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Exploratory Data Analysis (EDA)", page_eda_body)
app.add_page("BI: Pricing Strategy for Paid Courses", page_bi_case_study_1)
app.add_page("BI: Identifying Top Performing Courses for Marketing Campaigns", page_bi_case_study_2)
app.add_page("BI: Optimizing Course Content for Engagement and Retention", page_bi_case_study_3)
app.add_page("Content Duration vs. Engagement and Retention Analysis", analysis)
app.add_page("Model Training and Testing", page_model_training_and_testing_body)  # New page

app.run()
