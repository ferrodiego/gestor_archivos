import os
from pathlib import Path
import shutil

#Ruta base del programa (directorio actual)
ruta_actual = Path.cwd()


def listar_contenido():
    """ Muestra el contenido del directorio actual (carpetas y archivos)"""
    print("\nContenido")
    for item in ruta_actual.iterdir():
       tipo = "📁" if item.is_dir() else "📄"
       print(f" {tipo} {item.name}")


def cambiar_directorio():
    """ Cambia el directorio actual """
    global ruta_actual
    listar_contenido()
    nombre = input("\n 🔀 Ingresa el nombre de la carpeta (.. para volver): ")
    ruta_nueva = ruta_actual / nombre
    if nombre == "..":
        ruta_actual = ruta_actual.parent
        print(f"🔙 Volviste a: {ruta_actual} ")
    elif ruta_nueva.exists() and ruta_nueva.is_dir():
        ruta_actual = ruta_nueva.resolve()
        print(f"📂 Ahora estas en : {ruta_actual}")
    else:
        print("❌ Carpeta no valida")
    

def crear_archivo():
    """Crea un archivo vacío si no existe."""
    nombre = input("📝 Ingrese el nombre del archivo con extension ej: nota.txt: ")
    archivo = ruta_actual / nombre
    if archivo.exists():
        print("⚠️El archivo ya existe")
    else:
        try:
            archivo.touch()
            print(f"✅ Archivo creado: {archivo.name}")
        except Exception as e:
            print(f"❌ Error al crear el archivo: {e}")


def eliminar_archivo():
    """
    Elimina un archivo del directorio actual si existe y el usuario confirma la acción.
    """
    nombre = input("🗑️ Ingrese el nombre del archivo a eliminar (con extension): ")
    archivo = ruta_actual / nombre
    if archivo.exists() and archivo.is_file():
        confirmacion = input(f" ⚠️ ¿Estas seguro de que quieres eliminar: {archivo.name}? (s/n)")
        if confirmacion.lower()== 's':
            try:
                archivo.unlink()
                print(f"✅ Archivo eliminado: {archivo.name}")
            except Exception as e:
                print(f"❌ Error al eliminar el archivo: {e}")
        else:
            print("❎ Eliminacion cancelada")
    else:
        print("❌ El archivo no existe.")


def renombrar_archivo():
    """ Renombramos un archivo q ya existe
    """
    listar_contenido()
    nombre_actual = input("✏️ Ingresa el nombre actual del archivo (con extension)")
    archivo_actual = ruta_actual / nombre_actual
    if not archivo_actual.exists():
        print("❌ El archivo no existe")
        return
    nuevo_nombre = input("🆕 Ingresa el nuevo nombre del archivo (con extension)")
    archivo_nuevo = ruta_actual / nuevo_nombre
    if archivo_nuevo.exists():
        print("⚠️ Ya existe un archivo con ese nombre")
        return
    try:
        archivo_actual.rename(archivo_nuevo)
        print(f"✅ Archivo renombrado: {archivo_nuevo.name}")
    except Exception as e:
        print(f"❌ Error al nombrar el archivo: {e}")
    
    

def mostrar_menu():
    """Muestra el menú principal de opciones."""
    print("###############################################################")
    print("")
    print("\n === 📁 GESTOR DE ARCHIVOS === ")
    print(f" Directorio actual: {ruta_actual}")
    print("1️⃣. Listar archivos y carpetas")
    print("2️⃣. Cambiar de Directorio")
    print("3️⃣. Crear archivos")
    print("4️⃣. Eliminar archivo")
    print("5️⃣. Renombrar archivo")
    print("6️⃣. Salir")


def main():
    """Función principal que controla el menú y las opciones."""
    while True:
        mostrar_menu()
        opcion = input("👉 Elige una opcion: ")
        
        if opcion == "1":
            listar_contenido()
        elif opcion == "2":
            cambiar_directorio()
        elif opcion == "3":
            crear_archivo()
        elif opcion == '4':
            eliminar_archivo()
        elif opcion == '5':
            renombrar_archivo()
        elif opcion == "6":
            print("👋 Hasta luego")
            break
        
        else:
            print("❌ opcion no valida, intente de nuevo. ")    


# Ejecutar solo si el archivo se corre directamente
if __name__ == "__main__":
    main()