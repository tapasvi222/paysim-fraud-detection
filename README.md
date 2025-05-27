# paysim-fraud-detection🔴

A machine learning project using the PaySim dataset to detect fraudulent financial transactions. The model analyzes transaction patterns to identify potential fraud based on features like transaction type, amount, balance changes, and more.

**#introduction🚀**

In this project, I worked on detecting fraudulent transactions using the PaySim dataset, which simulates real mobile money transfers. The main goal was to understand the patterns of fraudulent behavior and build a machine learning model that can help identify these suspicious transactions effectively.I also developed a simple Flask web app where using input transaction details and detecting fraud predictions.

**Data Set Overview📊**

The PaySim dataset simulates mobile money transactions and includes different types of transactions like cash-in ,cash-out,Transfer, Payment.Each record has details like the transaction amount, type, and account balances before and after the transaction for both the sender and receiver. This helps us understand transaction behavior better and build models that can spot fraud effectively.

**columns used in dataset📚**

   **step**: It represents the time of transaction.
   
   **amount**:It represents the amount which should be transferred in transaction.
   
   **nameorig**: It represents the unique id of the sender’s account.
   
   **oldbalanceOrg**: The sender’s account balance before the transaction.
   
   **newbalanceOrig**: The sender’s account balance after the transaction.
   
   **nameDest**: It represents the unique id of the receiver's account.
   
   **oldbalanceDest**: The receiver’s account balance before the amount received.
   
   **newbalanceDest**: The receiver’s account balance after the amount received.
   
   **isFraud**: It tells whether the transaction is fraudulent(1) or non-fraud(0).
   
   **isFlaggedFraud**: This indicates whether a transaction was flagged as suspicious or not.

 **#Data cleaning🧹**
 
  **✅checked for missing values** : Used isnull().sum() to identify missing values in the dataset. Found two missing values isFraud and  isFlaggedFraud.
  
  **🗑️ handling missing values**: Removed null values in these rows using dropna(). This made the data more integrated and consistent
  
  **☑️checked for duplicates**: Used duplicated().sum() to check for any duplicate records in the dataset. No duplicate rows were found in my data.
  
  **📉detecting and removing outliers**: Outliers were identified using box plots and statistical methods like the Interquartile Range (IQR). Values outside the defined boundaries were removed to keep the data clean and consistent.

**Data transformation🔄**

In this step, the type column was transformed using one-hot encoding  to convert it into a numerical format which is suitable for machine learning models.

 **steps followed**
 
   1)Identified unique categories in the type column.
   
   2)Applied one-hot encoding using pandas.get_dummies() and created new binary columns like type_CASH_IN, type_CASH_OUT, type_DEBIT, type_PAYMENT, and type_TRANSFER.
   
   3)Ensured all expected encoded columns are present if not added missing ones with default value 0.
   
   4)Converted encoded columns to integer type for consistency.



 





  
  
