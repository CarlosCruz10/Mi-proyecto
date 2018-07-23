
operacion = input ("¿Que operacion quieres realizar? (multiplicacion/division/suma/resta): ")

primer_numero = int (input ("primer numero: "))
segundo_numero = int (input("segundo numero: "))

if operacion == "multiplicacion":
    resultado_operacion = (primer_numero) * (segundo_numero)

    print("El resultado es {}".format(resultado_operacion))

elif operacion == "division":
    resultado_operacion = (primer_numero) / (segundo_numero)

    print("El resultado es {}".format(resultado_operacion))

elif operacion == "suma":
    resultado_operacion = (primer_numero) + (segundo_numero)

    print("El resultado es {}".format(resultado_operacion))

elif operacion == "resta":
    resultado_operacion = (primer_numero) - (segundo_numero)

    print("El resultado es {}".format(resultado_operacion))