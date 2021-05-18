from src.file import read_theta_from_file

def predict_price(mileage):
	theta0, theta1 = read_theta_from_file()
	return theta0 + (theta1 * mileage)

def linear_regresion(data, learning_rate=0.3):
	tmpT0, tmpT1 = 0, 0
	