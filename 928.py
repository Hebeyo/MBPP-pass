'''Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
'''
def change_date_format(date):
    date = date.split('-')
    return date[2] + '-' + date[1] + '-' + date[0]
'''
Standard answer: 
import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
        return change_date_format(dt)
'''
assert change_date_format('2026-01-02')=='02-01-2026'
assert change_date_format('2021-01-04')=='04-01-2021'
assert change_date_format('2030-06-06')=='06-06-2030'
