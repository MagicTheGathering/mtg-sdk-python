#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of mtgsdk.
# https://github.com/MagicTheGathering/mtg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import urlencode


class RestClient(object):
    @staticmethod
    def get(url, params={}):
        """Invoke an HTTP GET request on a url
        
        Args:
            url (string): URL endpoint to request
            params (dict): Dictionary of url parameters 
        Returns:
            dict: JSON response as a dictionary
        """
        request_url = url
        
        if len(params) > 0:
            request_url = "{}?{}".format(url, urlencode(params))

        try:
            req = Request(request_url, headers={'User-Agent': 'Mozilla/5.0'})
            response = json.loads(urlopen(req).read().decode("utf-8"))

            return response
        except HTTPError as err:
            raise MtgException(err.read())


class MtgException(Exception):
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description
