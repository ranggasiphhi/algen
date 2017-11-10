import random

table = []
rand_chrom = []
oper_code = 0

def input_init():
	global table
	global oper_code
	j = int(input('Masukkan banyak job : '))
	m = int(input('Masukkan banyak machine : '))
	range_m = range(1,m+1)
	for i in range(1,j+1):
		o = int(input('Masukkan operasi di job '+ str(i) +' : '))
		operation = []
		for k in range(1,o+1):
			print "Operasi" + " " + str(k) + " " + "pada job " + str(i)
			machine = int(input('Machine : '))
			while machine not in range_m :
				print('Tidak ada machine. Silakan input ulang')
				machine = int(input('Machine : '))
			t = int(input('Masukkan operation time : '))
			operation.append([machine, t])
			oper_code = oper_code + 1
		table.append(operation)
	print table
	
def gen_chrom():
	global oper_code
	global rand_chrom
	for i in range(1,oper_code+1):
		r = random.randrange(1,oper_code+1)
		while r in rand_chrom:
			r = random.randrange(1,oper_code+1)
		rand_chrom.append(r)
	print rand_chrom

def main():
	input_init()
	x_chrom = int(input('Berapa kali generate chromosome ?'))
	
	gen_chrom()
	

main()
		
