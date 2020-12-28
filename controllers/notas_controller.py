from models.notas import Notas
from models.alumnos import Alumnos

class Notas_Controller:
    def __init__(self):
        self.nota = Notas()
        self.alumno = Alumnos()
        self.close = False
    
    def menu_notas(self):
        while True:
            try:
                print("\n\t       Notas - Alumnos")
                print("\n\t----Menu de Opcion----")
                print("""
        1) Registro de Notas de Alumnos
        2) Actualizar datos de Alumno
        3) Eliminar datos de Alumnos
        4) Salir
                """)

                opcion = int(input("Seleccione una opcion: "))

                if opcion == 1:
                    self.registro_notas_alumno()
                elif opcion == 2:
                    self.actualizar_notas_alumno()
                elif opcion == 3:
                    self.eliminar_notas_alumno()
                elif opcion == 4:
                    self.close =True
                    return True                    
                else: 
                    print("Valor seleccionado no existe en el menu, Intente nuevamente ...")
            except Exception as e:
                print(str(e))

    def listar_alumnos(self):
        alumnos = self.alumno.obtain_alumnos()
        if alumnos:
            print("Lista de Alumnos")
            for i in alumnos:
                print(f"({i[0]})\t({i[1]})\t({i[2]})\t({i[3]})\t({i[4]})\t")
        else:
            print("No se encuentra ningun alumno registrado en la base de datos")

    def registro_notas_alumno(self):
        self.listar_alumnos()
        alumnos = self.alumno.obtain_alumnos()

        while True:
            try:
                id_alumno = int(input("Seleccion alumno a quien se le agregara la nota: "))
                self.alumno.id_alumno = id_alumno

                for i in alumnos:
                    if i[0] == id_alumno:
                        print("Id seleccionado se encuentra en la lista")
                        nombres = i[2]
                        self.alumno.nombres = nombres
                        """print(f"({i[1]})\t({i[2]})")
                        print(nombres)"""
                    else:
                        print("Id no se encuentra en la lista")
                
                if alumnos:
                    for i in alumnos:
                        id_nota = self.alumno.id_alumno
                        self.nota.id_nota = id_nota

                print(f"Registro de Notas {nombres}")
                print("-----------------")
                notas = float(input("Ingrese Nota: "))
                self.nota.notas = notas

                self.nota.insert_notas()
                break
            except Exception as e:
                print(str(e))

    def actualizar_notas_alumno(self):
        self.listar_alumnos()
        calificaciones = self.nota.obtain_notas()
        alumnos = self.alumno.obtain_alumnos()
        
        id_nota = int(input("Seleccione un alumno de la lista: "))
        self.nota.id_nota = id_nota

        print("Datos que Actualizara")
        print("---------------------")
        respuesta = input("¿Esta seguro de actualizar nota del alumno? Y/N: ")

        if respuesta == 'Y' or respuesta == 'y':
            if calificaciones:   
                for i in calificaciones:
                    if i[0] == id_nota:
                        notas = float(input("Ingrese nota de alumno: "))
                        notas = notas
                        self.nota.notas = notas
                        print(f"({i[0]})\t({i[2]})")
                        print(notas)
            
        elif respuesta == 'N' or respuesta == 'n':
            for i in calificaciones:
                if i[0] == id_nota:
                    notas = i[2]
                    self.nota.notas = notas
                    print(f"({i[0]})\t({i[2]})")
                    print(notas)
            
        self.nota.update_notas()

    def eliminar_notas_alumno(self):
        self.listar_alumnos()

        id_alumno = int(input("Seleccione alumno que desea eliminar sus datos: "))
        self.alumno.id_alumno = id_alumno

        respuesta = input("¿Esta seguro que desea eliminar los datos del id seleccionado? Y/N: ")

        if respuesta == 'Y' or respuesta == 'y':
            self.alumno.delete_alumno()
        else:
            self.menu_notas()