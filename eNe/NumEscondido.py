import random as aleatorio

#####funcion que define el numero escondido de forma automatica
#####cuando los cuatro digitos sean distintos devuelve el numero escondido
def automatico(a=0,b=0,c=0,d=0):
    while(a==b or a==c or a==d or b==c or b==d or c==d):
        a=aleatorio.randint(0,9)
        b=aleatorio.randint(0,9)
        c=aleatorio.randint(0,9)
        d=aleatorio.randint(0,9)
        print(a,b,c,d)
    return a,b,c,d
    


#aa,bb,cc,dd=automatico()
#print(aa,bb,cc,dd)