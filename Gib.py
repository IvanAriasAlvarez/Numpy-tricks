
x={}
while True:
  n = input("si quieres terminar salir")
  count= 0
  if n != "salir":
    
    articulo = input("cual es el articulo")
    precio = int (input("cual es el precio"))
    
    x[articulo] = precio
    
  else:
    break
count = 0
for c,v in x.items():
  count += v
  print(c + "\t" + str(v) + "\n")
print("coste total: " + str(count))
