## This script generates synthetic data for clients, projects, monthly costs, change orders, and forecast history. The generated data is saved as CSV files for further analysis or testing purposes.

## Adding necessary imports
import random 
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import numpy as np
import pandas as pd
from scipy import stats

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
        DataFrame contains project information from a template. 
        project IDs, client IDs, industries, project type, original budget, duration in months, proj start date, proj end date, status, region, state
    """
    data = {
        'project_id': range(1, num_projects + 1),
        # Probabilistically assign projects to clients. Larger clients are more likely to receive projects. 
        'client_id': random.choices(clients_df['client_id'], weights=clients_df['business_scale'], k=num_projects),
    }
    projects_df = pd.DataFrame(data)
    projects_df = projects_df.merge(clients_df[['client_id', 'industry']], on='client_id', how='left')
    project_data = {
        'project_types': [],  
        'original_budgets': [],
        'duration_months': [],
        'start_dates': [],
        'end_dates': [],
        'status': [],
        'regions': [],
        'states': []
    }
    # Generate a project and add to project_df. 
    # Assign a random template to each project based on the industry of the client and derive needed values for DataFrame. 
    for industry in projects_df['industry']:
        available_templates = PROJECT_CATALOG[industry]
        project_type = random.choice(list(available_templates.keys()))
        original_budget = random.uniform(*available_templates[project_type]['budget_range'])
        duration_months = random.randint(*available_templates[project_type]['duration_months_range'])
        project_data['project_types'].append(project_type)
        project_data['original_budgets'].append(original_budget)
        project_data['duration_months'].append(duration_months)
        start_date, end_date = generate_project_dates(duration_months)
        project_data['start_dates'].append(start_date)
        project_data['end_dates'].append(end_date)
        if start_date > SIMULATION_DATE.date():
            project_data['status'].append('Planned')
        elif end_date <= SIMULATION_DATE.date():
            project_data['status'].append('Completed')
        else:
            project_data['status'].append('Active')
        project_region = random.choice(list(REGIONS.keys()))
        project_state = random.choice(list(REGIONS[project_region]))
        project_data['regions'].append(project_region)
        project_data['states'].append(project_state)
    projects_df['project_type'] = project_data['project_types']
    projects_df['original_budget'] = project_data['original_budgets']
    projects_df['duration_months'] = project_data['duration_months']
    projects_df['start_date'], projects_df['end_date'] = project_data['start_dates'], project_data['end_dates']
    projects_df['status'] = project_data['status']
    projects_df['region'] = project_data['regions']
    projects_df['state'] = project_data['states']
    # ------------ Validation ------------
    assert projects_df['client_id'].isin(clients_df['client_id']).all()
    assert len(projects_df) == num_projects
    assert (projects_df['end_date'] >= projects_df['start_date']).all()
    assert projects_df['duration_months'].between(3, 60).all()
    return projects_df

def generate_project_timeline(project_row):
    """
    Generate the monthly reporting timeline for a single project.
    Parameters
    ----------
    project_row: pd.Series or one row of a pd.DataFrame 
        One row from project_df.
    Required project fields:
        - project_id
        - start_date
        - duration_months
    
    Returns
    -------
    pandas.DataFrame
        Dataframe with project timeline information for a single project ID. 
        Project ID, reporting month, month number, duration months, planned progress.
    """
    # Sanity check of data input. 
    assert pd.notna(project_row['project_id'])
    assert pd.notna(project_row['start_date'])
    assert project_row['duration_months'] > 0

    # Create variables from inputs. 
    project_id = project_row['project_id']
    start_date = project_row['start_date']
    normalized_start_month = pd.Timestamp(f'{start_date.year}-{start_date.month}-1')    # Normalize date to beginning of month for reporting periods. 
    duration_months = project_row['duration_months']
    # Timeline dictionary for monthly records. 
    timeline_records = {
        'project_id': [],
        'reporting_month': [],
        'month_number': [],
        'duration_months': [],
        'planned_progress': []
    }
    # Generate timeline for a single project. Iterate through each month in the project. 
    for month_number in range(1, duration_months+1):
        reporting_month = normalized_start_month + relativedelta(months=month_number)
        planned_progress = month_number/duration_months
        timeline_records['project_id'].append(project_id)
        timeline_records['reporting_month'].append(reporting_month)
        timeline_records['month_number'].append(month_number)
        timeline_records['duration_months'].append(duration_months)
        timeline_records['planned_progress'].append(planned_progress)
    timeline_df = pd.DataFrame(timeline_records)
    return timeline_df

def apply_planned_burn_curve(timeline_df):  #TODO: add ability to do different burn curves (e.g. standard, front loaded, back loaded, etc.)
    """
    Apply a project burn curve for a single project.
    Parameters
    ----------
    timeline_df: pd.DataFrame of project timeline. 
        DataFrame of a single projects monthly timeline. 
    Required project fields:
        - planned_progress
    
    Returns
    -------
    pandas.DataFrame
        Dataframe with project timeline and burn curve weights added. 
        Project ID, reporting month, month number, duration months, planned progress, burn weights.
    """
    # Sanity check of data input. 
    #assert pd.notna(timeline_df['planned_progress'])

    planned_progress = timeline_df['planned_progress']
    mu = 0.5  # mean (average)
    sigma = 0.15   # standard deviation
    burn_curve = stats.norm.pdf(planned_progress, mu, sigma)
    burn_weights = burn_curve / burn_curve.sum()
    timeline_df['burn_weights'] = burn_weights
    return timeline_df

def simulate_actual_costs(timeline_df, cost_var=0.10, simulation_date=SIMULATION_DATE):       #TODO: add total project variance along with monthly noise. This creates a more realistic swing for costs. 
    """
    Simulate actual costs for a single project.
    Parameters
    ----------
    timeline_df: pd.DataFrame of project timeline. 
        DataFrame of monthly costs for single project with burn weigthts applied.
    cost_var: decimal
        Decimal for total cost variance on a project. Default 10%.
    simulation_date: date
        Date of the simulation, default using global SIMULATION_DATE from general.py
    
    Required project fields:
        - reporting_month
        - planned_cost
    
    Returns
    -------
    pandas.DataFrame
        Dataframe with project timeline information for a single project ID. 
        Project ID, reporting month, month number, duration months, planned progress, burn weights, planned cost, actual_cost
    """
    # Sanity check of data input
    #assert pd.notna(timeline_df['reporting_month'])
    #assert pd.notna(timeline_df['planned_cost'])

    actual_costs = []
    row_num = 0
    for reporting_month in timeline_df['reporting_month']:
        planned_cost = timeline_df['planned_cost'][row_num]
        if reporting_month <= simulation_date:
            actual_cost = planned_cost * (random.uniform(0, 2)*cost_var-cost_var+1)
            actual_costs.append(actual_cost)
        else:
            actual_costs.append(0)
        row_num += 1
    timeline_df['actual_cost'] = actual_costs
    return timeline_df

def calculate_cumulative_costs(timeline_df):
    """
    Calculate cumulative costs for a single project.
    Parameters
    ----------
    timeline_df: pd.DataFrame of project timeline. 
        DataFrame of monthly costs for single project with burn weigthts applied.
    Required project fields:
        - planned_cost
        - actual_cost

    Returns
    -------
    pandas.DataFrame
        Dataframe with project timeline information for a single project ID. 
        Project ID, reporting month, month number, duration months, planned progress, burn weights, planned cost, actual_cost, cumulative planned cost, cumulative actual cost
    """
    # Sanity check of data input
    #assert pd.notna(timeline_df['actual_cost'])
    #assert pd.notna(timeline_df['planned_cost'])
    
    timeline_df['cumulative_planned_cost'] = timeline_df['planned_cost'].cumsum()
    timeline_df['cumulative_actual_cost'] = timeline_df['actual_cost'].cumsum()
    return timeline_df

def generate_monthly_costs(project_df): 
    """
    Generate total monthly costs for a single project.
    Parameters
    ----------
    project_df: one row from a pd.DataFrame for a single project. 
        One row from a DataFrame with all project information for a single project.
    Required project fields:
        - project_id
        - duration_months
        - original_budget

    Returns
    -------
    pandas.DataFrame
        Dataframe with project timeline information for a single project ID. 
        Project ID, reporting month, month number, duration months, planned progress, burn weights, planned cost, actual_cost, cumulative planned cost, cumulative actual cost
    """
    # Sanity check of data input
    #assert pd.notna(project_df['project_id'])
    #assert pd.notna(project_df['duration_months'])
    #assert pd.notna(project_df['original_budget'])

    monthly_cost_tables = []
    for row in range(len(project_df['project_id'])):
        timeline = generate_project_timeline(project_df.iloc[row])
        #assert len(timeline) == project_df['duration_months'].max   # check timeline DataFrame generated correctly from project data. 
        #assert timeline['month_number'].iloc[-1] == project_df['duration_months'].max
        timeline = apply_planned_burn_curve(timeline_df=timeline)
        timeline['planned_cost'] = project_df['original_budget'][0] * timeline['burn_weights']
        timeline_actual_cost = simulate_actual_costs(timeline_df=timeline)
        timeline_cumulative_cost = calculate_cumulative_costs(timeline_df=timeline_actual_cost)
        monthly_cost_tables.append(timeline_cumulative_cost)
    monthly_costs_df = pd.concat(monthly_cost_tables, ignore_index=True)
    return monthly_costs_df

def generate_change_orders():
    pass

def generate_forecast_history():
    pass

def save_csvs():
    pass

def main():
    clients = generate_clients(num_clients=NUM_CLIENTS)
    projects = generate_projects(num_projects=NUM_PROJECTS, clients_df=clients)
    monthly_costs = generate_monthly_costs(project_df=projects)
    print(monthly_costs.head())
#    generate_change_orders()
#    generate_forecast_history()
#    save_csvs()

main()