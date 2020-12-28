from models.cursos import Cursos

class Cursos_Controller:
    def __init__(self):
        self.curso = Cursos()
        self.close = False

    def menu_cursos(self):
        while True:
            try:
                print("\n\t       Cursos")
                print("\n\t----Menu de Opcion----")
                print("""
        1) Listar Cursos
        2) Registro Cursos
        3) Actualizar datos de Curso
        4) Eliminar datos de Cursos
        5) Salir
                """)

                opcion = int(input("Seleccione una opcion: "))

                if opcion == 1:
                    self.listar_cursos()
                elif opcion == 2:
                    self.registro_curso()
                elif opcion == 3:
                    self.actualizar_datos_curso()
                elif opcion == 4:
                    self.eliminar_datos_curso()
                elif opcion == 5:
                    self.close =True
                    return True
                else: 
                    print("Valor seleccionado no existe en el menu, Intente nuevamente ...")
            except Exception as e:
                print(str(e))

    def listar_cursos(self):
        cursos = self.curso.obtain_cursos()
        if cursos:
            print("Lista de Cursos")
            print("ID CURSO     NOMBRE                  CODIGO")
            for i in cursos:
                print(f"({i[0]})\t({i[1]})\t            ({i[2]})\t")
        else:
            print("No se encuentra ningun curso registrado en la base de datos")

    def registro_curso(self):

        print("Registro")
        nombre_curso = input("Ingrese nombre de curso: ")
        self.curso.nombre_curso = nombre_curso

        for i in nombre_curso:
            codigo_curso = (nombre_curso[0]+nombre_curso[1]+nombre_curso[2]).upper() 
            self.curso.codigo_curso = codigo_curso

        self.curso.insert_cursos()

    def actualizar_datos_curso(self):
        self.listar_cursos()
        cursos = self.curso.obtain_cursos()
        
        id_curso = int(input("Seleccione un curso de la lista: "))
        self.curso.id_curso = id_curso

        print("Datos que Actualizara")
        print("---------------------")

        respuesta = input("¿Esta seguro de actualizar nombre del curso? Y/N: ")
        if respuesta == 'Y' or respuesta == 'y':
            nombre_curso = input("Ingrese nuevo nombre del curso: ")
            self.curso.nombre_curso = nombre_curso
            for i in nombre_curso:
                codigo_curso = (nombre_curso[0]+nombre_curso[1]+nombre_curso[2]).upper()
                self.curso.codigo_curso = codigo_curso
        elif respuesta == 'N' or respuesta == 'n':
            for i in cursos:
                if i[0] == id_curso:
                    nombre_curso = i[1]
                    print(f"({i[0]})\t({i[1]})")
                    print(nombre_curso)
                    self.curso.nombre_curso = nombre_curso
                    for i in nombre_curso:
                        codigo_curso = (nombre_curso[0]+nombre_curso[1]+nombre_curso[2]).upper()
                        self.curso.codigo_curso = codigo_curso

        self.curso.update_curso()

    def eliminar_datos_curso(self):
        self.listar_cursos()

        id_curso = int(input("Seleccione alumno que desea eliminar sus datos: "))
        self.curso.id_curso = id_curso

        respuesta = input("¿Esta seguro que desea eliminar los datos del id seleccionado? Y/N: ")

        if respuesta == 'Y' or respuesta == 'y':
            self.curso.delete_curso()
        else:
            self.menu_cursos()
