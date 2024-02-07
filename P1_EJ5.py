#Realiza un programa que le reciba una cantidad de minutos y muestre 
# por pantalla a cuantas horas y minutos corresponde

minutos=input('Anota minutos: ')
minutos=int(minutos)
hora=minutos/60
hora=int(hora)
minutosobrantes=int(minutos%60)
print(str(minutos)+' minutos son '+str(hora)+' horas y '+str(minutosobrantes)+' minutos')