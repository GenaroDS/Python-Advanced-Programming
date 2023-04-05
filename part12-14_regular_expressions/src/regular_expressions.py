# Write your solution here
import re

def is_dotw(my_string: str):
    pattern = r'^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)$'
    return bool(re.match(pattern, my_string))

def all_vowels(my_string: str):
    pattern = r'^[aeiouAEIOU]+$'
    return bool(re.match(pattern, my_string))

def time_of_day(my_string: str):
    pattern = r'^(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$'
    return bool(re.match(pattern, my_string))
