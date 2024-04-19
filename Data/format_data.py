import csv
import json

def csv_to_json(csv_file, json_file):
    data = []

    with open(csv_file, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)
            print(row)

    with open(json_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

if __name__ == "__main__":
    csv_file = "HistoricalCPI.csv"
    json_file = "data.json"
    csv_to_json(csv_file, json_file)
