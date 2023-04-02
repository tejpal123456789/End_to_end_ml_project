import streamlit as st
from src.pipeline.predict_pipeline import CustomData
from src.pipeline.predict_pipeline import PredictPipeline
st.title('Student Performance Indicator')

# gender=st.text_input('Gender')
# race_ethinicity=st.text_input('Race')
# parental_education=st.text_input('Education')
# lunch=st.text_input('Lunch')
# test_prepare=st.text_input('Test Prepare')
# reading_score=st.number_input('Reading Score')
# writing_score=st.number_input('Writing Score')
data=CustomData(st.text_input('Gender'),st.text_input('Race'),st.text_input('Education'),st.text_input('Lunch'),st.text_input('Test Prepare'),st.number_input('Reading Score'),st.number_input('Writing Score'))

#data=CustomData(gender,race_ethinicity,parental_education,lunch,test_prepare,reading_score,writing_score)


pred_df=data.get_data_as_data_frame()
print(pred_df)
print("Before Prediction")

predict_pipeline=PredictPipeline()
print("Mid Prediction")
results=predict_pipeline.predict(pred_df)
print("after Prediction")
print(results)

if st.button('predict'):

        
            st.write('Math score {}'.format(results))