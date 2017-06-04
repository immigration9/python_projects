## Chapter 01: Unpacking to modulate a sequence into variables
## Apostraphy front of middle means all the remaining variables except the selected ones
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

def avg(values):
    total = 0
    for value in values:
        total = total + value
    return total/len(values)

sample_grades = (50, 60, 80, 100, 90, 70, 55, 30, 40, 20, 10, 15)
drop_first_last(sample_grades)
avg(sample_grades)

user_record = ('Anthony', 'projgotham18@gmail.com', '1-216-222-2222', '82-2-565-1803')
name, email, *phone_numbers = record

name
email
phone_numbers
