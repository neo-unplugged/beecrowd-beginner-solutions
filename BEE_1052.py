import calendar

num = int(input())
print(calendar.month_name[num] if num in range(1, 13) else 'Invalid Number')
