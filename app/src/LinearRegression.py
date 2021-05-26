import numpy as np
from src.file import write_theta_to_file, read_theta_from_file
from src.data import visualize_data, get_data
import sys

class LRModel:

	def __init__(self, data, labels):
		self.data = data
		self.labels = labels
		self.norm_data = self.__standardize_data(data)
		self.norm_labels = self.__standardize_data(labels)
		self.theta0 = 0
		self.theta1 = 0
		self.size = len(data)

	def save_weights(self, path=None):
		if path:
			write_theta_to_file(self.theta0, self.theta1, path)
		else:
			write_theta_to_file(self.theta0, self.theta1)

	def load_weights(self, path=None):
		if path:
			read_theta_from_file(self.theta0, self.theta1, path)
		else:
			read_theta_from_file(self.theta0, self.theta1)

	def predict(self, values):
		return self.theta0 + (self.theta1 * values)

	def __least_squares(self):
		data_mean = np.mean(self.data)
		labels_mean = np.mean(self.labels)

		numerator, denominator = 0, 0
		numerator = sum((self.data - data_mean) * (self.labels - labels_mean))
		denominator = sum((self.data - data_mean) ** 2)
	
		theta1 = numerator / denominator
		theta0 = labels_mean - (theta1 * data_mean)
		self.theta0 = theta0
		self.theta1 = theta1

	def __min_max_scaling(self, data, min, max):
		data_min, data_max = data.min(), data.max()
		return np.interp(data, [data_min, data_max], [min, max])

	def __destandardize_data(self, data, original_data):
		return data * np.std(original_data) + np.mean(original_data)

	def __standardize_data(self, data):
		return (data - np.mean(data)) / np.std(data)

	def __gradient_descent(self, epochs, learning_rate):
		self.theta0, self.theta1 = 0, 0

		for _ in range(epochs):
			pred = self.predict(self.norm_data)
			error = self.norm_labels - pred

			tmpT1 = (1/self.size) * sum(self.norm_data * error)
			tmpT0 = (1/self.size) * sum(error)

			self.theta1 = self.theta1 + learning_rate * tmpT1
			self.theta0 = self.theta0 + learning_rate * tmpT0

	def __get_slope_intercept(self, point1, point2):
		x1, y1 = point1
		x2, y2 = point2
		slope = (y2 - y1) / (x2 - x1)
		intercept = y1 - slope * x1    
		return slope, intercept

	def __theta0_theta1_original_data(self):
		norm_pred = self.predict(self.norm_data)
		pred = self.__destandardize_data(norm_pred, self.labels)
		point1 = (self.data.min(), pred.min())
		point2 = (self.data.max(), pred.max())
		self.theta1, self.theta0 = self.__get_slope_intercept(point1, point2)

	def fit(self, epochs=500, learning_rate=0.05):
		assert learning_rate > 0 and learning_rate < 1, "learning_rate should be a value between 0 and 1"
		assert epochs > 0, "epochs cannot be less then 0"
		self.__gradient_descent(epochs, learning_rate)
		self.__theta0_theta1_original_data()
		# 8499.599649933216 -0.0214489635917023
		print(self.theta0, self.theta1)

