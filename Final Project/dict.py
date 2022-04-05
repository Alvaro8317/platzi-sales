rae = {}
rae['Pizza'] = 'Pedazo de masa, muy rico de Papa John\'s'
rae['Pasta'] = 'Masa muy usada en italia'
print(rae['Pasta'])
# print(rae['Helado']) #Trae un KeyError
print(rae.get('Helado','No sé quejeso'))
print(rae.get('Pizza','No sé quejeso')) # Si encuentra algún valor de esa llave, retorna el valor, en caso de no, retorna "No sé quejeso"
print(rae.keys())
print(rae.values())
print(rae.items())
for key in rae.keys():
    print(key)
for value in rae.values():
    print(value)
for it in rae.items():
    print(it)