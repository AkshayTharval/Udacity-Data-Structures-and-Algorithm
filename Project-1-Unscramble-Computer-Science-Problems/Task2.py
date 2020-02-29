"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
max_time = 0
telephone_dict = {}

for calls_info in calls:
    if (calls_info[0] in telephone_dict) and (calls_info[1] in telephone_dict):
        telephone_dict[calls_info[0]] += int(calls_info[3])
        telephone_dict[calls_info[1]] += int(calls_info[3])
    elif (calls_info[0] in telephone_dict) and (calls_info[1] not in telephone_dict):
        telephone_dict[calls_info[0]] += int(calls_info[3])
        telephone_dict[calls_info[1]] = int(calls_info[3])
    elif (calls_info[0] not in telephone_dict) and (calls_info[1] in telephone_dict):
        telephone_dict[calls_info[0]] = int(calls_info[3])
        telephone_dict[calls_info[1]] += int(calls_info[3])
    else:
        telephone_dict[calls_info[0]] = int(calls_info[3])
        telephone_dict[calls_info[1]] = int(calls_info[3])
    
for key in telephone_dict.keys():
    if telephone_dict[key] > max_time:
        max_time = telephone_dict[key]
        required_telephone_number = key

print("{} spent the longest time, {} seconds, on the phone during".format(required_telephone_number, max_time))