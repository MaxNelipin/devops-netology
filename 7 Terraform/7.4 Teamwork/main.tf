provider "yandex" {
  //token     = "<OAuth>"
  cloud_id  = "b1ghq301023687quik6d"
  folder_id = "b1gpooj85mh91so024vc"
  zone      = "ru-central1-a"
}

resource "yandex_compute_image" "ubnt2004" {
  name = "ubnt2004"
  source_family = "ubuntu-2004-lts"
}

resource "yandex_compute_instance" "vm-1" {
  name = "tr-test"

  boot_disk {
    initialize_params {
      //image_id = "fd81hgrcv6lsnkremf32"
      image_id = yandex_compute_image.ubnt2004.id
    }
  }
  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }


  resources {
    core_fraction = 20
    cores = 2
    memory = 2
  }
}
resource "yandex_vpc_network" "network-1" {
  name = "network1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["10.77.10.0/24"]
}
