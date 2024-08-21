def cambio():
    gasto = int(input("Ingresar gasto:\n")
    recibido = int(input("Dinero recibido:\n")
    
    vuelto = recibido - gasto
    
    pesos = int(vuelto)
    centavos = int((vuelto - pesos) * 100)

    print("\nVuelto\n")
    print(f"Pesos:\n{pesos}")
    print(f"Centavos:\n{centavos}")

cambio()
