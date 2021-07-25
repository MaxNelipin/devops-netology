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
