import sys
from src.data import get_data, visualize_data
from src.data import 

def usage():
	if len(sys.argv) != 2:
		print("Usage:	python3 train <path_dataset>")
		exit()

def main():
	usage()
	data = get_data(sys.argv[1])

	# visualize_data(data)

if __name__ == "__main__":
	main()
	