#classes for documentation

------------------------------------------------------------------------------------------------------------------------------------------

class Funcionario :
	def __init__ (self,nome,salario):
		self.nome = nome
		self.salario = float(salario)

	def return_nome(self):
		return self.nome

	def return_salario(self):
		return self.salario
#teste
andre = Funcionario("André",5200)
print('Nome: %s' % andre.return_nome())
print('Salário: %.2f' % andre.return_salario())

------------------------------------------------------------------------------------------------------------------------------------------

class Pessoa:
	def __init__(self,nome,idade,peso,altura):
		self.nome = nome 
		self.idade = idade #em anos
		self.peso = peso #em kg
		self.altura = altura #em cm
		
	def envelhecer (self,anos):
		if (self.idade<21):
			if (self.idade + anos)< 21:
				self.altura += 0.5*anos
			else:
				self.altura += (21 - anos)*0.5
		self.idade += anos

	def engordar (self,kilos):
		self.peso += kilos

	def emagrecer (self,kilos):
		if(self.peso>kilos):
			self.peso -= kilos
		else:
			self.peso = 0
	
	def crescer (self,cents):
		self.altura += cents
#teste
andre = Pessoa("André",16,50,150)
andre.envelhecer(3)
andre.engordar(10)
andre.crescer(10)

print(andre.idade)
print(andre.peso)
print(andre.altura)

------------------------------------------------------------------------------------------------------------------------------------------

class Macaco :
	def __init__ (self,nome):
		self.nome = nome
		self.estomago = []
	def comer(self,comida):
		self.estomago.append(comida)
	def verEstomago(self):
		print(self.estomago)
	def digerir(self,comida=""):
		if comida == "":
			self.estomago = []
		else:
			if comida in self.estomago:
				self.estomago.remove(comida)
			


m1 = Macaco("Caesar")
m2 = Macaco("Cornelius")

m1.comer("Banana")
m1.comer("Maçã")
m1.comer("Sopa")
m1.verEstomago()
m1.digerir("Banana")
m1.verEstomago()
m1.digerir()
m1.verEstomago()

m2.comer(m1)
m2.verEstomago()

#Conclui-se que o macaco pode ser canibal!Ele retorna o espaço de memória do outro macaco dentro do estômago

------------------------------------------------------------------------------------------------------------------------------------------

class lista:
	
	def __init__(self,lista = []): #inicia a lista
		self.lista = lista
	
	def insertbeg(self,element): #insere no início
		self.lista.insert(0,element)

	def insertend(self,element): #insere no final
		self.lista.append(element)

	def printa(self): #imprime a lista
		print(self.lista)

	def isempty(self): #checa se a lista é vazia
		if len(self.lista) == 0:
			print("Lista vazia!")
		else :
			print("Lista não vazia!")
	
	def search(self,element): #busca elemento
		indice = False
		for i in range(len(self.lista)):
			if self.lista[i] == element:
				indice = i
		if indice == False:
			print("Elemento não está presente na lista!")
		else:
			print("Elemento está presente na lista com índice %d!" %indice)
					

	def remove(self,element): #retira elemento
		self.lista.remove(element)
		
#teste simples

frutas = lista()
frutas.isempty()
frutas.insertbeg("Maçã")
frutas.insertend("Banana")
frutas.insertbeg("Laranja")
frutas.printa()
frutas.isempty()
frutas.search("Maçã")
frutas.remove("Maçã")
frutas.search("Maçã")

------------------------------------------------------------------------------------------------------------------------------------------

#descobre a partir de uma pilha se a expressão está balançeada 
#utilizou-se uma classe Stack com algumas operações típicas de uma pilha 
#definiu-se uma função isMatch para checar se os tipos de operações comparadas de dentro da expressão estão certas (colchetes com colchetes e parênteses com parênteses)
#definiu-se então a função isWellWritten que checa se a expressão está bem formada e retorna True ou False
# utilizou-se as operações de pilha para guardar todos os operadores de abertura("([") e mais a frente checa-se se eles fecham corretamente com os operadores de fechamento (")]")


class Stack():
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self,item):
		self.items.append(item)
	
	def pop(self):
		self.items.pop()
	
	def get(self):
		return self.items

def isMatch(op1,op2):
	if op1 == "(" and op2 == ")":
		return True
	if op1 == "[" and op2 == "]":
		return False
	

def isWellWritten(operation):
	s = Stack()
	well_written = True
	index = 0

	while index < len(operation) and well_written:
		op = operatin[index]
		if op in "([":
			s.push(op)
		else:
			if s.isEmpty:
				well_written = False
			else:
				if not s.isMatch(s.pop(),op):
					well_written = False

		index += 1

	if s.isEmpty() and well_written:
		return True
	else:
		return False

#realizar operação para caso 2*(3+4)/5-6

print("Insira a operação:")
op = input()

print(int(op[0])*(int(op[3])+int(op[5]))/int(op[8])-int(op[10]))

------------------------------------------------------------------------------------------------------------------------------------------

