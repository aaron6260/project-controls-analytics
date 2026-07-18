# Configuration file for project catalog. 

REGIONS = {
    "West": [
        "California",
        "Oregon",
        "Washington",
        "Nevada",
        "Arizona",
    ],
    "Southwest": [
        "New Mexico",
        "Texas",
        "Oklahoma",
    ],
    "Midwest": [
        "Illinois",
        "Indiana",
        "Ohio",
        "Michigan",
        "Wisconsin",
    ],
    "Southeast": [
        "Florida",
        "Georgia",
        "North Carolina",
        "South Carolina",
    ],
    "Northeast": [
        "New York",
        "Massachusetts",
        "Pennsylvania",
        "New Jersey",
    ],
}

STATUS_DISTRIBUTION = {
    "Planning": 0.05,
    "Active": 0.35,
    "Complete": 0.55,
    "On Hold": 0.05,
}

PROJECT_MANAGERS = {
    "Alice Johnson": 1.0,
    "Michael Chen": 2.0,
    "Sarah Martinez": 0.8,
    "David Wilson": 1.5,
    "Emily Davis": 1.2,
    "James Brown": 1.0,
    "Olivia Taylor": 1.3,
    "William Anderson": 0.9,
    "Sophia Thomas": 1.4,
    "Benjamin Lee": 1.1,
    "Mia Harris": 1.0,
    "Ethan Clark": 1.2,
    "Ava Lewis": 1.3,
    "Alexander Walker": 1.0,
    "Isabella Hall": 1.5,
    "Daniel Allen": 1.1,
    "Charlotte Young": 1.2,
    "Matthew King": 0.8,
    "Amelia Wright": 1.4,
    "Joseph Scott": 1.3,
    "Harper Green": 1.0,
    "Samuel Adams": 1.2,
    "Ella Baker": 1.1,
    "David Nelson": 1.0,
    "Grace Carter": 1.3,
    "Lucas Mitchell": 1.2,
    "Chloe Perez": 1.0,
    "Andrew Roberts": 1.4,
    "Lily Turner": 1.1,
    "Ryan Phillips": 1.0,
    "Zoe Campbell": 1.3,
    "Nathan Parker": 1.2,
    "Hannah Evans": 2.0,
    "Caleb Edwards": 1.4,
    "Avery Collins": 1.1,
}

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

