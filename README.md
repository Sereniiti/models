# Sereniiti production models

This folder contains Sereniiti production models for A.I.

## Using GitFlow

Here are the commands to use for Gitflow.

The GitFlow extension for Git is mandatory for this project.

### Feature branch

```sh
git flow feature start feature_branch
<work>
git flow feature finish feature_branch
```

### Release branch

```sh
git flow release start 0.0.x
<fixes>
git flow release finish '0.0.x'
```

## Using DVC

We rely on DVC to avoid having the model stored on GitHub. As it is > 1Go.

### Usual work

Get the model:

```sh
dvc pull
```

Update the model on the remote:

```sh
git commit -m "Dataset updates"
dvc push
```

Add a directory to DVC

```sh
dvc add data/data.xml
git commit data/data.xml.dvc -m "Dataset updates"
dvc push
```

### Configuration

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