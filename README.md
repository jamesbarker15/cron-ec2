# EC2 Start and Stop with Slack Functionality.

This project is designed to work on AWS Lambda and use Cloudwatch Events to schedule
it running. 

The scripts when executed will identify any EC2 resources on the account which 
have the tags (name "Environment", value:"Development"). Identifying non-essential
and non production assets which can be shutdown out of hours and at the weekend.
This will in turn save the company money on unused compute resource. The tags
can be fully customisable to suit you needs.

Cloudwatch Events with CRON can be established to run the stop script at 18:00hrs every day.
The start script can then be run at 08:00hrs to bring back the instances for example.

Each instance which is started or stopped, a Slack notification is sent with the 
instance ID. 

