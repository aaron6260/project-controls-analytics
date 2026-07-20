## This script generates synthetic data for clients, projects, monthly costs, change orders, and forecast history. The generated data is saved as CSV files for further analysis or testing purposes.

## Adding necessary imports
import random 
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from tkinter.font import names

import numpy as np
import pandas as pd

from config.general import NUM_CLIENTS, NUM_PROJECTS, START_YEAR, END_YEAR, RANDOM_SEED, SIMULATION_DATE
from config.clients import INDUSTRY_CONFIG, CLIENT_PREFIXES, CLIENT_SUFFIXES, CLIENT_SIZE_CONFIG
from config.projects import PROJECT_CATALOG, REGIONS, PROJECT_MANAGERS, STATUS_DISTRIBUTION

## Setting deterministic randomness for reproducability
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

def generate_dates(duration_months=1, start=START_YEAR, end=END_YEAR):
    min_date = datetime.strptime(f"{START_YEAR}-1-1", "%Y-%m-%d")
    max_date = datetime.strptime(f"{END_YEAR}-12-31", "%Y-%m-%d")
    delta_total = max_date - min_date
    random_start_days = random.randint(0, delta_total.days)
    #start_date, end_date = 0, 0
    start_date = min_date + timedelta(days=random_start_days)
    end_date = start_date + relativedelta(months=duration_months)
    return start_date, end_date

def generate_clients(num_clients=NUM_CLIENTS):
    """
    Generate a synthetic client table. 
    Parameters
    ----------
    num_clients : int
        Number of client records to generate. Default is 25 based on variables in general.py.

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
    """
    Generate a synthetic project table. 
    Parameters
    ----------
    num_projects : int
        Number of project records to generate. Default is 200 based on variables in general.py.
    dlients_df : DataFrame
        DataFrame returned from generate_clients function. 

    Returns
    -------
    pandas.DataFrame
        DataFrame contains project IDs, client IDs, industries, project type, original budget, and duration in months.
    """
    data = {
        'project_id': range(1, num_projects + 1),
        'client_id': random.choices(clients_df['client_id'], weights=clients_df['business_scale'], k=num_projects),
    }
    projects_df = pd.DataFrame(data)
    projects_df = projects_df.merge(clients_df[['client_id', 'industry']], on='client_id', how='left')
    project_type_list = list()  #will need to refactor multiple lists into one dictionary when lists become too long. 
    original_budget_list = list()
    duration_months_list = list()
    start_date_list = list()
    end_date_list = list()
    for industry in projects_df['industry']:
        available_templates = PROJECT_CATALOG[industry]
        project_type = random.choice(list(available_templates.keys()))
        original_budget = random.uniform(*available_templates[project_type]['budget_range'])
        duration_months = random.randint(*available_templates[project_type]['duration_months_range'])
        project_type_list.append(project_type)
        original_budget_list.append(original_budget)
        duration_months_list.append(duration_months)
    projects_df['project_type'] = project_type_list
    projects_df['original_budget'] = original_budget_list
    projects_df['duration_months'] = duration_months_list
    for duration in projects_df['duration_months']:
        start_date, end_date = generate_dates(projects_df['duration_months'][duration])
        start_date_list.append(start_date)
        end_date_list.append(end_date)
    projects_df['start_date'], projects_df['end_date'] = start_date_list, end_date_list
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
    print(clients.head())
    projects = generate_projects(num_projects=NUM_PROJECTS, clients_df=clients)
    print(projects.head())
    generate_dates()
#    generate_monthly_costs()
#    generate_change_orders()
#    generate_forecast_history()
#    save_csvs()

main()
