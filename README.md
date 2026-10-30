# e-commerce-project
E-Commerce Analytics Data Engineering Project using DBT

## Docker Configuration

 `Dockerfile`

Defines how to build the Docker image for the dbt environment. It specifies the base image, installs the required dependencies, and configures the environment needed to run dbt.

 `Docker-compose.yml`

Defines and manages the services required for the project, including the PostgreSQL database and the dbt environment. It configures how the containers communicate, which ports they use, and how the services run together.

## Data Generation

 `generate_sales.py`

Generates 1,000 synthetic e-commerce transactions using Python, Pandas, and Faker. The script includes customer details, product information, order dates, prices, payment methods, and order statuses. It also introduces simulated data-quality issues, such as missing values, invalid prices, negative quantities, future dates, and duplicate transaction IDs. The generated dataset is exported as ecommerce_sales.csv.