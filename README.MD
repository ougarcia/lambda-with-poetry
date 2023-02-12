# Lambda with poetry
An example of a aws lambda function using python and poetry.

## Novelty
`build.sh` will:
* build the package (with all of its dependencies) using poetry. By default the
  build package will be output in `./dist`
* use pip to build the package again, using `./dist` as a source and outputting
  in `./package`
* zip `./package` per the aws lambda docs.
