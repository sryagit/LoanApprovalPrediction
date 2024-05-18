import pickle
import streamlit as st 
from streamlit_option_menu import option_menu
import numpy as np


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# creating a function for Prediction

def Loanapprovalprediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      print('not Approved')
    else:
      print('approved')
  
    
  
def main():
    
    
    # giving a title
    st.title('Loan Approval Prediction Web App')
    
    
    # getting the input data from the user
    
    Gender 				= st.text_input('Gender')
    Married 			= st.text_input('Married')
    Dependents			= st.text_input('Dependents')
    Education 			= st.text_input('Education')
    Self_Employed 		= st.text_input('Self_Employed')
    ApplicantIncome 	= st.text_input('ApplicantIncome')
    CoapplicantIncome 	= st.text_input('CoapplicantIncome')
    LoanAmount 			= st.text_input('LoanAmount')
    Loan_Amount_Term 	= st.text_input('Loan_Amount_Term')
    Credit_History 		= st.text_input('Credit_History')
    Property_Area 		= st.text_input('Property_Area')

    
    
    # code for Prediction
    status = ''
    
    # creating a button for Prediction
    
    if st.button('Status Test Result'):
        status = Loanapprovalprediction([Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area])
        
        
    st.success(status)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  
