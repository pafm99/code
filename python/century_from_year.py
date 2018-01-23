def centuryFromYear(year):
    return (year) // 100 + 1    # 1 because 2017 is 21st century, and 1989 = 20th century

print(centuryFromYear(1905))  # --> 21
