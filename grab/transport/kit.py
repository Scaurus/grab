# Copyright: 2013, Grigoriy Petukhov
# Author: Grigoriy Petukhov (http://lorien.name)
# License: BSD
from __future__ import absolute_import
#import email
import logging
#import urllib
#try:
    #from cStringIO import StringIO
#except ImportError:
    #from io import BytesIO as StringIO
#import threading
#import random
#try:
    #from urlparse import urlsplit, urlunsplit
#except ImportError:
    #from urllib.parse import urlsplit, urlunsplit
#import pycurl
#import tempfile
#import os.path

#from ..base import UploadContent, UploadFile
#from .. import error
from ..response import Response
#from ..tools.http import encode_cookies, urlencode, normalize_unicode,\
                         #normalize_http_values
#from ..tools.user_agent import random_user_agent
from ..base import Grab
from grab.kit import Kit

logger = logging.getLogger('grab.transport.kit')

class KitTransport(object):
    """
    Grab network transport powered with QtWebKit module
    """

    pass
    #def __init__(self):
        #self.curl = pycurl.Curl()

    #def setup_body_file(self, storage_dir, storage_filename):
        #if storage_filename is None:
            #handle, path = tempfile.mkstemp(dir=storage_dir)
        #else:
            #path = os.path.join(storage_dir, storage_filename)
        #self.body_file = open(path, 'wb')
        #self.body_path = path

    def reset(self):
        self.request_object = {}
        self.response = None
        #self.response_head_chunks = []
        #self.response_body_chunks = []
        #self.response_body_bytes_read = 0
        #self.verbose_logging = False
        #self.body_file = None
        #self.body_path = None

        ## Maybe move to super-class???
        self.request_head = ''
        self.request_body = ''
        self.request_log = ''

    def process_config(self, grab):
        self.request_object['url'] = grab.config['url']

    def request(self):
        kit = Kit()
        self.kit_response = kit.request(self.request_object['url'])

    def prepare_response(self, grab):
        response = Response()
        # FIX
        response.head = ''
        response.body = self.kit_response.body

        # Fix
        response.code = 200
        response.url = self.kit_response.url

        response.parse(charset='utf-8')

        response.cookies = self.extract_cookies()
        return response

    def extract_cookies(self):
        """
        Extract cookies.
        """

        return self.kit_response.cookies

    #def __getstate__(self):
        #"""
        #Reset curl attribute which could not be pickled.
        #"""
        #state = self.__dict__.copy()
        #state['curl'] = None
        #return state

    #def __setstate__(self, state):
        #"""
        #Create pycurl instance after Grag instance was restored
        #from pickled state.
        #"""

        #state['curl'] = pycurl.Curl()
        #self.__dict__ = state


class GrabKit(Grab):
    def __init__(self, response_body=None, transport='grab.transport.curl.CurlTransport',
                 **kwargs):
        super(GrabMock, self).__init__(response_body=response_body,
                                       transport='grab.transport.kit.KitTransport',
                                       **kwargs)
