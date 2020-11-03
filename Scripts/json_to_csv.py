import json
import csv


def json_to_csv(json_file, csv_file):
    """
    > Function covert json into csv
    > Funtion need some changes according to your file
    """

    with open(json_file) as json_file_obj:
        data = json.loads(json_file_obj.read())

    with open(csv_file, "w") as csv_file_obj:
        writer = csv.DictWriter(csv_file_obj, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    return True
