def change(): 
    gasto: 23.75
    Dinero_recibido: 100
    
    Pesos: 76
    Centavos: 25
    
    gasto = float("23.75\n") 
    Dinero_recibido = float("100\n") 
    vuelto = Dinero_recibido - gasto
    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos)*100))
    
    print(f"Ingresar gasto:\n{gasto}")
    print(f"Dinero recibido\n{int(Dinero_recibido)}") 
    print("")
    print("Vuelto\n")
    print(f"Pesos:\n{pesos}")
    print(f"Centavos:\n{centavos}") 
change()
