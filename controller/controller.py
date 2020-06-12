from model.model import Model
from view.view import View
from datetime import date

class Controller():

    #*********************************#
    #  A Controller for a Restaurant  #
    #*********************************#

    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        string, user = self.login()
        if(string == "NIE"):
            return
        if(string.upper() == "ES CLIENTE"):
            self.main_menu_cliente()
        else:
            self.main_menu_empleado(user)
        
        
#General Controllers
    def update_lists(self,fs,vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if(v!= ''):
                fields.append(f + ' = %s')
                vals.append(v)
        return fields, vals


#Metodos de verificacion de usuario.

    def login(self):
        n_intententos = 0
        print("Usuario: ")
        user = input()
        verificacion = self.model.user_verification(user)
        if(verificacion.upper() == 'ES CLIENTE'):
            while(n_intententos < 3):
                print("Contraseña: ")
                password = input()
                verify_password = self.model.verify_cliente_login(user,password)
                if(verify_password == True):
                    return [verificacion,user]
                else:
                    self.view.msg("CONTRASEÑA INCORRECTA")
                    n_intententos = n_intententos + 1
            else:
                self.view.msg("Excediste el número de intentos.")                    
                return ["NIE",None]
        else:
            while(n_intententos < 3):
                print("Contraseña: ")
                password = input()
                verify_password = self.model.verify_empleado_login(user,password)
                if(verify_password == True):
                    return [verificacion,user]
                else:
                    self.view.msg("CONTRASEÑA INCORRECTA")
                    n_intententos = n_intententos + 1
            else:
                self.view.msg("Excediste el número de intentos.")                    
                return ["NIE",None]

    def verificacion(self,user):
        record = self.model.read_puesto_by_user(user)
        if(record.upper() == 'GERENTE'):
            self.main_menu_gerente()
        else:
            self.view.error("NO TIENES PERMISOS DE ADMINISTRADOR.")
        return


#Controller Clientes

    #Inicio de Clientes
    def main_menu_cliente(self):
        o = ''
        while(o != '0'):
            self.view.menu_cliente()
            self.view.option('3')
            o = input()
            if(o == '1'):
                self.create_reservacion()
            elif(o == '2'):
                self.ver_reservacion()
            elif(o == '3'):
                self.mostrar_menu()
            elif(o == '0'):
                self.view.end()
            else:
                self.view.opcion_invalid()
        return

    def ask_reservacion(self):
        print("Fecha [AAAA-MM-DD]: ")
        fecha = input()
        print("Hora [HH-MM AM-PM]: ")
        hora = input()
        print("Nombre Completo: ")
        nombre = input()
        print("Numero de personas: ")
        n_personas = input()
        return[fecha,hora,nombre,n_personas]

    def create_reservacion(self):
        fecha,hora,nombre,n_personas = self.ask_reservacion()
        id_cliente = self.model.read_id_clienteByname(nombre)
        if(id_cliente == None):
            self.view.error("El Cliente no existe en el sistema")
            return
        record = self.model.create_reservacion(fecha,hora,id_cliente,n_personas)
        if(record == True):
            self.view.ok('Reservacion','creo')
            id_reservacion = self.model.read_reservacion_BY_nombre_fecha_hora_npersonas(nombre,fecha,hora,n_personas)
            self.view.msg("ENTREGA ESTA CLAVE AL RESTAURANT")
            self.view.ver_clave(id_reservacion)
        else:
            self.view.error('No se pudo crear la reservación')
        return
            
    def ver_reservacion(self):
        self.view.msg("Ingresa la clave de reservación")
        id_reservacion = input()
        rerservacion = self.model.read_reservacion(id_reservacion)
        if(type(rerservacion) == tuple):
            self.view.mostrar_reservacion(rerservacion)
        else:
            self.view.error("La reservación no existe.")
        return
        
    def mostrar_menu(self):
        self.view.platillo_menu()
        platillos = self.model.read_all_platillos()
        if(type(platillos) == list):
            self.view.mostrar_platillo_header('LISTADO DE PLATILLOS')
            self.view.mostrar_platillos(platillos)
        else:
            self.view.error("No existe ningún registro")
        return



#Controller Empleados

    #Inicio de Empleados
    def main_menu_empleado(self,user):
        o = ''
        while(o != '0'):
            self.view.menu_empleado()
            self.view.option('10')
            o = input()
            if(o == '1'):
                self.verificacion(user)
            elif(o == '2'):
                self.create_orden()
            elif(o == '3'):
                self.create_detalle_orden()
            elif (o == '4'):
                self.create_detalle_reserva()
            elif(o == '5'):
                self.ver_ordenes_dia()
            elif(o == '6'):
                self.ver_ordenes_fecha()
            elif(o == '7'):
                self.ver_orden_clave()
            elif(o == '8'):
                self.ver_detalle_orden()
            elif(o == '9'):
                self.ver_detalle_reserva()
            elif(o == '10'):
                self.cambio_estatus_mesa()
            elif(o == '0'):
                self.view.end()
            else:
                self.view.opcion_invalid()
        return

    def cambio_estatus_mesa(self):
        print("Mesa: ")
        mesa = input()
        print("Estatus: ")
        estado = input()
        record = self.model.cambio_estatus_mesa(mesa,estado)
        if(record == True):
            self.view.ok('El estatus de la mesa','se actualizo')
        else:
            self.view.error("No se pudo actualizar. Revisa!")
        return

    def ask_orden(self):
        fecha = date.today()
        print("Clave platillo: ")
        platillo = input()
        print("Mesa: ")
        mesa = input()
        return[fecha,platillo,mesa]

    def create_orden(self):
        fecha, platillo, mesa = self.ask_orden()
        record = self.model.create_orden(fecha,platillo,mesa)
        if(record == True):
            self.view.ok('La orden','agrego')
            numero_orden = self.model.read_numero_orden_BY_platillo_fecha_mesa(platillo,fecha,mesa)
            self.view.msg("SE GENERO EL NUMERO DE ORDEN\n\n")
            self.view.ver_clave(numero_orden)
            self.model.cambio_estatus_mesa(mesa,'ocupado')
        else:
            self.view.error("No se pudo crear el registro")
        return

    def ask_detalle_orden(self):
        print("Numero de orden: ")
        n_orden = input()
        print("Nombre(completo) de cliente: ")
        nombre = input()
        return [n_orden,nombre]

    def create_detalle_orden(self):
        n_orden, nombre = self.ask_detalle_orden()
        id_cliente = self.model.read_id_clienteByname(nombre)
        record = self.model.create_detalle_orden(n_orden,id_cliente)
        if(record == True):
            self.view.ok_double_id(n_orden,id_cliente,'agregaron')
        else:
            self.view.error("No se pudo crear el detalle de la orden")
        return

    def ask_detalle_reserva(self):

        print("ID Reservación: ")
        reservacion = input()
        n_personas = self.model.read_NPersonas_byID(reservacion)
        mesas_disponibles = self.model.read_mesas_disponibles()
        mesa_coincidente = ''
        mesa_lista = []

        if(type(mesas_disponibles) == list):
            #BUSCAR SI COINCIDEN EL NUMERO DE PERSONAS CON EL NUMERO DE SILLAS DE UNA MESA
            #    4 personas
            #  0  1  0  1  0  1  0  1  0  1 0  1  ...
            #[(1,1),(2,1),(4,2),(5,3),(6,3),(7,4),(8,4),(9,6),(10,6),(11,8),(12,8)]
            #  0      1     2     3     4     5    ... n
            for mesa_disp in mesas_disponibles:
                if(n_personas in mesa_disp[1]):
                    mesa_coincidente = mesa_disp[0]
                    break
           #ACOMODAMOS AL MAYOR NUMERO POSIBLE DE PERSONAS EN UNA MESA Y A LAS RESTANTES EN LAS DEMAS
            #    7 personas
            #  0 1   0 1   0 1   0 1   0 1   0 1   0  1  0 1    0 1 <-- MESA_DISP 
            #[(1,1),(2,1),(4,2),(5,3),(6,3),(7,4),(8,4),(9,6),(10,6),(11,8),(12,8)]
            # 10      9     8      7     6     5     4      3    2    1       0     
            if(mesa_coincidente == ''):
                mesas_disponibles.reverse()
                n_personas = int(n_personas)
                for mesa_disp in mesas_disponibles:
                    if(n_personas < int(mesa_disp[1])):
                        continue
                    else:
                        mesa_lista.append(mesa_disp[0])
                        n_sillas = int(mesa_disp[1])
                        n_personas = n_personas - n_sillas

            if(mesa_coincidente == ''):
                mesa = mesa_lista
                disponibilidad = []
                for i in range(len(mesa)):
                    disponibilidad.append('ocupado')
            else:
                mesa = mesa_coincidente
                disponibilidad = 'ocupado'

            return[reservacion,mesa,disponibilidad]

        else:
            self.view.error("Error al cargar los registros")

    def create_detalle_reserva(self):
        id_reservacion,mesa,disponibilidad = self.ask_detalle_reserva()
        if (type(mesa) == list and type(disponibilidad) == list):
            for i,j in zip(mesa,disponibilidad):
                #CREAMOS TANTOS DE DETALLES DE RESERVACION COMO MESAS SE HAYAN OCUPADO
                record = self.model.create_detalle_reservacion(id_reservacion,i,j)
                if(record == True):
                    self.view.ok_double_id(id_reservacion,i,'agregaron')
                else:
                    self.view.error("No se pudieron agregar los registros")
        else:
            record = self.model.create_detalle_reservacion(id_reservacion,mesa,disponibilidad)
            if(record == True):
                self.view.ok_double_id(id_reservacion,mesa,'agregaron')
            else:
                self.view.error("No se pudieron agregar los registros")
        return

    def ver_ordenes_dia(self):
        fecha = date.today()
        records = self.model.read_all_ordenes_fecha(fecha)
        if(type(records) == list):
            self.view.mostrar_orden_header("LISTADO DE ORDENES DEL DIA")
            self.view.mostrar_ordenes(records)
            self.view.mostrar_orden_midder()
            self.view.mostrar_orden_footer()
        else:
            self.view.error("Error al cargar los registros. Revisa")
        return

    def ver_ordenes_fecha(self):
        fecha = input("Ingrese la fecha a consultar [AAAA-MM-DD]\nFecha: ")
        records = self.model.read_all_ordenes_fecha(fecha)
        if(type(records) == list):
            self.view.mostrar_orden_header("LISTADO DE ORDENES DE " + fecha)
            self.view.mostrar_ordenes(records)
            self.view.mostrar_orden_midder()
            self.view.mostrar_orden_footer()
        else:
            self.view.error("Error al cargar los registros. Revisa")
        return

    def ver_orden_clave(self):
        numero_orden = input("Ingrese el numero de orden \nOrden: ")
        record = self.model.read_orden(numero_orden)
        if(type(record) == tuple):
            self.view.mostrar_orden_header("Datos de la orden")
            self.view.mostrar_orden(record)
            self.view.mostrar_orden_midder()
            self.view.mostrar_orden_footer()
        else:
            self.view.error("Error al cargar los registros. Revisa")
        return

    def ver_detalle_orden(self):
        nombre = input("Ingrese el nombre del cliente \nCliente: ")
        fecha = input("Ingrese la fecha de la orden \nFecha: ")
        records = self.model.read_detalle_orden(nombre,fecha)
        if(type(records) == list):
            if(len(records) == 1):
                self.view.mostrar_detalle_orden_header("Datos del detalle de orden por " + nombre + ". Fecha " + fecha)
                self.view.mostrar_detalle_orden(records[0])
                self.view.mostrar_detalle_orden_midder()
                self.view.mostrar_detalle_orden_footer()
            else:
                self.view.mostrar_detalle_orden_header("Datos del detalle de ordenes por " + nombre + ". Fecha " + fecha)
                self.view.mostrar_detalle_ordenes(records)
                self.view.mostrar_detalle_orden_midder()
                self.view.mostrar_detalle_orden_footer()                
        else:
            self.view.error("Error al cargar los registros. Revisa")
        return

    def ver_detalle_reserva(self):
        nombre = input("Ingrese el nombre del cliente \nCliente: ")
        fecha = input("Ingrese la fecha de la reservación \nFecha: ")
        records = self.model.read_detalle_reserva(nombre,fecha)
        if(type(records) == list):
            if(len(records) == 1):
                self.view.mostrar_detalle_reservacion_header("Datos del detalle de reservación por " + nombre + ". Fecha " + fecha)
                self.view.mostrar_detalle_reservacion(records)
                self.view.mostrar_detalle_reservacion_midder()
                self.view.mostrar_detalle_reservacion_footer()
            else:
                self.view.mostrar_detalle_reservacion_header("Datos del detalle de reservaciones por " + nombre + ". Fecha " + fecha)
                self.view.mostrar_detalle_reservaciones(records)
                self.view.mostrar_detalle_reservacion_midder()
                self.view.mostrar_detalle_reservacion_footer()                
        else:
            self.view.error("Error al cargar los registros. Revisa")
        return



#Controller Gerentes

    #Inicio de Gerentes

    def main_menu_gerente(self):
        o = ''
        while(o != '0'):
            self.view.menu_gerente()
            self.view.option('8')
            o = input()
            if(o == '1'):
                self.clientes_menu()
            elif(o == '2'):
                self.empleados_menu()
            elif(o == '3'):
                self.ordenes_menu()
            elif (o == '4'):
                self.mesas_menu()
            elif(o == '5'):
                self.platillos_menu()
            elif(o == '6'):
                self.reservaciones_menu()
            elif(o == '7'):
                self.detalle_ordenes_menu()
            elif(o == '8'):
                self.detalle_reservaciones_menu()
            elif(o == '0'):
                self.view.end()
            else:
                self.view.opcion_invalid()
        return


#Controller Admin Clientes
    def clientes_menu(self):
        o = ''
        while(o != '0'):
            self.view.submenu_clientes()
            self.view.option('5')
            o = input()
            if(o == '1'):
                self.create_cliente()
            elif(o == '2'):
                self.update_cliente()
            elif(o == '3'):
                self.read_cliente()
            elif(o == '4'):
                self.read_cliente_ByName()
            elif(o == '5'):
                self.delete_cliente()
            elif(o == '0'):
                self.view.end()
            else:
                self.view.opcion_invalid()
        return
    
    def ask_cliente(self):

        nombre = input("Nombre completo: ")
        correo = input("Correo: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        usuario = input("Usuario: ")
        password = input("Password: ")
        
        return [nombre,correo,direccion,telefono,usuario,password]
    
    def create_cliente(self):
        nombre,correo,direccion,telefono,usuario,password = self.ask_cliente()
        record = self.model.create_cliente(nombre,correo,direccion,telefono,usuario,password)
        if(record == True):
            self.view.ok("El cliente ","agrego")
            id_cliente = self.model.read_id_clienteByname(nombre)
            self.view.msg("LA CLAVE DEL CLIENTE ES")
            self.view.ver_clave(id_cliente)
        else:
            self.view.error("No se pudo crear el cliente. Revisa!")
        return

    def update_cliente(self):
        self.view.ask('INGRESE ID CLIENTE A MODIFICAR: ')
        id_cliente = input()
        user = self.model.read_cliente(id_cliente)
        if(type(user) == tuple):
            self.view.mostrar_cliente_header('Datos del cliente: ' + id_cliente)
            self.view.mostrar_cliente(user)
            self.view.mostrar_cliente_midder()
            self.view.mostrar_cliente_footer()
        else:
            if user == None:
                self.view.error('EL CLIENTE NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DEL CLIENTE. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_cliente()
        fields, vals = self.update_lists(['nombre','correo','direccion','telefono','usuario','pass'], whole_vals)
        vals.append(id_cliente)
        vals = tuple(vals)
        out = self.model.update_cliente(fields,vals)
        if(out == True):
            self.view.ok(id_cliente,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL CLIENTE. REVISA')

    def read_cliente(self):
        self.view.msg("CLAVE Cliente")
        id_cliente = input()
        record = self.model.read_cliente(id_cliente)
        if(type(record) == tuple):
            self.view.mostrar_cliente_header("Datos del cliente " + id_cliente)
            self.view.mostrar_cliente(record)
            self.view.mostrar_cliente_midder()
            self.view.mostrar_cliente_footer()
        else:
            self.view.error("El cliente no existe")
        return

    def read_cliente_ByName(self):
        self.view.msg("Nombre cliente (corto)")
        nombre = input()
        record = self.model.read_cliente_nombre(nombre)
        if(type(record) == list):
            self.view.mostrar_clientes(record)
            self.view.mostrar_cliente_midder()
            self.view.mostrar_cliente_footer()
        else:
            self.view.error("El cliente no existe")
        return

    def delete_cliente(self):
        self.view.ask('INGRESE ID CLIENTE A ELIMINAR: ')
        id_cliente = input()
        count = self.model.delete_cliente(id_cliente)
        if count != 0:
            self.view.ok(id_cliente,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR EL CLIENTE. REVISA")


#Controller Admin empleados
    def empleados_menu(self):
        o = ''
        while(o != '0'):
            self.view.submenu_empleados()
            self.view.option('5')
            o = input()
            if(o == '1'):
                self.create_empleado()
            elif(o == '2'):
                self.update_empleado()
            elif(o == '3'):
                self.read_empleado()
            elif(o == '4'):
                self.read_empleado_ByName()
            elif(o == '5'):
                self.delete_empleado()
            elif(o == '0'):
                self.view.end()
            else:
                self.view.opcion_invalid()
        return
    
    def ask_empleado(self):
        puesto = input("Puesto: ")
        nombre = input("Nombre completo: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        direccion = input("Dirección: ")
        sueldo = input("Sueldo: ")
        antiguedad = input("Antiguedad: ")
        usuario = input("Usuario: ")
        password = input("Password: ")

        return [puesto,nombre,telefono,correo,direccion,sueldo,antiguedad,usuario,password]
    
    def create_empleado(self):
        puesto, nombre, telefono, correo, direccion, sueldo,antiguedad,usuario,password = self.ask_empleado()
        record = self.model.create_empleado(puesto, nombre, telefono, correo, direccion, sueldo,antiguedad,usuario,password)
        if(record == True):
            self.view.ok("El empleado ","agrego")
            id_empleado = self.model.read_id_empleadoByname(nombre)
            self.view.msg("LA CLAVE DEL EMPLEADO ES")
            self.view.ver_clave(id_empleado)
        else:
            self.view.error("No se pudo crear el empleado. Revisa!")
        return

    def update_empleado(self):
        self.view.ask('INGRESE ID EMPLEADO A MODIFICAR: ')
        id_empleado = input()
        user = self.model.read_empleado(id_empleado)
        if(type(user) == tuple):
            self.view.mostrar_empleado_header('Datos del empleado: ' + id_empleado)
            self.view.mostrar_empleado(user)
            self.view.mostrar_empleado_midder()
            self.view.mostrar_empleado_footer()
        else:
            if user == None:
                self.view.error('EL EMPLEADO NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DEL EMPLEADO. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_empleado()
        fields, vals = self.update_lists(['puesto', 'nombre', 'telefono', 'correo', 'direccion', 'sueldo','antiguedad','usuario','pass'], whole_vals)
        vals.append(id_empleado)
        vals = tuple(vals)
        out = self.model.update_empleado(fields,vals)
        if(out == True):
            self.view.ok(id_empleado,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL EMPLEADO. REVISA')

    def read_empleado(self):
        self.view.msg("CLAVE empleado")
        id_empleado = input()
        record = self.model.read_empleado(id_empleado)
        if(type(record) == tuple):
            self.view.mostrar_empleado_header("Datos del empleado " + id_empleado)
            self.view.mostrar_empleado(record)
            self.view.mostrar_empleado_midder()
            self.view.mostrar_empleado_footer()
        else:
            self.view.error("El empleado no existe")
        return

    def read_empleado_ByName(self):
        self.view.msg("Nombre empleado (corto)")
        nombre = input()
        record = self.model.read_empleado_nombre(nombre)
        if(type(record) == list):
            self.view.mostrar_empleados(record)
            self.view.mostrar_empleado_midder()
            self.view.mostrar_empleado_footer()
        else:
            self.view.error("El empleado no existe")
        return

    def delete_empleado(self):
        self.view.ask('INGRESE ID EMPLEADO A ELIMINAR: ')
        id_empleado = input()
        count = self.model.delete_empleado(id_empleado)
        if count != 0:
            self.view.ok(id_empleado,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR EL EMPLEADO. REVISA")


#Controller Admin ordenes
    def ordenes_menu(self):
        o = ''
        while(o != '0'):
            self.view.submenu_ordenes()
            self.view.option('4')
            o = input()
            if(o == '1'):
                self.update_orden()
            elif(o == '2'):
                self.read_ordenes_fecha()
            elif(o == '3'):
                self.read_orden()
            elif(o == '4'):
                self.delete_orden()
            elif(o == '0'):
                self.view.end()
            else:
                self.view.opcion_invalid()
        return
    
    def ask_orden_update(self):
        fecha = input("Fecha [AAAA-MM-DD]: ")
        platillo = input("ID Platillo: ")
        num_mesa = input("Numero de mesa: ")
        
        return [fecha, platillo, num_mesa]
    

    def update_orden(self):
        self.view.ask('INGRESE NUMERO DE ORDEN A MODIFICAR: ')
        numero_orden = input()
        orden = self.model.read_orden(numero_orden)
        if(type(orden) == tuple):
            self.view.mostrar_orden_header('Datos de Orden: ' + numero_orden)
            self.view.mostrar_orden(orden)
            self.view.mostrar_orden_midder()
            self.view.mostrar_orden_footer()
        else:
            if orden == None:
                self.view.error('LA ORDEN NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DE LA ORDEN. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_orden_update()
        fields, vals = self.update_lists(['fecha', 'platillo', 'num_mesa'], whole_vals)
        vals.append(numero_orden)
        vals = tuple(vals)
        out = self.model.update_orden(fields,vals)
        if(out == True):
            self.view.ok(numero_orden,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA ORDEN. REVISA')

    def read_orden(self):
        self.view.msg("CLAVE orden")
        id_orden = input()
        record = self.model.read_orden(id_orden)
        if(type(record) == tuple):
            self.view.mostrar_orden_header("Datos del orden " + id_orden)
            self.view.mostrar_orden(record)
            self.view.mostrar_orden_midder()
            self.view.mostrar_orden_footer()
        else:
            self.view.error("La orden no existe")
        return

    def read_ordenes_fecha(self):
        self.view.msg("Fecha de las ordenes.")
        fecha = input()
        records = self.model.read_all_ordenes_fecha(fecha)
        if(type(records) == list):
            self.view.mostrar_orden_header("DATOS DE LAS ORDENES DE " + fecha)
            self.view.mostrar_ordenes(records)
            self.view.mostrar_orden_midder()
            self.view.mostrar_orden_footer()
        else:
            self.view.error("NO HAY REGISTROS")
        return

    def delete_orden(self):
        self.view.ask('INGRESE NUMERO DE ORDEN A ELIMINAR: ')
        id_orden = input()
        count = self.model.delete_orden(id_orden)
        if count != 0:
            self.view.ok(id_orden,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR LA ORDEN. REVISA") 


#Controller Admin mesas
    def mesas_menu(self):
        o = ''
        while(o != '0'):
            self.view.submenu_mesas()
            self.view.option('5')
            o = input()
            if(o == '1'):
                self.create_mesa()
            elif(o == '2'):
                self.update_mesa()
            elif(o == '3'):
                self.read_mesa()
            elif(o == '4'):
                self.read_all_mesas()
            elif(o == '5'):
                self.delete_mesa()
            elif(o == '0'):
                self.view.end()
            else:
                self.view.opcion_invalid()
        return
    
    def ask_mesas(self):

        n_sillas = input("Numero de sillas: ")
        ubicacion = input("Ubicacion: ")
        id_empleado = input("ID Empleado: ")
        disponibilidad = input("Disponibilidad: ")
        
        return [n_sillas,ubicacion,id_empleado,disponibilidad]

    def create_mesa(self):
        n_sillas,ubicacion,id_empleado,disponibilidad = self.ask_mesas()
        record = self.model.create_mesa(n_sillas,ubicacion,id_empleado,disponibilidad)
        if(record == True):
            self.view.ok("La mesa ","agrego")
        else:
            self.view.error("No se pudo crear la mesa. Revisa!")
        return

    

    def update_mesa(self):
        self.view.ask('INGRESE NUMERO DE MESA A MODIFICAR: ')
        numero_mesa = input()
        mesa = self.model.read_mesa(numero_mesa)
        if(type(mesa) == tuple):
            self.view.mostrar_mesas_header('Datos de mesa: ' + numero_mesa)
            self.view.mostrar_mesa(mesa)
            self.view.mostrar_mesas_midder()
            self.view.mostrar_mesas_footer()
        else:
            if mesa == None:
                self.view.error('LA MESA NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DE LA MESA. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_mesas()
        fields, vals = self.update_lists(['numero_sillas','ubicacion','id_empleado','disponibilidad'], whole_vals)
        vals.append(numero_mesa)
        vals = tuple(vals)
        out = self.model.update_mesa(fields,vals)
        if(out == True):
            self.view.ok(numero_mesa,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA MESA. REVISA')

    def read_mesa(self):
        self.view.msg("CLAVE mesa")
        id_mesa = input()
        record = self.model.read_mesa(id_mesa)
        if(type(record) == tuple):
            self.view.mostrar_mesas_header("Datos del mesa " + id_mesa)
            self.view.mostrar_mesa(record)
            self.view.mostrar_mesas_midder()
            self.view.mostrar_mesas_footer()
        else:
            self.view.error("La mesa no existe")
        return

    def read_all_mesas(self):
        records = self.model.read_all_mesas()
        if(type(records) == list):
            self.view.mostrar_mesas_header("DATOS DE LAS MESAS")
            self.view.mostrar_mesas(records)
            self.view.mostrar_mesas_midder()
            self.view.mostrar_mesas_footer()
        else:
            self.view.error("NO HAY REGISTROS")
        return

    def delete_mesa(self):
        self.view.ask('INGRESE NUMERO DE MESA A ELIMINAR: ')
        numero_mesa = input()
        count = self.model.delete_mesa(numero_mesa)
        if count != 0:
            self.view.ok(numero_mesa,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR LA MESA. REVISA") 


#Controller Admin platillos
    def platillos_menu(self):
        o = ''
        while(o != '0'):
            self.view.submenu_platillos()
            self.view.option('5')
            o = input()
            if(o == '1'):
                self.create_platillo()
            elif(o == '2'):
                self.update_platillo()
            elif(o == '3'):
                self.read_platillo()
            elif(o == '4'):
                self.read_all_platillos()
            elif(o == '5'):
                self.delete_platillo()
            elif(o == '0'):
                self.view.end()
            else:
                self.view.opcion_invalid()
        return
    
    def ask_platillo(self):

        descripcion = input("Descripción: ")
        costo = input("Costo: ")
        
        return [descripcion,costo]

    def create_platillo(self):
        descripcion,costo = self.ask_platillo()
        record = self.model.create_platillo(descripcion,costo)
        if(record == True):
            self.view.ok("El platillo ","agrego")
        else:
            self.view.error("No se pudo crear el platillo. Revisa!")
        return
    

    def update_platillo(self):
        self.view.ask('INGRESE CLAVE PLATILLO A MODIFICAR: ')
        i_platillo = input()
        platillo = self.model.read_platillo(i_platillo)
        if(type(platillo) == tuple):
            self.view.mostrar_platillo_header('Datos de platillo: ' + i_platillo)
            self.view.mostrar_platillo(platillo)
            self.view.mostrar_platillo_midder()
            self.view.mostrar_platillo_footer()
        else:
            if platillo == None:
                self.view.error('EL PLATILLO NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DEL PLATILLO. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_platillo()
        fields, vals = self.update_lists(['descripcion','costo'], whole_vals)
        vals.append(i_platillo)
        vals = tuple(vals)
        out = self.model.update_platillo(fields,vals)
        if(out == True):
            self.view.ok(i_platillo,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL PLATILLO. REVISA')

    def read_platillo(self):
        self.view.msg("CLAVE platillo")
        id_platillo = input()
        record = self.model.read_platillo(id_platillo)
        if(type(record) == tuple):
            self.view.mostrar_platillo_header("Datos del platillo " + id_platillo)
            self.view.mostrar_platillo(record)
            self.view.mostrar_platillo_midder()
            self.view.mostrar_platillo_footer()
        else:
            self.view.error("El platillo no existe")
        return

    def read_all_platillos(self):
        records = self.model.read_all_platillos()
        if(type(records) == list):
            self.view.mostrar_platillo_header("DATOS DE LOS PLATILLOS")
            self.view.mostrar_platillos(records)
            self.view.mostrar_platillo_midder()
            self.view.mostrar_platillo_footer()
        else:
            self.view.error("NO HAY REGISTROS")
        return

    def delete_platillo(self):
        self.view.ask('INGRESE NUMERO DE PLATILLO A ELIMINAR: ')
        platillo = input()
        count = self.model.delete_platillo(platillo)
        if count != 0:
            self.view.ok(platillo,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR EL PLATILLO. REVISA") 


#Controller Admin reservaciones
    def reservaciones_menu(self):
        o = ''
        while(o != '0'):
            self.view.submenu_reservaciones()
            self.view.option('4')
            o = input()
            if(o == '1'):
                self.update_reservacion()
            elif(o == '2'):
                self.read_reservaciones_fecha()
            elif(o == '3'):
                self.read_reservacion()
            elif(o == '4'):
                self.delete_reservacion()
            elif(o == '0'):
                self.view.end()
            else:
                self.view.opcion_invalid()
        return
    
    def ask_reservacion_update(self):
        fecha = input("Fecha [AAAA-MM-DD]: ")
        hora = input("Hora [HH:MM AM/PM]: ")
        id_cliente = input("ID Cliente: ")
        n_personas = input("Numero Personas: ")        
        return [fecha,hora,id_cliente,n_personas]
    

    def update_reservacion(self):
        self.view.ask('INGRESE CLAVE DE RESERVACION A MODIFICAR: ')
        id_reservacion = input()
        reservacion = self.model.read_reservacion(id_reservacion)
        fecha2 = date.today()
        if (reservacion[1] == fecha2):
            self.view.error("NO PUEDES ACTUALIZAR LA RESERVACIÓN, ES HOY!")
            return
        if(type(reservacion) == tuple):
            self.view.mostrar_reservacion_header('Datos de reservacion: ' + id_reservacion)
            self.view.mostrar_reservacion(reservacion)
            self.view.mostrar_reservacion_midder()
            self.view.mostrar_reservacion_footer()
        else:
            if reservacion == None:
                self.view.error('LA RESERVACION NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DE LA RESERVACION. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_reservacion_update()
        fields, vals = self.update_lists(['fecha','hora','id_cliente','n_personas'], whole_vals)
        vals.append(id_reservacion)
        vals = tuple(vals)
        out = self.model.update_reservacion(fields,vals)
        if(out == True):
            self.view.ok(id_reservacion,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA RESERVACION. REVISA')

    def read_reservacion(self):
        self.view.msg("CLAVE reservacion")
        id_reservacion = input()
        record = self.model.read_reservacion(id_reservacion)
        if(type(record) == tuple):
            self.view.mostrar_reservacion_header("Datos del reservacion " + id_reservacion)
            self.view.mostrar_reservacion(record)
            self.view.mostrar_reservacion_midder()
            self.view.mostrar_reservacion_footer()
        else:
            self.view.error("La reservacion no existe")
        return

    def read_reservaciones_fecha(self):
        self.view.msg("Fecha de las reservaciones.")
        fecha = input()
        records = self.model.read_all_reservaciones_fecha(fecha)
        if(type(records) == list):
            self.view.mostrar_reservacion_header("DATOS DE LAS reservacionES DE " + fecha)
            self.view.mostrar_reservaciones(records)
            self.view.mostrar_reservacion_midder()
            self.view.mostrar_reservacion_footer()
        else:
            self.view.error("NO HAY REGISTROS")
        return

    def delete_reservacion(self):
        self.view.ask('INGRESE NUMERO DE RESERVACION A ELIMINAR: ')
        id_reservacion = input()
        count = self.model.delete_reservacion(id_reservacion)
        if count != 0:
            self.view.ok(id_reservacion,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR LA reservacion. REVISA") 


#Controller Admin Detalle-Ordenes
    def detalle_ordenes_menu(self):
        o = ''
        while(o != '0'):
            self.view.submenu_detalle_ordenes()
            self.view.option('3')
            o = input()
            if(o == '1'):
                self.update_detalle_orden()
            elif(o == '2'):
                self.delete_detalle_orden()
            elif(o == '3'):
                self.read_detalle_orden()
            elif(o == '4'):
                self.read_detalle_ordenes_nombre_fecha()
            elif(o == '0'):
                self.view.end()
            else:
                self.view.opcion_invalid()
        return
    
    def ask_detalle_orden_update(self):
        
        numero_orden = input("NUMERO ORDEN: ")
        id_cliente = input("ID CLIENTE: ")

        return [numero_orden,id_cliente]
    

    def update_detalle_orden(self):
        self.view.ask('INGRESE LA CLAVE DE DETALLE DE ORDEN A MODIFICAR: ')
        id_detalle_orden = input()
        detalle_orden = self.model.read_detalle_orden_id(id_detalle_orden)
        if(type(detalle_orden) == tuple):
            self.view.mostrar_detalle_orden_header('Datos de detalle_orden: ' + id_detalle_orden)
            self.view.mostrar_detalle_orden_gerente(detalle_orden)
            self.view.mostrar_detalle_orden_midder()
            self.view.mostrar_detalle_orden_footer()
        else:
            if detalle_orden == None:
                self.view.error('EL DETALLE DE LA ORDEN NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DEL DETALLE DE ORDEN. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_detalle_orden_update()
        fields, vals = self.update_lists(['numero_orden','id_cliente'], whole_vals)
        vals.append(id_detalle_orden)
        vals = tuple(vals)
        out = self.model.update_detalle_orden(fields,vals)
        if(out == True):
            self.view.ok(id_detalle_orden,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR. REVISA')

    def read_detalle_orden(self):
        self.view.msg("CLAVE DETALLE ORDEN")
        id_detalle_orden = input()
        record = self.model.read_detalle_orden_id(id_detalle_orden)
        if(type(record) == tuple):
            self.view.mostrar_detalle_orden_header("DATOS DE DETALLE ORDEN" + id_detalle_orden)
            self.view.mostrar_detalle_orden_gerente(record)
            self.view.mostrar_detalle_orden_midder()
            self.view.mostrar_detalle_orden_footer()
        else:
            self.view.error("NO EXISTEN DATOS")
        return

    def read_detalle_ordenes_nombre_fecha(self):
        nombre = input("NOMBRE CLIENTE (COMPLETO): ")
        fecha = input("FECHA DE ORDEN: ")
        records = self.model.read_detalle_orden(nombre,fecha)
        if(type(records) == list):
            self.view.mostrar_detalle_orden_header("DATOS DE LOS DETALLES DE ORDEN POR " + nombre + " Y FECHA " + fecha)
            self.view.mostrar_detalle_ordenes(records)
            self.view.mostrar_detalle_orden_midder()
            self.view.mostrar_detalle_orden_footer()
        else:
            self.view.error("NO HAY REGISTROS")
        return

    def delete_detalle_orden(self):
        self.view.ask('INGRESE NUMERO DE DETALLE DE ORDEN A ELIMINAR: ')
        id_detalle_orden = input()
        count = self.model.delete_detalle_orden(id_detalle_orden)
        if count != 0:
            self.view.ok(id_detalle_orden,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR. REVISA") 


#Controller Admin Detalle-Reservaciones
    def detalle_reservaciones_menu(self):
        o = ''
        while(o != '0'):
            self.view.submenu_detalle_reservaciones()
            self.view.option('3')
            o = input()
            if(o == '1'):
                self.update_detalle_reservacion()
            elif(o == '2'):
                self.read_detalle_reservaciones_nombre_fecha()
            elif(o == '3'):
                self.read_detalle_reservacion()
            elif(o == '4'):
                self.delete_detalle_reservacion()
            elif(o == '0'):
                self.view.end()
            else:
                self.view.opcion_invalid()
        return
    
    def ask_detalle_reservacion_update(self):
        
        id_reservacion = input("ID RESERVACION: ")
        numero_mesa = input("NUMERO MESA: ")
        disponibilidad = input("DISPONIBILIDAD: ")

        return [id_reservacion,numero_mesa,disponibilidad]
    

    def update_detalle_reservacion(self):
        self.view.ask('INGRESE LA CLAVE DETALLE DE RESERVACION A MODIFICAR: ')
        id_detalle_reservacion = input()
        detalle_reservacion = self.model.read_detalle_reserva_id(id_detalle_reservacion)
        if(type(detalle_reservacion) == tuple):
            self.view.mostrar_detalle_reservacion_header('Datos de detalle_reservacion: ' + id_detalle_reservacion)
            self.view.mostrar_detalle_reservacion_gerente(detalle_reservacion)
            self.view.mostrar_detalle_reservacion_midder()
            self.view.mostrar_detalle_reservacion_footer()
        else:
            if detalle_reservacion == None:
                self.view.error('EL DETALLE DE LA RESERVACION NO EXISTE!')
            else:
                self.view.error('PROBLEMA AL RECUPERAR LOS DATOS DEL DETALLE DE RESERVACION. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_detalle_reservacion_update()
        fields, vals = self.update_lists(['id_reservacion','numero_mesa','disponibilidad'], whole_vals)
        vals.append(id_detalle_reservacion)
        vals = tuple(vals)
        out = self.model.update_detalle_reserva(fields,vals)
        if(out == True):
            self.view.ok(id_detalle_reservacion,'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR. REVISA')

    def read_detalle_reservacion(self):
        self.view.msg("CLAVE detalle reservacion")
        id_detalle_reservacion = input()
        record = self.model.read_detalle_reserva_id(id_detalle_reservacion)
        if(type(record) == tuple):
            self.view.mostrar_detalle_reservacion_header("DATOS DE DETALLE RESERVACION" + id_detalle_reservacion)
            self.view.mostrar_detalle_reservacion_gerente(record)
            self.view.mostrar_detalle_reservacion_midder()
            self.view.mostrar_detalle_reservacion_footer()
        else:
            self.view.error("NO EXISTEN DATOS")
        return

    def read_detalle_reservaciones_nombre_fecha(self):
        nombre = input("NOMBRE CLIENTE (COMPLETO): ")
        fecha = input("FECHA DE RESERVACION: ")
        records = self.model.read_detalle_reserva(nombre,fecha)
        if(type(records) == list):
            self.view.mostrar_detalle_reservacion_header("DATOS DE LOS DETALLES DE RESERVACION POR " + nombre + " Y FECHA " + fecha)
            self.view.mostrar_detalle_reservaciones(records)
            self.view.mostrar_detalle_reservacion_midder()
            self.view.mostrar_detalle_reservacion_footer()
        else:
            self.view.error("NO HAY REGISTROS")
        return

    def delete_detalle_reservacion(self):
        self.view.ask('INGRESE NUMERO DE DETALLE DE RESERVACION A ELIMINAR: ')
        id_detalle_reservacion = input()
        count = self.model.delete_detalle_reserva(id_detalle_reservacion)
        if count != 0:
            self.view.ok(id_detalle_reservacion,'elimino')
        else:
            self.view.error("NO SE PUDO ELIMINAR. REVISA") 


