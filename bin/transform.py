#!/usr/bin/env python
'''
Transforms the extracted data
- upload phase: puts the extracted data into raw_ tables
- create phase: creates stage_ tables from raw_ tables
    to_ functions modify data
- update phase: removes/adds columns/rows from/to stage_ tables
    calc_pre scripts are run on the data before calc_
    calc_ columns are run in the update phase
    calc_post scripts are run on the data after call_
- verify phase:
    verify_ functions return a message and a value (return None for verified)
'''

import raws
import raw

def main():
    raw.process()

if __name__ == '__main__':
    main()
