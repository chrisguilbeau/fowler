from raw import Raw
from raw import _raws

class Owner(Raw):
    filePattern = '*Owner Upload.xlsx'

class Lease(Raw):
    filePattern = '*Tax Lease Upload.xlsx'

class Permit(Raw):
    filePattern = '*Permit Upload.xlsx'

class Production(Raw):
    filePattern = '*Production Upload.xlsx'
