# EC2 Start and Stop with Slack Functionality.

In my project, I've crafted a Python-based AWS Lambda function that harnesses the capabilities of AWS services and seamlessly integrates with Slack. 
The core objective of this function is to intelligently halt non-production, testing, and development Amazon EC2 instances during non-working hours, 
and subsequently restart them when needed. This strategic automation prevents companies from incurring unnecessary and expensive compute costs when 
instances are idle during evenings and weekends. To achieve this, I've employed the power of AWS CloudWatch Events and the cron scheduler to schedule 
the execution of the stop script on weekdays at 18:00 hours and the start script at 07:00 hours. This initiative results in substantial cost savings, 
potentially up to 85 hours of compute expenses per stopped instance. Additionally, to enhance team visibility and coordination, the Lambda function 
sends informative messages to a dedicated Slack channel whenever an EC2 instance undergoes a start or stop action, including the Instance ID and its 
current status. Lastly, I've implemented a secure approach by creating an IAM role, ensuring that the Lambda function has precise and controlled access 
to EC2 resources while maintaining security best practices.

Requirements.zip has been added for easy upload to Lambda Layers. 

