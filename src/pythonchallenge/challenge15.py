from calendar import isleap, weekday

#1xx6 years
for year in range(1006,2006,10):
    # leap year (366 days))
    if isleap(year):
        # weekday == 0 (tuesday)
        if weekday(year,1,27) == 1:
            print year
