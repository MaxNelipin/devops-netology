provider "yandex" {
  cloud_id = "b1ghq301023687quik6d"
  folder_id = "b1gpooj85mh91so024vc"
  zone = "ru-central1-a"
}

locals {
  platform_type_map = {
    stage = "standard-v1"
    prod = "standard-v3"
  }
  instance_count_map = {
    stage = 1
    prod = 2
  }
  instances = {
    "standard-v1" = yandex_compute_image.ubuntu_latest.id
    "standard-v3" = yandex_compute_image.ubuntu_latest.id
  }
}


resource "yandex_compute_image" "ubuntu_latest" {
  name = "ubuntu_latest"
  source_family = "ubuntu-2004-lts"
}

resource "yandex_compute_instance" "vm-1" {
  name = "7_3_Basic"

  platform_id = local.platform_type_map[terraform.workspace]
  count = local.instance_count_map[terraform.workspace]

  boot_disk {
    initialize_params {
      image_id = yandex_compute_image.ubuntu_latest.id
    }
  }
  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat = true
  }


  resources {
    core_fraction = 20
    cores = 1
    memory = 2
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "yandex_compute_instance" "vm-2" {
  for_each = local.instances
  platform_id = each.key

  boot_disk {
    initialize_params {
      image_id = each.value
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat = true
  }

  resources {
    core_fraction = 20
    cores = 1
    memory = 2
  }

}

resource "yandex_vpc_network" "network-1" {
  name = "network1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name = "subnet1"
  zone = "ru-central1-a"
  network_id = yandex_vpc_network.network-1.id
  v4_cidr_blocks = [
    "10.77.10.0/24"]
}

