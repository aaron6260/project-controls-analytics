## This script generates synthetic data for clients, projects, monthly costs, change orders, and forecast history. The generated data is saved as CSV files for further analysis or testing purposes.

## Adding necessary imports
import random 
from datetime import datetime, timedelta
from tkinter.font import names

import numpy as np
import pandas as pd

## defining variables
NUM_PROJECTS = 200
NUM_CLIENTS = 25
START_YEAR = 2021
END_YEAR = 2025

## Setting deterministic randomness for reproducability
random.seed(42)
np.random.seed(42)

def generate_clients(num_clients=NUM_CLIENTS):
    """
    Generate a synthetic client table. 
    Parameters
    ----------
    num_clients : int
        Number of client records to generate. Default is 25 based on variables above.

    Returns
    -------
    pandas.DataFrame
        DataFrame contains client IDs, client names, and industries.
    """

    industries = ['Technology', 'Healthcare', 'Utilities', 'Retail', 'Manufacturing', 'Agriculture', 'Education', 'Transportation', 'Energy', 'Telecommunications']
    industry_probabilities = [10,10,15,3,20,1,5,5,30,1] #Probabilities for each industry totaling to 100.
    client_prefixes = ['Blue', 'Alpha', 'Legacy', 'NextGen', 'Pinnacle', 'Summit', 'Vertex', 'Horizon', 'Apex', 'Zenith']
    client_suffixes = ['Solutions', 'Systems', 'Technologies', 'Enterprises', 'Industries', 'Dynamics', 'Innovations', 'Global', 'Networks', 'Partners']
#    client_names = [f"{random.choice(client_prefixes)} {random.choice(client_suffixes)}" for _ in range(num_clients)]
    names = set() #Ensures unique client names, no duplicates. 
    while len(names) < num_clients:
        name = f"{random.choice(client_prefixes)} {random.choice(client_suffixes)}"
        names.add(name)
    client_names = list(names) #Convert the set into a list for DataFrame creation. 
    data = {
        'client_id': range(1, num_clients + 1),
        'client_name': client_names,
        'industry': random.choices(industries, weights=industry_probabilities, k=num_clients)
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
    clients = generate_clients()
    print(clients.head())
#    generate_projects()
#    generate_monthly_costs()
#    generate_change_orders()
#    generate_forecast_history()
#    save_csvs()

main()
