import os
import shutil
import mysql.connector
from tkinter import messagebox
import tkinter as tk

# Función para conectar a la base de datos
def conectar_base_datos(nombre_usuario , nombre_contrasena):
    try:
        conexion = mysql.connector.connect(
            host= f"localhost",
            user=f"{nombre_usuario}",
            password=f"{nombre_contrasena}",
            database="control_versiones"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    # Función para iniciar sesion y abrir la ventana de opciones y cerrar la primera
def iniciar_sesion(nombre_usuario, nombre_contrasena, ventana_main):
    conexion_exitosa = conectar_base_datos(nombre_usuario, nombre_contrasena)
    if conexion_exitosa:
        print("Conexión exitosa. Iniciando opciones...")
        ventana_main.destroy()  # Cierra la ventana principal
        opciones()  # Si la conexión es exitosa, muestra las opciones
    else:
        print("Error: Usuario o contraseña incorrectos.")
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

# Guardar archivo en la base de datos
def guardar_archivo(nombre_archivo, tipo, contenido_binario):
    conexion = conectar_base_datos()
    if conexion is None:
        return
    cursor = conexion.cursor()
    query = "INSERT INTO documentos (nombre, tipo, contenido) VALUES (%s, %s, %s)"
    try:
        cursor.execute(query, (nombre_archivo, tipo, contenido_binario))
        conexion.commit()
        print(f"Archivo {nombre_archivo} guardado en la base de datos.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
    finally:
        conexion.close()

# Guardar una versión del archivo en la base de datos
def salvar_version_mysql(nombre_archivo, numero_version, contenido):
    conexion = conectar_base_datos()
    if conexion is None:
        return
    cursor = conexion.cursor()
    try:
        query_documento = "SELECT id FROM documentos WHERE nombre = %s"
        cursor.execute(query_documento, (nombre_archivo,))
        documento_id = cursor.fetchone()
        
        if documento_id:
            query = "INSERT INTO versiones (documento_id, version, contenido) VALUES (%s, %s, %s)"
            cursor.execute(query, (documento_id[0], numero_version, contenido))
            conexion.commit()
            print(f"Commit guardado como versión {numero_version}")
        else:
            print("Error: No se encontró el archivo.")
    except Exception as e:
        print(f"Error al guardar la versión: {e}")
    finally:
        conexion.close()

# Leer el contenido de un archivo en formato binario
def leer_contenido_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "rb") as archivo:
            return archivo.read()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

# Descargar archivo desde la base de datos
def cargar_archivo(nombre_archivo):
    conexion = conectar_base_datos()
    if conexion is None:
        return
    cursor = conexion.cursor()
    query = "SELECT contenido, tipo FROM documentos WHERE nombre = %s"
    cursor.execute(query, (nombre_archivo,))
    archivo = cursor.fetchone()
    
    if archivo:
        contenido_binario, tipo = archivo
        with open(f"{nombre_archivo}{tipo}", "wb") as file:
            file.write(contenido_binario)
        print(f"Archivo {nombre_archivo}{tipo} descargado.")
    else:
        print("Error: Archivo no encontrado.")
    conexion.close()

# Eliminar un archivo en la base de datos
def eliminar_archivo_mysql(nombre_archivo):
    conexion = conectar_base_datos()
    if conexion is None:
        return
    cursor = conexion.cursor()
    query = "DELETE FROM documentos WHERE nombre = %s"
    try:
        cursor.execute(query, (nombre_archivo,))
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"Archivo {nombre_archivo} eliminado de la base de datos.")
        else:
            print("Error: El archivo no existe en la base de datos.")
    except Exception as e:
        print(f"Error al eliminar el archivo: {e}")
    finally:
        conexion.close()

# Interfaz gráfica principal
def main():
    ventana = tk.Tk()
    ventana.title("Sistema de Control de Versiones")
    ventana.geometry("800x600")

    # Título
    tk.Label(ventana, text="Sistema de Control de Versiones", font=("Arial", 26)).pack(pady=10)
    tk.Label(ventana, text="Nombre de usuario", font=("Arial", 16)).pack(pady=5)
    nombre_usuario = tk.Entry(ventana, width=50)
    nombre_usuario.pack(pady=10)
    tk.Label(ventana, text="Contraseña", font=("Arial", 16)).pack(pady=5)
    nombre_contrasena = tk.Entry(ventana, width=50, show="*")  # Oculta la contraseña
    nombre_contrasena.pack(pady=10)
    
    tk.Button(ventana, text="Iniciar Sesión", font=("Arial", 15), 
              command=lambda: iniciar_sesion(nombre_usuario.get(), nombre_contrasena.get(), ventana)).pack(pady=40)

    ventana.mainloop()

# Botones de opciones y nueva ventana Main
def opciones():   
    ventana_opciones = tk.Tk()
    ventana_opciones.title("Opciones")
    ventana_opciones.geometry("800x600")
    
    tk.Label(ventana_opciones, text="OPCIONES", font=("Arial", 26)).pack(pady=10)
    tk.Button(ventana_opciones, text="Hacer un commit", font=("Arial", 16), command=hacer_commit).pack(pady=20)
    tk.Button(ventana_opciones, text="Copiar archivo", font=("Arial", 16), command=copiar_archivo).pack(pady=20)
    tk.Button(ventana_opciones, text="Visualizar archivos", font=("Arial", 16), command=visualizacion_archivos).pack(pady=20)
    tk.Button(ventana_opciones, text="Eliminar archivo", font=("Arial", 16), command=eliminar_archivo_interfaz).pack(pady=20)
    tk.Button(ventana_opciones, text="Salir", font=("Arial", 16), command=ventana_opciones.quit).pack(pady=20)

    ventana_opciones.mainloop()
    

# Ventana para hacer commit
def hacer_commit():
    commit_ventana = tk.Toplevel()
    commit_ventana.title("Hacer un Commit")
    commit_ventana.geometry("400x270")

    tk.Label(commit_ventana, text="Nombre del archivo", font=("Arial", 16)).pack(pady=5)
    nombre_archivo = tk.Entry(commit_ventana, width=50)
    nombre_archivo.pack(pady=10)

    tk.Label(commit_ventana, text="Número de la versión", font=("Arial", 16)).pack(pady=5)
    numero_version = tk.Entry(commit_ventana, width=5)
    numero_version.pack(pady=10)

    tk.Button(commit_ventana, text="Guardar Commit", font=("Arial", 15), 
              command=lambda: salvar_version_mysql(nombre_archivo.get(), numero_version.get(), leer_contenido_archivo(nombre_archivo.get()))).pack(pady=40)

# Ventana para copiar archivo (no implementada en MySQL, solo local)
def copiar_archivo():
    pass

# Visualización de archivos desde la base de datos (lista de documentos)
def visualizacion_archivos():
    conexion = conectar_base_datos()
    if conexion is None:
        return
    cursor = conexion.cursor()
    query = "SELECT nombre, tipo FROM documentos"
    cursor.execute(query)
    archivos = cursor.fetchall()
    
    if archivos:
        print("Archivos en la base de datos:")
        for archivo in archivos:
            nombre, tipo = archivo
            print(f"{nombre}{tipo}")
    else:
        print("No hay archivos en la base de datos.")
    conexion.close()

# Ventana para eliminar archivo
def eliminar_archivo_interfaz():
    eliminar_ventana = tk.Toplevel()
    eliminar_ventana.title("Eliminar Archivo")
    eliminar_ventana.geometry("400x150")

    tk.Label(eliminar_ventana, text="Nombre del archivo", font=("Arial", 16)).pack(pady=5)
    nombre_archivo = tk.Entry(eliminar_ventana, width=50)
    nombre_archivo.pack(pady=10)

    tk.Button(eliminar_ventana, text="Eliminar", font=("Arial", 15), 
              command=lambda: eliminar_archivo_mysql(nombre_archivo.get())).pack(pady=10)


if __name__ == "__main__":
    main()
