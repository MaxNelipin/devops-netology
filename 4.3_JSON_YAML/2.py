#!/usr/bin/env python3

import socket
import time
import json
import yaml

hostname = "mail.google.com"
port = 443
prevIP = ""
a = 0
while a < 15:
    currentIP = socket.gethostbyname(hostname)
    if currentIP != prevIP:
        print(f"[ERROR] {hostname} IP mismatch: previous: {prevIP} new: {currentIP}")
        prevIP = currentIP
        with open('2.yaml', 'w') as ym:
            ym.write(yaml.dump([{hostname: currentIP}]))
            ym.close()
        with open('2.json', 'w') as js:
            js.write(json.dumps({hostname: currentIP}))
            js.close()
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
    a += 1
    time.sleep(15)
