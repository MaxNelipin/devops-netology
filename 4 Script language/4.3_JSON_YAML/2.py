#!/usr/bin/env python3

import socket
import time
import json
import yaml

arHost = [{"mail.google.com": ""}, {"www.google.com": ""}]

port = 443
prevIP = ""
a = 0

while a < 15:
    # Флаг изменения IP
    changeIP = False
    for i in range(len(arHost)):
        for hostname, prevIP in arHost[i].items():
            currentIP = socket.gethostbyname(hostname)
            if currentIP != prevIP:
                print(f"[ERROR] {hostname} IP mismatch: previous: {prevIP} new: {currentIP}")
                prevIP = currentIP
                arHost[i][hostname] = currentIP
                changeIP = True
            else:
                print(f"{hostname} - {currentIP}")
            # Проверка доступности
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                conn.connect((hostname, port))
            except socket.error:
                print("Not available", "\n-----------------------------------------")
            else:
                print("Available", "\n-----------------------------------------")
            finally:
                conn.close()
    # Если IP менялись, то пишем новую структуру в файлы
    if changeIP:
        with open('2.yaml', 'w') as ym:
            ym.write(yaml.dump(arHost))
            ym.close()
        with open('2.json', 'w') as js:
            js.write(json.dumps(arHost))
            js.close()
    a += 1
    time.sleep(5)
