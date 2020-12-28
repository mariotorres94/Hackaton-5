from models.docentes import Docentes

class Docentes_Controller:
    def __init__(self):
        self.docente = Docentes()
        self.close = False

    def menu_docente(self):
        while True:
            try:
                print("\n\t       Docentes")
                print("\n\t----Menu de Opcion----")
                print("""
        1) Listar Docentes
        2) Registro Docente
        3) Actualizar datos de Docente
        4) Eliminar datos de Docente
        5) Salir
                """)

                opcion = int(input("Seleccione una opcion: "))

                if opcion == 1:
                    self.listar_docentes()
                elif opcion == 2:
                    self.registro_docentes()
                elif opcion == 3:
                    self.actualizar_datos_docente()
                elif opcion == 4:
                    self.eliminar_datos_docente()
                elif opcion == 5:
                    self.close =True
                    return True
                else: 
                    print("Valor seleccionado no existe en el menu, Intente nuevamente ...")
            except Exception as e:
                print(str(e))

    def listar_docentes(self):
        docentes = self.docente.obtain_docentes()
        if docentes:
            print("Lista de Docentes")
            print("ID DOCENTE   DNI          NOMBRES         APELLIDOS                   EMAIL             EDAD")
            for i in docentes:
                print(f"    ({i[0]})\t  ({i[1]})\t({i[2]})\t({i[3]})\t({i[4]})\t({i[5]})")
        else:
            print("No se encuentra ningun docente registrado en la base de datos")

    def registro_docentes(self):

        print("Registro")
        dni_profesor = input("Ingrese dni de docente: ")
        nombres = input("Ingrese nombres completo: ")
        apellidos = input("Ingrese apellidos completo: ")
        correo = input("Ingrese correo: ")
        edad = int(input("Ingrese edad: "))

        self.docente.dni_profesor = dni_profesor
        self.docente.nombres = nombres
        self.docente.apellidos = apellidos
        self.docente.correo = correo
        self.docente.edad = edad

        self.docente.insert_docente()

    def actualizar_datos_docente(self):
        self.listar_docentes()
        docentes = self.docente.obtain_docentes()
        
        id_profesor = int(input("Seleccione un alumno de la lista: "))
        self.docente.id_profesor = id_profesor

        print("Datos que Actualizara")
        print("---------------------")
        respuesta = input("¿Esta seguro de actualizar dni del docente? Y/N: ")

        if respuesta == 'Y' or respuesta == 'y':
            dni_profesor = input("Ingrese dni de docente: ")
            self.docente.dni_profesor = dni_profesor
        elif respuesta == 'N' or respuesta == 'n':
            for i in docentes:
                if i[0] == id_profesor:
                    dni_profesor = i[1]
                    self.docente.dni_profesor = dni_profesor
                    print(f"({i[0]})\t({i[1]})")
                    print(dni_profesor)
        
        respuesta = input("¿Esta seguro de actualizar nombres del docente? Y/N: ")
        if respuesta == 'Y' or respuesta == 'y':
            nombres = input("Ingrese nombres completos de docente: ")
            self.docente.nombres = nombres
        elif respuesta == 'N' or respuesta == 'n':
            for i in docentes:
                if i[0] == id_profesor:
                    nombres = i[2]
                    self.docente.nombres = nombres
                    print(f"({i[1]})\t({i[2]})")
                    print(nombres)

        respuesta = input("¿Esta seguro de actualizar apellidos del docente? Y/N: ")
        if respuesta == 'Y' or respuesta == 'y':
            apellidos = input("Ingrese apellidos completos de docente: ")
            self.docente.apellidos = apellidos
        elif respuesta == 'N' or respuesta == 'n':
            for i in docentes:
                if i[0] == id_profesor:
                    apellidos = i[3]
                    self.docente.apellidos = apellidos
                    print(f"({i[2]})\t({i[3]})")
                    print(apellidos)
        
        respuesta = input("¿Esta seguro de actualizar correo del docente? Y/N: ")
        if respuesta == 'Y' or respuesta == 'y':
            correo = input("Ingrese correo de docente: ")
            self.docente.correo = correo
        elif respuesta == 'N' or respuesta == 'n':
            for i in docentes:
                if i[0] == id_profesor:
                    correo = i[4]
                    self.docente.correo = correo
                    print(f"({i[3]})\t({i[4]})")
                    print(correo)
            
        self.docente.update_docente()

    def eliminar_datos_docente(self):
        self.listar_docentes()

        id_profesor = int(input("Seleccione docente que desea eliminar sus datos: "))
        self.docente.id_profesor = id_profesor

        respuesta = input("¿Esta seguro que desea eliminar los datos del id seleccionado? Y/N: ")

        if respuesta == 'Y' or respuesta == 'y':
            self.docente.delete_docente()
        else:
            self.menu_docente()

