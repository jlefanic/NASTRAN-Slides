#!/usr/bin/python

# pycon

# jlefanic
# Sat Feb 25 09:00:00 CET 2017
# Usage :
# pycon dat.f06
# output dat.conm2

import sys, re, csv
import numpy as np

def main():
	#
	I={}
	# 'r' means read-only
	file_for_reading = open(sys.argv[1], 'r')
	k=0
	#
	file_for_conm2= open(re.sub(r'\.f06',r'.conm2',sys.argv[1]), 'w')
	for line in file_for_reading :
		if re.search('^\s{22}\*', line):
			print line
			I[k,]=np.array([float(line.split()[1]), float(line.split()[2]), float(line.split()[3]),float(line.split()[4]), float(line.split()[5]), float(line.split()[6])])
			k=k+1
	file_for_reading.close()

	M=I[0,][0]
	Ixx=I[3,][3]
	Iyy=I[4,][4]
	Izz=I[5,][5]
	Ixy=-I[3,][4]
	Ixz=-I[3,][5]
	Iyz=-I[4,][5]
	#
	file_for_conm2.write('$ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +\n')
	file_for_conm2.write('$                                                                       |\n')
	file_for_conm2.write('$ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +\n')
	#                     $1      2               3               4               5               +
	#                     CONM2  *ID 
	file_for_conm2.write('$1      2               3               4               5               +\n')
	file_for_conm2.write('CONM2  * 9000           1000            9999            ')
	file_for_conm2.write('%-16.6e' % (M))
	file_for_conm2.write('+\n')
	file_for_conm2.write('+       0.000           0.000           0.000                           ')
	#file_for_conm2.write('{:16.5e}'.format(M.ljust(max_M)))
	file_for_conm2.write('+\n')
	file_for_conm2.write('+       ')
	file_for_conm2.write('%-16.6e%-16.6e%-16.6e%-16.6e' % (Ixx, Ixy, Iyy,Ixz))
	file_for_conm2.write('+\n')
	file_for_conm2.write('+       ')
	file_for_conm2.write('%-16.6e%-16.6e' % (Iyz,Izz))
	file_for_conm2.write('                                +\n')
	file_for_conm2.write('$ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +\n')	
	print M, Ixx, Iyy, Izz, Ixy, Ixz, Iyz
	file_for_conm2.close()
	
if __name__ == "__main__":
    main()
