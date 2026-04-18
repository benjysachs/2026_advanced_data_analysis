# Analysis of 311 calls about homeless individuals

This repository contains data, analytic code, and findings that support portions of the article, “[11 Calls About Homelessness Nearly Triple from Last April](tk.com),” published Month Date, Year. Please read that article, which contains important context and details, before proceeding.

## Data

This analysis uses one dataset.

The spreadsheets come from the following sources:

- Name of source:
  - `311_Service_Requests_from_2020_to_Present_20260418.csv`: Raw data of calls to 311 about homeless individuals from 2020 to the present: https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2020-to-Present/erm2-nwe9/about_data. (I filtered this to "Problems" that contain "Homeless."

Each of the spreadsheets contain, among others, the following columns relevant to the analysis:

- `year_closed` — The year the 311 call was responded to.
- `month_closed` — The month the 311 call was responded to.
- `Problem (formerly Complaint Type)` — The category of complaint. I looked at "Homeless Person Assistance" and "Homeless Street Condition"

## Methodology

The notebook [`homeless_311.ipynb`](notebooks/homeless_311.ipynb) performs the following analyses:

##### Part 1: Finding Data

Using NYC Open Data’s database on 311 service requests from 2020 to the present, I analyzed how many calls New Yorkers made each month about homeless individuals. I filtered for only complaints involving homelessness. I also looked at data specifically about homeless encampments (which 311 defines as involving structures and/or multiple unhoused people living together on the street), but data volume was lower and less consistent. The former metric seemed a more reliable metric of people’s perception of street homelessness over time.


##### Part 2: Grouping and Aggregating

Using pandas, I grouped these calls by month and year and sorted the data chronologically. First, I looked at all the data from 2020 to the present.

## Outputs

The notebooks output this spreadsheet which contains call volume by month from 2020 to April 2026: [`output/311_calls_by_month.csv`](output/311_calls_by_month.csv).

## Running the analysis yourself

You can run the analysis yourself. To do so, you'll need the following installed on your computer:

- Python 3
- The Python libraries specified in [`requirements.txt`](requirements.txt)

## Licensing

All code in this repository is available under the [MIT License](https://opensource.org/licenses/MIT). The data file in the output/ directory is available under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0) license. All files in the data/ directory are released into the public domain.

## Feedback / Questions?

Contact Benjy Sachs at benjy.sachs39@journalism.cuny.edu.
