import pandas as pd
import matplotlib.pyplot as plt

def get_data(path):
	try:
		data = pd.read_csv(path)
	except Exception as e:
		print(e)
		exit()
	return data

def visualize_data(X, y, theta0=0, theta1=0):
	pred = theta0 + (theta1 * X)
	plt.plot(X, pred, "-r", label="price=theta0+(theta1*mileage)")
	plt.title("Linear regression from mileage to price")
	plt.legend(loc="upper right")
	plt.scatter(X, y, marker="o")
	plt.xlabel("km")
	plt.ylabel("price")
	plt.show()
