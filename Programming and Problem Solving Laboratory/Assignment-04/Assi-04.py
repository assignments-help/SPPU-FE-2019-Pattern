# Problem Statement:
# To accept student’s five courses marks and compute his/her result. Student is passing if
# he/she scores marks equal to and above 40 in each course. If student scores aggregate
# greater than 75%, then the grade is distinction. If aggregate is 60>= and <75 then the
# grade if first division. If aggregate is 50>= and <60, then the grade is second division. If
# aggregate is 40>= and <50, then the grade is third division.

print('Enter Marks of 5 Subjects separated by single white space')
marks = [int(x) for x in input().split()]

is_failed = False

for mark in marks:
    if mark < 40:
        is_failed = True
        break

if(is_failed):
    print('Fail')
else:
    marks_sum = 0
    for mark in marks:
        marks_sum += mark
    
    agg = marks_sum / 500 * 100
    print('Aggregate:', agg)
    if agg >= 75:
        print('Distinction')
    elif agg >= 60 and agg < 75:
        print('First Division')
    elif agg >= 50 and agg < 60:
        print('Second Division')
    elif agg >= 40 and agg < 50:
        print('Third Division')