# Telco_Churn_Prediction_Case_Study

Read more about the dataset here: [Telco Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

A complete end to end ML design framework for Churn detection
This repository includes the following items
1. Comprehensive EDA on the dataset ([File link](EDA.ipynb))
2. Feature Engineering based on business use cases ([File link](https://github.com/IrishMehta/Telco_Churn_Prediction_Case_Study/blob/main/Feature%20Engineering%20%26%20Model%20Training.ipynb))
3. Model training with Feature selection techniques and Model Selection Techniques ([File link](https://github.com/IrishMehta/Telco_Churn_Prediction_Case_Study/blob/main/Feature%20Engineering%20%26%20Model%20Training.ipynb))
4. Hyperparameter tuning & Cross Validation to get the best results ([File link](https://github.com/IrishMehta/Telco_Churn_Prediction_Case_Study/blob/main/Feature%20Engineering%20%26%20Model%20Training.ipynb))
5. Local deployment using Streamlit ([File link](helper.py))
6. Complete Documentaion of Design Choices and Business use cases ([File link](Project_Report.pdf))
7. Link to deployed model: [https://poc-telco-churn.herokuapp.com/](https://poc-telco-churn.herokuapp.com/)



## Installation tutorial

**Source Data**: [Telco Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

1. **Code snippet to download dataset from windows terminal**

>1. Open terminal and run ``` pip install kaggle ```

>2. Create a python file called download_dataset.py and paste the following code (You can get your username and api key from you kaggle account and replace them in the placeholder values):
```
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
KaggleApi.config_values={"username":"enter_your_kaggle_username","key":"enter_your_kaggle_api_key"}
api = KaggleApi()
api.authenticate()

dataset = api.dataset_download_file('blastchar/telco-customer-churn','WA_Fn-UseC_-Telco-Customer-Churn.csv')
```

2. **Download the requirements.txt file from this repository and run this command to download all the required libraries for this project: ``` pip install -r requirements.txt ```**

3. **Download both the files named EDA.ipynb and Feature Engineering & Model Training and run them cell by cell on jupyter notebook.**

4. **Once the pickle file is ready, create a new python file called helper.py or download the one in this repository**

5. **Once the helper.py file is in place, create two files of these exact names: Procfile and setup.sh**

> **Write the following code on Procfile**
```
web: sh setup.sh && streamlit run helper.py
```

> **Write the following code on setup.sh**
```
mkdir -p ~/.streamlit/echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

6. **Once all this is done, run the following command on terminal to deploy the code on a local host:**
``` streamlit run helper.py ```


