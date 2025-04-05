run the commands

- dvc repro
    {it should run or "Data and pipelines are up to date." this message should come}

- dvc dag
    {see if the .ymal file connets all the python file}

api:
to run api the command is
- uvicorn main:app --reload