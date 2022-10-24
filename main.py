import os


base_directory = 'C:/Users/USER/Downloads/'
directories = ['Videos/', 'Imágenes/', 'Musicas/', 'Documentos/', 'Instaladores/', 'Comprimidos/']

# ---------- CREAR CARPETAS ----------
for directory in directories:
    folder = os.path.join(base_directory, directory)
    if not os.path.exists(folder):
        os.mkdir(folder)

    print('Carpetas creadas')

if __name__ == '__main__':
    for filename in os.listdir(base_directory):
        name, extension = os.path.splitext(base_directory + filename)

        # ---------- MOVER ARCHIVOS ----------
        if extension in ['.mp4', '.avi', '.flv', '.mov']:
            directory = os.path.join(base_directory, 'Videos/')
            os.rename(base_directory + filename, directory + filename)
            print('Archivo movido exitosamente a Videos')

        if extension in ['.jpg', '.jpeg', '.png', '.webp', '.svg', '.gif', '.jfif', '.bmp', '.stl']:
            directory = os.path.join(base_directory, 'Imágenes/')
            os.rename(base_directory + filename, directory + filename)
            print('Archivo movido exitosamente a Imágenes')

        if extension in ['.mp3', '.wav', '.wave', '.aac', '.flac', '.wma', '.ogg']:
            directory = os.path.join(base_directory, 'Musicas/')
            os.rename(base_directory + filename, directory + filename)
            print('Archivo movido exitosamente a Musicas')

        if extension in ['.doc', '.docx', '.pdf', '.xlsx', '.xls', '.txt', '.ppt', '.pptx', '.md', '.csv']:
            directory = os.path.join(base_directory, 'Documentos/')
            os.rename(base_directory + filename, directory + filename)
            print('Archivo movido exitosamente a Documentos')

        if extension in ['.exe', '.msi', '.bat', '.com']:
            directory = os.path.join(base_directory, 'Instaladores/')
            os.rename(base_directory + filename, directory + filename)
            print('Archivo movido exitosamente a Instaladores')

        if extension in ['.7z', '.jar', '.rar', '.zip']:
            directory = os.path.join(base_directory, 'Comprimidos/')
            os.rename(base_directory + filename, directory + filename)
            print('Archivo movido exitosamente a Comprimidos')
