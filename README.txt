run the commands to run the application
- dvc repro
    {it should run or "Data and pipelines are up to date." this message should come}

- dvc dag
    {see if the .ymal file connets all the python file}

api:
to run api the command is
- uvicorn main:app --reload

cloud:
paste the below link in chrome
- https://water-prediction-cloud.onrender.com/docs

steps:
- click on Post
- click on Try it out 
- replace the value with same other value (replace 0)
- than click on Execute
you will see your output in "Response body"