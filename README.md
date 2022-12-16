# Predicting bank customer churn using Machine Learning

Churn is defined as a measure of how many customers stop using a product or leave a service.



In this study, I aim to analyze a dataset involving bank customers to:

- explore and visualize the factors which lead to bank customer churn
- train a machine learning model to predict if a bank customer churns or not
- provide actionable insights to the bank to reduce customer churn

<br>

# About the dataset

The dataset contains the following columns:
- **customer_id** - unique ids for bank customer identification
- **credit_score** - the credit score of the customer
- **country** - the country of residence
- **gender** - male or female
- **age** - age of the customer
- **tenure** - how long the customer has had the bank account
- **balance** - bank balance of the customer
- **product_number** - the number of products from the bank
- **credit_card** - does the customer have a credit card?
- **active_member** - is the customer active?
- **estimated_salary** - the estimated salary of the customer
- **churn** - has the client left the bank?

<br>

# Requirements and Installation

**Requirements:**
- pyenv with Python: 3.9.8

<br>

**Environment:**

For installing the virtual environment you can either use the Makefile and run `make setup` in a terminal window within the project folder or install it manually using the following commands:

```zsh
pyenv local 3.9.8
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

<br>


# About this repo
- bank_customer_churn_dataset.csv
- Makefile
- requirements.txt


