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
		return np.sum(data) / len(data)

	def __linear_regression(self):
		data_mean = self.__calculate_mean(self.data)
		labels_mean = self.__calculate_mean(self.labels)

		numerator, denominator = 0, 0
		numerator = sum((self.data - data_mean) * (self.labels - labels_mean))
		denominator = sum((self.data - data_mean) ** 2)
	
		theta1 = numerator / denominator
		theta0 = labels_mean - (theta1 * data_mean)
		self.theta0 = theta0
		self.theta1 = theta1

	def fit(self, epochs=1000, learning_rate=0.03):

		self.__linear_regression()
		print(self.theta0, self.theta1)
		# m = 0
		# b = 0
		# for _ in range(epochs):
		# 	for i in range(self.size):
		# 		x = np.interp(self.data[i], [min(self.data), max(self.data)], [0, 1])
		# 		y = np.interp(self.labels[i], [min(self.labels), max(self.labels)], [0, 1])
		# 		guess = m * x + b
		# 		error = y - guess
		# 		m = m + (error * x) * learning_rate
		# 		b = b + (error) * learning_rate
		# print(m, b)

