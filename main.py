import os


base_directory = input('Ingrese la ruta de la carpeta a organizar: ')
if not base_directory.endswith('/'):
    base_directory += '/'
directories = ['Videos/', 'Imágenes/', 'Musicas/', 'Documentos/', 'Instaladores/', 'Comprimidos/']

# ---------- CREAR CARPETAS ----------
for directory in directories:
    folder = os.path.join(base_directory, directory)
    if not os.path.exists(folder):
        os.mkdir(folder)

doc_dirs = ['Word/', 'Excel/', 'PDF/', 'PowerPoint/', 'TXT/', 'CSV/']
for doc_dir in doc_dirs:
    folder = os.path.join(base_directory, directories[3], doc_dir)
    if not os.path.exists(folder):
        os.mkdir(folder)

    print('Carpetas creadas')

img_dirs = ['PNG/', 'JPG_JPEG/', 'SVG/', 'WEBP/', 'GIF/', 'JFIF/', 'BMP/', 'STL/']
for img_dir in img_dirs:
    folder = os.path.join(base_directory, directories[1], img_dir)
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

            # ---------- CLASIFICAR DOCUMENTOS ----------

            for img in os.listdir(directory):
                img_name, img_extension = os.path.splitext(base_directory + img)

                if img_extension in ['.png']:
                    doc_directory = os.path.join(directory, img_dirs[0])
                    os.rename(directory + img, doc_directory + img)

                if img_extension in ['.jpg', '.jpeg']:
                    doc_directory = os.path.join(directory, img_dirs[1])
                    os.rename(directory + img, doc_directory + img)

                if img_extension in ['.svg']:
                    doc_directory = os.path.join(directory, img_dirs[2])
                    os.rename(directory + img, doc_directory + img)

                if img_extension in ['.webp']:
                    doc_directory = os.path.join(directory, img_dirs[3])
                    os.rename(directory + img, doc_directory + img)

                if img_extension in ['.gif']:
                    doc_directory = os.path.join(directory, img_dirs[4])
                    os.rename(directory + img, doc_directory + img)

                if img_extension in ['.jfif']:
                    doc_directory = os.path.join(directory, img_dirs[5])
                    os.rename(directory + img, doc_directory + img)

                if img_extension in ['.bmp']:
                    doc_directory = os.path.join(directory, img_dirs[6])
                    os.rename(directory + img, doc_directory + img)

                if img_extension in ['.stl']:
                    doc_directory = os.path.join(directory, img_dirs[7])
                    os.rename(directory + img, doc_directory + img)

        if extension in ['.mp3', '.wav', '.wave', '.aac', '.flac', '.wma', '.ogg']:
            directory = os.path.join(base_directory, 'Musicas/')
            os.rename(base_directory + filename, directory + filename)
            print('Archivo movido exitosamente a Musicas')

        if extension in ['.doc', '.docx', '.pdf', '.xlsx', '.xls', '.txt', '.ppt', '.pptx', '.md', '.csv']:
            directory = os.path.join(base_directory, 'Documentos/')
            os.rename(base_directory + filename, directory + filename)
            print('Archivo movido exitosamente a Documentos')

            # ---------- CLASIFICAR DOCUMENTOS ----------

            for document in os.listdir(directory):
                doc_name, doc_extension = os.path.splitext(base_directory + document)

                if doc_extension in ['.doc', '.docx']:
                    doc_directory = os.path.join(directory, doc_dirs[0])
                    os.rename(directory + document, doc_directory + document)

                if doc_extension in ['.xlsx', '.xls']:
                    doc_directory = os.path.join(directory, doc_dirs[1])
                    os.rename(directory + document, doc_directory + document)

                if doc_extension in ['.pdf']:
                    doc_directory = os.path.join(directory, doc_dirs[2])
                    os.rename(directory + document, doc_directory + document)

                if doc_extension in ['.ppt', '.pptx']:
                    doc_directory = os.path.join(directory, doc_dirs[3])
                    os.rename(directory + document, doc_directory + document)

                if doc_extension in ['.txt']:
                    doc_directory = os.path.join(directory, doc_dirs[4])
                    os.rename(directory + document, doc_directory + document)

                if doc_extension in ['.csv']:
                    doc_directory = os.path.join(directory, doc_dirs[5])
                    os.rename(directory + document, doc_directory + document)

        if extension in ['.exe', '.msi', '.bat', '.com']:
            directory = os.path.join(base_directory, 'Instaladores/')
            os.rename(base_directory + filename, directory + filename)
            print('Archivo movido exitosamente a Instaladores')

        if extension in ['.7z', '.jar', '.rar', '.zip']:
            directory = os.path.join(base_directory, 'Comprimidos/')
            os.rename(base_directory + filename, directory + filename)
            print('Archivo movido exitosamente a Comprimidos')
