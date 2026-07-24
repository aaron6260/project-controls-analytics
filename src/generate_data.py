## This script generates synthetic data for clients, projects, monthly costs, change orders, and forecast history. The generated data is saved as CSV files for further analysis or testing purposes.

## Adding necessary imports
import random 
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from tkinter.font import names

import numpy as np
import pandas as pd

from config.general import NUM_CLIENTS, NUM_PROJECTS, START_YEAR, RANDOM_SEED, SIMULATION_DATE, PLANNING_HORIZON_MONTHS
from config.clients import INDUSTRY_CONFIG, CLIENT_PREFIXES, CLIENT_SUFFIXES, CLIENT_SIZE_CONFIG
from config.projects import PROJECT_CATALOG, REGIONS, PROJECT_MANAGERS

## Setting deterministic randomness for reproducability
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

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
        # probabilistically assign industries and client sizes to client ids. 
        'industry': random.choices(list(INDUSTRY_CONFIG.keys()), weights=[v['weight'] for v in INDUSTRY_CONFIG.values()], k=num_clients),
        'client_size': random.choices(list(CLIENT_SIZE_CONFIG.keys()), weights=[v['probability'] for v in CLIENT_SIZE_CONFIG.values()], k=num_clients),
    }
    clients_df = pd.DataFrame(data)
    # assign a business scaling factor for each client to be used later based on their size.
    clients_df['business_scale'] = clients_df.apply(lambda row: random.uniform(*CLIENT_SIZE_CONFIG[row['client_size']]['business_scale_range']), axis=1)
    # ------------ Validation ------------
    assert len(clients_df) == num_clients
    return clients_df

def generate_project_dates(duration_months=1):
    """
    Generate random start and end dates.
    Parameters
    ----------
    duration_months = int
        duration of project. Used to calculate end date. 
    
    Returns
    -------
    start_date, end_date
        date tuple for random start date and finish date based on duration length. 

    """
    min_date = datetime.strptime(f"{START_YEAR}-1-1", "%Y-%m-%d")
    max_date = SIMULATION_DATE + relativedelta(months=PLANNING_HORIZON_MONTHS) #Updated to have future planned projects
    delta_total = max_date - min_date
    random_start_days = random.randint(0, delta_total.days)
    start_date = min_date + timedelta(days=random_start_days)
    end_date = start_date + relativedelta(months=duration_months)
    return start_date.date(), end_date.date()

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
        DataFrame contains project IDs, client IDs, industries, project type, original budget, duration in months, start_date, end_date, status
    """
    data = {
        'project_id': range(1, num_projects + 1),
        # Probabilistically assign projects to clients. Larger clients are more likely to receive projects. 
        'client_id': random.choices(clients_df['client_id'], weights=clients_df['business_scale'], k=num_projects),
    }
    projects_df = pd.DataFrame(data)
    projects_df = projects_df.merge(clients_df[['client_id', 'industry']], on='client_id', how='left')
    project_type_list = []  #will need to refactor multiple lists into one dictionary when it makes sense. 
    original_budget_list = []
    duration_months_list = []
    start_date_list = []
    end_date_list = []
    status_list = []
    region_list = []
    state_list = []
    # Generate a project and add to project_df. 
    # Assign a random template to each project based on the industry of the client and derive needed values for DataFrame. 
    for industry in projects_df['industry']:
        available_templates = PROJECT_CATALOG[industry]
        project_type = random.choice(list(available_templates.keys()))
        original_budget = random.uniform(*available_templates[project_type]['budget_range'])
        duration_months = random.randint(*available_templates[project_type]['duration_months_range'])
        project_type_list.append(project_type)
        original_budget_list.append(original_budget)
        duration_months_list.append(duration_months)
        start_date, end_date = generate_project_dates(duration_months)
        start_date_list.append(start_date)
        end_date_list.append(end_date)
        if start_date > SIMULATION_DATE.date():
            status_list.append('Planned')
        elif end_date <= SIMULATION_DATE.date():
            status_list.append('Completed')
        else:
            status_list.append('Active')
        project_region = random.choice(list(REGIONS.keys()))
        project_state = random.choice(list(REGIONS[project_region]))
        region_list.append(project_region)
        state_list.append(project_state)
    projects_df['project_type'] = project_type_list
    projects_df['original_budget'] = original_budget_list
    projects_df['duration_months'] = duration_months_list
    projects_df['start_date'], projects_df['end_date'] = start_date_list, end_date_list
    projects_df['status'] = status_list
    projects_df['region'] = region_list
    projects_df['state'] = state_list
    # ------------ Validation ------------
    assert projects_df['client_id'].isin(clients_df['client_id']).all()
    assert len(projects_df) == num_projects
    assert (projects_df['end_date'] >= projects_df['start_date']).all()
    assert projects_df['duration_months'].between(3, 60).all()
    return projects_df

def generate_project_timeline(project_row):
    """
    Generate the monthly reporting timeline for a single project.

    Required project fields:
        - project_id
        - start_date
        - duration_months
    """
    #assert project_row['project_id'] is not []
    project_id = project_row['project_id']
    start_date = project_row['start_date']
    duration_months = project_row['duration_months']
    reporting_month = start_date
    month_number = 1
    timeline_records = {
        'project_id': [],
        'reporting_month': [],
        'month_number': [],
        'duration_months': [],
        'planned_progress': []
    }
    for month_number in range(1, duration_months+1):
        reporting_month = start_date + relativedelta(months=month_number)
        project_progress = month_number/duration_months
        timeline_records['project_id'].append(project_id)
        timeline_records['reporting_month'].append(reporting_month)
        timeline_records['month_number'].append(month_number)
        timeline_records['duration_months'].append(duration_months)
        timeline_records['planned_progress'].append(project_progress)
    timeline_df = pd.DataFrame(timeline_records)
    return timeline_df

def generate_monthly_costs(project_df=None, cost_var=0.10):
    assert not project_df['project_id'].empty
    assert not project_df['duration_months'].empty
    project_ids = []
    for project in project_df['project_id']:
            temp_date = project_df['start_date']

    pass

def generate_change_orders():
    pass

def generate_forecast_history():
    pass

def save_csvs():
    pass

def main():
    #clients = generate_clients(num_clients=NUM_CLIENTS)
    #print(clients.head())
    #projects = generate_projects(num_projects=NUM_PROJECTS, clients_df=clients)
    #print(projects.head())
    project = pd.Series({
    'project_id': 'P001',
    'start_date': pd.Timestamp('2025-01-01'),
    'duration_months': 6
    })

    timeline = generate_project_timeline(project)
    print(timeline)
    assert len(timeline) == 6
    assert timeline['month_number'].iloc[-1] == 6
#    generate_monthly_costs()
#    generate_change_orders()
#    generate_forecast_history()
#    save_csvs()

main()
