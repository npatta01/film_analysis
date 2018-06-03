from google.cloud import datastore
import googlemaps
API_KEY='AIzaSyC1Y6NHZG7x6EBYLONGIMG2tNeBs3QAffI'
# Instantiates a client
datastore_client = datastore.Client()
gmaps = googlemaps.Client(key=API_KEY)

def geocode(location, kind='Location'):
    name = 'sample task1'
    task_key = datastore_client.key(kind, location)

    # Prepares the new entity
    task = datastore.Entity(key=task_key)
    payload = None
    if task is None:
        payload = gmaps.geocode(location)   
        task['payload'] = payload
        datastore_client.put(task)
    else:
        payload = task['payload']
    return payload
