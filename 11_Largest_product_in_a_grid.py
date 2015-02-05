#https://projecteuler.net/problem=11
#calculate maximum products of four adjacent element in the direction of up to down, left to right and diagonally respectively, and store those four results
# in a list, then invoke max function once again to get the answer.
import time
start = time.time()
with open('11_grid.txt') as f:
	g = []
	for line in f:
		line = line.strip()
		line = line.split(' ')
		#print line
		g.append(line)
max_p = []
max_p.append(max(int(g[i][j])*int(g[i+1][j])*int(g[i+2][j])*int(g[i+3][j]) for i in xrange(len(g)) for j in xrange(len(g)) if i+3<len(g)))
max_p.append(max(int(g[i][j])*int(g[i][j+1])*int(g[i][j+2])*int(g[i][j+3]) for i in xrange(len(g)) for j in xrange(len(g)) if j+3<len(g)))
max_p.append(max(int(g[i][j])*int(g[i+1][j+1])*int(g[i+2][j+2])*int(g[i+3][j+3]) for i in xrange(len(g)) for j in xrange(len(g)) if i+3<len(g) and j+3<len(g)))
max_p.append(max(int(g[i][j])*int(g[i+1][j-1])*int(g[i+2][j-2])*int(g[i+3][j-3]) for i in xrange(len(g)) for j in xrange(len(g)) if i+3<len(g) and j-3>0))
print max(max_p)
end = time.time()
print end-start