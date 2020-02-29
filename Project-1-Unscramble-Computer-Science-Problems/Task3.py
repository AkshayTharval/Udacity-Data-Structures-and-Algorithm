"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

area_codes_set = set()
fixed_line_call_banglore_count = 0
banglore_call = 0

for calls_info in calls:
    if calls_info[0].startswith('(080)'):
        # Counting all calls originating from banglore
        banglore_call += 1
        # Calls going to fixed line from banglore
        if calls_info[1].startswith('('):
            area_codes_set.add(calls_info[1][calls_info[1].find("(")+1:calls_info[1].find(")")])
        
        # Calls going to mobile phones from banglore
        if calls_info[1][int(len(calls_info[1])/2)] == ' ' and calls_info[1].startswith(('7', '8', '9')):
            area_codes_set.add(calls_info[1][0:4])
        
        # Calls going to telemarketers
        if calls_info[1].startswith('140'):
            area_codes_set.add('140')
            
        if calls_info[1].startswith('(080)'):
            fixed_line_call_banglore_count += 1
        
        
        
area_codes_set = sorted(area_codes_set)
print('The numbers called by people in Bangalore have codes:')
for code in area_codes_set:
    print(code)
            
print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(round(fixed_line_call_banglore_count*100/banglore_call, 2)))