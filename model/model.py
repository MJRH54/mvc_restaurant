from mysql import connector

class Model:
    """
    A data model with MySQL for a Restaurant
    """

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key,val) = line.strip().split(':')
                d[key] = val
            return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor(buffered=True)
        #self.cursor2 = self.cnx.cursor(buffered=True)

    def close_db(self):
        self.cnx.close()

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#------------------------------Clientes------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------


        #**************************************************************#
        #                        *  Clientes *                         #
        #**************************************************************#

    def create_cliente(self,nombre,correo,direccion,telefono,usuario,password):
        try:
            sql = 'INSERT INTO clientes(`nombre`,`correo`,`direccion`,`telefono`,`usuario`,`pass`) VALUES (%s,%s,%s,%s,%s,%s)'
            vals = (nombre,correo,direccion,telefono,usuario,password)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_user_cliente_by_user(self,user):
        try:
            sql = "SELECT usuario FROM clientes WHERE usuario = %s"
            vals = (user,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            if(record == None):
                return None
            return record[0]        
        except connector.Error as err:
            print(err)
            return err

    def read_cliente(self,id_cliente):
        try:
            sql = 'SELECT * FROM clientes WHERE id_cliente = %s'
            vals = (id_cliente,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_id_clienteByname(self,nombre):
        try:
            sql = "SELECT clientes.id_cliente FROM clientes WHERE nombre = %s"
            vals = (nombre,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            if(record == None):
                return None
            return record[0]        
        except connector.Error as err:
            return err

    def read_all_clientes(self):
        try:
            sql = 'SELECT * FROM clientes'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_cliente_nombre(self,nombre):
        try:
            sql = "SELECT * FROM clientes WHERE nombre LIKE " + "'%" + nombre + "%';"
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_cliente(self,fields,vals):
        try:
            sql = 'UPDATE clientes SET '+','.join(fields)+' WHERE id_cliente = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_cliente(self,id_cliente):
        try:
            sql = 'DELETE FROM clientes WHERE id_cliente = %s'
            vals = (id_cliente,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#-------------------------------Empleados----------------------------------------------------------------

        #**************************************************************#
        #                        *  Empleados *                         #
        #**************************************************************#

    def create_empleado(self,puesto,nombre,telefono,correo,direccion,sueldo,antiguedad,usuario,password):
        try:
            sql = 'INSERT INTO empleados(`puesto`,`nombre`,`telefono`,`correo`,`direccion`,`sueldo`,`antiguedad`,`usuario`,`pass`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            vals = (puesto,nombre,telefono,correo,direccion,sueldo,antiguedad,usuario,password)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def read_user_empleado_by_user(self,user):
        try:
            sql = "SELECT usuario FROM empleados WHERE usuario = %s"
            vals = (user,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            if(record == None):
                return None
            return record[0]        
        except connector.Error as err:
            return err  

    def read_id_empleadoByname(self,nombre):
        try:
            sql = "SELECT empleados.id_empleado FROM empleados WHERE nombre = %s"
            vals = (nombre,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record[0]        
        except connector.Error as err:
            return err

    def read_empleado(self,id_empleado):
        try:
            sql = 'SELECT * FROM empleados WHERE id_empleado = %s'
            vals = (id_empleado,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_empleados(self):
        try:
            sql = 'SELECT * FROM empleados'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_empleado_nombre(self,nombre):
        try:
            sql = "SELECT * FROM empleados WHERE nombre LIKE " + "'%" + nombre + "%';"
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_empleado(self,fields,vals):
        try:
            sql = 'UPDATE empleados SET '+','.join(fields)+' WHERE id_empleado = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_empleado(self,id_empleado):
        try:
            sql = 'DELETE FROM empleados WHERE id_empleado = %s'
            vals = (id_empleado,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#------------------------------Mesas---------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #                        *  Mesas  *                           #
        #**************************************************************#

    def create_mesa(self,numero_sillas,ubicacion,id_empleado,disponibilidad):
        try:
            sql = 'INSERT INTO mesas(`numero_sillas`,`ubicacion`,`id_empleado`,`disponibilidad`) VALUES (%s,%s,%s,%s)'
            vals = (numero_sillas,ubicacion,id_empleado,disponibilidad)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def cambio_estatus_mesa(self,mesa,registro):
        try:
            sql = "UPDATE mesas SET disponibilidad = %s WHERE numero_mesa = %s"
            vals = (registro,mesa)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            print(err)
            return err

    def read_mesa(self,numero_mesa):
        try:
            sql = 'SELECT * FROM mesas WHERE numero_mesa = %s'
            vals = (numero_mesa,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_mesas_disponibles(self):
        try:
            sql = "SELECT numero_mesa, numero_sillas FROM mesas WHERE disponibilidad = 'disponible';"
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err


    def read_all_mesas(self):
        try:
            sql = 'SELECT * FROM mesas'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_mesa_numero_sillas(self,numero_sillas):
        try:
            sql = "SELECT * FROM mesas WHERE numero_sillas = " + "'" + numero_sillas + "';"
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_mesa(self,fields,vals):
        try:
            sql = 'UPDATE mesas SET '+','.join(fields)+' WHERE numero_mesa = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_mesa(self,numero_mesa):
        try:
            sql = 'DELETE FROM mesas WHERE numero_mesa = %s'
            vals = (numero_mesa,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#------------------------------Reservaciones-------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #                        *  Reservaciones  *                   #
        #**************************************************************#

    def create_reservacion(self,fecha,hora,id_cliente,n_personas):
        try:
            sql = 'INSERT INTO reservaciones(`fecha`,`hora`,`id_cliente`,`n_personas`) VALUES (%s,%s,%s,%s)'
            vals = (fecha,hora,id_cliente,n_personas)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def read_reservacion(self,id_reservacion):
        try:
            sql = 'SELECT * FROM reservaciones WHERE id_reservacion = %s'
            vals = (id_reservacion,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_NPersonas_byID(self, id_reservacion):
        try:
            sql = 'SELECT n_personas FROM reservaciones WHERE id_reservacion = %s'
            vals = (id_reservacion,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record[0]
        except connector.Error as err:
            return err

    def read_reservacion_BY_nombre_fecha_hora_npersonas(self,nombre,fecha,hora,n_personas):
        try:
            id_cliente = self.read_id_clienteByname(nombre)
            sql = 'Select id_reservacion FROM reservaciones WHERE id_cliente = %s AND fecha = %s AND hora = %s AND n_personas = %s'
            vals = (id_cliente,fecha,hora,n_personas)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record[0]
        except connector.Error as err:
            return err


    def read_all_reservaciones_fecha(self,fecha):
        try:
            sql = 'SELECT * FROM reservaciones WHERE fecha = %s'
            vals=(fecha,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_all_reservacion_fecha_hora(self,fecha,hora):
        try:
            sql = "SELECT * FROM reservaciones WHERE fecha = %s AND hora = %s"
            vals = (fecha,hora)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_reservacion(self,fields,vals):
        try:
            sql = 'UPDATE reservaciones SET '+','.join(fields)+' WHERE id_reservacion = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_reservacion(self,id_reservacion):
        try:
            sql = 'DELETE FROM reservaciones WHERE id_reservacion = %s'
            vals = (id_reservacion,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#------------------------------Ordenes-------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #                        *  Ordenes  *                   #
        #**************************************************************#


    def create_orden(self,fecha,platillo,numero_mesa):
        try:
            sql = 'INSERT INTO ordenes(`fecha`,`platillo`,`numero_mesa`) VALUES (%s,%s,%s)'
            vals = (fecha,platillo,numero_mesa)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_orden(self,numero_orden):
        try:
            sql = 'SELECT * FROM ordenes WHERE numero_orden = %s'
            vals = (numero_orden,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err


    def read_all_ordenes_fecha(self,fecha):
        try:
            sql = 'SELECT * FROM ordenes WHERE fecha = %s'
            vals=(fecha,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_numero_orden_BY_platillo_fecha_mesa(self,platillo,fecha,mesa):
        try:
            sql = 'SELECT numero_orden FROM ordenes WHERE fecha = %s AND platillo = %s AND numero_mesa = %s'
            vals = (fecha,platillo,mesa)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record[0]
        except connector.Error as err:
            return err

    def update_orden(self,fields,vals):
        try:
            sql = 'UPDATE ordenes SET '+','.join(fields)+' WHERE numero_orden = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_orden(self,numero_orden):
        try:
            sql = 'DELETE FROM ordenes WHERE numero_orden = %s'
            vals = (numero_orden,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#------------------------------Platillos-------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #                        *  Platillos  *                   #
        #**************************************************************#


    def create_platillo(self,descripcion,costo):
        try:
            sql = 'INSERT INTO platillos(`descripcion`,`costo`) VALUES (%s,%s)'
            vals = (descripcion, costo)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def read_platillo(self,platillo):
        try:
            sql = 'SELECT * FROM platillos WHERE platillo = %s'
            vals = (platillo,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err


    def read_all_platillos(self):
        try:
            sql = 'SELECT * FROM platillos'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_platillo(self,fields,vals):
        try:
            sql = 'UPDATE platillos SET '+','.join(fields)+' WHERE platillo = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_platillo(self,platillo):
        try:
            sql = 'DELETE FROM platillos WHERE platillo = %s'
            vals = (platillo,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#------------------------------Datalle-Ordenes-----------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #                        *  Detalle-Ordenes  *                 #
        #**************************************************************#

    def create_detalle_orden(self,numero_orden,id_cliente):
        try:
            sql = 'INSERT INTO detalle_orden(`numero_orden`,`id_cliente`) VALUES (%s,%s)'
            vals = (numero_orden,id_cliente)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def read_detalle_orden_id(self,id_detalle_orden):
        try:
            sql = "SELECT * FROM detalle_orden WHERE id_detalle_orden = %s"
            vals = (id_detalle_orden,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err


    def read_detalle_orden(self,nombre,fecha):
        try:
            sql = "SELECT detalle_orden.id_detalle_orden, ordenes.numero_orden, empleados.nombre, clientes.nombre, platillos.descripcion, platillos.costo, mesas.numero_mesa, mesas.ubicacion FROM detalle_orden JOIN ordenes ON ordenes.numero_orden = detalle_orden.numero_orden JOIN platillos ON ordenes.platillo = platillos.platillo JOIN clientes ON clientes.id_cliente = detalle_orden.id_cliente JOIN mesas ON ordenes.numero_mesa = mesas.numero_mesa JOIN empleados ON mesas.id_empleado = empleados.id_empleado AND clientes.nombre = " + "'" + nombre + "' AND ordenes.fecha = " + "'" + fecha + "';"
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def update_detalle_orden(self,fields,vals):
        try:
            sql = 'UPDATE detalle_orden SET '+','.join(fields)+' WHERE id_detalle_orden = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def delete_detalle_orden(self,id_detalle_orden):
        try:
            sql = 'DELETE FROM detalle_orden WHERE id_detalle_orden = %s'
            vals = (id_detalle_orden,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#------------------------------Datalle-Reservaciones-----------------------------------------------------
#--------------------------------------------------------------------------------------------------------

        #**************************************************************#
        #                        *  Detalle-Reservaciones  *           #
        #**************************************************************#

    def create_detalle_reservacion(self,id_reservacion,numero_mesa,disponibilidad_mesa):
        try:
            sql = 'INSERT INTO detalle_reserva(`id_reservacion`,`numero_mesa`,`disponibilidad_mesa`) VALUES (%s,%s,%s)'
            vals = (id_reservacion,numero_mesa,disponibilidad_mesa)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def read_detalle_reserva_id(self,id_detalle_reserva):
        try:
            sql = "SELECT * FROM detalle_reserva WHERE id_detalle_reserva = %s"
            vals = (id_detalle_reserva,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_detalle_reserva(self,nombre,fecha):
        try:
            sql = "SELECT detalle_reserva.id_detalle_reserva, reservaciones.id_reservacion, reservaciones.fecha, reservaciones.hora, clientes.nombre, reservaciones.n_personas, mesas.numero_mesa FROM detalle_reserva JOIN reservaciones ON reservaciones.id_reservacion = detalle_reserva.id_reservacion JOIN clientes ON clientes.id_cliente = reservaciones.id_cliente JOIN mesas ON mesas.numero_mesa = detalle_reserva.numero_mesa AND clientes.nombre = " + "'" + nombre + "' AND  reservaciones.fecha = " + "'" +fecha + "';"
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def update_detalle_reserva(self,fields,vals):
        try:
            sql = 'UPDATE detalle_reserva SET '+','.join(fields)+' WHERE id_detalle_reserva = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_detalle_reserva(self,id_detalle_reserva):
        try:
            sql = 'DELETE FROM detalle_reserva WHERE id_detalle_reserva = %s'
            vals = (id_detalle_reserva,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err



#*******************************************************************************************************************************************************
#   User Verification
#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************

    def user_verification(self, user):
        cliente = self.read_user_cliente_by_user(user)
        empleado = self.read_user_empleado_by_user(user)

        if(cliente == None):
            return 'Es empleado'
        else:
            return 'Es cliente'


    def verify_cliente_login(self,user,password):
        try:
            sql = "SELECT pass FROM clientes WHERE usuario = %s"
            vals = (user,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            if(password == record[0]):
                return True
            return False
        except connector.Error as err:
            return err


    def verify_empleado_login(self,user,password):
        try:
            sql = "SELECT pass FROM empleados WHERE usuario = %s"
            vals = (user,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            if(password == record[0]):
                return True
            return False
        except connector.Error as err:
            return err

    def read_puesto_by_user(self,user):
        try:
            sql = "SELECT puesto FROM empleados WHERE usuario = %s"
            vals = (user,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record[0]
        except connector.Error as err:
            return err