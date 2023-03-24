pyinstaller -F -w main.py -p json_jmx.py --hidden-import json_jmx
cd dist
ren main.exe json_jmx.exe