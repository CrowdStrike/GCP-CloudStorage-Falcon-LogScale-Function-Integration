
"""CrowdStrike LogScale GCP integration.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . | LogScale GCP integration
`-------'                         `-------'

This code is an example for LogStorage(bucket) function setup

11.28.22 - @@ihaque55
"""
#this pacakge is for accessing the file from bucket
from google.cloud [google.cloud] import storage
#this package for making network calls
import requests

##  sending logs using token

#dest_url = "https://cloud.community.humio.com/api/v1/ingest/hec/raw"
#dest_token1 = <xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx>
#header1 = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + dest_token1}

#initializing the storage object
storage_client = storage.Client()
#trigered when new file is available
def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    #this holds the file metadata ie filename,bucket etc
    file = event
    #initiliazing the bukcet object
    bucket = storage_client.get_bucket(event['bucket'])
    #initializing blob (file in bucket)
    blob = bucket.blob(event['name'])
    #read from file as string and then converting it to lines
    contents = blob.download_as_string().splitlines()
    #loop through the lines

    for lineContent in contents:
         #print the line item
         print(lineContent)


    ############Network call start
    #URL for http POST request (for REST API)
    url = 'https://httpxxxxxxxx/post [httpbin.org]'
    # request payload (the input to the server)
    myobj = {'somekey': 'somevalue'}
    #REST CALL to server
    x = requests.post [requests.post](url, json = myobj)
    #get the response back from server and print
    print(x.text)
    ##########Network call end
    print(f"Processing file completed: {file['name']}."
