# project-controls-analytics
## The Business Scenario
Imagine you work for a mid-sized EPC (Engineering, Procurement, and Construction) company.

The company manages approximately 200 active, planned, and completed projects ranging from January 2021 to December 2025 with a 24 month planning horizon for future projects. The 200 projects are spread across 25 unique clients. 

Each month, project controls exports reports from several systems into CSV files.

Management wants a reusable analytics toolkit that can answer questions such as:

Which projects are most likely to exceed budget?
Which project managers consistently perform well?
Which regions have the largest schedule delays?
Which clients generate the most change orders?
How accurate are our monthly forecasts?
Where should leadership focus attention?

The toolkit should work regardless of the month's data.

This is the business problem we're solving.

## Purpose
The purpose for this project it to strength data science/analytics skills through hands on practice. 

## Assumptions
Simulated date of 12-31-2025. Project data ranges from 1-1-2021 to 24 month planning horizon. 
Projects can start on any day of the calendar year. 
For simplicity, projects may begin on any day of the month, but progress and costs are reported at monthly intervals. Partial months at project start and completion are approximated as full reporting periods. This assumption keeps the simulation simple while remaining appropriate for monthly portfolio analytics.

## Data
The data used for this project is artificially generated in generate_data.py. For the purposes of this project, that gives us additional flexibility to add more or less complexity to the data in order to perform different analysis. It also allows us to continue to build and revist this project as experience grows. 

### Realistic Data
As with anything simulated, there are gives and takes when trying to make it realistic. I try to bridge that gap by making it appropriately realistic for the purposes of analysis without getting bogged down in trying to make it perfect. The data is a means to get to the analysis. To add realism to the data, we assigned a client size to each simulated client and weighted it such that larger clients have a higher likelihood of having more projects. Additionally in the client data, we assigned an industries probabilistically to each client. For projects, there are four different projects for each possible industry, and each project pulls randomly from a range of budgets and duration of project. For costs, a normal distribution was used for the burn curve. For simplicity, actual costs are a variance of 10% of the planned costs. 

## Future Work
Add different burn curve options (front loaded, back loaded, etc.) and total project variance in addition to a monthly variance to account for problem projects tend to continue having problems and vice versa. 
Finalized data will eventually be exported to csv files and stored in the data folder imported and cleaned. Cleaned data will be analyzed. 