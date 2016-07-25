#!/usr/bin/python
import sys

def mapper():
	for line in sys.stdin:
		line = line.strip()
		data = line.split(';')
		#l ultimo array e vuoto, quindi controllo se il primo
		#elemento dell array e vuoto, avendolo stippato in precendeza
		if data[0] != '':
			#check sull data: se e 2016 non stampa la riga
			if int(data[4].split('-')[0]) != 2016:
				continue
			else:
				nationality = data[2]
				price = data[6]
				print nationality + '\t' + price.strip()

if __name__ == '__main__':
	mapper()