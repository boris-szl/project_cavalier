import time # time module

"""
This is a module for measuring Wall-Time and Processing Time
"""

"""
First two functions are used for measuring wall time.
Third and fouth function are used for measuring processing time.
"""
def w_tic():
	global w_start
	w_start = time.time()

def w_toc():
	if 'w_start' in globals():
		print("Elapsed real time (wall time): {}".format(str(time.time()-w_start)))
	else:
		print("toc(): start time not set")

"""
time.process_time()
Return the value (in fractional seconds) of the sum of 
the system and user CPU time of the current process.
"""
def p_tic():
	global p_start
	p_start = time.process_time()

def p_toc():
	if 'p_start' in globals():
		print("Processing time: {}".format(str(time.process_time()-p_start)))
	else:
		print("toc(): start time ( p_tic() ) not set")

"""
time.perf_counter()
Return the value (in fractional seconds) of a performance counter, 
i.e. a clock with the highest available resolution to measure a short duration. 
It does include time elapsed during sleep and is system-wide.
"""

def pc_tic():
	global pc_start
	pc_start = time.perf_counter()

def pc_toc():
	if 'pc_start' in globals():
		print("Performance Counter Time: {}".format(str(time.perf_counter()-pc_start)))
	else:
		print("pc_toc(): start time ( pc_tic() ) not set")


# time.perf_counter() -> most accurate
# Why? 
# Source: https://www.webucator.com/article/python-clocks-explained/
def calculate_time(func):
	def inner1(*args, **kwargs):

		begin = time.perf_counter()
		func(*args, **kwargs)
		end = time.perf_counter()

		print("Total time taken for {} : {} ",format(func.__name__, end - begin))

	return inner1





