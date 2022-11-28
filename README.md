
# GCP Logging
- This is a package for parsing and monitoring Audit-logs produced with the GCP function using Cloud-Storage 

## Package Contents

- gcp-audit-log  
- functions
- python code
- images



## Cloud Storage triggers

bookmark_border
## In Cloud Functions, a Cloud Storage trigger enables a function to be called in response to changes in Cloud Storage. When you specify a Cloud Storage trigger for a function, you choose an event type and specify a Cloud Storage bucket. Your function will be called whenever a change occurs on an object (file) within the specified bucket.
 

## Trigger a Google Cloud Function

- A file gets written to the Cloud Storage Bucket.

- A Cloud Storage event is raised which in-turn triggers a Cloud Function. The function is passed some metadata about the event, including the object path.

- The Cloud Function issues a HTTP POST to invoke a job in Matillion ETL passing various parameters besides the job name and name/path of the file that caused this event.

- Matillion ETL launches the appropriate Orchestration job and initialises a variable to the file that was passed via the API call. The job loads data from the file into a staging table in BigQuery.

- We then launch a Transformation job to transform the data in stage and move into appropriate tables in the Data-warehouse.



## Example configuring python script ( main.py) to  trigger enables a function to be called in response to changes in Cloud Storage

- main.py

# this pacakge is for accessing the file from bucket

from google.cloud [google.cloud] import storage

# this package for making network calls
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


    ############  Network call start

    #URL for http POST request (for REST API)
    url = 'https://httpxxxxxxxx/post [httpbin.org]'
    # request payload (the input to the server)
    myobj = {'somekey': 'somevalue'}
    #REST CALL to server
    x = requests.post [requests.post](url, json = myobj)
    #get the response back from server and print
    print(x.text)
    ########## Network call end
    print(f"Processing file completed: {file['name']}."



