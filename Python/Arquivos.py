#Victor-Foscarini

#cria uma agenda telefônica


agenda = []

def pede_nome():
	return(input("Nome: "))

def pede_telefone():
	return(input("Telefone: "))

#foram adicionados abaixo os pedidos do nascimento e email do contato, sendo que estas funções foram também devidamente adicionadas nas outras funções quando necessário

def pede_nascimento():
    return(input("Nascimento: "))

def pede_email():
    return(input("Email: "))

def mostra_dados(nome,telefone,nascimento,email):
	print("Nome: %s Telefone: %s Nascimento: %s Email: %s" % (nome,telefone,nascimento,email))

def pede_nome_arquivo():
	return(input("Nome do arquivo: "))

def pesquisa(nome):
	mnome = nome.lower()
	for p, e in enumerate(agenda):
		if e[0].lower()== mnome:
			return p
	return None

def novo():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    nascimento = pede_nascimento()
    email = pede_email()
    agenda.append([nome,telefone,nascimento,email])

def apaga():
    global agenda
    nome = pede_nome()
    p = pesquisa(nome)
    if p != None:
        conf = input("Confimar exclusão? S-Sim N-Não ") #pede-se ao usuário uma confirmação da exclusão, note que para qualquer entrada diferente de S a operação é cancelada, mas sugere-se ao usuário usar N para cancelar a operação
        if (conf == "S"):
            del agenda[p]
            print("%s apagado da agenda." %nome)
        else:
            print("Exclusão cancelada!")
    else:
        print("Nome não encontrado.")

def altera():
    p = pesquisa(pede_nome())
    if p != None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        nascimento = agenda[p][2]
        email = agenda[p][3]
        print("Encontrado:")
        mostra_dados(nome, telefone,nascimento,email)
        nome = pede_nome()
        telefone = pede_telefone()
        nascimento = pede_nascimento()
        email = pede_email()
        conf = input("Confimar alteração? S-Sim N-Não ") #pede-se ao usuário uma confirmação da mudança, note que para qualquer entrada diferente de S a operação é cancelada, mas sugere-se ao usuário usar N para cancelar a operação
        if conf == "S":            
            agenda[p] = [nome, telefone,nascimento,email]
            print("Alteração realizada!")
        else:
            print("Alteração cancelada!")
    else:
        print("Nome não encontrado.")

def lista():
     print("\nAgenda\n\n------")
     for e in agenda:
         mostra_dados(e[0], e[1],e[2],e[3])
     print("------\n")

def lê():
     global agenda
     nome_arquivo = pede_nome_arquivo()
     arquivo = open(nome_arquivo, "r", encoding = "utf-8")
     agenda = []
     for l in arquivo.readlines():
         nome, telefone, nascimento, email = l.strip().split("#")
         agenda.append([nome, telefone, nascimento, email])
     arquivo.close()

def grava():
     nome_arquivo = pede_nome_arquivo()
     arquivo = open(nome_arquivo, "w", encoding = "utf-8")
     for e in agenda:
         arquivo.write("%s#%s#%s#%s\n" % (e[0], e[1], e[2], e[3]))
     arquivo.close()

def valida_faixa_inteiro(pergunta, inicio, fim):
     while True:
         try:
               valor = int(input(pergunta))
               if inicio <= valor <= fim:
                  	return(valor)
               else:
                  	int("a")
         except ValueError:
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def menu():
     print("""
   1 - Novo
   2 - Altera
   3 - Apaga
   4 - Lista
   5 - Ordena
   6 - Grava
   7 - Lê

   0 - Sai
""")
     return valida_faixa_inteiro("Escolha uma opção: ",0,7)


def ordena(): #função para ordenar a lista
#optou-se por deixar a ordenação como na tabela ASCII(função sort), visto que a maioria dos contatos seria dada com o primeiro caractere maiúsculo e esse me pareceu o jeito mais natural de ordenar. Caso quisse ordenar puramente por ordem alfabética seria necessário considerar o fato de os caracteres maiúsculos virem antes dos minúsculos na tabela ASCII e, dessa forma usar a função upper ou lower

    global agenda
    nomes = []
    for dados in agenda:
        nomes.append(dados[0])
    nomes.sort()
    agenda2 = []
    for nome in nomes:
        p = pesquisa(nome)
        agenda2.append(agenda[p])
    agenda = agenda2.copy()
    print("Agenda ordenada!")

while True:
     opção = menu()
     if opção == 0:
         break
     elif opção == 1:
         novo()
     elif opção == 2:
         altera()
     elif opção == 3:
         apaga()
     elif opção == 4:
         lista()
     elif opção == 5:
         ordena()
     elif opção == 6:
         grava()
     elif opção == 7:
         lê()

#adicionar ordenar
#altera e apague pedem confirmação 
#adicionar nascimento e email 
