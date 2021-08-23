#1.
```shell
a=1
b=2
c=a+b  // c=a+b, т.к. происходит присвоение строки 
d=$a+$b // d=1+2, т.к. происходит присвоение строки со значениями из переменных a и b
e=$(($a+$b)) // e=3, т.к. подобная запись предполагает приведение типа переменных по их содержимому и потом взятие результата арифметической операции 
````
#2.
Допустим, интересна дата последней успешной проверки
```shell
while ((1==1)
do
curl https://localhost:4757
if (($? == 0))
then
date >> curl.log // Пишем в лог дату успешной проверки доступности сервиса
break // выходим из цикла
fi
done
````
Допустим, интересна дата последней неудачной проверки
```shell
while ((1==1)
do
curl https://localhost:4757
if (($? != 0))
then
date > curl.log // Пишем в лог дату последней неуспешной проверки
else
break // выходим из цикла при начале доступности сервиса
fi
done
````

#3.
```shell
#!/usr/bin/env bash

ar_hosts=("192.168.0.9" "192.168.0.27" "192.168.0.35")
port=80
declare -i j
declare -i success
for i in ${ar_hosts[@]}; do
  j=0
  success=0
  while ((j < 5)); do
    curl http://$i:$port >/dev/null 2>&1
    if (($? == 0)); then
      success+=1
    fi
    j+=1
  done
  echo "$(date) успешно $success из $j для узла $i" >>curl.log
done
```


#4.
```shell
#!/usr/bin/env bash
    
ar_hosts=("192.168.0.9" "192.168.0.27" "192.168.0.35")
port=80
declare -i j
declare -i success
while ((1 == 1)); do
  for i in ${ar_hosts[@]}; do
    j=0
    success=0
    while ((j < 5)); do
      curl http://$i:$port >/dev/null 2>&1
      if (($? == 0)); then
        success+=1
      else
        echo "$(date) $i - недоступен" >>error.log
        break 3
      fi
      j+=1
    done
    echo "$(date) успешно $success из $j для узла $i" >>curl.log
  done
  sleep 60
done


```




