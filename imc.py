print ("calculadora imc")
altura = float (input ("digite sua altura"))
peso = float (input("digite seu peso"))

imc = peso/(altura*altura)

print (f"seu imc e {imc:.1f}")
if imc<=18.5:
    print("voce esta magro")
elif imc>=18.6 and imc<=24.9:
    print("voce esta normal")
elif imc>=25 and imc<=29.9:
    print("voce esta acima do peso")
elif imc>=30 and imc<=34.9:
    print("voce esta com obesidade tipo 1")
elif imc>=35 and imc<=39.9:
    print("voce esta com obesidade tipo 2")