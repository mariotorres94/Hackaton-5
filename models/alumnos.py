from conexion.conn import Conexion

class Alumnos(Conexion):
    def __init__(self, id_alumno='', dni_alumno='', nombres='', apellidos='', edad=''):
        self.model = Conexion('alumnos')
        self.id_alumno = id_alumno
        self.dni_alumno = dni_alumno
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad

    def obtain_alumnos(self):
        return self.model.get_all()

    def insert_alumno(self):
        query = f"""
            INSERT INTO alumnos(dni_alumno,nombres,apellidos,edad) VALUES('{self.dni_alumno}','{self.nombres}','{self.apellidos}',{self.edad});
        """
        cursor = self.model.execute_query(query)
        self.model.commit()       

    def update_alumno(self):
        query = f"""
            UPDATE alumnos SET dni_alumno='{self.dni_alumno}', nombres='{self.nombres}', apellidos='{self.apellidos}'
            WHERE id_alumno = {self.id_alumno};
        """
        cursor = self.model.execute_query(query)
        self.model.commit()

    def delete_alumno(self):
        query = f"""
            DELETE FROM alumnos WHERE id_alumno = {self.id_alumno};
        """
        cursor = self.model.execute_query(query)
        self.model.commit()
