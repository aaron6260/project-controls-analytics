## Configuration file for project controls analytics

NUM_PROJECTS = 200
NUM_CLIENTS = 25

#INDUSTRIES = ['Technology', 'Healthcare', 'Utilities', 'Retail', 'Manufacturing', 'Agriculture', 'Education', 'Transportation', 'Energy', 'Telecommunications']
#INDUSTRY_WEIGHTS = [10,10,15,3,20,1,5,5,30,1] #Probabilities for each industry totaling to 100.
INDUSTRY_CONFIG = {
    "Technology": 10,
    "Healthcare": 10,
    "Utilities": 15,
    "Retail": 3,
    "Manufacturing": 20,
    "Agriculture": 1,
    "Education": 5,
    "Transportation": 5,
    "Energy": 30,
    "Telecommunications": 1
}

CLIENT_PREFIXES = ['Blue', 'Alpha', 'Legacy', 'NextGen', 'Pinnacle', 'Summit', 'Vertex', 'Horizon', 'Apex', 'Zenith']
CLIENT_SUFFIXES = ['Solutions', 'Systems', 'Technologies', 'Enterprises', 'Industries', 'Dynamics', 'Innovations', 'Global', 'Networks', 'Partners']

PROJECT_TYPES = {
    "Energy": [
        "Pipeline Expansion",
        "Substation Upgrade",
        "Solar Farm",
        "Wind Farm",
    ],
    "Technology": [
        "Software Development",
        "IT Infrastructure Upgrade",
        "Data Center Expansion",
        "Cybersecurity Implementation",
    ],
    "Healthcare": [
        "Hospital Renovation",
        "Medical Equipment Installation",
        "Healthcare IT System Upgrade",
        "Pharmaceutical Research Facility",
    ],
    "Utilities": [
        "Water Treatment Plant Upgrade",
        "Electric Grid Modernization",
        "Gas Pipeline Maintenance",
        "Renewable Energy Integration",
    ],
    "Retail": [
        "Store Renovation",
        "E-commerce Platform Development",
        "Supply Chain Optimization",
        "Customer Experience Enhancement",
    ],
    "Manufacturing": [
        "Factory Expansion",
        "Production Line Automation",
        "Quality Control System Implementation",
        "Supply Chain Restructuring",
    ],
    "Agriculture": [
        "Irrigation System Installation",
        "Crop Monitoring Technology Implementation",
        "Farm-to-Table Supply Chain Development",
        "Sustainable Farming Practices Adoption",
    ],
    "Education": [
        "School Renovation",
        "E-learning Platform Development",
        "Curriculum Enhancement",
        "Teacher Training Program Implementation",
    ],
    "Transportation": [
        "Road Expansion",
        "Public Transit System Upgrade",
        "Traffic Management System Implementation",
        "Logistics Optimization",
    ],
    "Telecommunications": [
        "5G Network Deployment",
        "Fiber Optic Cable Installation",
        "Telecom Infrastructure Upgrade",
        "Satellite Communication System Implementation",
    ]
}

PROJECT_CHARACTERISTICS = {
    "Pipeline Expansion": {
        "budget": (50_000_000, 250_000_000),
        "duration_months": (24, 60)
    },
    "Substation Upgrade": {
        "budget": (10_000_000, 50_000_000),
        "duration_months": (12, 36)
    },
    "Solar Farm": {
        "budget": (20_000_000, 100_000_000),
        "duration_months": (18, 48)
    },
    "Wind Farm": {
        "budget": (30_000_000, 150_000_000),
        "duration_months": (24, 60)
    },
    "Software Development": {
        "budget": (500_000, 5_000_000),
        "duration_months": (6, 24)
    },
    "IT Infrastructure Upgrade": {
        "budget": (1_000_000, 10_000_000),
        "duration_months": (6, 18)
    },
    "Data Center Expansion": {
        "budget": (5_000_000, 20_000_000),
        "duration_months": (12, 36)
    },
    "Cybersecurity Implementation": {
        "budget": (250_000, 2_000_000),
        "duration_months": (3, 12)
    },
    "Hospital Renovation": {
        "budget": (10_000_000, 50_000_000),
        "duration_months": (12, 36)
    },
    "Medical Equipment Installation": {
        "budget": (500_000, 5_000_000),
        "duration_months": (6, 18)
    },
    "Healthcare IT System Upgrade": {
        "budget": (1_000_000, 10_000_000),
        "duration_months": (6, 24)
    },
    "Pharmaceutical Research Facility": {
        "budget": (20_000_000, 100_000_000),
        "duration_months": (24, 60)
    },
    "Water Treatment Plant Upgrade": {
        "budget": (5_000_000, 25_000_000),
        "duration_months": (12, 36)
    },
    "Electric Grid Modernization": {
        "budget": (10_000_000, 50_000_000),
        "duration_months": (12, 36)
    },
    "Gas Pipeline Maintenance": {
        "budget": (2_000_000, 10_000_000),
        "duration_months": (6, 18)
    },
    "Renewable Energy Integration": {
        "budget": (5_000_000, 25_000_000),
        "duration_months": (12, 36)
    },
    "Store Renovation": {
        "budget": (500_000, 5_000_000),
        "duration_months": (6, 18)
    },
    "E-commerce Platform Development": {
        "budget": (1_000_000, 10_000_000),
        "duration_months": (6, 24)
    },
    "Supply Chain Optimization": {
        "budget": (250_000, 2_000_000),
        "duration_months": (3, 12)
    },
    "Customer Experience Enhancement": {
        "budget": (100_000, 1_000_000),
        "duration_months": (3, 12)
    },
    "Factory Expansion": {
        "budget": (5_000_000, 25_000_000),
        "duration_months": (12, 36)
    },
    "Production Line Automation": {
        "budget": (1_000_000, 10_000_000),
        "duration_months": (6, 24)
    },
    "Quality Control System Implementation": {
        "budget": (500_000, 5_000_000),
        "duration_months": (6, 18)
    },
    "Supply Chain Restructuring": {
        "budget": (250_000, 2_000_000),
        "duration_months": (3, 12)
    },
    "Irrigation System Installation": {
        "budget": (100_000, 1_000_000),
        "duration_months": (3, 12)
    },
    "Crop Monitoring Technology Implementation": {
        "budget": (50_000, 500_000),
        "duration_months": (3, 12)
    },
    "Farm-to-Table Supply Chain Development": {
        "budget": (250_000, 2_000_000),
        "duration_months": (6, 24)
    },
    "Sustainable Farming Practices Adoption": {
        "budget": (50_000, 500_000),
        "duration_months": (3, 12)
    },
    "School Renovation": {
        "budget": (500_000, 5_000_000),
        "duration_months": (6, 18)
    },
    "E-learning Platform Development": {
        "budget": (250_000, 2_000_000),
        "duration_months": (6, 24)
    },
    "Curriculum Enhancement": {
        "budget": (100_000, 1_000_000),
        "duration_months": (3, 12)
    },
    "Teacher Training Program Implementation": {
        "budget": (50_000, 500_000),
        "duration_months": (3, 12)
    },
    "Road Expansion": {
        "budget": (5_000_000, 25_000_000),
        "duration_months": (12, 36)
    },
    "Public Transit System Upgrade": {
        "budget": (10_000_000, 50_000_000),
        "duration_months": (12, 36)
    },
    "Traffic Management System Implementation": {
        "budget": (1_000_000, 10_000_000),
        "duration_months": (6, 24)
    },
    "Logistics Optimization": {
        "budget": (500_000, 5_000_000),
        "duration_months": (6, 18)
    },
    "5G Network Deployment": {
        "budget": (10_000_000, 50_000_000),
        "duration_months": (12, 36)
    },
    "Fiber Optic Cable Installation": {
        "budget": (5_000_000, 25_000_000),
        "duration_months": (12, 36)
    },
    "Telecom Infrastructure Upgrade": {
        "budget": (1_000_000, 10_000_000),
        "duration_months": (6, 24)
    },
    "Satellite Communication System Implementation": {
        "budget": (5_000_000, 25_000_000),
        "duration_months": (12, 36)
    }
}