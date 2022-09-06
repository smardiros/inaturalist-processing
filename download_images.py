import csv
import json
import os
from sre_parse import CATEGORIES
import wget

DOWNLOAD_FOLDER = "images/"
CSV_FILE = "observations-257982-short.csv"
WORKING_DIRECTORY = os.getcwd()
PROJECT_JSON = "project.json"


with open(PROJECT_JSON) as file:
    project_json = json.load(file)

category = project_json["categorization"]["properties"][0]

category_options = {}

for option in category["options"]:
    category_options[option["name"]] = option["id"]


with open(CSV_FILE) as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    for row in csv_reader:
        id = row[0]
        url = row[1]
        species = row[2]
        image_filename = id + ".jpg"
        image_filepath = os.path.join(WORKING_DIRECTORY, DOWNLOAD_FOLDER, image_filename)
        if not os.path.exists(image_filepath):
            response = wget.download(url, image_filepath)

        json_filename = id + ".json"
        json_filepath = os.path.join(WORKING_DIRECTORY, DOWNLOAD_FOLDER, json_filename)

        if species not in category_options:
            continue

        img_json = {
            "objects": [],
            "categories": {
                "properties":[
                    {
                        "type": category["type"],
                        "property_id": category["id"],
                        "property_name": category["name"],
                        "option_id": category_options[species],
                        "option_name": species
                    }
                ]
            }
        }

        with open(json_filepath, "w") as file:
            json.dump(img_json, file)





