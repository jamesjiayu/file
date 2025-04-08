"""
# Lab Files (Chapter 10) 2
# Name: James Wang
# Date: 04/08/2025

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
import re
"""


def read_mileage_file():
    filename = "WangJ_file_mileage.txt"
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        # print(lines)#['03/07/2025\t175.3\t9.718\t$40.70\n', '03/08/2025\t157.1\t7.766\t$17.34\n', ...]
        print("Date       Trip  Gallons Cost  $/G  Mileage")
        print("=============================================")
        for line in lines:
            fields = line.strip().split("\t")
            # print(fields) #['03/07/2025', '175.3', '9.718', '$40.70']
            date = fields[0]
            trip = float(fields[1])
            gallons = float(fields[2])
            cost_str = fields[3]
            cost = float(cost_str.replace("$", ""))
            # cost = float(re.sub(r'[$,]', '', cost_str))
            # if gallons checks if the value of the gallons variable is not zero.
            # If the condition gallons is False (meaning gallons is 0), the expression evaluates to 0
            cost_per_gallon = cost / gallons if gallons else 0

            mileage = trip / gallons if gallons else 0
            # print(cost_per_gallon, mileage)
            print(
                f"{date} {trip:.1f} {gallons:.3f} {cost_str} ${cost_per_gallon:.2f} {mileage:.2f}"
            )
        print("===============================================")
    except Exception as e:
        print(f"Error: {e}")


read_mileage_file()
