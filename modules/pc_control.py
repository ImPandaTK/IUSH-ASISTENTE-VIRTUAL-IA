
import os
import subprocess
import pyautogui
import webbrowser

def abrir_programa(nombre):
    programas = {
        "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
        "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
        "spotify": r"C:\Users\bypan\AppData\Roaming\Spotify\Spotify.exe",
        "navegador": r"C:\Program Files\Opera GX\opera.exe",
        "bloc de notas": "notepad",
        "calculadora": "calc",
        "explorador": "explorer",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "steam": r"C:\Program Files (x86)\Steam\steam.exe", 
        "discord": r"C:\Users\bypan\AppData\Local\Discord\app-1.0.9003\Discord.exe",
        "vlc": r"C:\Program Files\VideoLAN\VLC\vlc.exe",
        "notion": r"C:\Users\bypan\AppData\Local\Programs\Notion\Notion.exe",
        "telegram": r"C:\Users\bypan\AppData\Roaming\Telegram Desktop\Telegram.exe",
        "microsoft edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "microsoft teams": r"C:\Users\bypan\AppData\Local\Microsoft\Teams\current\Teams.exe",
        "visual studio code": r"C:\Users\bypan\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "blender": r"C:\Program Files\Blender Foundation\Blender 3.5\blender.exe",
        "gimp": r"C:\Program Files\GIMP 2\bin\gimp-2.10.exe",
        "audacity": r"C:\Program Files (x86)\Audacity\audacity.exe",
        "obs": r"C:\Program Files\obs-studio\bin\64bit\obs64.exe",
        "notepad++": r"C:\Program Files\Notepad++\notepad++.exe",
        "filezilla": r"C:\Program Files\FileZilla FTP Client\filezilla.exe",
        "postman": r"C:\Users\bypan\AppData\Local\Postman\Postman.exe",
        "git": r"C:\Program Files\Git\bin\bash.exe",
        "powershell": r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe",
        "cmd": r"C:\Windows\System32\cmd.exe",
        "task manager": r"C:\Windows\System32\taskmgr.exe",
        "control panel": r"C:\Windows\System32\control.exe",
        "settings": r"C:\Windows\System32\ms-settings:appsfeatures",
        "calculator": r"C:\Windows\System32\calc.exe",
    }
    comando = programas.get(nombre.lower())
    if comando:
        subprocess.Popen(comando)
        return f"Abriendo {nombre}"
    else:
        return "No reconozco ese programa."

def cerrar_programa(nombre):
    tareas = {
        "word": "WINWORD.EXE",
        "excel": "EXCEL.EXE",
        "spotify": "Spotify.exe",
        "bloc de notas": "notepad.exe",
        "explorador": "explorer.exe",
        "chrome": "chrome.exe",
        "steam": "steam.exe",
        "discord": "Discord.exe",
        "vlc": "vlc.exe",
        "notion": "Notion.exe",
        "telegram": "Telegram.exe",
        "microsoft edge": "msedge.exe",
        "microsoft teams": "Teams.exe",
        "visual studio code": "Code.exe",
        "blender": "blender.exe",
        "gimp": "gimp-2.10.exe",
        "audacity": "audacity.exe",
        "obs": "obs64.exe",
        "notepad++": "notepad++.exe",
        "filezilla": "filezilla.exe",
        "postman": "Postman.exe",
        "git": "bash.exe",
        "powershell": "powershell.exe",
        "cmd": "cmd.exe",
        "task manager": "taskmgr.exe",
        "control panel": "control.exe",
        "settings": "ms-settings:appsfeatures",
        "calculator": "calc.exe",  
        "navegador": "opera.exe",  # Asumiendo que es Opera GX
    }
    proceso = tareas.get(nombre.lower())
    if proceso:
        os.system(f"taskkill /f /im {proceso}")
        return f"Cerrando {nombre}"
    else:
        return "No encontré ese programa para cerrar."

def escribir_texto(texto):
    pyautogui.write(texto, interval=0.05)
    return f"Escribiendo: {texto}"

def abrir_url(url):
    if not url.startswith("http"):
        url = "https://" + url
    webbrowser.open(url)
    return f"Abriendo navegador en: {url}"
