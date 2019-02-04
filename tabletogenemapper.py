# This script transforms a TAB-delimited table with microsatellite polymorphism data
# into GeneMapper file format

# Version 2019-01-16

# Соберем множество с локусами вносимых данных и проверим, что новых нет
import re
# Заберем заголовок infile в список
with open ('infile.txt') as inf:
	line = inf.readline()
	print(line)
	elements = re.findall(r'\S+', line.strip())
loci = []
for i in elements:
	loci.append(i)
with open ('infile.txt') as inf:
	data = inf.readlines()

with open ('GeneMapper.txt', 'w') as ouf:
	switch = 0 # Переключатель по локусам
	while switch < len(loci):
		runner = 1
		while runner < len(data):
			elements = re.split('\t', data[runner])
			ouf.write(elements[0])
			ouf.write('\t')
			ouf.write(loci[switch])
			ouf.write('\t')
			ouf.write(elements[switch+1].strip())
			ouf.write('\n')
			runner += 1
		switch += 1