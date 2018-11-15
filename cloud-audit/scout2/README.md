# scout2

This contains a Terraform module to set up the AWS role
& policy for Scout2 and automation help.

## Pre-Requisites
* Terraform
* Scout2 (installed via CLI). `pip install awsscout2`

## Instructions
1. Create the IAM role that allows Scout2 to execute.
   ```
   cd tf-aws-iam
   # Log into the AWS CLI
   terraform init
   terraform plan --var-file=[your file here]
   terraform apply --var-file=[your file here]
   ```
   This will output a Role ARN that a user can
   assume in order to execute Scout2 in an AWS
   resource account.
1. Get a report for the current state. This will
   save it under `scout2-report`, which you can open
   in the browser to check it out.
   ```
   inv report.save-current
   ```
1. Check out the report. If it reflects your desired
   state, you can save it.
   ```
   inv report.save-desired
   ```
1. Let's assume you already have a desired state.
   We'll compare the desired to the current.
   ```
   inv report.compare
   ```
   This command will run scout2, generate the report, and
   remove certain parts of the dictionary
   that change on every run, including time and SNS tokens.
   It then compares the desired to the current.

## References
* https://github.com/nccgroup/Scout2