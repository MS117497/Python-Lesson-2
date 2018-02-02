def computepay(hours, rate):
	othours = 0
	if hours > 40:
		othours = hours - 40
		hours = 40
	pay = othours*rate*1.5 + hours*rate
	print("Pay: " + str(pay))

while True:
	try:
		hours = float(raw_input("Enter Hours: "))
		break
	except ValueError:
		print "Error, please use numeric input"
while True:
	try:
		rate = float(raw_input("Enter Rate: "))
                break
        except ValueError:
                print "Error, please use numeric input"
computepay(hours, rate)
