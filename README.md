Assessment

1.	Create a DynamoDB table which should be used to contain customer data, such as their first and second name, telephone number, telephone password (a 6 digit number), and any other data or fields which are required.

2.	Create an S3 bucket, which allows only the root user of the AWS account to delete objects within it.

3.	Create two Lambda functions written in Python:
a.	The first Lambda function should take a telephone number as an event input and search the DynamoDB table to see if a customer with that telephone number exists. The Lambda function should return a JSON structure describing whether:
i.	A customer with the telephone number exists and has a phone password
ii.	A customer with that telephone number exists but does not have a phone password
iii.	A customer with that telephone number does not exist

b.	The second Lambda function should take a 6 digit number (representing a telephone password) and a telephone number as an event input, and place those 6 digits into the DynamoDB record for the customer with that telephone number (if a customer with that telephone number exists). Additionally, the Lambda function should create a .txt file and place that file into the S3 bucket created in step 2; the DynamoDB record for the customer should be updated with the name and size of the object created in S3, and the timestamp of when the file was created.

4.	Create a CloudFormation template and deployment package which can be used to deploy the Lambda, DynamoDB, S3 bucket, and other AWS resources required
