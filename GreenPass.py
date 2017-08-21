import random
import sys

x = sys.argv

def ajuda():
	print("""

 ========================================
 |  -p 	Password			|
 |  -e  Email				|
 ========================================
 |  -t  Tamanho              		|
 |  -l	Letras / Numeros     		|
 ========================================
  GreenPass.py -p -t 4 -l abc123
  GreenPass.py -e -t 3 -l aec123
""")
def banner():
	print("""
    ___                                            ___    ____   
  ,"___".   _ ___    ____      ____     _ ___     F _ ", F ___J  
  FJ---L]  J '__ ", F __ J    F __ J   J '__ J   J `-' |J |___:  
 J |  [""L | |__|-J| _____J  | _____J  | |__| |  |  __/F| _____| 
 | \___] | F L  `-'F L___--. F L___--. F L  J J  F |__/ F L____: 
 J\_____/FJ__L    J\______/FJ\______/FJ__L  J__LJ__|   J________L
  J_____F |__L     J______F  J______F |__L  J__||__L   |________|
				V1.0
""")

def gera_senha(palavra,tamanho):
	try:
		lista_gera = []
		lista = palavra.split()
		arruma = ' '.join(lista)
		string_vazia = ''
		for a in range(tamanho):
			randomico = random.choice(arruma) # escolhe palavra da lista
			lista_gera.append(randomico) # Adiciona a palavra escolhida na lista
			string_vazia+=randomico # vai definir as escolhas aleatorias em string vazia
		senha = ''.join(lista_gera)
		print('\n')
		print("[+]Sua senha --->  {} \n".format(senha))
		again = input('   [???]Deseja gerar denovo ? y/n ').lower()
		if again == 'y':
			gera_senha(charac,tamanho)
		else:
			exit()
	except KeyboardInterrupt:
		print('\n[-]Saindo')

def gera_email(tamanho,carac):
	try:
		string_vazia = ''
		carac = carac.split() ## JOGA EM UMA LISTA
		carac2 = ' '.join(carac) ## COLOCA UM ESPAÇO NA LISTA
		lista = []
		for a in range(tamanho): 
			escolhe=random.choice(carac2) # ESCOLHE OS CARACTERES QUE FORAM MUDADOS COM ESPAÇO
			lista.append(escolhe) # ADICIONA UMA ESCOLHA RANDOMICA NA LISTA
			string_vazia+=escolhe # INCREMENTA UMA ESCOLHA DE 'ESCOLHE' ATÉ ACABAR O FOR (DEPENDE DO TAMANHO)
		arruma = ''.join(lista)
		print('[+]Seu e-mail ---> {}'.format(arruma+'@hotmail.com'))
		again = input('   [???]Deseja gerar denovo ? y/n ').lower()
		if again == 'y':
			gera_email(tamanho,charac)
		else:
			exit()
	except KeyboardInterrupt:
		print('\n[-]Saindo')
		


global charac, tamanho
############# MAIN
if len(x) >= 5:
	if x[1] == '-p':
		if x[2] == '-t':
			tamanho = int(x[3])
			if x[4] == '-l':
				charac = x[5]
				gera_senha(charac,tamanho)
				exit()
			else:
				ajuda()
		else:
			ajuda()
######## EMAIL
	elif x[1] == '-e':
		if x[2] == '-t':
			tamanho = int(x[3])
			if x[4] == '-l':
				charac = x[5]
				gera_email(tamanho,charac)
				exit()
			else:
				ajuda()
		else:
			ajuda()
		
else:
	ajuda()
