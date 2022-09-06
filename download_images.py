import csv
import os
import wget

DOWNLOAD_FOLDER = "images/"
CSV_FILE = "observations-257982-short.csv"
WORKING_DIRECTORY = os.getcwd()


with open(CSV_FILE) as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    for row in csv_reader:
        id = row[0]
        url = row[1]
        filename = id + ".jpg"
        filepath = os.path.join(WORKING_DIRECTORY, DOWNLOAD_FOLDER, filename)

        response = wget.download(url, filepath)
