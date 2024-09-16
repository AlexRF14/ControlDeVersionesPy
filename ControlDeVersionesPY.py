import os
import shutil
import re
import tkinter as tk
from tkinter import messagebox

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

    if nuevo_nombre:
        # Si el nuevo nombre ya tiene una extensión, no agregamos otra
        if os.path.splitext(nuevo_nombre)[1]:
            ruta_destino = os.path.join(carpeta_destino, nuevo_nombre)
        else:
            ruta_destino = os.path.join(carpeta_destino, f"{nuevo_nombre}{extension}")
    else:
        ruta_destino = os.path.join(carpeta_destino, nombre_archivo)

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
    ventana = tk.Tk()
    ventana.title("Sistema de Control de Versiones")
    ventana.geometry("800x600")

    # Título
    tk.Label(ventana, text="Sistema de Control de Versiones", font=("Arial", 26)).pack(pady=10)

    # Botones de acciones
    tk.Button(ventana, text="Hacer un commit",font = ("Arial", 16),command=hacer_commit).pack(pady=20)
    tk.Button(ventana, text="Copiar archivo", font = ("Arial", 16), command=copiar_archivo).pack(pady=20)
    tk.Button(ventana, text="Visualizar archivos", font = ("Arial", 16) ,command=visualizacionArchivos).pack(pady=20)
    tk.Button(ventana, text="Eliminar archivo", font = ("Arial", 16) ,command=eliminar_archivo_interfaz).pack(pady=20)
    tk.Button(ventana, text="Salir", font = ("Arial", 16) ,command=ventana.quit).pack(pady=20)

    ventana.mainloop()

# Ventana para hacer commit
def hacer_commit():
    commit_ventana = tk.Toplevel()
    commit_ventana.title("Hacer un Commit")
    commit_ventana.geometry("400x270")

    tk.Label(commit_ventana, text="Nombre del archivo" , font=("Arial" , 16)).pack(pady=5)
    nombre_archivo = tk.Entry(commit_ventana , width = 50)
    nombre_archivo.pack(pady=10)

    tk.Label(commit_ventana, text="Número de la versión", font=("Arial" , 16)).pack(pady=5)
    numero_version = tk.Entry(commit_ventana, width= 5)
    numero_version.pack(pady=10)

    tk.Button(commit_ventana, text="Guardar Commit" ,font=("Arial" , 15) , command=lambda: salvarVersión(nombre_archivo.get(), numero_version.get())).pack(pady=40)

# Ventana para copiar archivo
def copiar_archivo():
    copiar_ventana = tk.Toplevel()
    copiar_ventana.title("Copiar Archivo")
    copiar_ventana.geometry("400x250")

    tk.Label(copiar_ventana, text="Nombre del archivo", font=("Arial" , 16)).pack(pady=5)
    nombre_archivo = tk.Entry(copiar_ventana, width=50)
    nombre_archivo.pack(pady=10)

    tk.Label(copiar_ventana, text="Nuevo nombre (opcional)", font=("Arial" , 16)).pack(pady=5)
    nuevo_nombre = tk.Entry(copiar_ventana, width=50)
    nuevo_nombre.pack(pady=10)

    tk.Button(copiar_ventana, text="Copiar" , font=("Arial" , 15), command=lambda: CopiarArchivo(nombre_archivo.get(), nuevo_nombre.get())).pack(pady=10)

# Ventana para eliminar archivo
def eliminar_archivo_interfaz():
    eliminar_ventana = tk.Toplevel()
    eliminar_ventana.title("Eliminar Archivo")
    eliminar_ventana.geometry("400x150")

    tk.Label(eliminar_ventana, text="Nombre del archivo", font=("Arial" , 16)).pack(pady=5)
    nombre_archivo = tk.Entry(eliminar_ventana, width=50)
    nombre_archivo.pack(pady=10)

    tk.Button(eliminar_ventana, text="Eliminar", font=("Arial" , 15), command=lambda: eliminarArchivo(nombre_archivo.get())).pack(pady=10)


if __name__ == "__main__":
    main()
