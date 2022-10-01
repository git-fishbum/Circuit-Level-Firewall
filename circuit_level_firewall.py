from datetime import datetime, timedelta
import time
import logo

print('Choose 1 for Blocking sites and 2 for Unblocking: \n')

print('1. Blocking. \n2. Unblocking')
choice = int(input("\nMake your choice 1 or 2: "))

if choice == 1:
	print("Enter time and date details for blocking the sites upto desired time.")
	year = int(input("Enter year: "))
	mon = int(input("Enter month: "))
	day = int(input("Enter day: "))
	hour = int(input("Enter hour: "))
	min = int(input("Enter minutes: "))
	end_time = datetime(year, mon, day, hour, min) # y, m, d, h, min

	sites_to_block = list(map(str,input("Enter sites to be blocked using spaces: ").split()))
	print("List of sites entered to be blocked: ", sites_to_block)
elif choice == 2:
	ini_time_for_now = datetime.now()
	end_time = ini_time_for_now - timedelta(days = 1) # y, m, d, h, min
	sites_to_block = list(map(str,input("Enter sites to unblocked using spaces: ").split()))