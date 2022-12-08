import mysql.connector

class Articulos:
    #Funcion que nos permite hacer nuesta conexion sql
    def abrir(self):
        conexion=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="artirulos-alejandra",
            port=3308
            )
        return conexion

    #Consulta sql para insertar un articulo
    def insertarArticulo(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into articulos(descripcion, precio) values (%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    #Consulta sql para consultar un articulo
    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    #Consulta sql para recuperar todos los datos de la tabla articulos
    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select codigo, descripcion, precio from articulos"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    #Consulta sql que nos permite eliminar un dato de la tabla
    def eliminar(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="delete from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount # retornamos la cantidad de filas borradas

    #Consulta sql que nos permite actualizar un dato
    def modificacion(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="update articulos set descripcion=%s, precio=%s where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount # retornamos la cantidad de filas modificadas