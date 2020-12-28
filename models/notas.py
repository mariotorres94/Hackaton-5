from conexion.conn import Conexion

class Notas:
    def __init__(self,id_nota='',id_alumno='',notas=''):
        self.model = Conexion('notas')
        self.id_nota = id_nota
        self.id_alumno = id_alumno
        self.notas  = notas

    def obtain_notas(self):
        return self.model.get_all()

    def insert_notas(self):
        query = f"""
            INSERT INTO notas(notas) VALUES('{self.notas}');
        """
        cursor = self.model.execute_query(query)
        self.model.commit()

    def update_notas(self):
        query = f"""
            UPDATE notas SET notas = '{self.notas}'
            WHERE id_nota = {self.id_nota};
        """
        cursor = self.model.execute_query(query)
        self.model.commit()

    def delete_notas(self):
        query = f"""
            DELETE FROM notas WHERE id_nota = {self.id_nota} or id_alumno = {self.id_alumno};
        """
        cursor = self.model.execute_query(query)
        self.model.commit()