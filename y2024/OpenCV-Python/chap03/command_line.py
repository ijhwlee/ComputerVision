title = '서기 1년 1월 1일부터 ' \
        '오늘까지 ' \
        '일수 구하기'
months = [31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]
year, month = 2023, 12
day = 29; ratio=365.2425

days = (year - 1)*ratio + \
        sum(months[:month-1]) + day

print(title), print(' - 년:{0}'.format(year)), print(' - 월:{0}'.format(month))
print(' - 일:{0}'.format(day)), print(' * 일수 총합:{0}'.format(int(days)))
