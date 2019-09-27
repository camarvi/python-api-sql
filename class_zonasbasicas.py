from db_conn import ConexionDB

class zonasbasicas:
    def __init__(self):
        self.__cod_zbs =""
        self.__zbs = ""
        self.db=ConexionDB()
        

    def listado_zonas(self):
        query = "SELECT COD_ZBS,ZBS FROM ZONAS_BASICAS WHERE ACTIVO=1 ORDER BY ZBS"
        return self.db.ejecutar(query)

    def busca_zona(self):
        query ="SELECT COD_ZBS,ZBS FROM ZONAS_BASICAS WHERE ACTIVO=1 AND COD_ZBS=? ORDER BY ZBS"
        valores =(self.__cod_zbs)
        return self.db.ejecutar(query, valores)
