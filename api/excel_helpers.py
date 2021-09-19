import pandas as pd

def read_excel(file):
	data = pd.read_excel(file, header=None)
	return data