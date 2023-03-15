print('Por gentileza, informar os valores de faturamento referente a cada Estado Solicitado.')

sp = float(input('Informe os valores do faturamento mensal do Estado de São Paulo: '))
rj = float(input('Informe os valores do faturamento mensal do Estado do Rio de Janeiro: '))
mg = float(input('Informe os valores do faturamento mensal do Estado de Minas Gerais: '))
es = float(input('Informe os valores do faturamento mensal do Estado de Espírito Santo: '))
outros = float(input('Informe os valores do Faturamento dos demais Estados: '))

total = sp + rj + mg + es + outros

print("Esse é o valor total de faturamento: ", total)

percentual_sp = ((sp/total)*100)
percentual_rj = ((rj/total)*100)
percentual_mg = ((mg/total)*100)
percentual_es = ((es/total)*100)
percentual_outros = ((outros/total)*100)

print ('A porcentagem de participação no faturamento do Estado de São Paulo é: {:.2f}'.format(percentual_sp))
print ('A porcentagem de participação no faturamento do Estado do Rio de Janeiro é: {:.2f}'.format(percentual_rj))
print ('A porcentagem de participação no faturamento do Estado de Minas Gerais: {:.2f}'.format(percentual_mg))
print ('A porcentagem de participação no faturamento do Estado de Espírito Santo é: {:.2f}'.format(percentual_es))
print ('A porcentagem de participação no faturamento dos demais Estados é: {:.2f}'.format(percentual_outros))