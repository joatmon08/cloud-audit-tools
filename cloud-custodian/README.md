# Cleaning Up Resources with Cloud Custodian
To clean up untagged AWS resources, you can use a tool called Cloud Custodian.
This will allow you to check what resources are untagged and
determine which ones can be removed.

## Pre-Requisites
* Python2
* [Cloud Custodian](https://github.com/capitalone/cloud-custodian)
  ```
  pip install c7n
  ```

## Instructions
1. Create a `policy.yml` file. This should outline what you're looking for in
   your AWS environment. [Documentation here](https://capitalone.github.io/cloud-custodian/docs/overview/index.html).
   The example below looks for the "di" tags in AWS EC2 (and stops anything without it) and S3 buckets.
1. Run `custodian validate policy.yml` to check if your policy YAML is correct.
1. Run custodian in dry-run to get a `resources.json` file in an `out` directory that will list the
   resources violating the tag requirements.
   ```
   AWS_DEFAULT_REGION=<region you want to check> aws-vault exec <read-only profile> -- custodian run --dryrun -s out policy.yml
   ```
   You should see a new out directory with a resources.json under the policy section you created. This will contain the resources that violate your policy.

## Example
See `policy.yml`.