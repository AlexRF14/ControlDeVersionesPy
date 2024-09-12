import os
import shutil
import re

# Función para salvar versión como .txt
def salvarVersión(nombre_archivo, numero_version):
    carpeta = "C:/Users/Usuario/Desktop/PythoonPruebas/PythonControlDeVersión/RutaDondeGuardarLasCosas"
    nombre_archivo_limpio = re.sub(r"commit_|_\d+$", "", nombre_archivo)
    versionPath = os.path.join(carpeta , f"commit_{nombre_archivo_limpio}_{numero_version}.py")
    ruta_destino = os.path.join(carpeta, f"{nombre_archivo}.py")
# Prueba de que se está guardando el archivo
    with open(versionPath, "w") as file:
        file.write(f"# Nombre del archivo: {nombre_archivo_limpio}\n")
        file.write(f"# Numero de la versión: {numero_version}\n")
        file.write("\n")
    print(f"Commit guardada en {versionPath}")
    
    try:
        shutil.copy(ruta_destino, versionPath)
    except FileNotFoundError:
        print("Error: El archivo que intentas guardar no existe.")
    except Exception as e:
        print(f"Error al copiar el archivo: {e}")

# Función para cargar versión
def cargarVersión(nombre_archivo):
    carpeta = "C:/Users/Usuario/Desktop/PythoonPruebas/PythonControlDeVersión/RutaDondeGuardarLasCosas"
    versionPath = os.path.join(carpeta , f"{nombre_archivo}.py")
    
    if os.path.exists(versionPath):
        with open(versionPath, "r") as file:
            data = file.read()
            return data
    else:
        print(f"Error: {nombre_archivo} no existe")
        return None
    
# Copia un archivo existente de la carpeta PythoonPruebas
def CopiarArchivo(NombreArchivo , nuevo_nombre):
    carpeta_destino = "C:/Users/Usuario/Desktop/PythoonPruebas/PythonControlDeVersión/RutaDondeGuardarLasCosas"
    carpeta_origen = "C:/Users/Usuario/Desktop/PythoonPruebas"
    ruta_origen = os.path.join(carpeta_origen , f"{NombreArchivo}.py")

    # Permite dejar o mofificar el nombre de la copia del archivo
    if nuevo_nombre:
        ruta_destino = os.path.join(carpeta_destino, f"{nuevo_nombre}.py")
    else:
        ruta_destino = os.path.join(carpeta_destino , f"{NombreArchivo}.py")
    
    try:
        # Copiar archivo a la carpeta RutaDondeGuardarLasCosas
        shutil.copy(ruta_origen, ruta_destino)
        print(f"Archivo copiado exitosamente a {ruta_destino}")
    except FileNotFoundError:
        print("Error: El archivo que intentas copiar no existe.")
    except Exception as e:
        print(f"Error al copiar el archivo: {e}")
        
# Visualizar los archivos de una carpeta
def visualizacionArchivos():
    carpeta = "C:/Users/Usuario/Desktop/PythoonPruebas/PythonControlDeVersión/RutaDondeGuardarLasCosas"
    if os.path.exists(carpeta):
        archivos = os.listdir(carpeta)
        if archivos:
            print("Archivos en la carpeta: ")
            for archivo in archivos:
                print(archivo)
        else:
            print("La carpeta está vacía.")
    else:
        print(f"Error: La carpeta {carpeta} no existe")

# Eliminar archivo
def eliminarArchivo(nombre_archivo):
    carpeta = "C:/Users/Usuario/Desktop/PythoonPruebas/PythonControlDeVersión/RutaDondeGuardarLasCosas"
    versionPath = os.path.join(carpeta , nombre_archivo)
    if os.path.exists(versionPath):
        os.remove(versionPath)
        print(f"Archivo {nombre_archivo} eliminado")
    else:
        print(f"Archivo no encontrado en la dirección {carpeta}")
def main():
    while True:
        print("\nSistema de control de versiones")
        print("1. Hacer un commit")
        print("2. Cargar versión")
        print("3. Copiar archivo ya existente")
        print("4. Visualizar los archivos")
        print("5. Eliminar archivos y commits")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_archivo = input("Ingrese el nombre del archivo: ")
            numero_version = input("Ingrese el nuevo número de la versión: ")
            carpeta_destino = "C:/Users/Usuario/Desktop/PythoonPruebas/PythonControlDeVersión/RutaDondeGuardarLasCosas"
            comparador_de_replicados = os.path.join(carpeta_destino , f"commit_{nombre_archivo}.py")
            
            if not os.path.exists(comparador_de_replicados):
                salvarVersión(nombre_archivo, numero_version)
            else:
                print(f"Nombre: {nombre_archivo} y versión: {numero_version} ya utilizados o no encontrados")
                
        elif opcion == "2":
            nombre_archivo = input("Ingrese el nombre del archivo: ")
            versionData = cargarVersión(nombre_archivo)
            if versionData:
                print(f"Datos cargados:\n{versionData}")
                
        elif opcion == "3":
            nombreArchivo = input("Ingrese el nombre del archivo que desea copiar: ")
            nuevo_nombre = input("Por si quieres modificar su nombre: ")
            CopiarArchivo(nombreArchivo , nuevo_nombre)
            
        elif opcion == "4":
            visualizacionArchivos()
            
        elif opcion == "5":
            nombre_archivo = input("Como se llama el archivo que quieres eliminar, incluya .py o .txt: ")
            eliminarArchivo(nombre_archivo)
            
        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
