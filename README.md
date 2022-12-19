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
- Makefile
- requirements.txt
- bank_customer_churn_dataset.csv
- churn_prediction_notebook.ipynb

<br>

# Conclusions
- The customers that have a high balance and a high number of products from the bank are the highest value customers. The "best" customers (high balance, high number of products) are also very likely to churn. Therefore the bank should focus on preventing churn in these group of customers. The customers with zero balance who churn are less critical.

- Even though France has the highest number of customers overall, Germany has the highest number of churners and the largest percentage of its customers that churn. A higher percentage of customers in Germany churn compared to France and Spain. The bank should investigate if there are other competitors within Germany that are offering a better product or better services.

- Customers that have a higher number of products are also more likely to churn. The bank should investigate if their fees are too high for their products compared to other competitors or if their competitors are offering more competitive products.

- Active customers are also less likely to churn. The bank should look into campaigns to engage their customers to encourage them to use their services or products more. There may be services or products that the customers are not aware of and thus are not using them.


