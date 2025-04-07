"""
# Lab Files (Chapter 10)
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

import datetime as dt
import random


def generate_mileage_data(num_rows=5):
    # Generates a list of dictionaries representing car mileage data
    data = []
    start_date = dt.date(2025, 3, 7)
    for i in range(num_rows):
        trip_date = start_date + dt.timedelta(days=i)
        # uniform() get a random number between 2 numbers
        trip_mileage = round(random.uniform(100, 200), 1)
        gallons = round(trip_mileage / random.uniform(15, 25), 3)
        cost = round(gallons * random.uniform(2.0, 4.5), 2)
        data.append(
            {
                "date": trip_date.strftime("%m/%d/%Y"),
                "trip": trip_mileage,
                "gallons": gallons,
                "cost": f"${cost:.2f}",
            }
        )
    return data


def write_mileage_to_file(data, filename):
    try:
        with open(filename, "w") as f:
            for row in data:
                f.write(f"{row.get('date')}\t\t")
                f.write(f"{row.get('trip')}\t\t")
                f.write(f"{row.get('gallons')}\t\t")
                f.write(f"{row.get('cost')}\n")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    data = generate_mileage_data(6)
    filename = "WangJ_file_mileage.txt"
    write_mileage_to_file(data, filename)
