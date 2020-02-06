import os
import time

def clearscr():
	os.system("clear")

def banner(message):
	print("")
	print("")
	print("")
	print("\t**************************************************************")
	print message
	print("\t**************************************************************")
	print("")
	print("")

def clock(year):
	print(" ")
	print(" ")
	print(" ")
	print("\t========================  Contador de Edad =========================")
	print("\t*==================================================================*")
	print("\t|      Anio      |       HEX      |        BIN       |     DEC     |")
	print(year)
	print("\t*==================================================================*")

def print_cake1():
	print(" ")
	print(" ")
	print(" ")
	print("\t\t   A        A     A      A      A       ")
	print("\t\t  ( )      ( )  ( )      ( )   ( )      ")
	print("\t\t    Y      Y      Y      Y       Y      ")
	print("\t\t   | |    | |    | |    | |     | |     ")
	print("\t\t   | |    | |    | |    | |     | |     ")
	print("\t\t   | |    | |    | |    | |     | |     ")
	print("\t\t|**************************************|")
	print("\t\t| ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ |")
	print("\t\t|--------------------------------------|")
	print("\t\t|----Happy 0x20 | 0b100000 Birthday----|")
	print("\t\t|----------------Jorge-----------------|")
	print("\t\t| ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ |")
	print("\t\t****************************************") 

def print_cake2():
	print(" ")
	print(" ")
	print(" ")
	print("\t\t     A     A       A    A        A      ")
	print("\t\t   ( )    ( )    ( )   ( )       ( )    ")
	print("\t\t    Y      Y      Y      Y       Y      ")
	print("\t\t   | |    | |    | |    | |     | |     ")
	print("\t\t   | |    | |    | |    | |     | |     ")
	print("\t\t   | |    | |    | |    | |     | |     ")
	print("\t\t|**************************************|")
	print("\t\t| ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ |")
	print("\t\t|--------------------------------------|")
	print("\t\t|----Happy 0x20 | 0b100000 Birthday----|")
	print("\t\t|----------------Jorge-----------------|")
	print("\t\t| ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ |")
	print("\t\t****************************************") 	

def print_moving_cake():
	
	for i in range(20):
		clearscr()
		print_cake1()
		time.sleep(0.2)
		clearscr()
		print_cake2()
		time.sleep(0.2)
		
def main():
	clearscr()
	
	msg	= ["\t\t     ... Este Cumpleanos es Especial ....","\t\t     ... Mi edad se vuelve de 6 bits ....","\t\t             ... Quieren ver? ....   ","\t\t     ... Asi que me hice un pastel ... "]



	for i in range(0,3):
		clearscr()
		print banner(msg[i])
		time.sleep(3)
	
	
	for i in range(0,33):
		clearscr()
		year="\t|"+"\t"+str(1988+i)+"\t\t"+str(hex(i))+"\t\t"+str(bin(i))+"\t\t"+str(i)+"\t|"
		clock(year)
		if i==32:
			time.sleep(2)
		time.sleep(0.5)

	clearscr()
	banner(msg[3])
	time.sleep(2)	
	print_moving_cake()




	input("Presiona cualquier tecla para continuar... siendo viejo... (~0.0~)")

main()
