import os
import zipfile
from datetime import datetime
from tqdm import tqdm  # Barra de progreso

def validar_ruta(ruta: str) -> bool:
    """
    Verifica que la ruta exista y sea una carpeta válida.
    """
    if not os.path.exists(ruta):
        print(f"❌ La ruta no existe: {ruta}")
        return False
    if not os.path.isdir(ruta):
        print(f"❌ La ruta no es una carpeta válida: {ruta}")
        return False
    return True

def crear_respaldo(origen: str, destino: str) -> str:
    """
    Crea un archivo .zip con el respaldo de la carpeta origen, guardándolo en destino.
    """
    carpeta_respaldo = os.path.join(destino, "respaldos")
    os.makedirs(carpeta_respaldo, exist_ok=True)

    fecha_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_zip = f"respaldo_{fecha_hora}.zip"
    ruta_zip = os.path.join(carpeta_respaldo, nombre_zip)

    total_archivos = sum(len(files) for _, _, files in os.walk(origen))

    try:
        with zipfile.ZipFile(ruta_zip, 'w', zipfile.ZIP_DEFLATED, allowZip64=True) as zipf:
            with tqdm(total=total_archivos, desc="🔄 Creando respaldo", unit="archivo") as barra:
                for carpeta, _, archivos in os.walk(origen):
                    for archivo in archivos:
                        ruta_completa = os.path.join(carpeta, archivo)
                        arc_rel = os.path.relpath(ruta_completa, origen)

                        # 🚫 Evita incluir el archivo ZIP en construcción
                        if ruta_completa == ruta_zip:
                            continue

                        try:
                            zipf.write(ruta_completa, arc_rel)
                        except Exception as e:
                            print(f"⚠️ No se pudo añadir '{archivo}': {e}")
                        barra.update(1)
    except Exception as e:
        print(f"❌ Error durante la compresión: {e}")
        return ""

    return ruta_zip

def main():
    print("📦 Bienvenido al creador de respaldos ZIP\n")

    try:
        carpeta_origen = input("📁 Ingresa la ruta de la carpeta que quieres respaldar: ").strip()
        if not validar_ruta(carpeta_origen):
            return

        carpeta_destino = input("📂 Ingresa la ruta donde deseas guardar el respaldo: ").strip()
        if not validar_ruta(carpeta_destino):
            return

        # 🚫 Verifica que no se respalde dentro de la misma carpeta
        if os.path.commonpath([carpeta_origen]) == os.path.commonpath([carpeta_origen, carpeta_destino]):
            print("❌ No puedes guardar el respaldo dentro de la misma carpeta que estás respaldando.")
            print("💡 Por favor elige una carpeta de destino diferente.")
            return

        ruta_zip = crear_respaldo(carpeta_origen, carpeta_destino)
        if ruta_zip:
            print(f"\n✅ Respaldo completado con éxito en: {ruta_zip}")

    except KeyboardInterrupt:
        print("\n❌ Operación cancelada por el usuario.")

if __name__ == "__main__":
    main()