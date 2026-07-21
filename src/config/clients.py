# Configuration file for clients.

# Assigning weights to different industries to adjust probabilities.
INDUSTRY_CONFIG = {
    "Technology": {"weight": 10},
    "Healthcare": {"weight": 10},
    "Utilities": {"weight": 15},
    "Retail": {"weight": 3},
    "Manufacturing": {"weight": 20},
    "Agriculture": {"weight": 1},
    "Education": {"weight": 5},
    "Transportation": {"weight": 5},
    "Energy": {"weight": 30},
    "Telecommunications": {"weight": 1}
}

CLIENT_PREFIXES = ['Blue', 'Alpha', 'Legacy', 'NextGen', 'Pinnacle', 'Summit', 'Vertex', 'Horizon', 'Apex', 'Zenith']
CLIENT_SUFFIXES = ['Solutions', 'Systems', 'Technologies', 'Enterprises', 'Industries', 'Dynamics', 'Innovations', 'Global', 'Networks', 'Partners']

# Creates probabilistic assignment option for client size. 
CLIENT_SIZE_CONFIG = {
    "Small": {
        "business_scale_range": (0.5, 0.9),
        "probability": .45
    },
    "Medium": {
        "business_scale_range": (1.0, 1.8),
        "probability": .30
    },
    "Large": {
        "business_scale_range": (2.0, 3.2),
        "probability": .18
    },
    "Enterprise": {
        "business_scale_range": (3.5, 5.0),
        "probability": 0.07
    }
}