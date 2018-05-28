from itertools import cycle

def validate_pesel(PESEL):
	weight = [1, 3, 7 ,9, 1 ,3 ,7 ,9 ,1 , 3]
	PList = list(map(int, PESEL))
	Control = PList.pop(len(PList)-1)
	result = 0
	for i in range(len(weight)):
		result += weight[i] * PList[i]
	print(result)
	result = 10 - result % 10
	print(result)
	return result == Control
#or
	# for weight, PList in zip(cycle(weight), PList):
		# result += weight * PList
print(validate_pesel("900525472210"))
