# PDteamCSV

Export information about PagerDuty teams to CSV format

## Output

This tool outputs information about Services, Escalation Policies and Escalation Policy Targets (Schedules and Users) belonging to Teams in a CSV format suitable for import into a relational database. Each row in the output represents a unique combination of Team, Service, Escalation Policy and Target. You can query this data to answer questions like "what EPs are in this team," or "what services have EPs that reference this schedule?"

## Installation and Use

1. Clone this repo
2. Create a Python 3 virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `./venv/bin/activate`
4. Install the dependencies: `pip install -r requirements.txt`
5. Provide your PagerDuty API token: `export PD_API_KEY=<YOUR_API_KEY>`
6. Run the script and send output to a file you choose: `./report.py > ~/Documents/my_report_output.csv`
7. Share and Enjoy!
