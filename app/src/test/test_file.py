import os
import sys
app_path = os.path.dirname(os.path.realpath(__file__))[:-8]
sys.path.append(app_path)
import random
from src.file import read_theta_from_file, write_theta_to_file

def no_file_exists():
	theta0, theta1 = read_theta_from_file("fake_file.txt")
	assert theta0 == 0
	assert theta1 == 0

def file_exists(path):
	t0, t1 = random.randint(0, 50), random.randint(51, 100)
	write_theta_to_file(t0, t1, path)
	theta0, theta1 = read_theta_from_file(path)
	assert theta0 == t0
	assert theta1 == t1

def test_read_write_theta(tmpdir):
	path = os.path.join(tmpdir, "theta.txt")
	no_file_exists()
	file_exists(path)

