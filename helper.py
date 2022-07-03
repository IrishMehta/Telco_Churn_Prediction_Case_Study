import streamlit as st
import pickle
import pandas as pd

pickle_out = open("telecom_churn_prediction.pkl", "rb")
telecom_churn_prediction_model = pickle.load(pickle_out)


@st.cache
def model_prediction(MonthlyCharges, payment_per_month, tenure,
                     service_change_impact, total_payment_cycles,
                     Contract_Month_to_Month):
    prediction = telecom_churn_prediction_model.predict(pd.DataFrame([[MonthlyCharges, payment_per_month, tenure,
                                                                       service_change_impact, total_payment_cycles,
                                                                       Contract_Month_to_Month]],
                                                                     columns=['MonthlyCharges', 'payment_per_month',
                                                                              'tenure',
                                                                              'service_change_impact',
                                                                              'total_payment_cycles',
                                                                              'Contract_Month-to-month']))

    return prediction


st.title('Telecom Churn Predictor')
st.header('Enter the details of the customer:')


def perc_chage():
    st.session_state['service_change'] = (st.session_state['monthly_charge'] - st.session_state[
        'lifetime_monthly_charge']) / (st.session_state['monthly_charge'])


MonthlyCharges = st.number_input('Payment per month of the user (current):', key='monthly_charge', min_value=1.00,
                                 on_change=perc_chage, format="%.2f")

payment_per_month = st.number_input('Payment per month of the user (lifetime):', key='lifetime_monthly_charge',
                                    min_value=1.00000, on_change=perc_chage, format="%.5f")

tenure = st.number_input('Tenure of the user in Months:', key='tenure', min_value=1, )

service_change_impact = st.number_input(
    '% change in current monthly price and lifetime monthly price: (The field will be automatically populated based on your entries for the above 3 fields',
    format="%.5f", key='service_change')

total_payment_cycles = st.number_input('Total Payment Cycles:', key='total_payment_cycles', min_value=1, value=tenure,
                                       max_value=tenure)

Contract_Month_to_Month = st.selectbox('Monthly Subscriber Flag:', [0, 1])

if st.button('Predict Churn possibility'):
    churn = model_prediction(MonthlyCharges, payment_per_month, tenure,
                             service_change_impact, total_payment_cycles,
                             Contract_Month_to_Month)
    if churn[0] >= 0.8:
        st.success(f'The user will churn')
    else:
        st.success(f'The user will not churn')
