import mysql.connector

class conexion:
    def conexionBD():
        try:
            conexion = mysql.connector.connect(user="root", password="root",
                                               host="localhost",
                                               database="usuarios",
                                               port="3306")

            print("Conexion Correcta")
            return conexion
        
        except mysql.connector.Error as error:
            print("Error al conectar a la BD: {}".format(error))
            return conexion
    conexionBD()





