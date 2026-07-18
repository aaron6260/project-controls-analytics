## This script generates synthetic data for clients, projects, monthly costs, change orders, and forecast history. The generated data is saved as CSV files for further analysis or testing purposes.

## Adding necessary imports
import random 
from datetime import datetime, timedelta
from tkinter.font import names

import numpy as np
import pandas as pd

from config.general import NUM_CLIENTS, NUM_PROJECTS, START_YEAR, END_YEAR, RANDOM_SEED
from config.clients import INDUSTRY_CONFIG, CLIENT_PREFIXES, CLIENT_SUFFIXES, CLIENT_SIZE_CONFIG
from config.projects import PROJECT_CATALOG, REGIONS, PROJECT_MANAGERS, STATUS_DISTRIBUTION

## Setting deterministic randomness for reproducability
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

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
    used_names = set() #A set ensures unique client names, no duplicates.
    client_names = []
    while len(client_names) < num_clients:
        temporary_name = f"{random.choice(CLIENT_PREFIXES)} {random.choice(CLIENT_SUFFIXES)}"
        if temporary_name not in used_names: #checks that the newly generated name is unique before adding it to the list. 
            used_names.add(temporary_name) #add unique name to set. Unordered collection, so random.seed won't work properly. 
            client_names.append(temporary_name) #adding to list because it will preserve the order of generation, which is important for reproducibility.
    data = {
        'client_id': range(1, num_clients + 1),
        'client_name': client_names,
        'industry': random.choices(list(INDUSTRY_CONFIG.keys()), weights=[v['weight'] for v in INDUSTRY_CONFIG.values()], k=num_clients),
        'client_size': random.choices(list(CLIENT_SIZE_CONFIG.keys()), weights=[v['probability'] for v in CLIENT_SIZE_CONFIG.values()], k=num_clients),
    }
    clients_df = pd.DataFrame(data)
    clients_df['business_scale'] = clients_df.apply(lambda row: random.uniform(*CLIENT_SIZE_CONFIG[row['client_size']]['business_scale_range']), axis=1)
    return clients_df

def generate_projects(num_projects=NUM_PROJECTS, clients_df=None):
    projects_df = None
    data = {
        'project_id': range(1, num_projects + 1),
        'client_id': random.choices(clients_df['client_id'], k=num_projects),
        
    }
    return projects_df

def generate_monthly_costs():
    pass

def generate_change_orders():
    pass

def generate_forecast_history():
    pass

def save_csvs():
    pass

def main():
    clients = generate_clients(num_clients=NUM_CLIENTS)
    #print(clients)
#    generate_projects()
#    generate_monthly_costs()
#    generate_change_orders()
#    generate_forecast_history()
#    save_csvs()

main()
