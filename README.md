# SortableChallenge
Sortable coding challenge. The implementation was done in python in the [auction package](auction)

## API and Documentation
See [auction package](auction) package documentation here: https://jhexan.github.io/SortableChallenge/

## Example build and execution
```
$ git clone https://github.com/jhexan/SortableChallenge.git
$ cd SortableChallenge
$ docker build -t challenge .
$ docker run -i -v /path/to/config.json:/auction/config.json challenge < /path/to/input.json
```
