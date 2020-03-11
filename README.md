# SortableChallenge
Sortable coding challenge. The implementation was done in python in the [auction package](auction)

## API and Documentation
See [auction package](auction) documentation here: https://jhexan.github.io/SortableChallenge/

Generated with:
```
$ make docs
```

## Example build and execution
First clone the repository:
```
$ git clone https://github.com/jhexan/SortableChallenge.git
$ cd SortableChallenge
```
The [auction package](auction) can then be run as a script in a docker container as follows:
```
$ docker build -t challenge .
$ docker run -i -v /path/to/config.json:/auction/config.json challenge < /path/to/input.json
```
Or in a python environment with python version >=3.6:
```
$ cp /path/to/config.json auction/
$ python -m auction < /path/to/input.json
```

## Unit Tests
Basic unit tests are under [tests](tests), and can be run with 
```
$ make test
```

## Assumptions
- All input data is well formed and json is valid (see https://jsonlint.com/) 
- config.json is expected to be under the [auction](auction) project folder
- Input is given through standard in
- Output is printed to standard out
