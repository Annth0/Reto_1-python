def CDT(usuario :str,capital: int,tiempo: int):
  
    if tiempo > 2 :
        
        porcentaje_interes = 0.03
        v_interes = capital * porcentaje_interes * tiempo /12
        total = v_interes + capital
        
        resultado = f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {total}"
        
    else:
        
        porcentaje_perder = 0.02
        v_perder = capital * porcentaje_perder
        total = capital - v_perder
        
        resultado = f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {total}"
        
    return resultado

  #lo de aquí abajo es apra probar que funcione, esto no se debe poner en el bot, pues él mismo las pone
  
print(CDT("AB1012",1000000,3))
print(CDT("QW3456",5000000,2))
