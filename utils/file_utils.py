import csv
import json
from .datetime_utils import dt_now

def read_file(filename):
    f = open(filename, "r", encoding="utf-8")
    return f.read()

def save_file(filename, data):
    f = open(filename, "w")
    response = f.write(data)
    f.close()
    return response

# open json
def read_json(filename):
    f = open(filename, 'r', encoding='utf-8')
    return json.load(f)


# save json
def save_json(filename, data):
    f = open(filename, 'w', encoding='utf-8')
    f.write(json.dumps(data, ensure_ascii=False, indent=4))
    f.close()


def read_csv(filename, delimiter):
    # Returns csv contents as a list of lists
    csvfile = open(filename, newline='')
    csv_reader = csv.reader(csvfile, delimiter=delimiter)
    csv_contents = list(csv_reader)
    csvfile.close()
    return csv_contents


def read_csv_as_dict(filename, delimiter):
    # Returns csv contents as a list of dicts
    csvfile = open(filename, newline='')
    csv_reader = csv.DictReader(csvfile, delimiter=delimiter)
    csv_contents = list(csv_reader)
    csvfile.close()
    return csv_contents


def save_csv(filename, data):
    # = data: list[lists]
    f = open(filename, 'w', encoding='utf-8', newline='')
    wr = csv.writer(f, dialect='excel')
    wr.writerows(data)
    f.close()

def save_csv_dict(filename, data):
    # = data: list[dicts]
    keys = data[0].keys()
    f = open(filename, 'w', encoding='utf-8', newline='')
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)
    f.close()


# decode portuguese text
def decode_pt(s):
    return s.encode("iso-8859-1").decode("utf-8")