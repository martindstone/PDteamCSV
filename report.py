#!/usr/bin/env python

import pd
import csv
import os
import sys

pd_api_key = os.environ.get('PD_API_KEY')

if not pd_api_key:
	sys.exit("Please set your PD_API_KEY environment variable to a PagerDuty v2 API key (read-only is fine)")

eps = pd.fetch(api_key=pd_api_key, endpoint="escalation_policies")

results = []
for ep in eps:
	for service in ep['services']:
		for team in ep['teams']:
			for rule in ep['escalation_rules']:
				for target in rule['targets']:
					target_type = "schedule" if target['type'] == "schedule_reference" else "user"
					results.append({
						"team id": team['id'],
						"team summary": team['summary'],
						"service id": service['id'],
						"service summary": service['summary'],
						"ep id": ep['id'],
						"ep summary": ep['summary'],
						"target id": target['id'],
						"target summary": target['summary']
					})

writer = csv.DictWriter(sys.stdout, fieldnames=results[0].keys())
writer.writeheader()
for result in results:
	writer.writerow(result)