from project.results import Results
from project.actions.read import File_csv
import os
from grapics.grap import Grap_view as gp
from tabulate import tabulate


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


# instancia del objeto multiples metodos
result = Results(route='./files')

print("""
Bienvenido a mi app, por favor antes de empezar
necesito saver cual es tu nombre.

""")
user_name = input("Por favor ingresa tu nombre: ")

clearConsole()
print(f"""

    Hola {user_name}, eligue una opcion:

    1) Ver Ganadores      2) Ver Grafica con los Ganadores
    3) Generar csv con ganadores  4) Generar jpg imagen con la grafica
    5) ...Más
    """
      )

option = int(input("-Elige una opcion :"))

if option == 1:
    clearConsole()

    # obtencion de los ganadores maximo 3 ganadores segun el limite
    winners = result.get_winners(limit=3)
    d = [[winners[0]['Full Name'], winners[0]['Score']], [winners[1]['Full Name'],
                                                          winners[1]['Score']], [winners[2]['Full Name'], winners[2]['Score']]]
    print("""

GANADORES - PRIMEROS 3

    """)
    print(tabulate(d, headers=['Nombre Completo', 'Puntaje']))
elif option == 2:
    clearConsole()
    winners = result.get_winners(limit=3)
    data_gp = {
        winners[0]['Full Name']: winners[0]['Score'],
        winners[1]['Full Name']: winners[1]['Score'],
        winners[2]['Full Name']: winners[2]['Score'],
    }

    grap = gp("Resultado Quizz", data=data_gp,
              destination_route="./result_files/img")
    print("""

GRAFICA - RESULTADOS

    """)
    print("""
    La Grafica fue abierta en ventana emergente.
    para CERRAR oprima CONTROL + C y finalize el programa.
    """)
    grap.show_graph()

elif option == 3:
    clearConsole()
    winners = result.get_winners(limit=3)
    # Generar un archivo csv con los resultados generales -- el archivo se genera en la carpeta result files
    status = File_csv.converto_csv(winners, "./result_files/csv")
    if status:
        print("El archivo con los resultados fue generado con exito en la ruta ./result_files/csv")
elif option == 4:
    clearConsole()
    winners = result.get_winners(limit=3)
    data_gp = {
        winners[0]['Full Name']: winners[0]['Score'],
        winners[1]['Full Name']: winners[1]['Score'],
        winners[2]['Full Name']: winners[2]['Score'],
    }

    grap = gp("Resultado Quizz", data=data_gp,
              destination_route="./result_files/img")
    print("""

IMAGEN JPG - GRAFICA RESULTADOS

    """)
    print("""
    La imagen JPG con el grafico resultado, fue guardado en la carpeta ./result_files/img
    por favor verifique, si no, vuelva intentarlo.
    """)
    grap.show_graph(save_png=True)
else:
    clearConsole()
    print("""

MAS OPCIONES

    """)
    print(f"""

    {user_name.title()}, eligue una opcion:

    1) Buscar Resultados por nombre   2) Obtener el puntaje Máximo
    3) Obtener el puntaje mínimo  4) Ver todos los resultados
    """
          )
    option2 = int(input("-Elige una opcion :"))

    if option2 == 1:
        clearConsole()
        # Buscar registro por nombre de alumno
        print("¿Que nombre quieres buscar?")
        name = input("Ingresa Nombre: ")
        student_result = find_by_name = result.get_data_by_name(name=name)
        d = []
        for item in student_result:
            d.append([item['Full Name'], item['Score']])
        print("""

RESULTADOS DE BUSQUEDA

        """)
        print(tabulate(d, headers=['Nombre Completo', 'Puntaje']))
    elif option2 == 2:
        clearConsole()
        # Obtener el puntaje maximo
        max_result = result.get_max_result
        print("""

PUNTAJE MÁXIMO

        """)
        print(f"""
        El máximo puntaje lo obtuvo {max_result['Full Name']}.

        Nombre: {max_result['Full Name']}
        Puntaje: {max_result['Score']}
        
        """)
    elif option2 == 3:
        clearConsole()
        # Obtener el puntaje minimo
        min_result = result.get_min_result
        print("""

PUNTAJE MINIMO

        """)
        print(f"""
        El minimo puntaje lo obtuvo {min_result['Full Name']}.

        Nombre: {min_result['Full Name']}
        Puntaje: {min_result['Score']}
        
        """)
    elif option2 == 4:
        clearConsole()
        # Ver el resultado de todos
        all_results = result.get_general_results
        d = []
        for item in all_results:
            d.append([item['Full Name'], item['Score']])
        print("""

RESULTADOS GENERALES

        """)
        print(tabulate(d, headers=['Nombre Completo', 'Puntaje']))
    else:
        clearConsole()
        print("""

OPCION INVALIDA

        """)
        print("Opcion Invalida, por favor reincie el programa.")


"""

Developed by: Daniel Ramos
App: Python app

"""
