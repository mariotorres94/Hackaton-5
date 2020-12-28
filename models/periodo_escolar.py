from conexion.conn import Conexion

class Periodo_Escolar:
    def __init__(self,id_periodo='',nombre_periodo='',codigo_periodo=''):
        self.model = Conexion('periodo_escolar')
        self.id_periodo = id_periodo
        self.nombre_periodo = nombre_periodo
        self.codigo_periodo = codigo_periodo

    def obtain_periodo(self):
        return self.model.get_all()

    def insert_new_periodo(self):
        query = f"""
            INSERT INTO periodo_escolar(nombre_periodo,codigo_periodo) VALUES('{self.nombre_periodo}','{self.codigo_periodo}');
        """
        cursor = self.model.execute_query(query)
        self.model.commit()

    def update_periodo(self):
        query = f"""
            UPDATE periodo_escolar SET nombre_periodo = '{self.nombre_periodo}', codigo_periodo = '{self.codigo_periodo}'
            WHERE id_periodo = '{self.id_periodo}';
        """
        cursor = self.model.execute_query(query)
        self.model.commit()

    def delete_periodo(self):
        query = f"""
            DELETE FROM periodo_escolar WHERE id_periodo = '{self.id_periodo}';
        """
        cursor = self.model.execute_query(query)
        self.model.commit()