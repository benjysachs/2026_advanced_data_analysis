# Analysis of 311 calls about homeless individuals
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

https://www.datawrapper.de/_/r5Sfj/

#### Part 3: Analysis

My initial observation was the seasonality of the call volume. Winter and spring are the lowest, then calls peak in the summer and decline through the fall. My hypothesis is that, in colder months, unhoused people are more likely to accept shelter or find a warmer place away from areas with a lot of people. Also, people are outside their houses in general more in warmer months so are more likely to see unhoused people.

Another observation is the gradual decline in calls throughout Mayor Adams’ administration (highlighted in the chart below). He made a high-profile show about cracking down on visible homeless encampments. Complaint volume dropped dramatically in 2024 and early 2025. But it seemed to rebound in 2025 starting in the summertime.

Zooming in to just the past two years (April 2024 through the present) shows us what has happened since Adams term ended and Mayor Mamdani’s term began at the start of 2026.

https://www.datawrapper.de/_/1rMvB/?v=2

Typically, call volumes are low in the first few months of the year. However, starting a few days into his administration, Mamdani ended the longstanding practice of sweeping homeless encampments. January 2026 saw 2,345 calls — a big jump from 507 calls in January 2025. 311 complaints fell in February, likely due to the extremely cold spell and winter storms. In mid-February, Mamdani reversed course and decided to resume sweeps.

But still, once the extreme cold retreated, call volumes surged to 2,522 in March — up from 655 a year prior. It’s possible that homelessness grew more visible due to the pause on sweeps, which likely increased political pressure on Mamdani to “do something” about homelessness. It’s also possible that City employees helped drive the jump in calls, as they began clearing homeless encampments again, causing people to disperse from wherever they were staying.


## Outputs

The notebooks output this spreadsheet which contains call volume by month from 2020 to April 2026: [`output/311_calls_by_month.csv`](output/311_calls_by_month.csv).

## Running the analysis yourself

You can run the analysis yourself. To do so, you'll need the following installed on your computer:

- Python 3
- Pandas

## Licensing

All code in this repository is available under the [MIT License](https://opensource.org/licenses/MIT). The data file in the output/ directory is available under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0) license. All files in the data/ directory are released into the public domain.

## Feedback / Questions?

Contact Benjy Sachs at benjy.sachs39@journalism.cuny.edu.
