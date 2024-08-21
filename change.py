def cambio():
    gasto = float(input("Ingresar gasto:\n"))
    recibido = float(input("Dinero recibido:\n"))
    
    vuelto = recibido - gasto
    
    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))

    print("\nVuelto\n")
    print(f"Pesos:\n{pesos}")
    print(f"Centavos:\n{centavos}")
    
cambio()
