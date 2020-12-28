from conexion.conn import Conexion

class Salones:
    def __init__(self, id_salon='', nombre_salon=''):
        self.model = Conexion('salones')
        self.id_salon = id_salon
        self.nombre_salon = nombre_salon

    def obtain_salones(self):
        return self.model.get_all()

    def insert_salones(self):
        query = f"""
            INSERT INTO salones(nombre_salon) VALUES('{self.nombre_salon}');
        """
        cursor = self.model.execute_query(query)
        self.model.commit()

    def update_salon(self):
        query = f"""
            UPDATE salones SET nombre_salon = '{self.nombre_salon}'
            WHERE id_salon = '{self.id_salon}';
        """
        cursor = self.model.execute_query(query)
        self.model.commit()

    def delete_salon(self):
        query = f"""
            DELETE FROM salones WHERE id_salon = '{self.id_salon}';
        """
        cursor = self.model.execute_query(query)
        self.model.commit()
