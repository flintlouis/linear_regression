import argparse
from src.file import read_theta_from_file, THETA_FILE_PATH

def usage():
	parser = argparse.ArgumentParser(description="Predict mileage using theta0 and theta1")
	parser.add_argument("-f", "--file", metavar="", default=THETA_FILE_PATH, type=str, help="path to file with stored theta")
	args = parser.parse_args()
	return args

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
	args = usage()
	theta0, theta1 = read_theta_from_file(args.file)
	print(f"theta0 {theta0} theta1 {theta1}")
	while True:
		success, mileage = read_mileage()
		if success:
			price = theta1 * mileage + theta0
			if price < 0:
				price = 0
			print(f"price prediction: ${price:.2f}")
		else:
			continue

if __name__ == "__main__":
	main()
