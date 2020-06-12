from functools import reduce
import operator

def get_value(data_dict, query):
    return reduce(operator.getitem, query.split("/"), data_dict)
