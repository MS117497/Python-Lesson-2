def computegrade(score):
	grade = 'F'
	if score >= 0.9:
		grade = 'A'
	elif score >= 0.8:
		grade = 'B'
	elif score >= 0.7:
	        grade = 'C'
	elif score >= 0.6:
	        grade = 'D'
	return grade
while True:
        try:
                score = float(raw_input("Enter score: "))
		if 0 <= score <= 1.0:
			break
		else:
			print "Bad score"
        except ValueError:
                print "Bad score"

print computegrade(score)
