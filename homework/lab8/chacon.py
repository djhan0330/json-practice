#!/usr/bin/python3

import json

with open("chacon.json", "r") as file:
	data = json.load(file)

with open('chacon.csv', 'w') as csv_file:
	for entry in data[:5]:
		name = entry['name']
		html_url = entry['html_url']
		updated_at = entry['updated_at']
		visibility = entry['visibility']

		line = f"{name},{html_url},{updated_at},{visibility}\n"

		csv_file.write(line)

