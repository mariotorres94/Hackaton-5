from models.salones import Salones

class Salones_Controller:
    def __init__(self):
        self.salon = Salones()
        self.close = False

    def menu_salon(self):
        while True:
            try:
                print("\n\t       Salones")
                print("\n\t----Menu de Opcion----")
                print("""
        1) Listar Salones
        2) Registro Salon
        3) Editar datos de salon
        4) Eliminar datos de Salon
        5) Salir
                """)

                opcion = int(input("Seleccione una opcion: "))

                if opcion == 1:
                    self.listar_salones()
                elif opcion == 2:
                    self.registro_salon()
                elif opcion == 3:
                    self.actualizar_datos_salon()
                elif opcion == 4:
                    self.eliminar_datos_salon()
                elif opcion == 5:
                    self.close =True
                    return True
                else: 
                    print("Valor seleccionado no existe en el menu, Intente nuevamente ...")
            except Exception as e:
                print(str(e))

    def listar_salones(self):
        salones = self.salon.obtain_salones()
        if salones:
            print("Lista de Salones")
            for i in salones:
                print(f"({i[0]})\t({i[1]})")
        else:
            print("No se encuentra ningun salon registrado en la base de datos")

    def registro_salon(self):

        print("Registro")
        nombre_salon = input("Ingrese nombre de salon: ")

        self.salon.nombre_salon = nombre_salon

        self.salon.insert_salones()

    def actualizar_datos_salon(self):
        self.listar_salones()
        salones = self.salon.obtain_salones()
        
        id_salon = int(input("Seleccione un salon de la lista: "))
        self.salon.id_salon = id_salon

        print("Datos que Actualizara")
        print("---------------------")
        respuesta = input("¿Esta seguro de actualizar nombre de salon? Y/N: ")

        if respuesta == 'Y' or respuesta == 'y':
            nombre_salon = input("Ingrese nombre de salon: ")
            self.salon.nombre_salon = nombre_salon
        elif respuesta == 'N' or respuesta == 'n':
            for i in salones:
                if i[0] == id_salon:
                    nombre_salon = i[1]
                    self.salon.nombre_salon = nombre_salon
                    print(f"({i[0]})\t({i[1]})")
                    print(nombre_salon)
            
        self.salon.update_salon()

    def eliminar_datos_salon(self):
        self.listar_salones()

        id_salon = int(input("Seleccione salon que desea eliminar sus datos: "))
        self.salon.id_salon = id_salon

        respuesta = input("¿Esta seguro que desea eliminar los datos del id seleccionado? Y/N: ")

        if respuesta == 'Y' or respuesta == 'y':
            self.salon.delete_salon()
        else:
            self.menu_salon()


