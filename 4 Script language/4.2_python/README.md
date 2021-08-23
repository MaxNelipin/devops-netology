#1.
```python
#!/usr/bin/env python3
a = 1
b = '2'
c = a + b # ошибка, т.к. операнды разного типа
c = str(a) + b # c=12, результат строка
c = a + int(b) # c=3, результат целое число
````

#2.
Скрипт выполняется под Windows
```python
#!/usr/bin/env python3
import os

pathRepo = "C:\\Users\\max\\git\\devops-netology"

bash_command = ["cd "+pathRepo, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        prepare_result = prepare_result.replace('/', '\\')
        print(pathRepo + "\\" + prepare_result)
````
#3.
Скрипт выполняется под Windows
```python
#!/usr/bin/env python3

import os
import sys

pathRepo = sys.argv[1]
# Воспринимаем под Windows пути ~\git\devops-netology
if sys.platform == 'win32':
    pathRepo = pathRepo.replace('~', os.getenv('USERPROFILE'))
#Если переданный путь является локальной директорией
if os.path.isdir(pathRepo):

    bash_command = ["cd " + pathRepo, "git status"]
    result_os = os.popen(' && '.join(bash_command)).read()
    for result in result_os.split('\n'):
        if result.find('modified') != -1:
            prepare_result = result.replace('\tmodified:   ', '')
            prepare_result = prepare_result.replace('/', '\\')
            print(pathRepo + "\\" + prepare_result)
else:
    print("Путь " + pathRepo + " не существует")
````

#4.
```python
#!/usr/bin/env python3

import socket
import time

hostname = "google.com"
port = 443
prevIP = ""
a = 0
while a < 15:
    currentIP = socket.gethostbyname(hostname)
    if currentIP != prevIP:
        print(f"[ERROR] {hostname} IP mismatch: previous: {prevIP} new: {currentIP}")
        prevIP = currentIP
    else:
        print(f"{hostname} - {currentIP}")
    # Проверка доступности
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        conn.connect((hostname, port))
    except socket.error:
        print("Not available" , "\n-----------------------------------------")
    else:
        print("Available", "\n-----------------------------------------")
    finally:
        conn.close()
    a += 1
    time.sleep(15)
````