import os
import threading
from pathlib import Path
from tkinter import messagebox,ttk

def Success():
    messagebox.showinfo('','Task Complete!')


def Error():
    messagebox.showerror('','Enter valid Path!')


DIRECTORIES = {
      "Html": [".html5", ".html", ".htm", ".xhtml"],
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg",
               ".heif", ".psd"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx",".pages",".numbers"],
    "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip",".xz",".pkg",".deb",".rpm"],
    "DiskImages": [".iso",".img",".vcd",".dmg"],
    "Audio_Files": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PlainTexts": [".txt", ".in", ".out"],
    "PowerShell":[".ps1",".psm1",".psd1"],
    "PDFs": [".pdf"],
    "Python_Files": [".py",".pyi",".pyc"],
    "XML": [".xml","fxml",".rss"],
    "EXE": [".exe",".run"],
    "SHELL": [".sh"],
    "DATABASE":[".db",".sql"],
    "C#" :[".cs"],
    "C++": [".cpp"],
    "C": [".c"],
    "GO": [".go"],
    "YAML": [".yaml"],
    "JSON": [".json"],
    "ASP Classic": [".asp"],
    "ASP_NET": [".aspx", ".axd", ".asx", ".asmx", ".ashx"],
    "CSS": [".css"],
    "Coldfusion": [".cfm"],
    "Erlang": [".yaws"],
    "Flash": [".swf"],
    "Java": [".jar",".java",".jsp", ".jspx", ".wss", ".do", ".action",".class"],
    "Kotlin": [".kt",".kts",".ktm"],
    "JavaScript": [".js"],
    "TypeScript": [".ts"],
    "Rust": [".rs",".rlib"],
    "Toml": [".toml"],
    "Travis": [".travis"],
    "Perl": [".pl"],
    "PHP": [".php", ".php4", ".php3", ".phtml"],
    "Ruby": [".rb", ".rhtml"],
    "SSI": [".shtml"],
    "APPS": [".app",".ipa",".apk"],
    "LINKS":[".webloc",".lnk"],
    "CERTIFICATES":[".cer",".cert",".crt",".pvk",".pfx",".pem",".jks",".der",".key"]
}

FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}

def Action(progress,path):
    try:
        os.chdir(path)
        for e in  os.scandir():
            if e.is_dir():
                continue
            file_path = Path(e)
            file_format = file_path.suffix.lower()
            if file_format in FILE_FORMATS:
                directory_path = Path(FILE_FORMATS[file_format])
                directory_path.mkdir(exist_ok=True)
                file_path.rename(directory_path.joinpath(file_path))
        for dir in os.scandir():
            try:
                os.rmdir(dir)
            except:
                pass
        progress['value']=100
        threading.Thread(target=Success).start()

    except:
        progress['value']=50
        threading.Thread(target=Error).start()
