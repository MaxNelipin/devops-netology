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
