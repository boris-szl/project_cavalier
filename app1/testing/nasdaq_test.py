import os, sys

sys.path.insert(0, '..')

from modules import nasdaq as nd

def lenEquals(*args):
	# description
	for param in args:
		print(param)


def main():
	symbol_list = nd.symbol_list
	company_names = nd.company_names
	print(type(symbol_list))
	print(type(company_names))
	print(len(company_names)
	lenEquals(company_names, symbol_list)



if __name__ == "__main__":
	main()