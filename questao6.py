qntpizza = int(input("Quantas pizzas desejadas: "))
precopizza = float(input("Valor da Pizza: R$ "))
custo = qntpizza*precopizza
imposto = custo-custo*0.8
total = custo + imposto
print("O valor total do pedido é: R$ %.2f" %(total))
