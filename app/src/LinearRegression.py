import numpy as np
from src.file import write_theta_to_file
from src.data import visualize_data, get_data
import sys

class LRModel:

	def __init__(self, data, labels):
		self.data = data
		self.labels = labels
		self.theta0 = 0
		self.theta1 = 0
		self.size = len(data)

	def save_weights(self, path=None):
		if path:
			write_theta_to_file(self.theta0, self.theta1, path)
		else:
			write_theta_to_file(self.theta0, self.theta1)

	def predict(self, values):
		return self.theta0 + (self.theta1 * values)

	def __calculate_mean(self, data):
		return np.mean(data)

	def __least_squares(self):
		data_mean = self.__calculate_mean(self.data)
		labels_mean = self.__calculate_mean(self.labels)

		numerator, denominator = 0, 0
		numerator = sum((self.data - data_mean) * (self.labels - labels_mean))
		denominator = sum((self.data - data_mean) ** 2)
	
		theta1 = numerator / denominator
		theta0 = labels_mean - (theta1 * data_mean)
		self.theta0 = theta0
		self.theta1 = theta1

	def __min_max_scaling(self, data):
		data_min, data_max = data.min(), data.max()
		return np.interp(data, [data_min, data_max], [0, 1])

	def __standardize_data(self, data):
		return (data - np.mean(data)) / np.std(data)

	def __gradient_descent(self, epochs, learning_rate):
		self.data = self.__standardize_data(self.data)
		self.labels = self.__standardize_data(self.labels)

		for _ in range(epochs):
			pred = self.predict(self.data)
			error = self.labels - pred

			tmpT1 = (1/self.size) * sum(self.data * error)
			tmpT0 = (1/self.size) * sum(error)

			self.theta1 = self.theta1 + learning_rate * tmpT1
			self.theta0 = self.theta0 + learning_rate * tmpT0


	def fit(self, epochs=500, learning_rate=0.05):
		assert learning_rate > 0 and learning_rate < 1, "learning_rate should be a value between 0 and 1"
		assert epochs > 0, "epochs cannot be less then 0"
		self.__gradient_descent(epochs, learning_rate)
		# 8499.599649933216 -0.0214489635917023
		print(self.theta0, self.theta1)

