# queue user role
resource "aws_iam_policy" "scout2_role_policy" {
  provider = "aws.${var.aws_account}"
  name     = "Scout2RolePolicy"
  path     = "/"
  policy   = "${file("./policy.json")}"
}

resource "aws_iam_role" "scout2_role" {
  provider = "aws.${var.aws_account}"
  name     = "Scout2Role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": {
    "Effect": "Allow",
    "Principal": { "AWS": "arn:aws:iam::${var.billing_account_id}:root" },
    "Action": "sts:AssumeRole"
  }
}
EOF
}

resource "aws_iam_policy_attachment" "scout2_role_attachment_to_scout2_role_policy" {
  provider   = "aws.${var.aws_account}"
  name       = "scout2_policy_attachment"
  roles      = ["${aws_iam_role.scout2_role.name}"]
  policy_arn = "${aws_iam_policy.scout2_role_policy.arn}"
}
