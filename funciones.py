print("Ejemplo de funciones")

def fun():
    print("ejecutado funcion")
    
def c(m):
    print(m)    

def e(m):
    print(m)

def en(ap,n):
    print(f"Nom Completo: {n} {ap}")
    
def suma(a,b):
    r=a+b
    return r

def resta(a,b):
    r=a-b
    return r

def multi(a,b):
    r=a*b
    return r

def divi(a,b):
    r=a/b
    return r

fun()
c("hola")
e("como estas")
en("Montes", "Gabriel")
print("")

print("---operacion de suma----")
n1=int(input("Ingresa el primer numero "))
n2=int(input("Ingresa el segundo numero "))
rs=suma(n1,n2)
print(f"Suma de {n1} + {n2} = ",rs)
print("")

print("---operacion de resta----")
n3=int(input("Ingresa el primer numero "))
n4=int(input("Ingresa el segundo numero "))
rr=resta(n3,n4)
print(f"Suma de {n3} - {n4} = ",rr)
print("")

print("---operacion de multiplicacion----")
n5=int(input("Ingresa el primer numero "))
n6=int(input("Ingresa el segundo numero "))
rm=multi(n5,n6)
print(f"Suma de {n5} * {n6} = ",rm)
print("")

print("---operacion de division----")
n7=int(input("Ingresa el primer numero "))
n8=int(input("Ingresa el segundo numero "))
rd=divi(n7,n8)
print(f"Suma de {n7} / {n8} = ",rd)
print("")

# python funciones.py