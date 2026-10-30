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

