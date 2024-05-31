import os
import shutil

directory = os.path.join(os.path.expanduser('~'), 'Downloads')

extensions = {
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "gif": "Images",
    "bmp": "Images",
    "webp": "Images",
    "tiff": "Images",
    "mp4": "Videos",
    "mov": "Videos",
    "avi": "Videos",
    "doc": "Documents",
    "docx": "Documents",
    "pdf": "Documents",
    "xls": "Documents",
    "xlsx": "Documents",
    "txt": "Documents",
    "mp3": "Music",
    "wav": "Music",
    "flac": "Music",
    "zip": "Archives",
    "rar": "Archives",
    "tar": "Archives",
    "gz": "Archives",
    "exe": "Programs",
    "msi": "Programs",
    "apk": "Programs",
    "deb": "Programs",
    "dmg": "Programs",
    "iso": "Programs",
    "html": "Websites",
    "css": "Websites",
    "js": "Websites",
    "php": "Websites",
    "json": "Websites",
    "xml": "Websites",
    "py": "Websites",

}

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        extension = filename.split(".")[-1]
        folder_name = extensions.get(extension, "Others")
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        if not os.path.exists(os.path.join(folder_path, filename)):
            shutil.move(file_path, os.path.join(folder_path, filename))
        else:
            i = 1
            while os.path.exists(os.path.join(folder_path, f"{filename.split('.')[0]}({i}).{extension}")):
                i += 1
            shutil.move(file_path, os.path.join(folder_path, f"{filename.split('.')[0]}({i}).{extension}"))
    elif os.path.isdir(file_path):
        if not os.path.exists(os.path.join(directory, "Folders")):
            os.mkdir(os.path.join(directory, "Folders"))
        if not os.path.exists(os.path.join(directory, "Folders", filename)):
            shutil.move(file_path, os.path.join(directory, "Folders", filename))
        else:
            i = 1
            while os.path.exists(os.path.join(directory, "Folders", f"{filename}({i})")):
                i += 1
            shutil.move(file_path, os.path.join(directory, "Folders", f"{filename}({i})"))
  