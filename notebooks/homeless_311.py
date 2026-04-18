import pandas as pd

homeless_df = pd.read_csv("../data/311_Service_Requests_from_2020_to_Present_20260418.csv",
dtype = {"Incident Zip":"str", "Unique Key":"str"},
parse_dates=['Created Date', 'Closed Date'])

homeless_df["year_created"] = pd.to_datetime(homeless_df["Created Date"]).dt.year
#homeless_df["year_created"] = homeless_df["year_created"].astype('str')

homeless_df["month_created"] = pd.to_datetime(homeless_df["Created Date"]).dt.month
#homeless_df["month_created "] = homeless_df["month_created"].astype('str')

homeless_df["year_closed"] = pd.to_datetime(homeless_df["Closed Date"]).dt.year
#homeless_df["year_closed"] = homeless_df["year_closed"].astype('str')

homeless_df["month_closed"] = pd.to_datetime(homeless_df["Closed Date"]).dt.month
#homeless_df["month_closed"] = homeless_df["month_closed"].astype('str')

encampments = pd.read_csv("../data/311_Homeless_2020_to_Present_20260415.csv",
dtype = {"Incident Zip":"str", "Unique Key":"str", "Problem Detail (formerly Descriptor)":"str"},
parse_dates=['Created Date', 'Closed Date'])

encampments["year_created"] = pd.to_datetime(encampments["Created Date"]).dt.year
#homeless_df["year_created"] = homeless_df["year_created"].astype('str')

encampments["month_created"] = pd.to_datetime(encampments["Created Date"]).dt.month
#homeless_df["month_created "] = homeless_df["month_created"].astype('str')

encampments["year_closed"] = pd.to_datetime(encampments["Closed Date"]).dt.year
#homeless_df["year_closed"] = homeless_df["year_closed"].astype('str')

encampments["month_closed"] = pd.to_datetime(encampments["Closed Date"]).dt.month
#homeless_df["month_closed"] = homeless_df["month_closed"].astype('str')

encampments_only = encampments[encampments["Problem (formerly Complaint Type)"].str.contains("Encampment")]

h_df = homeless_df[["Unique Key", "year_created", "month_created", "year_closed", "month_closed", "Agency", "Incident Zip",
"Problem (formerly Complaint Type)", "Problem Detail (formerly Descriptor)",
"Location Type", "Facility Type", "Borough"
]]

year_table_all = h_df.groupby(
    ["year_closed", "month_closed"]
    ).agg(
        {
            "Unique Key":"count"
        }
    ).sort_values(
        by= ["year_closed", "month_closed"],
        ascending=True
    )

year_table_all.to_csv("../output/311_calls_by_month.csv")

