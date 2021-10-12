#1.
1. 

      1. Инфраструктура изменяемая, потому что будет много итераций разработки и тестов, нужна быстрота изменения.
      2. На данный момент нет, т.к. инфраструктура ещё не устоялась
      3. Нет, т.к. всегда возникают проблемы с их обновлением, + их то же нужно настраивать, а это время
      4. Обязательно, т.к. нужно всем этим управлять и в будущем масштабировать

2. Terraform, Parcker для шаблонизации ВМ, Docker+Kubernetes для быстрого развертывания изменений, TeamCity - CI/CD, 
3. В будущем можно добавить Ansible для каких-то рутинных задач, которые уже будут известны.

#2.
maxn@docker-nm:~$ terraform --version
Terraform v1.0.8
on linux_amd64


#3.
При помощи tfswitch

```shell


maxn@docker-nm:~$ terraform -v
Terraform v0.12.31

Your version of Terraform is out of date! The latest version
is 1.0.8. You can update by downloading from https://www.terraform.io/downloads.html



maxn@docker-nm:~$ terraform -v
Terraform v1.0.8
on linux_amd64


```