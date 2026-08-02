# Architecture Overview
This document serves as a critical, living template designed to equip agents with a rapid and comprehensive understanding of the codebase's architecture, enabling efficient navigation and effective contribution from day one. Update this document as the codebase evolves.

## 1. Project Structure
Project Root/
|- data/
|   |- raw/
|   |   |- processed/
|   |   |   |- clean-data
|- docs/
|   |- architecure.md
|   |- data_dictionary.md
|   |- project_scope.md
|- notebooks/
|   |- 01_data_exploration.ipynb
|   |- 02_cleaning.ipynb
|   |- 03_analysis.ipynb
|- reports/
|- src/
|   |- config/
|   |   |- clients.py               # Includes information needed to generate a list of simulated clients 
|   |   |- general.py               # Specifies general information for simulated data
|   |   |- projects.py              # Specifies data needed to generate projects. Includes a catalog of projects, regions, and project managers 
|   |- cleaning.py
|   |- generate_data.py
|   |- metrics.py
|   |- visualizations.py 
|- tests/                           # Folder for tests and practice files              
|- .gitignore                       # Speciifies intentionally ugracked files to ignore
|- LICENSE                          
|- README.md                        # Project Overview and quick start guide
|- requirements.txt                 # Necessary Python libraries

## 2. High-Level System Diagram 
### generate_data.py 
Clients
    │
    ▼
Project Dates
    │
    ▼
Projects
    │
    ▼
Project Timeline
    │
    ▼
Apply Burn Curve
    │
    ▼
Calculate Planned Costs
    │
    ▼
Simulate Actual Costs
    │
    ▼
Calculate Cumulative Costs
    │
    ▼
Monthly Cost Table