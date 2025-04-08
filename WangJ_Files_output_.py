"""
# Lab Files (Chapter 10) 2
# Name: James Wang
# Date: 04/07/2025

data =[
    {
        "date": "5/2/2008",
        "trip": 293.7,
        "gallons": 17.931,
        "cost": "$62.02"
    },
        {
        "date": "/12/2008",
        "trip": 293.1,
        "gallons": 12.931,
        "cost": "$64.12"
    }
]
"""

def read_mileage_file():
    filename = "WangJ_file_mileage.txt"
    try:
        with open(filename, "r") as f:
            