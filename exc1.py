def VM(nota1, nota2):
    media= (nota1+nota2)/2
    
    if media>=6.0:
        print("você foi reprovado")
    else:
        print( 'você foi aprovado')    

nota1= float(input('digite sua primeira nota:'))
nota2= float(input('digite sua segunda nota:'))
VM(nota1, nota2)