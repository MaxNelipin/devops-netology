#1

- Высоконагруженное монолитное java веб-приложение - ВМ, т.к. нужно дать много ресурсов;
- Go-микросервис для генерации отчетов - Docker для легкого масштабирования 
- Nodejs веб-приложение  - Docker для легкого масштабирования;
- Мобильное приложение c версиями для Android и iOS - Docker, чтобы на одном базовом слое работал код для двух платформ;
- База данных postgresql используемая, как кэш - голое железо для IOPS;
- Шина данных на базе Apache Kafka - Docker для надёжности;
- Очередь для Logstash на базе Redis - Docker для распределения нагрузки с подключенным хранилищем логов;
- Elastic stack для реализации логирования продуктивного веб-приложения - три ноды elasticsearch, два logstash и две ноды kibana
   Elastic - на ВМ для выделения больших ресусрсов на поиск, logstash и kibana - на Docker для однородности среды и конфигов ;
- Мониторинг-стек на базе prometheus и grafana - На Docker, чтобы обеспечить отказоустойчивость и скорость разворачивания новых нод;
- Mongodb, как основное хранилище данных для java-приложения - ВМ, чтобы БД была ближе к железу;
- Jenkins-сервер- Docker, чтобы ноды можно было быстро разворачивать из тестовой среды в боевой или облаке для разнесения нагрузки
  
#2

https://hub.docker.com/layers/164833902/maxnelipin/devops-netology/httpd5_3/images/sha256-e8e5620687045e5d755e560c19af299c468c55a41534c3905c8cbc129d414467?context=repo

#3
``` bash
CONTAINER ID   IMAGE     COMMAND       CREATED              STATUS              PORTS     NAMES
9a41cdc50e33   debian    "bash"        3 seconds ago        Up 2 seconds                  kind_vaughan
159e943b6293   centos    "/bin/bash"   About a minute ago   Up About a minute             vibrant_cartwright

docker exec -it 159e943b6293 bash -c "echo 123 > /share/info/centos1.txt"

root@9a41cdc50e33:/# ls -lh /info/
total 12K
-rw-r--r-- 1 root root  4 Aug 30 13:50 centos.txt
-rw-r--r-- 1 root root  4 Aug 30 13:53 centos1.txt
-rw-r--r-- 1 root root 12 Aug 30 13:51 host.txt
root@9a41cdc50e33:/#
