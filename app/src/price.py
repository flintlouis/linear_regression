from src.file import read_theta_from_file

def predict_price(mileage):
	theta0, theta1 = read_theta_from_file()
	return theta0 + (theta1 * mileage)
