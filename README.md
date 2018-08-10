# GCP-CronJob-To-CloudFunction
Simple Cron job on app engine to activate a Cloud Function
This code can activate as many functions as you set on cron.yaml
just set a new cron and it will pick the url and pass to app to call cloud function

You must change URL on main.py 
and them deploy you cron job like the model

# Make all necessary changes to files then 

gcloud app deploy

gcloud app deploy cron.yaml
