# Important!
# Please ensure that your Zendesk API account's "Password access" is enabled. 
# This allows the python script to login and authenticate via username/password
# To check, go to your account Admin>Channels>Api then enable "Password Access"

# Python Prerequisites
# pip install requests
# pip install boto3

# AWS Prerequisites
# Please create your access key and secret key
# Please create aws bucket

# Code is written for Python 3.7*
import requests
import csv
import boto3
import os

# Parameters: Please only edit these variables
ZENDESK_URL = '<insert your zendesk url here>'
ZENDESK_USER = '<insert your zendesk user here>'
ZENDESK_PWS = '<insert your zendesk password here>'
FILE_NAME = '<file name to be uploaded to S3>'
AWS_ACCESS_KEY = '<insert your aws access key here>'
AWS_SECRET_KEY = '<insert your secret key here>'
AWS_BUCKET = '<insert your aws bucket name here>'

# Sample parameters
# ZENDESK_URL = 'https://clinton.zendesk.com/api/v2/users.json'
# ZENDESK_USER = 'clinton.buzon@gmail.com'
# ZENDESK_PWS = 'XXXXXXXXXX'
# FILE_NAME = 'users.csv'
# AWS_ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXX' 
# AWS_SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
# AWS_BUCKET = 'XXXXXXXXXXXXXXXXXXXX'

# Function to create CSV file
def create_csv(local_file, data, column_list):
    with open(local_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_list)
        writer.writeheader()
        for user in data:
            writer.writerow(user)

# Function to upload to S3 bucket
def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY,
                      aws_secret_access_key=AWS_SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

# Do the HTTP get request
response = requests.get(ZENDESK_URL, auth=(ZENDESK_USER, ZENDESK_PWS))

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()

# Capture users data only
users = data['users']

# Create dynamic column list
csv_columns = []
for key in users[0]:
   csv_columns.append(key)
  
# Write temporary csv file   
create_csv(FILE_NAME, users, csv_columns)

# Upload to S3
upload_to_aws(FILE_NAME, AWS_BUCKET, FILE_NAME)
        
# File cleanup
if os.path.exists(FILE_NAME):
  os.remove(FILE_NAME)
else:
  print(FILE_NAME)