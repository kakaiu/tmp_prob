import os
import sys
import math
import random
import itertools
from multiprocessing import Process, cpu_count, current_process
import time

#setting: acceptable probability of throwing a valid mapping
prob_t = 0.1

#init
n = -1
f = -1
n_trials = -1

def throw_balls(number_balls, number_bins):
	balls = []
	bins = dict()
	for i in range(0, number_balls):
		bin_id = -1
		bin_id = random.randint(0, number_bins-1)
		balls.append(bin_id)
		if bin_id not in bins:
			bins[bin_id] = [i]
		else:
			bins[bin_id].append(i)
	return balls, bins

def check(thrown, combination, number_one_ball_bin):
	tmp = dict()
	for ball_id in combination:
		bin_of_ball = thrown[ball_id]
		if bin_of_ball in tmp:
			#print ball_id, bin_of_ball, combination
			tmp[bin_of_ball] = tmp[bin_of_ball] + 1
		else:
			tmp[bin_of_ball] = 1
	counter = 0
	for bin_id in tmp:
		if tmp[bin_id]==1:
			counter = counter + 1
			if counter >= number_one_ball_bin:
				return True
	return False

def trial(n, f, c, d):
	number_balls = n
	number_bins = math.ceil(c*f)
	throwns = []
	n_throws = int(math.ceil(math.log(n, 2)) * d)
	for i in range(n_throws):
		thrown, bin_status = throw_balls(number_balls, number_bins)
		throwns.append(thrown)

	for k in range(2, f+1): #get 2 ~ f
		for k_combination in itertools.combinations(range(0, n), k):
			test = False
			for thrown in throwns:
				if check(thrown, k_combination, math.floor(k/2))==True:
					test = True
					break
			if test == False:
				return False
	return True

def proc(c, d):
	count = 0
	random.seed(int(current_process().name[-1]))
	for i in range(n_trials):
		if trial(n, f, c, d) == True:
			count = count + 1
	print count, n_trials

if __name__ == "__main__":
	n = int(sys.argv[1])
	f = int(sys.argv[2])
	c = int(sys.argv[3])
	d = int(sys.argv[4])
	n_trials = int(sys.argv[5])

	process_list = []
	for i in range(cpu_count()):
		p = Process(target=proc, args=(c, d, ))
		p.start()
		process_list.append(p)

	for p in process_list:
		p.join()
