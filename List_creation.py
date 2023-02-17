lista=[]
counter=100
while counter>=0:
    if counter%2==0:
      lista.append("Pari:")
    if counter%2==1:
      lista.append("Dispari:")
    lista.append(counter)
    counter-=1
print(lista)
