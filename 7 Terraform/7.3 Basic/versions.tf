variable "sckey" {
  default = ""
}
variable "ackey" {
  default = ""
}
terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = "0.64.0"
    }
  }

  backend "s3" {
    endpoint   = "storage.yandexcloud.net"
    bucket     = "tfnetology"
    region     = "us-east-1"
    key        = "v1/terraform.tfstate"
    access_key = "${var.ackey}"
    secret_key = "${var.sckey}"
    dynamodb_endpoint = "https://docapi.serverless.yandexcloud.net/ru-central1/b1ghq301023687quik6d/etnmbh8i0ncbn7sr2fok"
    dynamodb_table = "tfnelipin"
    skip_region_validation      = true
    skip_credentials_validation = true
  }

}