def CDT(usuario,cantidad,tiempo):
    
    if tiempo > 2 :
        
        porcentaje_interes = 0.03
        v_intereses = cantidad * porcentaje_interes * tiempo / 12
        v_total_a = v_intereses + cantidad

        resultado = f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {cantidad} para un tiempo de {tiempo} meses es: {v_total_a}"
    
    else:
        
        porcentaje_perder = 0.02
        v_perder = cantidad * porcentaje_perder
        v_total_b = cantidad - v_perder
        
        resultado = f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {cantidad} para un tiempo de {tiempo} meses es: {v_total_b}"
        
    return resultado

print(CDT("ESea",1000000,3))
# print(CDT("assdf",500000,2))