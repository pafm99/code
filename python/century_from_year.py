def centuryFromYear(year):
    return 1 + (year - 1) // 100    # 1 because 2017 is 21st century, and 1989 = 20th century

print(centuryFromYear(1905))  
