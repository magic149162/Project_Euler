with open(r'.\p022_names.txt') as f:
	name = f.readline().replace('"','').split(',')
name =sorted(name)
def score(s):
	return sum(ord(c)-ord('A')+1 for c in s)

scores = 0
for i in xrange(len(name)):
	scores += score(name[i]) * (i+1)
print scores
