import sys

n = int(sys.argv[1])
f = int(sys.argv[2])
c = int(sys.argv[3])
d = int(sys.argv[4])

filename = "{0}_{1}_{2}_{3}.txt".format(n, f, c, d)
f = open(filename, "r")
content = f.read()
groups = content.split("\n")
n_trials = 0
n_success = 0
for group in groups:
	if len(group)==0:
		continue
	tmp = group.split(" ")
	n_success = n_success + int(tmp[0])
	n_trials = n_trials + int(tmp[1])

print(n_success, n_trials, n_success*1.0/n_trials)
