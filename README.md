# Tyropoirex

Tyropoirex is an self-made REST API client, made for personal projects.

## Installation

Download the file, and set it in a folder. Done.


## Usage

```python
import tyropoirex

# Instanciate the REST Client
rest_client = AbstractRestClient(url='http://thisismyurl.com/', auth_type='KEY', auth_params={'key':'thisismykey'}

# Make a GET request 
# will fetch 'http://thisismyurl.com/myresource'
rest_client.get('myresource')

# Make a POST request 
# will fetch 'http://thisismyurl.com/myresource'
rest_client.post('myresource', mydata)

# Make a PUT request 
# will fetch 'http://thisismyurl.com/myresource'
rest_client.get('myresource', PUT)

# Make a DELETE request 
# will delete 'http://thisismyurl.com/myresource'
rest_client.get('myresource')
```
Of course, each function returns the response code and the response data.

## Support
Leave me a message and I'll try to help you.


## License

[LGPL 3.0](https://choosealicense.com/licenses/lgpl-3.0/)