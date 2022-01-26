#write a program to prompt the user for hours and rate per hour to compute gross pay.
#enter hours = 35
#enter rate = 2.75
#pay should give you 96.25

hours = int(input("Enter the number of hours: "))
rate = float(input("Enter the rate of pay per hour: "))
pay = hours * rate
print ("For hours ",hours, ",")
print("And rate ",rate,",")
print ("Total pay = $",pay)   