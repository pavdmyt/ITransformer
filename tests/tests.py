from nose.tools import *  # noqa
from parse import parse
from main import str_to_float, get_SAS


def flatten_list(lst):
    return [item for sublist in lst for item in sublist]


class TestParser(object):

    def setUp(self):
        # file paths:
        path = '/home/fiodrn/Documents/py_stuff/projects/Itransformer/'
        self.file_name1 = path + 'test.csv'
        self.file_name2 = path + 'test.xls'

        # get data:
        self.parsed_data = parse(self.file_name1, ',')
        self.parsed_values = str_to_float(self.parsed_data)

        # create convenient data structure:
        self.str_lst = flatten_list(self.parsed_data)
        self.floats_lst = flatten_list(self.parsed_values)

    def test_parse(self):
        assert_equal(type(self.parsed_data), list)
        assert_equal(parse(self.file_name2, ','), None)

    def test_str_to_float(self):
        for i in range(len(self.str_lst)):
            assert_equal(float(self.str_lst[i]), self.floats_lst[i])

    def test_get_SAS(self):
        sas_lst = flatten_list(get_SAS(self.parsed_values))
        for i in range(len(sas_lst)):
            assert_equal(sas_lst[i], self.floats_lst[i] * 0.5)

    def test_get_deltas(self):
        pass  # TODO
