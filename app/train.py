import sys
from src.data import get_data
from src.LinearRegression import LRModel
from src.data import visualize_data
import numpy as np

def usage():
	if len(sys.argv) != 2:
		print("Usage:	python3 train <path_dataset>")
		exit()

def main():
	usage()
	data = get_data(sys.argv[1])
	model = LRModel(data.km, data.price)
	model.fit()
	# model.save_weights()
	visualize_data(model.data, model.labels, model.theta0, model.theta1)

if __name__ == "__main__":
	main()
