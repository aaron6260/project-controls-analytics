## This script generates synthetic data for clients, projects, monthly costs, change orders, and forecast history. The generated data is saved as CSV files for further analysis or testing purposes.

## Adding necessary imports
import random 
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

## defining variables
NUM_PROJECTS = 200
NUM_CLIENTS = 25
START_YEAR = 2021
END_YEAR = 2025

def generate_clients(num_clients=NUM_CLIENTS):
    industry = ['Technology', 'Healthcare', 'Utilities', 'Retail', 'Manufacturing', 'Agriculture', 'Education', 'Transportation', 'Energy', 'Telecommunications']
    client_pre = ['Blue', 'Alpha', 'Legacy', 'NextGen', 'Pinnacle', 'Summit', 'Vertex', 'Horizon', 'Apex', 'Zenith']
    client_suf = ['Solutions', 'Systems', 'Technologies', 'Enterprises', 'Industries', 'Dynamics', 'Innovations', 'Global', 'Networks', 'Partners']
    client_names = [f"{random.choice(client_pre)} {random.choice(client_suf)}" for _ in range(num_clients)]
    data = {
        'Client_id': range(1, num_clients + 1),
        'Client_name': client_names,
        'Industry': random.choices(industry, k=num_clients)
    }
    clients_df = pd.DataFrame(data)
    return clients_df

def generate_projects():
    pass

def generate_monthly_costs():
    pass

def generate_change_orders():
    pass

def generate_forecast_history():
    pass

def save_csvs():
    pass

def main():
    clients_df = generate_clients()
    print(clients_df)
#    generate_projects()
#    generate_monthly_costs()
#    generate_change_orders()
#    generate_forecast_history()
#    save_csvs()

main()
