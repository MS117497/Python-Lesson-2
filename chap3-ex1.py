hours = float(raw_input("Enter Hours: "))
rate = float(raw_input("Enter Rate: "))
othours = 0
if hours > 40:
	print("hours greater than 40")
	othours = hours - 40
	hours = 40
pay = othours*rate*1.5 + hours*rate
print("Pay: " + str(pay))
