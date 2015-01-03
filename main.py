"""
Calculates SAS values, delta values and writes into CSV files.
"""

import csv
import sys
from datetime import datetime
import parse


FILENAME = sys.argv[1]


def str_to_float(parsed_data):
    """Converts each value into a float."""
    # parsed_data = lists of strings
    return [[float(item) for item in line] for line in parsed_data]


def get_SAS(parsed_values, sas_coef=0.5):
    """Multiplies each value on SAS coefficient."""
    # parsed_values = lists of floats
    res_lst = []
    for lst in parsed_values:
        res_lst.append(map(lambda x: x * sas_coef, lst))
    return res_lst


def get_deltas(parsed_values):
    """Calculates deltas for subsequent phases."""
    # parsed_values = lists of floats
    res_lst = []

    for lst in parsed_values:
        tmp_lst = [lst[0]]

        for i in range(1, len(lst)):
            tmp_lst.append(lst[i] - lst[i-1])
        res_lst.append(tmp_lst)

    return res_lst


def csv_writer(data, filename):
    """Writes data into CSV file."""
    with open(filename, 'w') as f:
        writer = csv.writer(f, dialect='excel')
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    parsed_values = str_to_float(parse.parse(FILENAME, ','))

    # build SAS list:
    sas = get_SAS(parsed_values, sas_coef=0.5)

    # build Subs deltas list:
    subs_delta = get_deltas(parsed_values)

    # build SAS deltas list:
    sas_delta = get_deltas(sas)

    # inserting labels before appropriate tables:
    sas.insert(0, ['SAS:'])
    subs_delta.insert(0, ['Subs deltas:'])
    sas_delta.insert(0, ['SAS deltas:'])

    # aggregate lists:
    agg_lst = []
    for lst in [sas, subs_delta, sas_delta]:
        agg_lst.extend(lst)

    # get current time:
    time = str(datetime.now().time())[:8].replace(':', '.')

    # WRITE to CSV:
    csv_writer(agg_lst, 'results_' + time + '.csv')
