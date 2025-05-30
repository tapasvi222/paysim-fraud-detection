# paysim-fraud-detection🔴

A machine learning project using the PaySim dataset to detect fraudulent financial transactions. The model analyzes transaction patterns to identify potential fraud based on features like transaction type, amount, balance changes, and more.

****#introduction🚀****

In this project, I worked on detecting fraudulent transactions using the PaySim dataset, which simulates real mobile money transfers. The main goal was to understand the patterns of fraudulent behavior and build a machine learning model that can help identify these suspicious transactions effectively.I also developed a simple Flask web app where using input transaction details and detecting fraud predictions.

****Data Set Overview📊****

The PaySim dataset simulates mobile money transactions and includes different types of transactions like cash-in ,cash-out,Transfer, Payment.Each record has details like the transaction amount, type, and account balances before and after the transaction for both the sender and receiver. This helps us understand transaction behavior better and build models that can spot fraud effectively.

****columns used in dataset📚****

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

** **#Data cleaning🧹****
 
  **✅checked for missing values** : Used isnull().sum() to identify missing values in the dataset. Found two missing values isFraud and  isFlaggedFraud.
  
  **🗑️ handling missing values**: Removed null values in these rows using dropna(). This made the data more integrated and consistent
  
  **☑️checked for duplicates**: Used duplicated().sum() to check for any duplicate records in the dataset. No duplicate rows were found in my data.
  
  **📉detecting and removing outliers**: Outliers were identified using box plots and statistical methods like the Interquartile Range (IQR). Values outside the defined boundaries were removed to keep the data clean and consistent.

****Data transformation🔄****

In this step, the type column was transformed using one-hot encoding  to convert it into a numerical format which is suitable for machine learning models.

 **steps followed**
 
   1)Identified unique categories in the type column.
   
   2)Applied one-hot encoding using pandas.get_dummies() and created new binary columns like type_CASH_IN, type_CASH_OUT, type_DEBIT, type_PAYMENT, and type_TRANSFER.
   
   3)Ensured all expected encoded columns are present if not added missing ones with default value 0.
   
   4)Converted encoded columns to integer type for consistency.

****Feature Engineering 🔑****

In this step, we selected and prepared the most meaningful input features to train our fraud detection model. These input columns help the model learn the difference between genuine and fraudulent transactions.⚠️

 Key inputs included:

Transaction type (one-hot encoded): type_CASH_IN, type_CASH_OUT, type_DEBIT, type_PAYMENT, type_TRANSFER.

Transaction amount 

Sender’s balance before and after the transaction: oldbalanceOrg, newbalanceOrig 

Receiver’s balance before and after the transaction: oldbalanceDest, newbalanceDest 

isFraud 🚨 – Indicates whether the transaction is fraudulent (1) or not (0).

****Model building🧱****

In this project, I experimented with three different machine learning models to detect fraudulent transactions:

Logistic Regression (LR)✅

Random Forest (RF)🌲

Decision Tree (DT)🌳

To begin, I split the dataset into input features and the target column (isFraud). Using train_test_split(), I divided the data into training and testing sets (80/20 split) to evaluate model performance properly.

  After training all three models, I compared their metrices like accuracy, precision, recall, and F1-score. Among them, the Decision Tree classifier gave the best performance, so i  selected it for the final model.

****Flask Web App and Pickle Integration🌐****

  To make the fraud detection model more interactive and user-friendly, I built a simple Flask web application that allows users to enter input transaction details and get instant fraud predictions.

  The trained Decision Tree model was saved using Python’s pickle module, which allowed me to load the model into the Flask app.

  Users can enter values like transaction type, amount, and balances. When they submit the form, the app processes the input, runs it to the model, and displays whether the transaction is predicted to be fraudulent or not.

****output🎏****

Once the user enters the transaction details in the web app and clicks submit, the model checks the input and instantly gives a prediction Whether fraud or not.

If the transaction looks normal, it shows a message like: **Fraud Detection: 0.0**.

If the model finds the transaction suspicious, it returns: **Fraud Detection: 1.0**.

****summary📌****

Frauds occur due to specific patterns observed in the transaction data.

**pattern1️⃣:  Full Balance Sent to an Empty Account**

    amount=old balance orig=new balance dest—>some amount
    full balance sent and receivers account starts with 0 it occurs fraud

**Pattern 2️⃣:   Sender Sends All Funds but Receiver Gets Nothing**

  If amount = oldbalanceOrig
  
 oldbalanceDest = newbalanceDest = 0

**🔍 This means:**
The sender transfers their entire balance.

But the receiver's balance stays at 0, before and after the transaction.

So, the money was not actually received — it likely disappeared or was redirected.

So it is considered a fraud.

**pattern 3️⃣: No Real Transfer (Zero Balances)**

amount=some amount

Old balance orig=new balance orig =old and new balance dest=0

type==cash out

Amount is neither transferred nor received so it is fraud.

**Pattern 4️⃣: Insufficient Funds, But Money Still Received**

Amount >old balance 

New balance dest= some value or = amount

Old balance orig and dest=0

There is not enough in the sender's account but some amount received in the new balance so it is fraud.

**pattern 5️⃣: Receiver Gets Less Than Sent**

amount=some value

Sender's account=some amount

A specific amount is deducted from the sender’s account

But the receiver does not receive the full amount

This discrepancy indicates tampering or incomplete fund transfer

Common in fraudulent activity where money is intercepted or misdirected











 


 





  
  
