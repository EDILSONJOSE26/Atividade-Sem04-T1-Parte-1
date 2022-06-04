altura = int(input())
comprimento = int(input())
largura = int(input())

area_piso = largura * comprimento
vol_sala = area_piso * altura
area_paredes = 2 * altura * largura + 2 * altura * comprimento

print(area_piso)
print(vol_sala)
print(area_paredes)
