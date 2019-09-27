from db_conn import ConexionDB

class centros:
    def __init__(self,cod_centro,cod_zbs,nombre):
        self.__cod_cen =cod_centro
        self.__cod_zbs = cod_zbs
        self.__nombre = nombre
        self.db=ConexionDB()

    def centrosugc(self):
        query = "SELECT COD_CEN,COD_ZBS,NOMBRE FROM CENTROS WHERE COD_ZBS=? ORDER BY NOMBRE"
        valores =(self.__cod_zbs)
        return self.db.ejecutar(query, valores)


    def nuevo_centro(self):
        query ='INSERT INTO CENTROS (cod_cen,cod_zbs,nombre) VALUES (?,?,?)'
        valores = (self.__cod_cen, self.__cod_zbs, self.__nombre)
        self.db.ejecutar(query, valores)

    def elimina_centro(self):
        query = "DELETE FROM CENTROS WHERE COD_CEN=?"
        valores = self.__cod_cen
        self.db.ejecutar(query, valores)
        