# Importar datos
from lifestore_file import *

# Agregar a cada venta el mes
ventas_copia = lifestore_sales[:]
for venta in ventas_copia:
  mes = venta[3][3:5]
  venta.append(mes)

# Agregar a cada venta el monto
for venta in ventas_copia:
  for producto in lifestore_products:
    if venta[1] == producto[0]:
      venta.append(producto[2])

# Crear variable para organizar las ventas por mes
ventas_mensuales = []

# Agrupar las ventas por mes
while ventas_copia:
  mes = ventas_copia[0][5]
  ventas = 0
  monto = 0
  lista = []
  for venta in ventas_copia:
    if venta[5] == mes and venta[4] == 0:
      ventas += 1
      monto += venta[6]
      lista.append(venta)
    elif venta[5] == mes:
      lista.append(venta)
  ventas_mensuales.append([mes, ventas, monto])
  for agregado in lista:
    ventas_copia.remove(agregado)

# Crear una variable para los productos por categoria
categorias = []

# Agrupar los productos por categoria
auxiliar = lifestore_products[:]
while auxiliar:
  lista = []
  categoria = auxiliar[0][3]
  for elemento in auxiliar:
    if elemento[3] == categoria:
      categoria = auxiliar[0][3]
      lista.append(elemento)
  for agregado in lista:
    auxiliar.remove(agregado)
  categorias.append(lista)

# Ventas totales por producto
ventas_totales = []
for producto in lifestore_products:
    ventas = 0
    for venta in lifestore_sales:
        if producto[0] == venta[1]:
            ventas += 1
    ventas_totales.append([producto[0],ventas,producto[1],producto[2]])

# Agrupar ventas por categoría
ventas_por_categoria = []
for i in range(len(categorias)):
  lista = []
  for producto in categorias[i]:
    ventas = 0
    for venta in lifestore_sales:
        if producto[0] == venta[1]:
            ventas += 1
    lista.append([producto[0],ventas,producto[1],producto[2]*ventas])
  ventas_por_categoria.append(lista)

# Obtener cantidad total de búsquedas
busquedas_totales = []
for producto in lifestore_products:
    busquedas = 0
    for busqueda in lifestore_searches:
        if producto[0] == busqueda[1]:
            busquedas += 1
    busquedas_totales.append([producto[0],busquedas,producto[1]])

# Obtener reseña promedio por producto
score_global = []
lugar = 0
for producto in lifestore_products:
    score = 0
    for venta in lifestore_sales:
        if producto[0] == venta[1]:
            score += venta[2]
    if ventas_totales[lugar][1] != 0:
        score = score / ventas_totales[lugar][1]
    score_global.append([producto[0],score,producto[1]])
    lugar += 1

# Quitar productos no vendidos de las reseñas
no_vendidos = []
for producto in ventas_totales:
  if producto[1] == 0:
    no_vendidos.append(producto)
for producto in no_vendidos:
  for indice in score_global:
    if producto[0] == indice[0]:
      score_global.remove(indice)

# Obtener devoluciones por producto
devoluciones_totales = []
for producto in lifestore_products:
    devoluciones = 0
    for venta in lifestore_sales:
        if producto[0] == venta[1]:
            devoluciones += venta[4]
    devoluciones_totales.append([producto[0],devoluciones,producto[1]])

# Ventas brutas menos devoluciones
ventas_netas = []
for producto in ventas_totales:
    venta_neta = producto[1] - devoluciones_totales[producto[0]-1][1]
    ventas_netas.append([producto[0],venta_neta,producto[2],producto[3]*venta_neta])

# Ingresos a partir de las ventas netas
Ingresos = 0
for producto in ventas_netas:
  Ingresos += producto[3]


# Ordenar las ventas totales
ventas_totales_ordenadas = []
while ventas_totales:
    minimo = ventas_totales[0][1]
    elemento = ventas_totales[0]
    for venta in ventas_totales:
        if venta[1] < minimo:
            minimo = venta[1]
            elemento = venta
    ventas_totales_ordenadas.append(elemento)
    ventas_totales.remove(elemento)

# Ordenar las ventas netas
ventas_netas_ordenadas = []
while ventas_netas:
    minimo = ventas_netas[0][1]
    elemento = ventas_netas[0]
    for venta in ventas_netas:
        if venta[1] < minimo:
            minimo = venta[1]
            elemento = venta
    ventas_netas_ordenadas.append(elemento)
    ventas_netas.remove(elemento)

# Ordenar las ventas mensuales
ventas_mensuales_ordenadas = []
while ventas_mensuales:
  minimo = ventas_mensuales[0][2]
  elemento = ventas_mensuales[0]
  for mes in ventas_mensuales:
    if mes[2] < minimo:
      minimo = mes[2]
      elemento = mes
  ventas_mensuales_ordenadas.append(elemento)
  ventas_mensuales.remove(elemento)

# Agregar ventas promedio
for mes in ventas_mensuales_ordenadas:
  if mes[1] != 0:
    promedio = mes[2] / mes[1]
  else:
    promedio = 0
  mes.append(promedio)
# Invertir ventas promedio
ventas_mensuales_ordenadas = ventas_mensuales_ordenadas[::-1]

# Ordenar las ventas por categoría
ventas_ordenadas_categoria = []
for i in range(len(ventas_por_categoria)):
  lista = []
  while ventas_por_categoria[i]:
    minimo = ventas_por_categoria[i][0][1]
    elemento = ventas_por_categoria[i][0]
    for venta in ventas_por_categoria[i]:
      if venta[1] < minimo:
        minimo= venta[1]
        elemento = venta
    lista.append(elemento)
    ventas_por_categoria[i].remove(elemento)
  ventas_ordenadas_categoria.append(lista)
  
# Ordenar las búsquedas
busquedas_ordenadas = []
while busquedas_totales:
    minimo = busquedas_totales[0][1]
    elemento = busquedas_totales[0]
    for busqueda in busquedas_totales:
        if busqueda[1] < minimo:
            minimo = busqueda[1]
            elemento = busqueda
    busquedas_ordenadas.append(elemento)
    busquedas_totales.remove(elemento)


# Ordenar las reseñas
scores_ordenados = []
while score_global:
    minimo = score_global[0][1]
    elemento = score_global[0]
    for score in score_global:
        if score[1] < minimo:
            minimo = score[1]
            elemento = score
    scores_ordenados.append(elemento)
    score_global.remove(elemento)


# Listas con usuarios y contraseñas
usuarios = ['Admin', 'Javier', 'Mariana']
claves = ['admin', 'javier', 'mariana']

# Definir condiciones de parao para
# el menú y el login
salir_menu = '0'
login = 0

# Menú de inicio de sesión
while salir_menu == '0':
    print('\t *** Bienvenido al sistema de inteligencia de LifeStore ***')
    print('\n > Para iniciar sesión escribe tu nombre de usuario')
    print('\n > Para salir escribe "salir"')
    usuario = input('\nEntrada de usuario: ')
    for nombre in range(len(usuarios)):
        if usuario == usuarios[nombre]:
            clave = input('\nEscribe tu contraseña: ')
            if clave == claves[nombre]:
                print('\n Has iniciado sesión como ', usuarios[nombre] )
                salir_menu = '1'
                login = 1
                break
            else:
                print('Contraseña incorrecta.\nCerrando el sistema por motivos de seguridad\nPara más información contacta a tu administrador')
                salir_menu = '1'
        elif usuario == 'salir':
            print('Saliendo del menú...')
            print('Terminando todos los procesos...')
            print('Ejecución terminada')
            salir_menu = '1'
            break
    if login == 1:
        print('\n\n\t\t *** Inicio de sesión exitoso ***')
        salir_menu = '0'

    # Menú principal
    while login == 1 and salir_menu == '0':
        print('\n\n\t\t Escribe la opción que deseas consultar')
        print('\nListados de productos por ventas:')
        print('\n>1: Listado de los productos más vendidos')
        print('\n>2: Listado de los productos más buscados')
        print('\n>3: Listado de los productos menos vendidos por categoría')
        print('\n\nListados de productos por reseñas:')
        print('\n>4: Listado de los productos con mejores reseñas')
        print('\n>5: Listado de los productos con peores reseñas')
        print('\n\nAcciones administrativas:')
        print('\n>6: Resumen financiero de la empresa')
        print('\n>7: Agregar usuarios')
        print('\n\n>10: Regresar al menú de inicio de sesión')

        seleccion = input('\nEscribe el número de tu elección: ')

        if seleccion == '1':
            print('¿Desas consultar ventas brutas (incluyendo devoluciones) o netas?')
            tipo_consulta = input('Escribe 1 para ventas brutas y cualquier otra cosa para ventas netas: ')


            if tipo_consulta == '1':
                print('No.\tId\tDescripción\tVentas')
                for i in range(50):
                    print(i+1, '\t' , ventas_totales_ordenadas[len(ventas_totales_ordenadas)-(i+1)][0],'\t', ventas_totales_ordenadas[len(ventas_totales_ordenadas)-(i+1)][2], '\t',ventas_totales_ordenadas[len(ventas_totales_ordenadas)-(i+1)][1] )
                continuar = int(input('\n Si deseas hacer otra consulta escribe 0, de lo contrario escribe 1 :'))
                if continuar in ['0','1']:
                    salir_menu = continuar
                else:
                    print('Entrada no válida, regresando al menú')


            else:
                print('No.\tId\tDescripción\tVentas')
                for i in range(50):
                    print(i+1, '\t' , ventas_netas_ordenadas[len(ventas_netas_ordenadas)-(i+1)][0],'\t', ventas_netas_ordenadas[len(ventas_netas_ordenadas)-(i+1)][2], '\t',ventas_netas_ordenadas[len(ventas_netas_ordenadas)-(i+1)][1] )
                continuar = int(input('\n Si deseas hacer otra consulta escribe 0, de lo contrario escribe 1 :'))
                if continuar in ['0','1']:
                    salir_menu = continuar
                else:
                    print('Entrada no válida, regresando al menú')# Ventas netas



        elif seleccion == '2':
            print('No.\tId\tDescripción\tBúsquedas')
            for i in range(96):
                print(i+1, '\t', busquedas_ordenadas[len(busquedas_ordenadas)-(i+1)][0],'\t',busquedas_ordenadas[len(busquedas_ordenadas)-(i+1)][2],'\t',busquedas_ordenadas[len(busquedas_ordenadas)-(i+1)][1])
            continuar = input('\n Si deseas hacer otra consulta escribe 0, de lo contrario escribe 1 :')
            if continuar in ['0','1']:
                salir_menu = continuar
            else:
                print('Entrada no válida, regresando al menú')





        elif seleccion == '3':
            
            consulta = 1
            while consulta == 1:
              print('\nCategorías:')
              print('\n1: Procesadores \n2: Tarjetas de video \n3: Tarjetas madre \n4: Discos duros \n5: Memorias USB \n6: Pantallas \n7: Bocinas \n8: Audífonos')
              print('Presiona 0 para regresar al menú principal')
              categoria = input('Selecciona la categoría a consultar: ')
              
              if categoria == '1':
                print('No. \t Id \t Descripción \t Ventas')
                for i in range(len(ventas_ordenadas_categoria[0])):
                  print(i+1, '\t', ventas_ordenadas_categoria[0][i][0], '\t', ventas_ordenadas_categoria[0][i][2], '\t', ventas_ordenadas_categoria[0][i][1])
                input('Escribe cualquier tecla para regresar al menú anterior: ')
              elif categoria == '2':
                print('No. \t Id \t Descripción \t Ventas')
                for i in range(len(ventas_ordenadas_categoria[1])):
                  print(i+1, '\t', ventas_ordenadas_categoria[1][i][0], '\t', ventas_ordenadas_categoria[1][i][2], '\t', ventas_ordenadas_categoria[1][i][1])
                input('Escribe cualquier tecla para regresar al menú anterior: ')
                continue
              elif categoria == '3':
                print('No. \t Id \t Descripción \t Ventas')
                for i in range(len(ventas_ordenadas_categoria[2])):
                  print(i+1, '\t', ventas_ordenadas_categoria[2][i][0], '\t', ventas_ordenadas_categoria[2][i][2], '\t', ventas_ordenadas_categoria[2][i][1])
                input('Escribe cualquier tecla para regresar al menú anterior: ')
                continue
              elif categoria == '4':
                print('No. \t Id \t Descripción \t Ventas')
                for i in range(len(ventas_ordenadas_categoria[3])):
                  print(i+1, '\t', ventas_ordenadas_categoria[3][i][0], '\t', ventas_ordenadas_categoria[3][i][2], '\t', ventas_ordenadas_categoria[3][i][1])
                input('Escribe cualquier tecla para regresar al menú anterior: ')
                continue
              elif categoria == '5':
                print('No. \t Id \t Descripción \t Ventas')
                for i in range(len(ventas_ordenadas_categoria[4])):
                  print(i+1, '\t', ventas_ordenadas_categoria[4][i][0], '\t', ventas_ordenadas_categoria[4][i][2], '\t', ventas_ordenadas_categoria[4][i][1])
                input('Escribe cualquier tecla para regresar al menú anterior: ')
                continue
              elif categoria == '6':
                print('No. \t Id \t Descripción \t Ventas')
                for i in range(len(ventas_ordenadas_categoria[5])):
                  print(i+1, '\t', ventas_ordenadas_categoria[5][i][0], '\t', ventas_ordenadas_categoria[5][i][2], '\t', ventas_ordenadas_categoria[5][i][1])
                input('Escribe cualquier tecla para regresar al menú anterior: ')
                continue
              elif categoria == '7':
                print('No. \t Id \t Descripción \t Ventas')
                for i in range(len(ventas_ordenadas_categoria[6])):
                  print(i+1, '\t', ventas_ordenadas_categoria[6][i][0], '\t', ventas_ordenadas_categoria[6][i][2], '\t', ventas_ordenadas_categoria[6][i][1])
                input('Escribe cualquier tecla para regresar al menú anterior: ')
                continue
              elif categoria == '8':
                print('No. \t Id \t Descripción \t Ventas')
                for i in range(len(ventas_ordenadas_categoria[7])):
                  print(i+1, '\t', ventas_ordenadas_categoria[7][i][0], '\t', ventas_ordenadas_categoria[7][i][2], '\t', ventas_ordenadas_categoria[7][i][1])
                input('Escribe cualquier tecla para regresar al menú anterior: ')
                continue
              elif categoria == '0':
                consulta = 0
              else:
                print('Orden no reconocida')
            #Mostrar 3




        elif seleccion == '4':
            print('Productos con las mejores reseñas:')
            print('No.\tId\tDescripción\tScore')
            for i in range(20):
                print(i+1, '\t', scores_ordenados[len(scores_ordenados)-(i+1)][0], '\t', scores_ordenados[len(scores_ordenados)-(i+1)][2], '\t', scores_ordenados[len(scores_ordenados)-(i+1)][1])
            continuar = input('\n Si deseas hacer otra consulta escribe 0, de lo contrario escribe 1 :')
            if continuar in ['0','1']:
                salir_menu = continuar
            else:
                print('Entrada no válida, regresando al menú')


        elif seleccion == '5':
            print('Productos con las peores reseñas:')
            print('No.\tId\tDescripción\tScore')
            for i in range(20):
                print(i+1, '\t', scores_ordenados[i][0], '\t', scores_ordenados[i][2], '\t', scores_ordenados[i][1])
            continuar = input('\n Si deseas hacer otra consulta escribe 0, de lo contrario escribe 1 :')
            if continuar in ['0','1']:
                salir_menu = continuar
            else:
                print('Entrada no válida, regresando al menú')
            #Mostrar 5


        elif seleccion == '6':
            if usuario == 'Admin':
                print('\n\t\t***Resumen del año 2020***')
                print('\nIngresos anuales: $', Ingresos,'.00 pesos M/N')
                print('\nVentas mensuales (de mayor a menor):')
                print('Mes\t Ventas\t Monto \t Promedio')
                for mes in ventas_mensuales_ordenadas:
                  print('\n',mes[0], mes[1], mes[2], mes[3])
                print('En los meses no listados no se registraron ventas')
                print('\n*En los meses en ceros se reportaron ventas pero hubo devoluciones en el 100% de los casos')
                print('\nPromedio de ventas mensual: $', Ingresos/12, 'pesos M/N' )
                continuar = input('\n Si deseas hacer otra consulta escribe 0, de lo contrario escribe 1 :')
                if continuar in ['0','1']:
                    salir_menu = continuar
                else:
                    print('Entrada no válida, regresando al menú')
            else:
                print('ERROR: Solo los administradores pueden acceder a las opciones administrativas')
                continue

        elif seleccion == '7':
            if usuario == 'Admin':
                nuevo_usuario = input('\nIngresa el nuevo usuario: ')
                nueva_clave = input('\nIngresa la nueva contraseña: ')
                usuarios.append(nuevo_usuario)
                claves.append(nueva_clave)
            else:
                print('ERROR: Solo los administradores pueden acceder a las opciones administrativas')
                continue
        elif seleccion == '10':
            login = 0
            continue
        else:
            print('\n Orden no reconocida, regresando al menú')
            continue
    if login == 0 and salir_menu == '0':
        print('Usuario no registrado, inténtalo nuevamente')

# Mostrar al terminar el programa
print('\n\nSaliendo del sistema...')
