from crudMySQL import *


class usuarios:
    def mostrarClientes():
        try:
            cone = conexion.conexionBD()
            cursor = cone.cursor()
            cursor.execute("SELECT * FROM personal;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado



        except mysql.connector.Error as error:
            print("Error de mostrar datos {}".format(error))


    def ingresarUsuarios(cc,nombre,apellido,):
        try:
            cone = conexion.conexionBD()
            cursor = cone.cursor()
            sql = "insert into personal values(%s,%s,%s,null);"
            valores = (cc,nombre,apellido)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            cone.close()



        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))

    def modificacionDatos(cc,nombre,apellido,id):
        try:
            cone = conexion.conexionBD()
            cursor = cone.cursor()
            sql = "update personal set personal.cc = %s,personal.nombre = %s,personal.apellido = %s where personal.id = %s;"
            valores = (cc,nombre,apellido,id)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
            cone.close()



        except mysql.connector.Error as error:
            print("Error de actualizacion de datos {}".format(error))

    def eliminarUsuarios(id):
        try:
            cone = conexion.conexionBD()
            cursor = cone.cursor()
            sql = "delete from personal where personal.id  = %s;"
            valores = (id,)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            cone.close()



        except mysql.connector.Error as error:
            print("Error de eliminacion de datos {}".format(error))