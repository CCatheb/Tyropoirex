""" Tyropoirex is an self-made generic REST API Client made for personnal use.

@CCatheb ; V1.0 ; 01 - 2023
"""

import json
import logging
import urllib.request
from abc import ABC, abstractmethod

class RestException(Exception):
    pass

class AbstractRestClient(ABC):
    """ This class implements an abstract REST Client.
    """

    def __init__(self, url, auth_type, auth_params=None, context=None):
        self.url = url
        self.access_token = None
        self.context = context

        if auth_type == "USER":
            self.user = auth_params['user']
            self.password = auth_params['password']
        elif auth_type == "KEY" :
            self.key = auth_params['key']
        elif auth_type is None :
            pass
        else :
            raise AssertionError(f"Authentication type {auth_type} is not currently supported.")

    def request(self, url, data, method, timeout=5, headers=None):
        """This functions establishes an HTTP or HTTPS request to the specified URL.
        Returns JSON data if success.

        Args:
            url (str): URL to the endpoint. Should be the full URL.
            data (json): JSON message body
            method (str): Method to use (GET, POST, etc)
            timeout (int): Timeout - Default is 5s
        """

        if method not in ["GET", "PUT", "POST", "DELETE"]:
            raise AssertionError(f"Current method {method} is not supported.")

        if not headers:
            headers = {'content-type': 'application/vnd.api+json'}

        # We do the request below, and we check for potential errors
        req = urllib.request.Request(url=url, headers=headers, data=data, method=method)
        response = None
        try:
            response = urllib.request.urlopen(req, timeout=timeout, context=self.context)
        except urllib.error.HTTPError as err:
            response = err # Treat the error as a response
        except Exception as err:
            msg = "HTTP request failed\nError: {0}\nURL: {1}\nMethod: {2}\nResponse code: {3}\nData: {4}\n" \
                  "Headers: {5}".format(err, url, method, response.code, str(data), headers)
            raise RestException(msg)

        # Treat response, and make it usable.
        resp_data = None
        if (response and response.code != 307):                     #307 is server redirection
            result = response.read().decode('utf-8', 'replace')
            try:
                resp_data = json.loads(result)
            except Exception as err:
                msg = "HTTP request failed\nError: {0}\nURL: {1}\nMethod: {2}\nResponse code: {3}\nData: {4}\n" \
                  "Headers: {5}".format(err, url, method, response.code, str(data), headers)
                raise RestException(msg)
        return(response.code, resp_data)

    def get(self, resource, payload=None):
        """Establishes a GET resquest
        """
        return self.request(url=self.url+resource, data=payload, method="GET")

    def post(self, resource, payload):
        """Establishes a POST resquest
        """
        return self.request(url=self.url+resource, data=payload, method="POST")

    def put(self, resource, payload):
        """Establishes a PUT resquest
        """
        return self.request(url=self.url+resource, data=payload, method="PUT")

    def delete(self, resource, payload=None):
        """Establishes a DELETE resquest
        """
        return self.request(url=self.url+resource, data=payload, method="DELETE")