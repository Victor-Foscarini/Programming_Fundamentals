
#lê dois vetores com 10 elementos e gera um terceiro vetor de 20 elementos intercalados
l1 = []
l2 = []
l3 = []

l1.extend(input().split())
l2.extend(input().split())

for i in range(0,10):
	l3.append(int(l1[i]))
	l3.append(int(l2[i]))

print("O vetor intercalado é",l3)

#brincando com notas

v = []

x = int(input())
while (x!=-1):
	v.append(x)
	x = int(input())

print("Quantidade de valores: %d" %len(v))

for i in v:
	print(i,end=" ")
print("")

soma = 0
for i in reversed(v):
	print(i,end=" ")
	soma += i
print("")
print("Soma: %d" %soma)
media = soma/len(v)
print("Média: %f" %(media))

sob = 0
sub = 0
for i in v:
	if(i>media):
		sob+=1
	elif (i<media):
		sub+=1
print("Valores acima da média: %d" %sob)
print("Valores abaixo da média: %d" %sub)

#função simples
def f(a,b,c):
	f = a+b+c
	return f

#positivo ou negativo
def f(n):
	if (n>0):
		return "P"
	else:
		return "N"

#taxa de imposto
def somaImposto(taxaImposto,custo):
	return custo*(1+taxaImposto/100)

#pagamentoConta
def valorPagamento(prestacao_,atraso_):
	if atraso_ == 0:
		return prestacao_
	else:
		return prestacao_ * (1 + 0.03 + 0.001 * atraso_)

prestacao = float(input("Insira o valor da prestacao: "))
atraso = int(input("Insira o número de dias em atraso: "))
relatorio = []

soma = 0
n = 0
while(prestacao!=0):

	soma += valorPagamento(prestacao,atraso)
	n += 1

	prestacao = float(input("Insira o valor da prestacao: "))
	atraso = int(input("Insira o número de dias em atraso: "))

print("Relatório do dia:")
print("Quantidade de prestacoes: %d" %n)
print("Valor total pago: %f" %soma)
