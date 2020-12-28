from models.alumnos import Alumnos

class Alumnos_Controller:
    def __init__(self):
        self.alumno = Alumnos()
        self.close = False

    def menu_alumno(self):
        while True:
            try:
                print("\n\t       Alumnos")
                print("\n\t----Menu de Opcion----")
                print("""
        1) Listar Alumnos
        2) Registro Alumnos
        3) Actualizar datos de Alumno
        4) Eliminar datos de Alumnos
        5) Salir
                """)

                opcion = int(input("Seleccione una opcion: "))

                if opcion == 1:
                    self.listar_alumnos()
                elif opcion == 2:
                    self.registro_alumno()
                elif opcion == 3:
                    self.actualizar_datos_alumno()
                elif opcion == 4:
                    self.eliminar_datos_alumno()
                elif opcion == 5:
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
            print("ID ALUMNO          DNI             NOMBRES         APELLIDOS                 EDAD")
            for i in alumnos:
                print(f"  ({i[0]})           ({i[1]})     ({i[2]}   )      ({i[3]})            ({i[4]})")
        else:
            print("No se encuentra ningun alumno registrado en la base de datos")

    def registro_alumno(self):

        print("Registro")
        dni_alumno = input("Ingrese dni de alumno: ")
        nombres = input("Ingrese nombres completo: ")
        apellidos = input("Ingrese apellidos completo: ")
        edad = int(input("Ingrese edad: "))

        self.alumno.dni_alumno = dni_alumno
        self.alumno.nombres = nombres
        self.alumno.apellidos = apellidos
        self.alumno.edad = edad

        self.alumno.insert_alumno()

    def actualizar_datos_alumno(self):
        self.listar_alumnos()
        alumnos = self.alumno.obtain_alumnos()

        id_alumno = int(input("Seleccione un alumno de la lista: "))
        self.alumno.id_alumno = id_alumno

        print("Datos que Actualizara")
        print("---------------------")
        respuesta = input("¿Esta seguro de actualizar dni? Y/N:")
        
        if respuesta == 'Y' or respuesta == 'y':
            dni_alumno = input("Ingrese dni: ")
            self.alumno.dni_alumno = dni_alumno
        elif respuesta == 'N' or respuesta == 'n':
            for i in alumnos:
                if i[0] == id_alumno:
                    dni_alumno = i[1]
                    self.alumno.dni_alumno = dni_alumno
                    print(f"({i[0]})\t({i[1]})")
                    print(dni_alumno)

        respuesta = input("¿Esta seguro de actualizar nombres? Y/N:")
        if respuesta == 'Y' or respuesta == 'y':
            nombres = input("Ingrese nombre completo: ")
            self.alumno.nombres = nombres
        elif respuesta == 'N' or respuesta == 'n':
            for i in alumnos:
                if i[0] == id_alumno:
                    nombres = i[2]
                    self.alumno.nombres = nombres
                    print(f"({i[1]})\t({i[2]})")
                    print(nombres)

        respuesta = input("¿Esta seguro de actualizar apellidos? Y/N:")
        if respuesta == 'Y' or respuesta == 'y':
            apellidos = input("Ingrese apellidos completos: ")
            self.alumno.apellidos = apellidos
        elif respuesta == 'N' or respuesta == 'n':
            for i in alumnos:
                if i[0] == id_alumno:
                    apellidos = i[3]
                    self.alumno.apellidos = apellidos
                    print(f"({i[2]})\t({i[3]})")
                    print(nombres)
        
        self.alumno.update_alumno()
        
    def eliminar_datos_alumno(self):
        self.listar_alumnos()

        id_alumno = int(input("Seleccione alumno que desea eliminar sus datos: "))
        self.alumno.id_alumno = id_alumno

        respuesta = input("¿Esta seguro que desea eliminar los datos del id seleccionado? Y/N: ")

        if respuesta == 'Y' or respuesta == 'y':
            self.alumno.delete_alumno()
        else:
            self.menu_alumno()