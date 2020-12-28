from conexion.conn import Conexion

class Docentes:
    def __init__(self,id_profesor='', dni_profesor='', nombres='', apellidos='', correo='', edad=''):
        self.model = Conexion('docentes')
        self.id_profesor = id_profesor
        self.dni_profesor = dni_profesor
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo
        self.edad = edad        

    def obtain_docentes(self):
        return self.model.get_all()

    def insert_docente(self):
        query = f"""
            INSERT INTO docentes(dni_profesor,nombres,apellidos,correo,edad) VALUES('{self.dni_profesor}','{self.nombres}','{self.apellidos}','{self.correo}',{self.edad});
        """
        cursor = self.model.execute_query(query)
        self.model.commit()       

    def update_docente(self):
        query = f"""
            UPDATE docentes SET dni_profesor='{self.dni_profesor}', nombres='{self.nombres}', apellidos='{self.apellidos}', correo='{self.correo}'
            WHERE id_profesor = {self.id_profesor};
        """
        cursor = self.model.execute_query(query)
        self.model.commit()

    def delete_docente(self):
        query = f"""
            DELETE FROM docentes WHERE id_profesor = {self.id_profesor};
        """
        cursor = self.model.execute_query(query)
        self.model.commit() 