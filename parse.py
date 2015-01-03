"""
Parses data from CSV file.
"""

import csv


def parse(file_name, delimiter):
    """Parses a raw CSV file, each line into the list."""
    # check that input file is a *.csv file:
    if file_name[-3:] != 'csv':
        print "ERROR: input file should have .csv extension"
        return

    parsed_data = []

    with open(file_name, 'r') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=delimiter)
        for line in csv_data:
            parsed_data.append(line)

    return parsed_data
