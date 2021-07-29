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
