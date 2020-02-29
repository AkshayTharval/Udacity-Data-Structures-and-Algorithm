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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

output_set = set()
for call_info in calls:
    output_set.add(call_info[0])

# Phone numbers that receive incoming calls
non_telemarketers = set()
for call_info in calls:
    if call_info[1] in output_set:
        output_set.remove(call_info[1])

# Phone numbers that send or receive texts
for text_info in texts:
    if text_info[0] in output_set:
        output_set.remove(text_info[0])
    if text_info[1] in output_set:
        output_set.remove(text_info[1])

# Final list which satisfy all given telemarketers conditions
output_set = sorted(output_set)
print("These numbers could be telemarketers: ")
for telephone in output_set:
    print(telephone)