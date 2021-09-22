def isYearLeap(year):
    if year%4!=0:
        return False
    elif year%100!=0:
        return True
    elif year%400!=0:
        return False
    else :
        return True

def daysInMonth(year, month):
    meses=[1,2,3,4,5,6,7,8,9,10,11,12]
    db=[31,29,31,30,31,30,31,31,30,31,30,31]
    dnb=[31,28,31,30,31,30,31,31,30,31,30,31]
    if month in meses:
        if isYearLeap(year)==True :
            return db[month-1]
        else:
            return dnb[month-1]
    else:
        return None

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	print(result)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
