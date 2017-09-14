#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of mtgsdk.
# https://github.com/MagicTheGathering/mtg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>
from mtgsdk.restclient import RestClient
from mtgsdk.config import __endpoint__


class QueryBuilder(object):
    def __init__(self, type):
        self.params = {}
        self.type = type

    def find(self, id):
        """Get a resource by its id
        
        Args:
            id (string): Resource id    
        Returns:
            object: Instance of the resource type
        """
        url = "{}/{}/{}".format(__endpoint__, self.type.RESOURCE, id)
        response = RestClient.get(url)[self.type.RESOURCE[:-1]]
        return self.type(response)

    def find_many(self, url, type, resource):
        """Get a list of resources
        
        Args:
            url (string): URL to invoke
            type (class): Class type
            resource (string): The REST Resource
        Returns:
            list of object: List of resource instances
        """
        list = []
        response = RestClient.get(url)[resource]
        if len(response) > 0:
            for item in response:
                list.append(type(item))

        return list

    def where(self, **kwargs):
        """Adds a parameter to the dictionary of query parameters
        
        Args:
            **kwargs: Arbitrary keyword arguments.
        Returns:
            QueryBuilder: Instance of the QueryBuilder
        """
        for key, value in kwargs.items():
            self.params[key] = value

        return self

    def all(self):
        """Get all resources, automatically paging through data

        Returns:
            list of object: List of resource objects
        """
        list = [x for x in self.iter()]

        return list
    
    def iter(self):
        """Gets all resources, automating paging through data
        
        Returns:
            iterable of object: Iterable of resource objects
        """
        
        page = 1
        fetch_all = True
        url = "{}/{}".format(__endpoint__, self.type.RESOURCE)

        if 'page' in self.params:
            page = self.params['page']
            fetch_all = False

        while True:
            response = RestClient.get(url, self.params)[self.type.RESOURCE]
            if len(response) > 0:
                for item in response:
                    yield self.type(item)

                if not fetch_all:
                    break
                else:
                    page += 1
                    self.where(page=page)
            else:
                break

        return
    
    def array(self):
        """Get all resources and return the result as an array

        Returns:
            array of str: Array of resources
        """
        url = "{}/{}".format(__endpoint__, self.type.RESOURCE)
        return RestClient.get(url, self.params)[self.type.RESOURCE]
