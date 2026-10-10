edad =int(input("Introduzca la edad "))
dia = input("Introduzca el dia de la semana ")

if edad < 0:
    print("Edad no valida")
else:
    entrada = 10000    
    
    if edad < 2:
        print("Tiene 100% de decuento ")
        p_descuento = 100
    elif edad <= 5:
        print("Tiene 50% de decuento ")
        p_descuento = 50
    elif edad <= 10:
        print("Tiene 20% de decuento ")
        p_descuento =  20
    elif edad < 55:
        p_descuento = 0
        print("No obtiene descuento por edad")
    else:
        sexo = input("Introduzca el genero (M o F)")
        if (sexo.upper()=="M" and edad >=65) or (sexo.upper()=="F"):
            print("Tiene 30% de decuento ")
            p_descuento = 30
        else:
            p_descuento =0    

    if p_descuento < 50:
        if dia.lower()== "lunes":
            p_descuento = 50
            print(f"Tiene un descuento  del {p_descuento}% por ser dia lunes")
    

    if p_descuento < 30:
            estudiante = input("Es estudiante ( si o no ) ")
            if estudiante.lower()== "si":
                p_descuento = 25

    if p_descuento != 0:
        descuento = entrada * p_descuento / 100
        print(f"El porcentaje de descuento aignado es {descuento}")
        print(f"El monto del descuento es {descuento}")        
    else:
        descuento = 0        

    monto_pagar = entrada - descuento   

    print(f"El monto a pagar es {monto_pagar}")
    






