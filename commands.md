# Create a bucket and link to to DVC

For the following bucket:

https://s3.console.aws.amazon.com/s3/buckets/sereniiti-models

the command is:

```s
dvc remote add -d models s3://sereniiti-models
```

Then, to add a directory in DVC:

```s
dvc add models
```