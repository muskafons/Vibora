print("\n\n:::::: LISTAS ::::::\n\n")

ratas = ['CARECULO','CUSCOña', 'Espi','BETICO Hp','CHIMBALA','TeniCIUOUS T','ranque']
print(ratas)

ratasCaraCassa = ratas.pop()
ratasCaraCassa1 = ratas.pop(5)

ratas.remove('Espi')

del ratas[3]

print(ratasCaraCassa)
print(ratasCaraCassa1)
print(ratas)

#print(ratas)

#ratas.insert(2,'JIRAFA')

#print(ratas)


#------------------------------------------------------------------
print("----------------------\n\n")

pcs = [] #Se declara la lista vacia

print(pcs)

pcs.append('VOLVO')
pcs.append('YAMAHA')
pcs.append('SONY')
pcs.append('TOSHIBA')

print(pcs)

#------------------------------------------------------------------
print("----------------------\n\n")

carros = ["honda","FORD","MAZDA","PEAGUT","Mercedez","BMW"]

print(carros)

print("\n\n")

carros[-3]="XXX"

print(carros)

#------------------------------------------------------------------
print("----------------------\n\n")

bicicleta = ['pedal','lujo',23]

print(bicicleta)

print('\n\n\n',bicicleta[0])

print('\n\n\n',bicicleta[-1])

#------------------------------------------------------------------
print("----------------------\n\n")

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].upper()}."
print(message)

#------------------------------------------------------------------
print("----------------------\n\n")

names = ['camilo','freddy','monixa','rambo',"HONDA"]

print("HOLA ME LLAMO", names[0])
print(names[1], "ES my brother")
print(f'{names[2]} se llama mi señora')
print(names[3], "kill all these motherfuckerss")

#------------------------------------------------------------------
print("----------------------\n\n")

mensajeX = f"I would like to own a {names[-1]} motorcycle"

print(mensajeX)