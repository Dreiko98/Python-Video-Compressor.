import subprocess
from pathlib import Path
from moviepy.editor import VideoFileClip
import time

def comprimir(input_video_path, output_video_path):
    command = [
        'ffmpeg',
        '-i', input_video_path,
        '-s', 'hd720',
        '-r', '30',
        '-c:v', 'libx264',
        '-b:v', '5000k',
        '-preset', 'slow',
        '-profile:v', 'main',
        '-c:a', 'aac',
        '-b:a', '64k',
        output_video_path
    ]
    subprocess.run(command)
    print('Video comprimido')

ruta_carpeta = Path(str(input('Ingrese la ruta de la carpeta: ')))
carpeta_revision = Path(str(input('Carpeta para revisar: ')))
for archivo in ruta_carpeta.glob('**/*'):
    if archivo.is_file() and archivo.suffix == '.mp4' and not archivo.stem.endswith('_compressed'):
        # Usar moviepy para verificar la duración y luego cerrar el clip explícitamente
        clip = VideoFileClip(str(archivo))
        if clip.duration > 60:
            clip.close()
            archivo.rename(carpeta_revision / archivo.name)
            continue
        clip.close()  # Asegurarse de cerrar el clip
        
        output_video_path = archivo.with_name(archivo.stem + '_compressed' + archivo.suffix)
        comprimir(archivo, output_video_path)

        # Intentar eliminar el archivo original con manejo de excepciones
        for i in range(5):  # Reintentar hasta 5 veces
            try:
                archivo.unlink()
                print('Archivo original eliminado')
                break  # Salir del bucle si la eliminación fue exitosa
            except PermissionError:
                time.sleep(1)  # Esperar un segundo antes de reintentar

print('Todos los videos han sido comprimidos con éxito')