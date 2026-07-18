import pandas as pd
import numpy as np
from config import RAW_DATA

facility_types = pd.read_csv(RAW_DATA / "facility_types.csv")
governorates = pd.read_csv(RAW_DATA / "governorates.csv")
districts = pd.read_csv(RAW_DATA / "districts.csv")

facilities = []
num_facilities = 120

for i in range(num_facilities):

    facility_type_id = np.random.choice(
        facility_types["facility_type_id"],
        p=[0.10, 0.51, 0.20, 0.10, 0.05, 0.04]
    )

    facility_type = facility_types.loc[
        facility_types["facility_type_id"] == facility_type_id,
        "facility_type"
    ].iloc[0]
    governorate_id = np.random.choice(
        governorates["governorate_id"],
        p=[0.20, 0.05, 0.02, 0.03, 0.10, 0.10, 0.025, 0.30, 0.025, 0.03, 0.02, 0.05, 0.04, 0.01]
    )

    governorate = governorates.loc[
        governorates["governorate_id"] == governorate_id,
        "governorate"
    ].iloc[0]

    districts_in_governorate = districts[
        districts["governorate_id"] == governorate_id
    ]

    district_id = np.random.choice(
        districts_in_governorate["district_id"]
    )

    district = districts_in_governorate.loc[
        districts_in_governorate["district_id"] == district_id,
        "district"
    ].iloc[0]

    facility_prefix = {
    "Hospital": "General Hospital",
    "Primary Health Center (PHC)": "PHC",
    "Nutrition Center": "NC",
    "Rehabilitation Center": "RC",
    "Maternity Center": "MC",
    "Mobile Clinic": "MC"
    }
    facility_name = f"{district} {facility_prefix[facility_type]} {i+1:03d}"

    # if facility_type == "Hospital":
#         facility_name = f"{district} General Hospital {i+1:03d}"
#     elif facility_type == "Primary Health Center (PHC)":
#         facility_name = f"{district} PHC {i+1:03d}"
#     elif facility_type == "Nutrition Center":
#         facility_name = f"{district} NC {i+1:03d}"
#     elif facility_type == "Rehabilitation Center":
#         facility_name = f"{district} RH {i+1:03d}"
#     elif facility_type == "Maternity Center":
#         facility_name = f"{district} MH {i+1:03d}"
#     elif facility_type == "Mobile Clinic":
#         facility_name = f"{district} MC {i+1:03d}"
#     else :  
#         facility_name == "HC none"
    latitude = districts.loc[districts["district_id"] == district_id, "latitude"].iloc[0]

    longitude= districts.loc[districts["district_id"] == district_id, "longitude"].iloc[0]

    opening_date = np.random.choice(
        pd.date_range("1930-01-01","2010-12-31"),
    )

    ownership = np.random.choice(
    ["Ministry of Health", "NGO", "Private", "UN Agency"],
        p = [0.4,0.1,0.3,0.2]
    )

    operational_status = np.random.choice(
        ["Active", "Suspended", "Closed"],
        p=[0.8,0.15,0.05]
    )

    facility = {
        "facility_id": f"fac{i + 1:03d}",
        "facility_type_id": facility_type_id,
        "facility_type": facility_type,
        "facility": facility_name,
        "governorate_id": governorate_id,
        "governorate": governorate,
        "district_id": district_id,
        "district": district,
        "latitude": latitude,
        "longitude": longitude,
        "opening_date": opening_date,
        "ownership": ownership,
        "operational_status": operational_status
    }

    facilities.append(facility)

facilities = pd.DataFrame(facilities)

facilities.to_csv(RAW_DATA / "facilities.csv", index=False)

print(facilities)




 