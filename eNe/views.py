from django.http import HttpResponse
from django.shortcuts import render
import random
from . NumEscondido import automatico

#variable para controlar que si hay un ganador en la partida, los otros que sigan
#acertando, no tengan contador
ganador=[2]
partida=0
numeros_guardados=[]
lista_resultados=[]
juego_nuevo=True
##clase para registrar numeros para adivinar
class n:
    def iniciar(self,num1,num2,num3,num4):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        self.num4=num4

    #def imprimir(self):
        #print("el numero es: ", self.num1)

number=n()

### primer paso, ingresar los numeros para adivinar en la instancia number
def ingresar(request):
    global juego_nuevo
### controla que no se ingrese un nuevo numero secreto mientras se esta jugando
### cuando se aciertan los cuatro numeros_guardados queda en 0 entonces se puede ingresar numero secreto "if len(numeros_guardados)==0:""
### solo se puede ingresar un nuevo numero secreto si se reinicia el servidor o si no se empezo a jugar(/ene/x/x/x/x)

###se actualizó el control de ingreso, ahora lo controla la variable global juego_nuevo
###cuando se acierta el numero juego _nuevo pasa a TRue y se puede ingresar un nuevo num secreto
### solo se puede ingresar un nuevo numero secreto si se reinicia el servidor o si se acierta el num secreto
    try:
        if request.method == 'POST':
            #print("VALOR JUEGO_NUEVO",juego_nuevo)
            if juego_nuevo == True:


            #if len(numeros_guardados)==0:
                v1=int(request.POST.get("num1"))
                v2=int(request.POST.get("num2"))
                v3=int(request.POST.get("num3"))
                v4=int(request.POST.get("num4"))

                if v1 >=0 and v1 <10 and v2 >=0 and v2 <10 and v3 >=0 and v3 <10 and v4 >=0 and v4 <10:
                    if v1 != v2 and v1 !=v3 and v1 !=v4 and v2 !=v3 and v2 !=v4 and v3 !=v4:
                        juego_nuevo=False
                        del numeros_guardados[:]
                        del lista_resultados[:]
                        #print("VALOR JUEGO_NUEVO2",juego_nuevo)
                        number.iniciar(v1,v2,v3,v4)

                        ganador[0]=1
                        ###contador de partidas
                        global partida
                        partida=partida+1
                        #number.imprimir()
                        #return HttpResponse(" %s " %number.num1)
                        #return HttpResponse("Ingreso correcto! partida #: %s " %partida)
                        return render(request, 'ingreso/ingreso_correcto.html', {'form':partida})
                    return render(request, 'ingreso/distintos.html')
                return render(request, 'ingreso/rango.html')
            else:
                print("Ya existe un num secreto ingresado")
                return render(request,'ingreso/existe.html')
        else:

            return render(request,'ingreso/ingresar.html')
    except:
        print("debe ingresar numeros")
        return render(request,'ingreso/ingresar.html')

#############Ingreso automaticamente
### primer paso, ingresar los numeros automaticamente
def ingresarAutomatico(request):
    global juego_nuevo
### controla que no se ingrese un nuevo numero secreto mientras se esta jugando
### cuando se aciertan los cuatro numeros_guardados queda en 0 entonces se puede ingresar numero secreto "if len(numeros_guardados)==0:""
### solo se puede ingresar un nuevo numero secreto si se reinicia el servidor o si no se empezo a jugar(/ene/x/x/x/x)

###se actualizó el control de ingreso, ahora lo controla la variable global juego_nuevo
###cuando se acierta el numero juego _nuevo pasa a TRue y se puede ingresar un nuevo num secreto
### solo se puede ingresar un nuevo numero secreto si se reinicia el servidor o si se acierta el num secreto
    try:
        if juego_nuevo == True:
            v1,v2,v3,v4=automatico()
            juego_nuevo=False
            del numeros_guardados[:]
            del lista_resultados[:]
            #print("VALOR JUEGO_NUEVO2",juego_nuevo)
            number.iniciar(v1,v2,v3,v4)

            ganador[0]=1
            ###contador de partidas
            global partida
            partida=partida+1
            return render(request, 'ingreso/ingreso_correcto.html', {'form':partida})
        else:
            print("Ya existe un num secreto ingresado")
            return render(request,'ingreso/existe.html')

    except:
        print("debe ingresar numeros")
        return render(request,'index.html')

### segundo paso, ingresar los numeros para inetnatr adivinar los numeros del primer paso
def numeros(request):
    try:
        if request.method == 'POST':
            valor1=int(request.POST.get("nm1"))
            valor2=int(request.POST.get("nm2"))
            valor3=int(request.POST.get("nm3"))
            valor4=int(request.POST.get("nm4"))
            if valor1>=0 and valor1<10 and valor2>=0 and valor2<10 and valor3>=0 and valor3<10 and valor4>=0 and valor4<10:
                if valor1 != valor2 and valor1 !=valor3 and valor1 !=valor4 and valor2 !=valor3 and valor2 !=valor4 and valor3 !=valor4:


                    #val1=2
                    #val2=4
                    #val3=6
                    #val4=8
        ### guarda en val1,2,3 y 4 los valores guardados previeamente en el objeto number(secreto)
        ### se captura error cuando no se ingresan los numeros para adivinar y se ingresan los numeros para intentar adivinar
                    print(ganador)
                    try:
                        val1=number.num1
                        val2=number.num2
                        val3=number.num3
                        val4=number.num4
                        acertados="NADA"
                        n1="NADA"
                        n2="NADA"
                        n3="NADA"
                        n4="NADA"
        ### castea a sttring los 4 num ingresados, los concatena y los guarada en "numeros_strings"
        ### "numeros_strings" se va a ir agregando a la lista "numeros_guardados"
                        nume1=str(valor1)
                        nume2=str(valor2)
                        nume3=str(valor3)
                        nume4=str(valor4)
                        numeros_strings=nume1+nume2+nume3+nume4

                        numeros_guardados.append(numeros_strings)
                        print(numeros_guardados)

                        #ganador=True
            ### compara numeros ingresados con numeros objeto(secreto)
                        if val1==valor1:
                            #return HttpResponse("Hola %s" %numero)
                            n1="ACERTASTE"
                        if val2==valor2:
                            #return HttpResponse("Hola %s" %numero)
                            n2="ACERTASTE"
                            #return HttpResponse(" %s " %acertados)
                        if val3==valor3:
                            #return HttpResponse("Hola %s" %numero)
                            n3="ACERTASTE"
                            #return HttpResponse(" %s " %acertados)
                        if val4==valor4:
                            #return HttpResponse("Hola %s" %numero)
                            n4="ACERTASTE"
                            #return HttpResponse(" %s " %acertados)


                        if val1==valor2:
                            #return HttpResponse("Hola %s" %numero)
                            n2="CASI"
                            #return HttpResponse(" %s " %acertados)
                        if val2==valor1:
                            #return HttpResponse("Hola %s" %numero)
                            n1="CASI"
                            #return HttpResponse(" %s " %acertados)
                        if val3==valor1:
                            #return HttpResponse("Hola %s" %numero)
                            n1="CASI"
                            #return HttpResponse(" %s " %acertados)
                        if val4==valor1:
                            #return HttpResponse("Hola %s" %numero)
                            n1="CASI"
                            #return HttpResponse(" %s " %acertados)
                        if val1==valor3:
                            #return HttpResponse("Hola %s" %numero)
                            n3="CASI"
                            #return HttpResponse(" %s " %acertados)
                        if val2==valor3:
                            #return HttpResponse("Hola %s" %numero)
                            n3="CASI"
                            #return HttpResponse(" %s " %acertados)
                        if val3==valor2:
                            #return HttpResponse("Hola %s" %numero)
                            n2="CASI"
                            #return HttpResponse(" %s " %acertados)
                        if val4==valor2:
                            #return HttpResponse("Hola %s" %numero)
                            n2="CASI"
                            #return HttpResponse(" %s " %acertados)
                        if val4==valor3:
                            #return HttpResponse("Hola %s" %numero)
                            n3="CASI"
                            #return HttpResponse(" %s " %acertados)
                        if val1==valor4:
                            #return HttpResponse("Hola %s" %numero)
                            n4="CASI"
                            #return HttpResponse(" %s " %acertados)
                        if val2==valor4:
                            #return HttpResponse("Hola %s" %numero)
                            n4="CASI"
                            #return HttpResponse(" %s " %acertados)
                        if val3==valor4:
                            #return HttpResponse("Hola %s" %numero)
                            n4="CASI"
                            #return HttpResponse(" %s " %acertados)
            ### si todos son ACERTASTE, guarda en intentos el numero de la lista, luego elimina la lista numeros_guardados y lista_resultados
                        #cuando el primero acierta tiene contador, los otros que acierten no
                        #juego_nuevo es global asi modifica a true cuando se acierta el num, de esta forma se puede ingresar un num secreto otra vez
                        if n1=="ACERTASTE" and n2=="ACERTASTE" and n3=="ACERTASTE" and n4=="ACERTASTE":

                            global juego_nuevo
                            #print("VALOR JUEGO_NUEVO3",juego_nuevo)
                            juego_nuevo=True
                            #print("VALOR JUEGO_NUEVO4",juego_nuevo)
                            if ganador[0]==1:
                                ganador[0]=3
                                #ganador=False
                                intentos=len(numeros_guardados)
                                del numeros_guardados[:]
                                del lista_resultados[:]
                                #number.iniciar(None,None,None,None)
                                print(ganador)
                                print(intentos)
                                print(numeros_guardados)
                                print(lista_resultados)
                                contexto={"primer cifra":valor1,"segunda cifra":valor2,"tercer cifra":valor3,"cuarta cifra":valor4,"cantidad intentos":intentos,"partida":partida}
                                ### pintamos html con los numeros ACERTASTE, numero de partida y la cantidad de intentos
                                #return HttpResponse("<html><body><br>ACERTASTE EL NÃšMERO: %s-%s-%s-%s </br><br>EN: %s INTENTOS</br><br>PARTIDA NÃšMERO: %s</br>#######################################</body></html>" % (valor1,valor2,valor3,valor4,intentos,partida))
                                return render(request,'adivinar/correcto.html', {'form':contexto})
                            else:

                                intentos=len(numeros_guardados)
                                del numeros_guardados[:]
                                del lista_resultados[:]
                                contexto2={"primer cifra":valor1,"segunda cifra":valor2,"tercer cifra":valor3,"cuarta cifra":valor4,"cantidad intentos":"ACERTADO ANTES,NO HAY CONTADOR DE INTENTOS","partida":partida}
                                print(ganador)
                                print(intentos)
                                print(numeros_guardados)
                                print(lista_resultados)
                                ### pintamos html con los numeros ACERTASTE, numero de partida y la cantidad de intentos
                                #return HttpResponse("<html><body><br>ACERTASTE EL NÃšMERO: %s-%s-%s-%s </br>FUÃ‰ ACERTADO ANTES,NO HAY CONTADOR DE INTENTOS<br></br><br>PARTIDA NÃšMERO: %s</br>#######################################</body></html>" % (valor1,valor2,valor3,valor4,partida))
                                return render(request,'adivinar/correcto.html', {'form':contexto2})
                                #return HttpResponse("DDDDDD")
                        acertados=n1 + "-" + n2 + "-" + n3 + "-" + n4
                        acertados2=n1 + "-" + n2 + "-" + n4 + "-" + n3
                        acertados3=n1 + "-" + n3 + "-" + n2 + "-" + n4
                        acertados4=n1 + "-" + n3 + "-" + n4 + "-" + n2
                        acertados5=n1 + "-" + n4 + "-" + n2 + "-" + n3
                        acertados6=n1 + "-" + n4 + "-" + n3 + "-" + n2

                        acertados7=n2 + "-" + n1 + "-" + n3 + "-" + n4
                        acertados8=n2 + "-" + n1 + "-" + n4 + "-" + n3
                        acertados9=n2 + "-" + n3 + "-" + n4 + "-" + n1
                        acertados10=n2 + "-" + n3 + "-" + n1 + "-" + n4
                        acertados11=n2 + "-" + n4 + "-" + n1 + "-" + n3
                        acertados12=n2 + "-" + n4 + "-" + n3 + "-" + n1

                        acertados13=n3 + "-" + n1 + "-" + n2 + "-" + n4
                        acertados14=n3 + "-" + n1 + "-" + n4 + "-" + n2
                        acertados15=n3 + "-" + n2 + "-" + n1 + "-" + n4
                        acertados16=n3 + "-" + n2 + "-" + n4 + "-" + n1
                        acertados17=n3 + "-" + n4 + "-" + n1 + "-" + n2
                        acertados18=n3 + "-" + n4 + "-" + n2 + "-" + n1

                        acertados19=n4 + "-" + n1 + "-" + n2 + "-" + n3
                        acertados20=n4 + "-" + n1 + "-" + n3 + "-" + n2
                        acertados21=n4 + "-" + n2 + "-" + n1 + "-" + n3
                        acertados22=n4 + "-" + n2 + "-" + n3 + "-" + n1
                        acertados23=n4 + "-" + n3 + "-" + n1 + "-" + n2
                        acertados24=n4 + "-" + n3 + "-" + n2 + "-" + n1

                        #acertados=random.choice(["n1,n2,n3"])
            ### en resultado se guarda lista de acertados con todas las combinaciones y aplicando una eleccion aleatoria
            ### de esta forma evitamos que las columnas(resultado-numero) coincida, puede coincidir o no
                        resultado=random.choice([acertados,acertados2,acertados3,acertados4,acertados5,acertados6,acertados7,
                        acertados8,acertados9,acertados10,acertados11,acertados12,acertados13,acertados14,acertados15,
                        acertados16,acertados17,acertados18,acertados19,acertados20,acertados21,acertados22,acertados23,acertados24])
            ### el resultado se va almacenando en ista_resultados
                        lista_resultados.append(resultado)
        ### se enumeran lista_resultados y numeros_guardados, se muestran en html
                    except:
                        #print(number)
                        #print("HAY QUE INGRESAR NÃšMERO SECRETO PRIMERO,/INGRESO/X/X/X/X")
                        return render(request, 'adivinar/sin_ingresar.html')
                    #return HttpResponse("<html><body><br>%s </br>###########PARTIDA: %s<br>%s </br></body></html>" %(list(enumerate(lista_resultados)),partida,list(enumerate(numeros_guardados))))
                    contexto3={"partida":partida, "resultados":list(enumerate(lista_resultados)), "jugados":list(enumerate(numeros_guardados))}
                    return render(request,'adivinar/partida.html', {"form":contexto3})
                return render(request, 'adivinar/distintos.html')
            return render(request,'adivinar/rango.html')
        else:
            return render(request,'adivinar/adivinar.html')

    except:
        print("debe ingresar numeros")
        return render(request,'adivinar/adivinar.html')

def inicio(request):
    if ganador[0]==3:
        ingreso={"num_secreto":"EL NÚMERO ESCONDIDO FUE ADIVINADO",}
        return render(request,'index.html', {'form':ingreso})
    elif ganador[0]==2:
        ingreso={"num_secreto":"EL NÚMERO ESCONDIDO AÚN NO FUE INGRESADO",}
        return render(request,'index.html', {'form':ingreso})
    else:
        ingreso={"num_secreto":"EL NÚMERO ESCONDIDO AÚN NO FUE ADIVINADO",}
        return render(request,'index.html', {'form':ingreso})


