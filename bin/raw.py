from table import Table
from fnmatch import fnmatch
import os
import pandas as pd

_raws = []

data_path = '../data'

class RawMeta(Table.__class__):
    def __init__(cls, name, bases, dct):
        if not dct.get('_abstract_', False):
            print 'adding it'
            _raws.append(cls)
        super(RawMeta, cls).__init__(name, bases, dct)

class Raw(Table):
    __metaclass__ = RawMeta
    _abstract_ = True
    filePattern = ''

def get_file_paths(filePattern):
    return list(os.path.join(data_path, f) for f in os.listdir(data_path)
        if os.path.isfile(os.path.join(data_path, f))
            and fnmatch(f, filePattern))

def process():
    for raw in _raws:
        colnames = None
        for path in get_file_paths(raw.filePattern):
            xl = pd.ExcelFile(path)
            df = xl.parse(xl.sheet_names[0])
