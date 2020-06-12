class View:

    def start(self):
        print("***************************************************")
        print("       Bienvenido Al Sistema Del Restaurante:      ")
        print("***************************************************")

    def end(self):
        print("\n-------------------")
        print("   ¡Vuelve pronto!")
        print("---------------------")

    def option(self, last):
        print("Selecciona una opcion (1 - " + last + '): ', end="")

    def ask(self,msg):
        print(msg)


    def opcion_invalid(self):
        print("*************************************") 
        print("¡Opción incorrecta vuelva a intentar!") 
        print("*************************************") 
    
    def no_admin(self):
        print("*****************************************") 
        print("¡Solo los administradores pueden acceder!") 
        print("*****************************************")    

    def success(self):    
         print(f"Los cambios se guardaron correctamente ")

    def id_invalido(self):
        print("Error. el id es invalido") 

    def mostrar_update(self):
        print("Actualiza los campos que sean necesarios")

    def mostrar_total(self, total):
        print("\nTotal del pedido: ", total) 

    def datos_incorrectos(self):
        print('\nUsuario o contraseña incorrectos')   
    
    def ok(self, name, op):
        print('+'*(len(str(name))+len(op)+24))
        print('+ ¡'+str(name)+ ' se '+op+' correctamente! + ')
        print('+'*(len(str(name))+len(op)+24))

    def ver_clave(self,clave):
        print("*".center(20,'*'))
        print(str(clave).center(20,'*'))
        print("*".center(20,'*'))

    def ok_double_id(self, id1, id2, op):
        print('+'*(len(str(id1))+len(op)+24))
        print('+ ¡'+str(id1)+ ' y ' + str(id2) + ' se '+op+' correctamente! + ')
        print('+'*(len(str(id1))+len(op)+24))

    def msg(self,output):
        print(output)

    def error(self,err):
        print(' ¡ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

#*******************************************************************************************************************************************************
#*******************************************************-------------***********************************************************************************
#******************************************************|    Menús    |**********************************************************************************
#*******************************************************-------------***********************************************************************************
#*******************************************************************************************************************************************************

    def menu_cliente(self):
        print("---------------------")
        print("    Menú Clientes:  ")
        print("---------------------") 
        print("1. Hacer reservación") 
        print("2. Ver reservación")
        print("3. Ver Menú")
        print("\n0. Salir")

    def platillo_menu(self):
        print("---------------------")
        print("         Menú        ")
        print("---------------------") 
        print("**********************")        

    def menu_empleado(self):
        print("---------------------")
        print("    Menú Empleados:  ")
        print("---------------------") 
        print("1. Administrar")
        print("2. Crear Orden")
        print("3. Crear Detalle-Orden")
        print("4. Crear Detalle-Reservacion")
        print("5. Ver ordenes del dia")
        print("6. Ver orden por fecha")
        print("7. Ver orden por clave")
        print("8. Ver detalle-orden")
        print("9. Ver detalle-reservacion")
        print("10. Cambiar estatus de mesa")
        print("\n0. Salir")

    def menu_gerente(self):
        print("---------------------")
        print("    Menú Gerentes:  ")
        print("---------------------") 
        print("1. Administrar Clientes")
        print("2. Administrar Empleados")
        print("3. Administrar Ordenes")
        print("4. Administrar Mesas")
        print("5. Administrar Platillos")
        print("6. Administrar Reservaciones")
        print("7. Administrar Detalle-Ordenes")
        print("8. Administrar Detalle-Reservaciones")
        print("\n0. Salir")

    def submenu_clientes(self):
        print("-----------------------")
        print("    Submenú clientes:  ")
        print("-----------------------") 
        print("1. Agregar clientes")
        print("2. Actualizar clientes")
        print("3. Ver cliente por clave")
        print("4. Ver cliente(s) por nombre")
        print("5. Eliminar cliente")
        print("\n0. Salir")

    def submenu_empleados(self):
        print("-----------------------")
        print("    Submenú empleados:  ")
        print("-----------------------") 
        print("1. Agregar empleados")
        print("2. Actualizar Empleados")
        print("3. Ver empleado por clave")
        print("4. Ver empleado(s) por nombre")
        print("5. Eliminar empleado")
        print("\n0. Salir")


    def submenu_ordenes(self):
        print("-----------------------")
        print("    Submenú ordenes:  ")
        print("-----------------------") 
        print("1. Actualizar orden")
        print("2. Ver ordenes por fecha")
        print("3. Ver ordenes por numero_orden")
        print("4. Eliminar orden")
        print("\n0. Salir")

    def submenu_mesas(self):
        print("-----------------------")
        print("    Submenú mesas:  ")
        print("-----------------------") 
        print("1. Agregar mesa")
        print("2. Actualizar mesa")
        print("3. Ver mesa por numero de mesa")
        print("4. Ver todas las mesas")
        print("5. Eliminar mesa")
        print("\n0. Salir")
    
    def submenu_platillos(self):
        print("-----------------------")
        print("    Submenú platillos:  ")
        print("-----------------------") 
        print("1. Agregar platillo")
        print("2. Actualizar platillo")
        print("3. Ver platillo por clave")
        print("4. Ver todos las platillos")
        print("5. Eliminar platillo")
        print("\n0. Salir")
        
    def submenu_reservaciones(self):
        print("-----------------------")
        print("    Submenú reservaciones:  ")
        print("-----------------------") 
        print("1. Actualizar reservacion")
        print("2. Ver reservaciones por fecha")
        print("3. Ver reservaciones por id_reservacion")
        print("4. Eliminar reservacion")
        print("\n0. Salir")

    def submenu_detalle_reservaciones(self):
        print("-----------------------------------------")
        print("    Submenú detalle de reservaciones:    ")
        print("-----------------------------------------") 
        print("1. Actualizar detalle reservacion")
        print("2. Ver detalle reservacion(es) por nombre y fecha")
        print("3. Ver detalle de reservacion con CLAVE DE DETALLE")
        print("4. Eliminar detalle reservacion")
        print("\n0. Salir")

    def submenu_detalle_ordenes(self):
        print("---------------------------------")
        print("    Submenú detalle de ordenes:  ")
        print("---------------------------------") 
        print("1. Actualizar detalle orden")
        print("2. Eliminar detalle orden")
        print("3. Ver detalle de reservacion con CLAVE DE DETALLE")
        print("4. Ver detalles de orden(es) por nombre de cliente y fecha.")
        print("\n0. Salir")

#*******************************************************************************************************************************************************
#*******************************************************-------------***********************************************************************************
#******************************************************|   VIEW's    |**********************************************************************************
#*******************************************************-------------***********************************************************************************
#*******************************************************************************************************************************************************
        
#*******************************************************************************************************************************************************
    #Ver Platillos
#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************

    def mostrar_platillo(self, platillo):
        print('*****Datos de la reservación**********')
        print('ID Platillo: ', platillo[0])
        print('**********************************')
        print('Descripcion: ', platillo[1])
        print('**********************************')
        print('Costo: ', platillo[2])


    def mostrar_platillos(self, platillos):
        print('\n' + 'Clave'.ljust(8) + '|' + 'Descripción'.ljust(100) + '|' + 'Costo'.ljust(10) + '|')

        for record in platillos:
            print(f'{record[0]:<8}|{record[1]:<100}|{record[2]:<10}')

    def mostrar_platillo_header(self, header):
        print(str(header).center(180,'*'))
        print('-'*180)

    def mostrar_platillo_midder(self):
            print('/'*180)

    def mostrar_platillo_footer(self):
            print('*'*180)

#*******************************************************************************************************************************************************
    #Ver cliente(s)
#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************

    def mostrar_cliente(self, cliente):
        print('*****Información Cliente**********')
        print('ID: ', cliente[0])
        print('**********************************')
        print('Nombre: ', cliente[1])
        print('**********************************')
        print('Correo: ', cliente[2])
        print('**********************************')
        print('Direccion: ', cliente[3])
        print('**********************************') 
        print('Teléfono: ', cliente[4]) 
        print('**********************************')
        print('Usuario: ', cliente[5])
        print("**********************************")
        
    def mostrar_cliente_header(self, header):
            print(str(header).center(180,'*'))
            print('-'*180)

    def mostrar_cliente_midder(self):
            print('/'*180)

    def mostrar_cliente_footer(self):
            print('*'*180)


    def mostrar_clientes(self, clientes):
        print('\n' + 'ID'.ljust(5) + '|' + 'Nombre'.ljust(30) + '|'+'Correo'.ljust(25)+'|' +' Direccion'.ljust(60)+'|' +'Teléfono'.ljust(10)+'|' +' Usuario'.ljust(15))

        for record in clientes:
            print(f'{record[0]:<5}|{record[1]:<30}|{record[2]:<25}|{record[3]:<60}|{record[4]:<10}|{record[5]:<15}')

#*******************************************************************************************************************************************************
    #Ver empleado(s)
#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************


    def mostrar_empleado(self, empleado):
        print('*****Información empleado**********')
        print('ID: ', empleado[0])
        print('**********************************')
        print('Nombre: ', empleado[2])
        print('**********************************')
        print('Puesto: ', empleado[1])
        print('**********************************')
        print('Direccion: ', empleado[5])
        print('**********************************') 
        print('Teléfono: ', empleado[3]) 
        print('**********************************')
        print('Correo: ', empleado[4])
        print("**********************************")
        print('Sueldo: ', empleado[6])
        print("**********************************")
        print('Antiguedad: ', empleado[7])
        print("**********************************")
        print('Usuario: ', empleado[8])
        print("**********************************")
        
    def mostrar_empleado_header(self, header):
            print(str(header).center(180,'*'))
            print('-'*180)

    def mostrar_empleado_midder(self):
            print('/'*180)

    def mostrar_empleado_footer(self):
            print('*'*180)


    def mostrar_empleados(self, empleados):
        print('\n' + 'ID'.ljust(5) + '|' + 'Puesto'.ljust(8) + '|' + 'Nombre'.ljust(30) + '|' + 'Teléfono'.ljust(11) + '|'+'Correo'.ljust(25)+'|' +' Direccion'.ljust(60)+'|' +'Sueldo'.ljust(10)+'|' +'Antiguedad'.ljust(11)+'|' +' Usuario'.ljust(15))

        for record in empleados:
            print(f'{record[0]:<5}|{record[1]:<8}|{record[2]:<30}|{record[3]:<11}|{record[4]:<25}|{record[5]:<60}|{record[6]:<10}|{record[7]:<11}|{record[8]:<15}')

#*******************************************************************************************************************************************************
    #Ver ordenes
#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************


    def mostrar_orden(self, orden):
        print('*****Información de la Orden**********')
        print('Numero de Orden: ', orden[0])
        print('**********************************')
        print('Fecha: ', orden[1])
        print('**********************************')
        print('Platillo: ', orden[2])
        print('**********************************')
        print('Mesa: ', orden[3]) 
        print('**********************************')
        
    def mostrar_orden_header(self, header):
            print(str(header).center(180,'*'))
            print('-'*180)

    def mostrar_orden_midder(self):
            print('/'*180)

    def mostrar_orden_footer(self):
            print('*'*180)


    def mostrar_ordenes(self, ordenes):
        print('\n' + 'Orden'.ljust(7) + '|' + 'Fecha'.ljust(10) + '|' + 'Platillo'.ljust(10)  + '|'+'Mesa'.ljust(7)+'|' )

        for record in ordenes:
            print(f'{record[0]:<7}|{record[1]}|{record[2]:<10}|{record[3]:<7}|')

#*******************************************************************************************************************************************************
    #Ver Mesas
#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************


    def mostrar_mesa(self, mesa):
        print('*****Información de la mesas**********')
        print('Numero de mesa: ', mesa[0])
        print('**********************************')
        print('Numero de sillas: ', mesa[1])
        print('**********************************')
        print('Ubicacion de la mesa: ', mesa[2])
        print('**********************************')
        print('ID Empleado: ', mesa[3])
        print('**********************************') 
        print('Disponibilidad: ', mesa[4])
        print('**********************************') 

        
    def mostrar_mesas_header(self, header):
            print(str(header).center(180,'*'))
            print('-'*180)

    def mostrar_mesas_midder(self):
            print('/'*180)

    def mostrar_mesas_footer(self):
            print('*'*180)


    def mostrar_mesas(self, mesas):
        print('\n' + 'Mesa'.ljust(7) + '|' + 'Sillas'.ljust(10) + '|' + 'Ubicacion Mesa'.ljust(30) + '|' + 'ID Empleado'.ljust(15) + '|' + 'Disponibilidad'.ljust(20) + '|')

        for record in mesas:
            print(f'{record[0]:<7}|{record[1]:<10}|{record[2]:<30}|{record[3]:<15}|{record[4]:<20}')


#*******************************************************************************************************************************************************
    #Ver Reservaciones
#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************


    def mostrar_reservacion(self, reservacion):
        print('*****Datos de la reservación**********')
        print('ID Reservación: ', reservacion[0])
        print('**********************************')
        print('Fecha: ', reservacion[1])
        print('**********************************')
        print('Hora: ', reservacion[2])
        print('**********************************')
        print('ID Cliente: ', reservacion[3])
        print('**********************************') 
        print('Numero Personas: ', reservacion[4])
        print('**********************************') 


    def mostrar_reservacion_header(self, header):
        print(str(header).center(180,'*'))
        print('-'*180)

    def mostrar_reservacion_midder(self):
            print('/'*180)

    def mostrar_reservacion_footer(self):
            print('*'*180)


    def mostrar_reservaciones(self, reservaciones): #Ver en controlador
        print('\n' + 'ID'.ljust(5) + '|' + 'Fecha'.ljust(10) + '|'+'Hora'.ljust(10)+'|' +' ID Cliente'.ljust(15)+'|' +'Numero de personas'.ljust(30)+'|')

        for record in reservaciones:
            print(f'{record[0]:<5}|{record[1]:<10}|{record[2]}|{record[3]:<15}|{record[4]:<30}')


#*******************************************************************************************************************************************************
    #Ver Detalle-Ordenes
#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************

    def mostrar_detalle_orden_gerente(self,detalle_orden):
        print('*****Información sobre la orden**********')
        print('ID Detalle-Orden: ', detalle_orden[0])
        print('**********************************')
        print('Numero Orden: ', detalle_orden[1])
        print('**********************************')
        print('ID CLIENTE: ', detalle_orden[2])
        print('**********************************')
 



    def mostrar_detalle_orden(self, detalle_orden):
        print('*****Información sobre la orden**********')
        print('ID Detalle-Orden: ', detalle_orden[0])
        print('**********************************')
        print('Numero de Orden: ', detalle_orden[1])
        print('**********************************')
        print('Mesero: ', detalle_orden[2])
        print('**********************************')
        print('Nombre del Cliente: ', detalle_orden[3]) 
        print('**********************************') 
        print('Platillo: ', detalle_orden[4])
        print('**********************************') 
        print('Costo: ', detalle_orden[5]) 
        print('**********************************') 
        print('Mesa: ', detalle_orden[6]) 
        print('**********************************') 
        print('Ubicacion de mesa: ', detalle_orden[7]) 
        print('**********************************') 



    def mostrar_detalle_orden_header(self, header):
        print(str(header).center(180,'*'))
        print('-'*180)

    def mostrar_detalle_orden_midder(self):
            print('/'*180)

    def mostrar_detalle_orden_footer(self):
            print('*'*180)


    def mostrar_detalle_ordenes(self, detalle_ordenes): #Ver en controlador
        print('\n' + 'ID'.ljust(5) + '|' + 'Numero de orden'.ljust(15) + '|'+'Mesero'.ljust(25)+'|'+'Cliente'.ljust(30)+'|' +'Platillo'.ljust(60)+'|' +'Costo'.ljust(7)+'|'  +'Mesa'.ljust(6)+'|' +'Ubicacion de Mesa'.ljust(20)+'|')

        for record in detalle_ordenes:
            print(f'{record[0]:<5}|{record[1]:<15}|{record[2]:<25}|{record[3]:<30}|{record[4]:<60}|{record[5]:<7}|{record[6]:<6}|{record[7]:<20}')


#*******************************************************************************************************************************************************
    #Ver Detalle-Reservaciones
#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************


    def mostrar_detalle_reservacion_gerente(self,detalle_reservacion):
        print('*****Información sobre la reservacion**********')
        print('ID Detalle-Reserva: ', detalle_reservacion[0])
        print('**********************************')
        print('Clave reservación: ', detalle_reservacion[1])
        print('**********************************')
        print('Mesa: ', detalle_reservacion[2])
        print('**********************************')
        print('Disponibilidad: ', detalle_reservacion[3])
        print('**********************************')



    def mostrar_detalle_reservacion(self, detalle_reservacion):
        print('*****Información sobre la reservacion**********')
        print('ID Detalle-Reserva: ', detalle_reservacion[0])
        print('**********************************')
        print('Clave reservación: ', detalle_reservacion[1])
        print('**********************************')
        print('Nombre del Cliente: ', detalle_reservacion[4]) 
        print('**********************************') 
        print('Fecha: ', detalle_reservacion[2])
        print('**********************************')
        print('Hora: ', detalle_reservacion[3])
        print('**********************************') 
        print('Numero de personas: ', detalle_reservacion[5]) 
        print('**********************************') 
        print('Mesa: ', detalle_reservacion[6]) 

    def mostrar_detalle_reservacion_header(self, header):
        print(str(header).center(180,'*'))
        print('-'*180)

    def mostrar_detalle_reservacion_midder(self):
            print('/'*180)

    def mostrar_detalle_reservacion_footer(self):
            print('*'*180)


    def mostrar_detalle_reservaciones(self, detalle_reservaciones): #Ver en controlador
        print('\n' + 'ID'.ljust(5) + '|' + 'CLAVE DE RESERVACIÓN'.ljust(20) + '|'+'Cliente'.ljust(30)+'|' +'Fecha'.ljust(10)+'|' +'Hora'.ljust(10)+'|'  +'Numero de personas'.ljust(20)+'|' +'Mesa'.ljust(7)+'|')

        for record in detalle_reservaciones:
            print(f'{record[0]:<5}|{record[1]:<20}|{record[4]:<30}|{record[2]}|{record[3]:<10}|{record[5]:<20}|{record[6]:<7}|')



