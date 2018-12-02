Setup
=====
1. Install [pipenv](https://pipenv.readthedocs.io/en/latest/)

2. Install dependencies

    ```
    pipenv install
    ```

Testing
=======
```
pipenv run python -m pytest tests
```

Watch for file changes
----------------------
```
pipenv run ptw --runner "python -m pytest tests"
```
