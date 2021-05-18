import os
THETA_FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__))[:-3], "data", "theta.txt") 

def read_theta_from_file(path=THETA_FILE_PATH):
	try:
		with open(path, 'r') as f:
			theta0 = int(f.readline())
			theta1 = int(f.readline())
	except:
		theta0, theta1 = 0, 0
	return theta0, theta1

def write_theta_to_file(theta0, theta1, path=THETA_FILE_PATH):
	with open(path, 'w') as f:
		f.write(str(theta0) + "\n")
		f.write(str(theta1) + "\n")
