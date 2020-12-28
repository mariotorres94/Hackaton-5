from models.periodo_escolar import Periodo_Escolar

class Periodo_Escolar_Controller:
    def __init__(self):
        self.periodo_escolar = Periodo_Escolar()
        self.close = False

    def menu_periodo_escolar(self):
        while True:
            try:
                print("\n\t       Periodo Escolar")
                print("\n\t----Menu de Opcion----")
                print("""
        1) Listar Periodo Escolar
        2) Registro de Periodo
        3) Actualizar Periodo Escolar
        4) Eliminar Periodo Escolar
        5) Salir
                """)

                opcion = int(input("Seleccione una opcion: "))

                if opcion == 1:
                    self.listar_periodo_escolar()
                elif opcion == 2:
                    self.registro_periodo_escolar()
                elif opcion == 3:
                    self.actualizar_periodo_escolar()
                elif opcion == 4:
                    self.eliminar_datos_alumno()
                elif opcion == 5:
                    self.close = True
                    return True
                else: 
                    print("Valor seleccionado no existe en el menu, Intente nuevamente ...")
            except Exception as e:
                print(str(e))

    def listar_periodo_escolar(self):
        periodos = self.periodo_escolar.obtain_periodo()
        if periodos:
            print("Lista de Periodo Escolar")
            for i in periodos:
                print(f"({i[0]})\t({i[1]})\t({i[2]})")
        else:
            print("No se encuentra ningun periodo escolar registrado en la base de datos")

    def registro_periodo_escolar(self):

        print("Registro")
        nombre_periodo = input("Ingrese nombre del periodo: ")
        self.periodo_escolar.nombre_periodo = nombre_periodo
        for i in nombre_periodo:
            codigo_periodo = (nombre_periodo[0]+nombre_periodo[1]+nombre_periodo[2]).upper()+nombre_periodo[-4:]
            print(codigo_periodo)
            self.periodo_escolar.codigo_periodo = codigo_periodo

        self.periodo_escolar.insert_new_periodo()

    def actualizar_periodo_escolar(self):
        self.listar_periodo_escolar()
        periodos = self.periodo_escolar.obtain_periodo()

        id_periodo = int(input("Seleccione un periodo de la lista: "))
        self.periodo_escolar.id_periodo = id_periodo

        print("Datos que Actualizara")
        print("---------------------")
        respuesta = input("¿Esta seguro de actualizar periodo? Y/N:")
        
        if respuesta == 'Y' or respuesta == 'y':
            nombre_periodo = input("Ingrese nombre del periodo: ")
            self.periodo_escolar.nombre_periodo = nombre_periodo
            for i in nombre_periodo:
                codigo_periodo = (nombre_periodo[0]+nombre_periodo[1]+nombre_periodo[2]).upper()+nombre_periodo[-4:]
                self.periodo_escolar.codigo_periodo = codigo_periodo

        elif respuesta == 'N' or respuesta == 'n':
            for i in periodos:
                if i[0] == id_periodo:
                    nombre_periodo = i[1]
                    self.periodo_escolar.nombre_periodo = nombre_periodo
                    print(f"({i[0]})\t({i[1]})")
                    print(nombre_periodo)
                    for i in nombre_periodo:
                        codigo_periodo = (nombre_periodo[0]+nombre_periodo[1]+nombre_periodo[2]).upper()+nombre_periodo[-4:]
                        self.periodo_escolar.codigo_periodo = codigo_periodo
        
        self.periodo_escolar.update_periodo()
        
    def eliminar_datos_alumno(self):
        self.listar_periodo_escolar()

        id_periodo = int(input("Seleccione alumno que desea eliminar sus datos: "))
        self.periodo_escolar.id_periodo = id_periodo

        respuesta = input("¿Esta seguro que desea eliminar los datos del id seleccionado? Y/N: ")

        if respuesta == 'Y' or respuesta == 'y':
            self.periodo_escolar.delete_periodo()
        else:
            self.menu_periodo_escolar()