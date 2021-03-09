"""
Module to wrap naics descriptions from census.gov

Default mapping is the 2017 version of naics.

Two functions provided:

valid_code - lookup a given naics code str

title - return the text title of the naics code
"""

import pandas as pd

class naics:

    def __init__(self, naics_xls='../data/2-6 digit_2017_Codes.xls'):
        self.codes = pd.read_excel(naics_xls, usecols="B:C", names=['Code', 'Title'], dtype={'Code': str})
        self.lookup_dict = self.codes[['Code', 'Title']].set_index('Code')['Title'].to_dict()

naics_2017 = naics()

def valid_code(code, naics_db=naics_2017):

    return code in naics_db.lookup_dict.keys()


def title(code, naics_db=naics_2017):
    if valid_code(code):
        return naics_db.lookup_dict[code]
    else:
        return None
