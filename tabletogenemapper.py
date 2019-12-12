# This script transforms a TAB-delimited table with haploid microsatellite polymorphism data
# into GeneMapper file format, suitable for R poppr and polysat packages

# Version 2019-12-12 by Ivan Pchelin arcella.oraia@gmail.com

import re
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
    ouf.write('Sample.Name\tMarker\tAllele.1\tAllele.2\n')
    switch = 0
    while switch < len(loci):
        runner = 1
        while runner < len(data):
            elements = re.split('\t', data[runner])
            ouf.write(elements[0])
            ouf.write('\t')
            ouf.write(loci[switch])
            ouf.write('\t')
            ouf.write(elements[switch+1].strip())
            ouf.write('\t\n')
            runner += 1
        switch += 1