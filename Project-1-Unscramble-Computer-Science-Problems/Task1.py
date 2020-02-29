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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
all_records_telephone_numbers = set()
for text_info in texts:
    all_records_telephone_numbers.add(text_info[0])
    all_records_telephone_numbers.add(text_info[1])

for call_info in calls:
    all_records_telephone_numbers.add(call_info[0])
    all_records_telephone_numbers.add(call_info[1])

print("There are {} different telephone numbers in the records.".format(len(all_records_telephone_numbers)))