import pandas as pd
import matplotlib.pyplot as plt

def get_data(path):
	try:
		data = pd.read_csv(path)
	except Exception as e:
		print(e)
		exit()
	return data

def visualize_data(data):
	plt.scatter(data.km, data.price, marker='o')
	plt.xlabel('km')
	plt.ylabel('price')
	plt.show()
