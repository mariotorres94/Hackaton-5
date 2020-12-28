from controllers.alumnos_controller import Alumnos_Controller
from controllers.docentes_controller import Docentes_Controller
from controllers.cursos_controller import Cursos_Controller
from controllers.salones_controller import Salones_Controller
from controllers.notas_controller import Notas_Controller
from controllers.periodo_escolar_controller import Periodo_Escolar_Controller

alumnos = Alumnos_Controller()
docentes = Docentes_Controller()
cursos = Cursos_Controller()
salones = Salones_Controller()
notas = Notas_Controller()
periodo_escolar = Periodo_Escolar_Controller()

print("\n\t  Menu Principal")
print("\t------------------")
print("""\t
    \t1. Alumnos
    \t2. Docentes
    \t3. Cursos
    \t4. Salones
    \t5. Notas
    \t6. Periodo Escolar
    \t7. Salir
""")

opcion = int(input("Seleccione una opcion: "))

if opcion == 1:
    alumnos.menu_alumno()
elif opcion == 2:
    docentes.menu_docente()
elif opcion == 3:
    cursos.menu_cursos()
elif opcion == 4:
    salones.menu_salon()
elif opcion == 5:
    notas.menu_notas()
elif opcion == 6:
    periodo_escolar.menu_periodo_escolar()
elif opcion == 7:
    exit()