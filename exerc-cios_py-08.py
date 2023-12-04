kg_maça = float(input("Insira a quantidade (kg) de maças adiquiridas:"))
kg_morango = float(input("Insira a quantidade (kg) de morangos adiquiridos:"))

#função para definir o valor das frutas baseada na quantidade 
def valor_morango() :
    if kg_morango <= 5:
        return 2.5
    elif kg_morango > 5:
        return 2.2
    
def valor_maça():
    if kg_maça <= 5:
        return 1.8
    elif kg_maça > 5:
        return 1.5
    

custo_maça = kg_maça * valor_maça() 

custo_morango = kg_morango * valor_morango()

custo_total= custo_maça + custo_morango


if (kg_morango + kg_maça) > 8 or custo_total >= 25:
    desconto = custo_total * 0.10

else:
    desconto = 0 

print("Total a ser pago: ", custo_total + desconto)