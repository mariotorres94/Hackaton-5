from conexion.conn import Conexion

class Cursos:
    def __init__(self,id_curso='', nombre_curso='', codigo_curso=''):
        self.model = Conexion('cursos')
        self.id_curso = id_curso
        self.nombre_curso = nombre_curso
        self.codigo_curso = codigo_curso

    def obtain_cursos(self):
        return self.model.get_all()

    def insert_cursos(self):
        query = f"""
            INSERT INTO cursos(nombre_curso,codigo_curso) VALUES('{self.nombre_curso}','{self.codigo_curso}');
        """
        cursor = self.model.execute_query(query)
        self.model.commit()

    def update_curso(self):
        query = f"""
            UPDATE cursos SET nombre_curso='{self.nombre_curso}', codigo_curso='{self.codigo_curso}' 
            WHERE id_curso = {self.id_curso};
        """
        cursor = self.model.execute_query(query)
        self.model.commit()

    def delete_curso(self):
        query = f"""
            DELETE FROM cursos WHERE id_curso = {self.id_curso};
        """
        cursor = self.model.execute_query(query)
        self.model.commit()

    
