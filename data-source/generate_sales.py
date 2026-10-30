import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# CONFIGURATION
NUM_RECORDS = 1000
ERROR_PERCENTAGE = 0.08   # 8% of records will contain errors

countries = ["US", "UK", "IN", "DE", "FR", "CA", "AU"]
categories = ["Electronics", "Clothing", "Home", "Books", "Sports"]
payment_methods = ["Credit Card", "PayPal", "UPI", "Debit Card"]

def generate_data():
    data = []

    for i in range(NUM_RECORDS):
        order_date = fake.date_between(start_date='-1y', end_date='today')
        quantity = random.randint(1, 5)
        price = round(random.uniform(10, 500), 2)

        data.append({
            "transaction_id": f"T{i+1}",
            "order_date": order_date,
            "customer_id": f"C{random.randint(1, 300)}",
            "customer_name": fake.name(),
            "country": random.choice(countries),
            "product_id": f"P{random.randint(1, 200)}",
            "product_category": random.choice(categories),
            "quantity": quantity,
            "price": price,
            "payment_method": random.choice(payment_methods),
            "order_status": random.choice(["Completed", "Cancelled", "Returned"])
        })