lugar= ""
año= 0

lugar = input("Write the name of your city: ")
año =int(input("Write the year you were born: "))


numbers= input("Write a secuence of numbers")

filas= int(input("Write the number of rows"))
columnas= int(input("Write the number of columns"))


array_numbers=[]
print("Write the numbers of the ",filas,"x", columnas,":")
print(f"Write the numbers of the {filas}x{columnas}:")
for i in range(filas):
    fila_actual = []
    for j in range(columnas):
        valor = int(input(f"Elemento en posición [{i}][{j}]: "))
        fila_actual.append(valor)
    array_numbers.append(fila_actual)

    hola= 2
    