import argparse
from src.data import get_data
from src.LinearRegression import LinearRegression
from src.data import visualize_data

def usage():
	parser = argparse.ArgumentParser(description="Train a LinearRegression model")
	parser.add_argument("data", type=str, help="path to dataset")
	parser.add_argument("-v", "--visualize", action="store_true", help="visualize dataset and regression")
	args = parser.parse_args()
	return args

def main():
	args = usage()
	data = get_data(args.data)
	model = LinearRegression(data.km, data.price)
	model.fit()
	model.save_weights()
	if args.visualize:
		visualize_data(data.km, data.price, model.theta0, model.theta1)

if __name__ == "__main__":
	main()
