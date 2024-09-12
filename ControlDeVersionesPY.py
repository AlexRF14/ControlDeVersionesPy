import os
import shutil
import re

# Función para salvar versión como .py
def salvarVersión(nombre_archivo, numero_version):
    carpeta = "C:/Users/Usuario/Desktop/PythoonPruebas/PythonControlDeVersión/RutaDondeGuardarLasCosas"
    extension = os.path.splitext(nombre_archivo)[1]
    nombre_archivo_limpio = re.sub(r"commit_|_\d+$", "", os.path.splitext(nombre_archivo)[0])

    if extension in [".py", ".java", ".txt", ".docx"]:
        versionPath = os.path.join(carpeta, f"commit_{nombre_archivo_limpio}_{numero_version}{extension}")
        ruta_destino = os.path.join(carpeta, f"{nombre_archivo_limpio}{extension}")
    else:
        print("Error: Extensión no soportada.")
        return

    try:
        shutil.copy(ruta_destino, versionPath)
        with open(versionPath, "a") as file:
            file.write(f"# Nombre del archivo: {nombre_archivo_limpio}\n")
            file.write(f"# Numero de la versión: {numero_version}\n")
            file.write("\n")
        print(f"Commit guardada en {versionPath}")
    except FileNotFoundError:
        print("Error: El archivo que intentas guardar no existe.")
    except Exception as e:
        print(f"Error al copiar el archivo: {e}")
        
# Copia un archivo existente de la carpeta PythoonPruebas
def CopiarArchivo(nombre_archivo , nuevo_nombre):
    carpeta_destino = "C:/Users/Usuario/Desktop/PythoonPruebas/PythonControlDeVersión/RutaDondeGuardarLasCosas"
    carpeta_origen = "C:/Users/Usuario/Desktop/PythoonPruebas"
    
    extension = os.path.splitext(nombre_archivo)[1]
    ruta_origen = os.path.join(carpeta_origen, f"{nombre_archivo}")
    
    if extension in [".py", ".java", ".txt", ".docx"]:
        ruta_destino = os.path.join(carpeta_destino, f"{nombre_archivo}")
    else:
        print("Error: Extensión no soportada.")
        return

    # Permite dejar o modificar el nombre de la copia del archivo
    if nuevo_nombre:
        ruta_destino = os.path.join(carpeta_destino, f"{nuevo_nombre}{extension}")
    else:
        ruta_destino = os.path.join(carpeta_destino, f"{nombre_archivo}{extension}")

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
    extension = os.path.splitext(nombre_archivo)[1]

    if not extension:
        print("Error: Debes incluir la extensión del archivo.")
        return

    # Verifica que la extensión sea válida
    if extension not in [".py", ".java", ".txt", ".docx"]:
        print("Error: Extensión no soportada.")
        return

    versionPath = os.path.join(carpeta, f"{nombre_archivo}")

    try:
        # Verifica si el archivo existe y lo elimina
        if os.path.exists(versionPath):
            os.remove(versionPath)
            print(f"Archivo {nombre_archivo} eliminado")
        else:
            print(f"Archivo no encontrado en la dirección {carpeta}")
    except FileNotFoundError:
        print("Error: El archivo que intentas eliminar no existe.")
    except PermissionError:
        print("Error: No tienes permiso para eliminar el archivo.")
    except Exception as e:
        print(f"Error inesperado: {e}")
        
def main():
    while True:
        print("\nSistema de control de versiones")
        print("1. Hacer un commit")
        print("2. Copiar archivo ya existente")
        print("3. Visualizar los archivos")
        print("4. Eliminar archivos y commits")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_archivo = input("Ingrese el nombre del archivo: ")
            numero_version = input("Ingrese el nuevo número de la versión: ")
            carpeta_destino = "C:/Users/Usuario/Desktop/PythoonPruebas/PythonControlDeVersión/RutaDondeGuardarLasCosas"
            comparador_de_replicados = os.path.join(carpeta_destino , f"commit_{os.path.splitext(nombre_archivo)[0]}.py")
            
            if not os.path.exists(comparador_de_replicados):
                salvarVersión(nombre_archivo, numero_version)
            else:
                print(f"Nombre: {nombre_archivo} y versión: {numero_version} ya utilizados o no encontrados")
                
        elif opcion == "2":
            nombreArchivo = input("Ingrese el nombre del archivo que desea copiar: ")
            nuevo_nombre = input("Por si quieres modificar su nombre: ")
            CopiarArchivo(nombreArchivo , nuevo_nombre)
            
        elif opcion == "3":
            visualizacionArchivos()
            
        elif opcion == "4":
            nombre_archivo = input("Como se llama el archivo que quieres eliminar, incluya .py o .txt: ")
            eliminarArchivo(nombre_archivo)
            
        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
