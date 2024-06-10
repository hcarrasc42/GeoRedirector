import requests
from flask import Flask, redirect, request
import os

app = Flask(__name__)

num = 0  # Inicializa la variable num
redirect_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Enlace por defecto

def printHeader():
    header = '''
   ▄████ ▓█████  ▒█████   ██▀███  ▓█████ ▓█████▄  ██▓ ██▀███  ▓█████  ▄████▄  ▄▄▄█████▓ ▒█████   ██▀███  
  ██▒ ▀█▒▓█   ▀ ▒██▒  ██▒▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▓██▒▓██ ▒ ██▒▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
 ▒██░▄▄▄░▒███   ▒██░  ██▒▓██ ░▄█ ▒▒███   ░██   █▌▒██▒▓██ ░▄█ ▒▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
 ░▓█  ██▓▒▓█  ▄ ▒██   ██░▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌░██░▒██▀▀█▄  ▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
 ░▒▓███▀▒░▒████▒░ ████▓▒░░██▓ ▒██▒░▒████▒░▒████▓ ░██░░██▓ ▒██▒░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
  ░▒   ▒ ░░ ▒░ ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░▓  ░ ▒▓ ░▒▓░░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
   ░   ░  ░ ░  ░  ░ ▒ ▒░   ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒  ▒ ░  ░▒ ░ ▒░ ░ ░  ░  ░  ▒       ░      ░ ▒ ▒░   ░▒ ░ ▒░
 ░ ░   ░    ░   ░ ░ ░ ▒    ░░   ░    ░    ░ ░  ░  ▒ ░  ░░   ░    ░   ░          ░      ░ ░ ░ ▒    ░░   ░ 
       ░    ░  ░    ░ ░     ░        ░  ░   ░     ░     ░        ░  ░░ ░                   ░ ░     ░     
                                         ░                          ░                                   
                      proudly desing by ASHI02
    '''
    print(header)

def printMenu():
    print("proudly desing by ASHI02")
    print(" --------------------------------------------------MENU--------------------------------------------------")
    print(" |                                                                                                      |")
    print(" |                                               1- Exit                                                |")
    print(" |                                               2- Start                                               |")
    print(" |                                     3- Customize the redirect link                                   |")
    print(" |                                   4- Delete the file \"user_data.txt\"                                 |")
    print(" |                                                                                                      |")
    print(" --------------------------------------------------------------------------------------------------------")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        return "exit"
    elif opcion == "2":
        return "start"
    elif opcion == "3":
        global redirect_link
        nuevo_enlace = input("Ingrese el nuevo enlace de redirección: ")
        redirect_link = nuevo_enlace
    elif opcion == "4":
        if os.path.exists("user_data.txt"):
            confirmacion = input("¿Estás seguro que deseas eliminar el archivo? (yes/no): ")
            if confirmacion.lower() == "yes":
                os.remove("datos_usuarios.txt")
                print("El archivo ha sido eliminado.")
            else:
                print("Operación cancelada.")
        else:
            print("Este archivo no existe.")
    else:
        print("Opción inválida.")

    return None

def createReadmeFileES():
    if not os.path.exists("Readme_ES.txt"):
        with open("Readme_ES.txt", "w") as archivo:
            archivo.write("Instrucciones para el programa de redireccion web\n")
            archivo.write("Este programa de redireccion web fue creado con Python utilizando Flask. Su objetivo es recibir solicitudes web y redirigirlas a un enlace predeterminado o personalizado, mientras registra informacion sobre los usuarios que acceden al servicio.\n\n")
            archivo.write("Requisitos previos\n")
            archivo.write("- Python 3.x instalado en tu sistema.\n")
            archivo.write("- Dependencias Python instaladas. Puedes instalarlas ejecutando pip install -r requirements.txt.\n\n")
            archivo.write("Configuracion\n")
            archivo.write("- Descarga el codigo del programa.\n")
            archivo.write("- Abre una terminal y navega hasta el directorio donde se encuentra el codigo.\n")
            archivo.write("- Ejecuta el programa con el comando python GeoRedirection.py.\n\n")
            archivo.write("Uso\n")
            archivo.write("Una vez que el programa este en funcionamiento, puedes acceder a el desde un navegador web. Aqui hay algunas opciones disponibles en el menu:\n\n")
            archivo.write("1- Exit: Para salir del programa.\n")
            archivo.write("2- Start: Para comenzar el servicio de redireccion.\n")
            archivo.write("3- Customize the redirect link: Para personalizar el enlace de redireccion.\n")
            archivo.write("4- Delete the file \"user_data.txt\": Para eliminar el archivo de registro de usuarios.\n\n")
            archivo.write("Funcionamiento\n")
            archivo.write("Cuando el servicio esta activo, cualquier solicitud web recibida sera redirigida al enlace especificado.\n")
            archivo.write("Se registra informacion sobre el usuario que realizo la solicitud, incluida su direccion IP y datos de geolocalizacion.\n")
            archivo.write("Los datos registrados se guardan en un archivo llamado \"user_data.txt\".\n\n")
            archivo.write("Notas adicionales\n")
            archivo.write("Si deseas detener el programa, simplemente elige la opcion \"Exit\" en el menu o cierra la terminal donde se esta ejecutando el programa.\n")
            archivo.write("Asegurate de no eliminar el archivo user_data.txt accidentalmente, ya que contiene informacion importante sobre los usuarios que han accedido al servicio.\n")
            archivo.write("Disfruta utilizando el programa GeoRedirection\n")

def createReadmeFileEN():
    if not os.path.exists("Readme_EN.txt"):
        with open("Readme_EN.txt", "w") as archivo:
            archivo.write("Instructions for the web redirection program\n")
            archivo.write("This web redirection program was created using Python with Flask. Its purpose is to receive web requests and redirect them to a default or customized link, while logging information about the users accessing the service.\n\n")
            archivo.write("Prerequisites\n")
            archivo.write("- Python 3.x installed on your system.\n")
            archivo.write("- Python dependencies installed. You can install them by running pip install -r requirements.txt.\n\n")
            archivo.write("Setup\n")
            archivo.write("- Download the program code.\n")
            archivo.write("- Open a terminal and navigate to the directory where the code is located.\n")
            archivo.write("- Run the program using the command python GeoRedirection.py.\n\n")
            archivo.write("Usage\n")
            archivo.write("Once the program is running, you can access it from a web browser. Here are some options available in the menu:\n\n")
            archivo.write("1- Exit: To exit the program.\n")
            archivo.write("2- Start: To start the redirection service.\n")
            archivo.write("3- Customize the redirect link: To customize the redirection link.\n")
            archivo.write("4- Delete the file \"user_data.txt\": To delete the user data log file.\n\n")
            archivo.write("Operation\n")
            archivo.write("When the service is active, any incoming web request will be redirected to the specified link.\n")
            archivo.write("Information about the user who made the request, including their IP address and geolocation data, is logged.\n")
            archivo.write("The logged data is saved in a file named \"user_data.txt\".\n\n")
            archivo.write("Additional Notes\n")
            archivo.write("If you wish to stop the program, simply choose the \"Exit\" option in the menu or close the terminal where the program is running.\n")
            archivo.write("Be sure not to accidentally delete the user_data.txt file, as it contains important information about the users who have accessed the service.\n")
            archivo.write("Enjoy using the GeoRedirection program!\n")


def getClientIP():
    # Lista de cabeceras comunes que pueden contener la IP pública del cliente
    cabeceras = [
        'X-Forwarded-For',
        'X-Real-Ip',
        'HTTP_X_FORWARDED_FOR',
        'HTTP_X_REAL_IP'
    ]
    for cabecera in cabeceras:
        if cabecera in request.headers:
            # Obtenemos la IP desde la cabecera
            ip = request.headers[cabecera]
            # En caso de que haya múltiples IPs, tomamos la primera
            ip = ip.split(',')[0].strip()
            return ip
    # Si ninguna cabecera contiene la IP pública, usamos la dirección remota del request
    return request.remote_addr

@app.route('/')
def index():
    global num
    
    # Verificar si la solicitud es la principal
    if request.path == '/':
        num += 1
        ip = getClientIP()  # Obtiene la dirección IP pública del cliente
        if ip:
            try:
                response = requests.get(f'http://ip-api.com/json/{ip}')
                response.raise_for_status()  
                geolocation_data = response.json()
                with open('user_data.txt', 'a+') as archivo:  # Cambio de nombre y modo a 'a+'
                    archivo.write("\nUsuario " + str(num) + " => " + str(ip) + '\n')
                    for key, value in geolocation_data.items():
                        archivo.write(f"{key}: {value}\n")
                response = redirect(redirect_link)
                response.headers['ngrok-skip-browser-warning'] = 'false'
                return response
            except requests.exceptions.RequestException as e:
                print('Error al obtener la información de geolocalización:', e)
                return 'Error al obtener la información de geolocalización'
        else:
            return 'Error al obtener la dirección IP'
    else:
        return ''  # Ignorar cualquier solicitud que no sea la principal

if __name__ == '__main__':
    createReadmeFileES()
    createReadmeFileEN()
    while True:
        opcion = printMenu()
        if opcion == "start":
            break
        elif opcion == "exit":
            exit()  # Salir del programa por completo si elige "Exit"
    printHeader()
    app.run(host='0.0.0.0', port=5000)
