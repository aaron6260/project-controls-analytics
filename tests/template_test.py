# Practicing a template to pull project type, budget, duration. 

PROJECT_CATALOG = {
    "Energy": {
        "Pipeline Expansion":{
            "budget": (50_000_000, 250_000_000),
            "duration_months": (24, 60)
        },
        "Substation Upgrade":{
            "budget": (10_000_000, 50_000_000),
            "duration_months": (12, 36)
        },
        "Solar Farm":{
            "budget": (20_000_000, 100_000_000),
            "duration_months": (18, 48)
        },
        "Wind Farm":{
            "budget": (30_000_000, 150_000_000),
            "duration_months": (24, 60)
        }
    },
    "Technology": {
        "Software Development":{
            "budget": (500_000, 5_000_000),
            "duration_months": (6, 24)
        },
        "IT Infrastructure Upgrade":{
            "budget": (1_000_000, 10_000_000),
            "duration_months": (6, 18)
        },
        "Data Center Expansion":{
            "budget": (5_000_000, 20_000_000),
            "duration_months": (12, 36)
        },
        "Cybersecurity Implementation":{
            "budget": (250_000, 2_000_000),
            "duration_months": (3, 12)
        }
    },
    "Healthcare": {
        "Hospital Renovation":{
            "budget": (10_000_000, 50_000_000),
            "duration_months": (12, 36)
        },
        "Medical Equipment Installation":{
            "budget": (500_000, 5_000_000),
            "duration_months": (6, 18)
        },
        "Healthcare IT System Upgrade":{
            "budget": (1_000_000, 10_000_000),
            "duration_months": (6, 24)
        },
        "Pharmaceutical Research Facility":{
            "budget": (20_000_000, 100_000_000),
            "duration_months": (24, 60)
        }
    },
    "Utilities": {
        "Water Treatment Plant Upgrade":{
            "budget": (5_000_000, 25_000_000),
            "duration_months": (12, 36)
        },
        "Electric Grid Modernization":{
            "budget": (10_000_000, 50_000_000),
            "duration_months": (12, 36)
        },
        "Gas Pipeline Maintenance":{
            "budget": (2_000_000, 10_000_000),
            "duration_months": (6, 18)
        },
        "Renewable Energy Integration":{
            "budget": (5_000_000, 25_000_000),
            "duration_months": (12, 36)
        }
    },
    "Retail": {
        "Store Renovation":{
            "budget": (500_000, 5_000_000),
            "duration_months": (6, 18)
        },
        "E-commerce Platform Development":{
            "budget": (1_000_000, 10_000_000),
            "duration_months": (6, 24)
        },
        "Supply Chain Optimization":{
            "budget": (250_000, 2_000_000),
            "duration_months": (3, 12)
        },
        "Customer Experience Enhancement":{
            "budget": (100_000, 1_000_000),
            "duration_months": (3, 12)
        }
    },
    "Manufacturing": {
        "Factory Expansion":{
            "budget": (5_000_000, 25_000_000),
            "duration_months": (12, 36)
        },
        "Production Line Automation":{
            "budget": (1_000_000, 10_000_000),
            "duration_months": (6, 24)
        },
        "Quality Control System Implementation":{
            "budget": (500_000, 5_000_000),
            "duration_months": (6, 18)
        },
        "Supply Chain Restructuring":{
            "budget": (250_000, 2_000_000),
            "duration_months": (3, 12)
        }
    },
    "Agriculture": {
        "Irrigation System Installation":{
            "budget": (100_000, 1_000_000),
            "duration_months": (3, 12)
        },
        "Crop Monitoring Technology Implementation":{
            "budget": (50_000, 500_000),
            "duration_months": (3, 12)
        },
        "Farm-to-Table Supply Chain Development":{
            "budget": (250_000, 2_000_000),
            "duration_months": (6, 24)
        },
        "Sustainable Farming Practices Adoption":{
            "budget": (50_000, 500_000),
            "duration_months": (3, 12)
        }
    },
    "Education": {
        "School Renovation":{
            "budget": (500_000, 5_000_000),
            "duration_months": (6, 18)
        },
        "E-learning Platform Development":{
            "budget": (250_000, 2_000_000),
            "duration_months": (6, 24)
        },
        "Curriculum Enhancement":{
            "budget": (100_000, 1_000_000),
            "duration_months": (3, 12)
        },
        "Teacher Training Program Implementation":{
            "budget": (50_000, 500_000),
            "duration_months": (3, 12)
        }
    },
    "Transportation": {
        "Road Expansion":{
            "budget": (5_000_000, 25_000_000),
            "duration_months": (12, 36)
        },
        "Public Transit System Upgrade":{
            "budget": (10_000_000, 50_000_000),
            "duration_months": (12, 36)
        },
        "Traffic Management System Implementation":{
            "budget": (1_000_000, 10_000_000),
            "duration_months": (6, 24)
        },
        "Logistics Optimization":{
            "budget": (500_000, 5_000_000),
            "duration_months": (6, 18)
        }
    },
    "Telecommunications": {
        "5G Network Deployment":{
            "budget": (10_000_000, 50_000_000),
            "duration_months": (12, 36)
        },
        "Fiber Optic Cable Installation":{
            "budget": (5_000_000, 25_000_000),
            "duration_months": (12, 36)
        },
        "Telecom Infrastructure Upgrade":{
            "budget": (1_000_000, 10_000_000),
            "duration_months": (6, 24)
        },
        "Satellite Communication System Implementation":{
            "budget": (5_000_000, 25_000_000),
            "duration_months": (12, 36)
        }
    }
}

import random

industry = "Energy" #assume this is given. How would you pull the project type? 

energy_type = PROJECT_CATALOG[industry]
sub_project = random.choice(list(energy_type))
sub_project_budget_range = energy_type[sub_project]['budget']
sub_project_budget = random.uniform(*sub_project_budget_range)
project_type = random.choice(list(PROJECT_CATALOG[industry]))

#print(project_type)
#print(energy_type.keys()) # dict_keys object. 
#random.choice(project_type.items()) # random.choice can't take dict_items/keys/etc. type. It needs to be a sequence. 
#print(random.choice(list(energy_type.keys())))
print(energy_type)
print(sub_project)
print(sub_project_budget_range)
print(sub_project_budget)
#print(project_type)
# Possible output: "Solar Farm"

## When needing to refactor multiple lists into one dictionary. 
#projects = {
#    'project_type': project_type
#    'budget': budget
#    'duration': duration
#}
#projects.append(project)