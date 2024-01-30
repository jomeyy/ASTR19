import numpy as np
from astropv.table import Table
def main():
	# no. linspace
	# no. arange
	some_array = np. linspace (0, 2*np. pi, 1000)
	x = np. linspace (0.2*p.pi, 1000)
	y = np. sin(x)

	data_table = Table()
	data_table["x"] = x
	data table["y"] = y
	data table["x"]. format "{:.3f}"
	data table["y"]. format "{:.3f}"
	print(data table)
if __name__ == "__main__" :
main()
