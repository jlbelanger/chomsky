# Chomsky

## Developing

### Setup

``` bash
cp config.py.sample config.py
brew install pipenv
brew install portaudio
pipenv install
```

### Run

``` bash
pipenv shell
python main.py
```

### Record

``` bash
pipenv shell
python main.py listen
```

### Train

``` bash
pipenv shell
python main.py train
```

## Linting

``` bash
pylint *.py chomsky/*.py chomsky/commands/*.py
```

## Testing

``` bash
python -m unittest chomsky/test/*.py
```
