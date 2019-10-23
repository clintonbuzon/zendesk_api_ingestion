# zendesk_api_ingestion
Sample python script that will ingest all users from the Zendesk REST API into an AWS S3 bucket. Converts the JSON response to .csv file format.

Parameters to edit:

    ZENDESK_URL = '<insert your zendesk url here>'
    ZENDESK_USER = '<insert your zendesk user here>'
    ZENDESK_PWS = '<insert your zendesk password here>'
    FILE_NAME = '<file name to be uploaded to S3>'
    AWS_ACCESS_KEY = '<insert your aws access key here>'
    AWS_SECRET_KEY = '<insert your secret key here>'
    AWS_BUCKET = '<insert your aws bucket name here>'

Sample parameters for reference:

    ZENDESK_URL = 'https://clinton.zendesk.com/api/v2/users.json'
    ZENDESK_USER = 'clinton.buzon@gmail.com'
    ZENDESK_PWS = 'XXXXXXXXXX'
    FILE_NAME = 'users.csv'
    AWS_ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXX' 
    AWS_SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    AWS_BUCKET = 'my_sample_bucket'
