#
    #     ____            _    _                 ____ _
    #    |  _ \  ___  ___| | _| |_ ___  _ __    / ___| | ___  __ _ _ __   ___ _ __ 
    #    | | | |/ _ \/ __| |/ / __/ _ \| '_ \  | |   | |/ _ \/ _` | '_ \ / _ \ '__|
    #    | |_| |  __/\__ \   <| || (_) | |_) | | |___| |  __/ (_| | | | |  __/ |
    #    |____/ \___||___/_|\_\\__\___/| .__/   \____|_|\___|\__,_|_| |_|\___|_|
    #                                  |_|



import time
import os 
import json
import shutil
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from time import gmtime, strftime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'Archive':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '\\' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime('%Y')
                    month = now.strftime('%m')

                    folder_destination_path = extensions_folders[extension]
                    
                    year_exists = False
                    month_exists = False
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + '\\' +year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = extensions_folders[extension] + '\\' + year + '\\' + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + '\\' + year)
                        folder_destination_path = extensions_folders[extension] + '\\' + year
                    if not month_exists:
                        os.mkdir(folder_destination_path + '\\' + month)
                        folder_destination_path = folder_destination_path + '\\' + month


                    file_exists = os.path.isfile(folder_destination_path + '\\' + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '\\' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '\\' + filename)[1]
                        new_name = new_name.split('\\')[4]
                        file_exists = os.path.isfile(folder_destination_path + '\\' + new_name)
                    src = folder_to_track + '\\' + filename

                    new_name = folder_destination_path + '\\' + new_name
                    os.rename(src, new_name)
                # except Exception:
                #     print(filename)


extensions_folders = {

# No name
    'noname' : 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Uncategorized',
# Audio
    '.aif' : 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Audio',
    '.cda' : 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Audio',
    '.mid' : 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Audio',
    '.midi' : 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Audio',
    '.mp3' : 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Audio',
    '.mpa' : 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Audio',
    '.ogg' : 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Audio',
    '.wav' : 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Audio',
    '.wma' : 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Audio',
    '.wpl' : 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Audio',
    '.m3u' : 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Audio',
# 2D and 3D Models
    '.dwg' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.dxf' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.stp' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.step' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.rfa' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.rvt' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.nwc' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.nwf' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.nwd' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.dbx' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.cuix' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.dct' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.pat' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.dbx' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.blend' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.fbx' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.ctb' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.rws' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.ifc' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.FCStd' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.FCStd1' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.stl' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.obj' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.dae' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.sldasm' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',
    '.sldprt' : 'C:\\Users\\WN001\\Desktop\\Archive\\Models',

# Text
    '.txt' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\TextFiles',
    '.doc' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Microsoft',
    '.docx' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Microsoft',
    '.odt' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\TextFiles',
    '.pdf': 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\PDF',
    '.rtf': 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\TextFiles',
    '.tex': 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\TextFiles',
    '.wks ': 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\TextFiles',
    '.wps': 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\TextFiles',
    '.wpd': 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\TextFiles',
    '.md': 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\TextFiles',
    '.one' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Microsoft',
    '.pub' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Microsoft',
# Video
    '.3g2': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
    '.3gp': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
    '.avi': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
    '.flv': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
    '.h264': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
    '.m4v': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
    '.mkv': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
    '.mov': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
    '.mp4': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
    '.mpg': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
    '.mpeg': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
    '.rm': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
    '.swf': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
    '.vob': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
    '.wmv': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
    '.trec': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
    '.tscproj': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
    '.webm': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
    '.kdenlive': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Video',
# Images
    '.ai': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Images',
    '.bmp': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Images',
    '.gif': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Images',
    '.ico': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Images',
    '.jpg': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Images',
    '.jpeg': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Images',
    '.png': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Images',
    '.ps': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Images',
    '.psd': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Images',
    '.svg': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Images',
    '.tif': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Images',
    '.tiff': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Images',
    '.CR2': 'C:\\Users\\WN001\\Desktop\\Archive\\Media\\Images',
# Internet
    '.asp': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Internet',
    '.aspx': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Internet',
    '.cer': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Internet',
    '.cfm': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Internet',
    '.cgi': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Internet',
    '.pl': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Internet',
    '.css': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Internet',
    '.htm': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Internet',
    '.js': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Internet',
    '.jsp': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Internet',
    '.part': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Internet',
    '.php': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Internet',
    '.rss': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Internet',
    '.xhtml': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Internet',
# Compressed
    '.7z': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Compressed',
    '.arj': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Compressed',
    '.deb': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Compressed',
    '.pkg': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Compressed',
    '.rar': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Compressed',
    '.rpm': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Compressed',
    '.tar.gz': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Compressed',
    '.z': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Compressed',
    '.zip': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Compressed',
# Disc
    '.bin': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Disc',
    '.dmg': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Disc',
    '.iso': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Disc',
    '.toast': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Disc',
    '.vcd': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Disc',
# Data
    '.csv': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\Database',
    '.dat': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\Database',
    '.db': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\Database',
    '.dbf': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\Database',
    '.log': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\Database',
    '.mdb': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\Database',
    '.sav': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\Database',
    '.sql': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\Database',
    '.tar': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\Database',
    '.xml': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\Database',
    '.json': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\Database',
# Diagrams
    '.vssx': 'C:\\Users\\WN001\\Desktop\\Archive\\Diagrams',
    '.vsdx': 'C:\\Users\\WN001\\Desktop\\Archive\\Diagrams',
    '.drawio': 'C:\\Users\\WN001\\Desktop\\Archive\\Diagrams',
# Executables
    '.apk': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Executables',
    '.bat': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Executables',
    '.com': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Executables',
    '.exe': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Executables',
    '.gadget': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Executables',
    '.jar': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Executables',
    '.wsf': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Executables',
# Fonts
    '.fnt': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Fonts',
    '.fon': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Fonts',
    '.otf': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Fonts',
    '.ttf': 'C:\\Users\\WN001\\Desktop\\Archive\\Other\\Fonts',
# Presentations
    '.key': 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Presentations',
    '.odp': 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Presentations',
    '.pps': 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Presentations',
    '.ppt': 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Presentations',
    '.pptx': 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Presentations',
# Programming
    '.c': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\C&C++',
    '.class': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\Java',
    '.dart': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\Dart',
    '.py': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\Python',
    '.sh': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\Shell',
    '.swift': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\Swift',
    '.html': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\C&C++',
    '.h': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\C&C++',
    '.vb': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\C&C++',
    '.ahk': 'C:\\Users\\WN001\\Desktop\\Archive\\Programming\\AHK',
# Spreadsheets
    '.ods' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Microsoft',
    '.xlr' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Microsoft',
    '.xls' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Microsoft',
    '.xlsx' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Microsoft',
    '.xlsm' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Microsoft',
# System
    '.bak' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Other\\System',
    '.cab' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Other\\System',
    '.cfg' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Other\\System',
    '.cpl' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Other\\System',
    '.cur' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Other\\System',
    '.dll' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Other\\System',
    '.dmp' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Other\\System',
    '.drv' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Other\\System',
    '.icns' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Other\\System',
    '.ico' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Other\\System',
    '.ini' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Other\\System',
    '.lnk' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Other\\System',
    '.msi' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Other\\System',
    '.sys' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Other\\System',
    '.tmp' : 'C:\\Users\\WN001\\Desktop\\Archive\\Documents\\Other\\System',
}

folder_to_track = 'C:\\Users\\WN001\\Desktop'
folder_destination = 'C:\\Users\\WN001\\Desktop\\Archive'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:           
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()