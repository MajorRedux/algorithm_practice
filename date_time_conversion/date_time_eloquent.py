"""
You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and you see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
- the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'

Input: Time in a 24-hour format (as a string).

Output: Time in a 12-hour format (as a string).
"""

def time_converter(time):
    h, m = map(int, time.split(':'))
    return f"{(h-1)%12+1}:{m:02d} {'ap'[h>11]}.m."
