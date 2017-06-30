# increment the day to the next day in the week
def inc_day(day):
	#check if day is inbetween 0 and 6
	if (day < 0 or 6 < day):
		return -1
	elif (day == 6):
		return 0
	else:
		return day + 1

# get index of current month for list
def get_month(l):
	m = int(l[6:8])

	#make sure it is a valid month
	if (m < 0 or 11 < m):
		return -1
	else:
		return m - 1

# get price of float at particular date
def get_price(l):
	p = float(l[22:])
	return p

# get day of month from 1 to 31
def get_day_of_month(l):
	d = int(l[9:11])
	return d

def get_year(l):
	y = int(l[1:5])
	return y

# average of a list
def average(lst):
	sum = 0.0
	total = len(lst)
	for i in lst:
		sum = sum + i

	return sum / total
		

filename = 'cdnew.csv' #btc history by day
f = open(filename, 'r')

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',  \
	'Friday', 'Saturday']

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', \
	'August', 'September', 'October', 'November', 'December']

#days list - index 0 is sunday index 6 is saturday
days_list = [ [], [], [], [], [], [], [] ]

#months list - index 0 is January index 11 is Decemember
months_list = [ [], [], [], [], [], [], [], [], [], [], [], [] ] 

#day of month list - index 0 is 1st index 30 is 31st
days_of_month_list = [ [], [], [], [], [], [], [], [], [], [], [], [], [], \
	[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ]

data = f.readlines()
#remove lines without important data
data = data[1:-3]

# get analysis range from user
firstDate = str(get_month(data[0])+1) + "/" + str(get_day_of_month(data[0])) \
	+ "/" + str(get_year(data[0]))

lastDate = str(get_month(data[-1])+1) + "/" + str(get_day_of_month(data[-1])) \
	+ "/" + str(get_year(data[-1]))

print("Enter a start date (mm/dd/yyyy) inbetween " + firstDate + " and " + \
	lastDate)
begin_date = input("> ")
print("Enter an end date (mm/dd/yyyy) inbetween " + begin_date + " and " + \
	lastDate)
end_date = input("> ")

print(firstDate)
# create list for days of month
dom_list = [17] # 29th first date
for x in data:
	dom_list.append(get_day_of_month(x))

# create day and month lists
dayIndex = 6
domIndex = 0
for x in data:
	day_of_month = dom_list[domIndex] - 1
	day = dayIndex
	month = get_month(x)	
	price = get_price(x)
	
	days_list[day].append(price)
	months_list[month].append(price)
	days_of_month_list[day_of_month].append(price)

	dayIndex = inc_day(dayIndex)
	domIndex = domIndex + 1
	
# print dom averages
currentDOM = 1
for d in days_of_month_list:
	avg = average(d)
	print("Average of " + str(currentDOM) + ": " + str(avg))
	currentDOM = currentDOM + 1

print("")

# print data averages
mIndex = 0
for m in months_list:
	avg = average(m)
	mName = months[mIndex]
	print("Average of " + mName + ": " + str(avg))
	mIndex = mIndex + 1

print("")

first_day = True
dom = 30
dIndex = 0
for d in days_list:
	
	avg = average(d)
	dName = days[dIndex]
	print("Average of " + dName + ": " + str(avg))
	dIndex = dIndex + 1

	
	
f.close()
