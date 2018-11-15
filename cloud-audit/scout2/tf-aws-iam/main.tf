terraform {
  required_version = ">= 0.11"
}

provider "aws" {
  version = "~> 1.7"
  alias = "${var.aws_account}"
  region = "${var.aws_region}"
}