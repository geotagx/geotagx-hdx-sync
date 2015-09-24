#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests


def _load_json(path=None):
  '''Loads local JSON into a dictionary.'''

  #
  # Checking if a path as been provided.
  #
  if path is None:
    print 'No path provided. Terminating.'
    return False

  with open(path) as json_file:
    data = json.load(json_file)

  return data


def CreateDataset(apikey, **kwargs):
  '''Creates a dataset on the Humanitarian Data Exchange repository.'''

  #
  # Checks if API key has been provided.
  #
  if apikey is None:
    print 'Please provide API Key. Terminating.'
    return False

  #
  # Builds URL string:
  #
  # u = Base URL.
  # m = Method or, in the case of CKAN, action.
  # h = Headers. This is where we add our API key.
  # p = Parameters. In our case we are sending a dictionary.
  #
  u = 'https://data.hdx.rwlabs.org/api/3/action'
  m = '/package_create'
  p = _load_json(kwargs.get('path', None))
  h = {
    'X-CKAN-API-Key': apikey,
    'Content-type': 'application/json'
  }

  #
  # Making POST request to CKAN.
  # This will effectivelly create the dataset.
  #
  print h
  r = requests.post(u + m, headers=h, data=json.dumps(p))

  #
  # Requests will automatically raise an error
  # if there are issues with the request.
  #
  r.raise_for_status()


def CreateResource(apikey, **kwargs):
  '''Adds a resource to an existing dataset.'''

  #
  # Checks if API key has been provided.
  #
  if apikey is None:
    print 'Please provide API Key. Terminating.'
    return False

  #
  # Builds URL string:
  #
  # u = Base URL.
  # m = Method or, in the case of CKAN, action.
  # h = Headers. This is where we add our API key.
  # p = Parameters. In our case we are sending a dictionary.
  #
  u = 'https://data.hdx.rwlabs.org/api/3/action'
  m = '/resource_create'
  p = _load_json(kwargs.get('path', None))
  h = {
    'X-CKAN-API-Key': apikey,
    'Content-type': 'application/json'
  }

  #
  # Making POST request to CKAN.
  # This will effectivelly adds a resource
  # to an existing dataset.
  #
  r = requests.post(u + m, headers=h, data=json.dumps(p))

  #
  # Requests will automatically raise an error
  # if there are issues with the request.
  # Let's also print the resulting JSON
  # to inspect if it all worked well.
  #
  print r.json()
  r.raise_for_status()


def Main():
  '''Wrapper.'''
  apikey = None
  CreateDataset(apikey=apikey, path='dataset.json')
  CreateResource(apikey=apikey, path='resource.json')


#
# Run it all.
#
if __name__ == '__main__':
  Main()

