provider "aws" {
  region = "us-east-1"
}

# This is insecure because it is public
resource "aws_s3_bucket" "my_insecure_bucket" {
  bucket = "my-test-insecure-bucket-12345"
}

resource "aws_s3_bucket_public_access_block" "example" {
  bucket = aws_s3_bucket.my_insecure_bucket.id
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

