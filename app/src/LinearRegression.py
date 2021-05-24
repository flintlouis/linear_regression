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

	def __standard_deviation(self, data):
		data_mean = self.__calculate_mean(data)
		std = sum((data - data_mean)**2)
		std *= (1/len(data))
		return np.sqrt(std)

	def __normalize_data(self, data):
		# return (data - self.__calculate_mean(data)) / self.__standard_deviation(data)
		return (data - np.mean(data)) / np.std(data)

	def __gradient_descent(self, epochs, learning_rate):
		data = self.__normalize_data(self.data)
		labels = self.__normalize_data(self.labels)
		tmpT0, tmpT1 = 0, 0
		for _ in range(epochs):
			tmpT0 = learning_rate * (1/self.size) * (sum(self.predict(data) - labels))
			tmpT1 = learning_rate * (1/self.size) * (sum((self.predict(data) - labels) * data))
			self.theta0 -= tmpT0
			self.theta1 -= tmpT1


	def fit(self, epochs=500, learning_rate=0.05):

		assert epochs > 0, "epochs cannot be less then 0"
		self.__gradient_descent(epochs, learning_rate)
		# 8499.599649933216 -0.0214489635917023
		print(self.theta0, self.theta1)

