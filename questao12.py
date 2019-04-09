tdias = list()
valorp = float(input())
while (valorp != 0):
    datraso = int(input())
    if (da==0):
        print("O valor total da Prestação: R$ %.2f" %(valorp))
        tdias.append(valorp)
    else:
        juros = valorp+(10*0.3)+((10*0.01)*datraso)
        print("O valor total da Prestação: R$ %.2f" %(juros))
        tdias.append(juros)
    valorp = float(input())


calculoFinal = sum(tdias)

print("Total de Prestações pagas no dia de hoje: R$ %.2f" %(calculoFinal))
