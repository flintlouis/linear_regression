import sys
from src.theta import predict_price

def usage():
	if len(sys.argv) != 1:
		print("Usage:	python3 predict")
		exit()

def read_mileage():
	value = input("Mileage: ")
	if value == "exit":
		exit()
	try:
		value = int(value)
	except:
		return False , value
	return True , value

def main():
	usage()
	while True:
		success, mileage = read_mileage()
		if success:
			price = predict_price(mileage)
			print("price prediction :", price)
		else:
			continue

if __name__ == "__main__":
	main()
