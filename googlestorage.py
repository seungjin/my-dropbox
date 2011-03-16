#!/usr/bin/env python


# http://code.google.com/apis/storage/docs/gspythonlibrary.html
import StringIO
import os
import shutil
import tempfile
import time
import ConfigParser

import boto

class Googlestorage(object):
  
  def __init__(self):
    # READ developer keys from the ~/.boto config file
    self.config = boto.config
    # let's see your ~/.boto credential
    
    #config.add_section('Credentials')
    #config.set('Credentials', 'gs_access_key_id', 'YOURACCESSKEY')
    #config.set('Credentials', 'gs_secret_access_key', 'YOURSECRETKEY')

    
    #config = ConfigParser.RawConfigParser()
    #config.read(os.path.dirname(os.path.realpath(__file__))+'/config')
    #gs_access_key_id = config.get('google storage','gs_access_key_id')
    #gs_secret_access_key = config.get('google storage','gs_secret_access_key')
    
    # URI scheme for Google Storage
    self.GOOGLE_STORAGE = 'gs'
    # URI scheme for accessing local files
    self.LOCAL_FILE = 'file'
  
  def create_buckets(self):
    now = time.time()
    CATS_BUCKET = 'cats-%d' % now
    DOGS_BUCKET = 'dogs-%d' % now
    
    for name in (CATS_BUCKET, DOGS_BUCKETS):
      # Instantiate a BucketStorageUri object
      uri = boto.storage_uri(name, GOOGLE_STORAGE)
      try :
        uri.create_bucket()
        print "Suceesfully created bucket \"%s\"" %name
      except boto.exception.StorageCreateError, e:
        print "Failed to create bucket:" , e

  def list_buckets(self):
    uri = boto.storage_uri('',self.GOOGLE_STORAGE)
    for bucket in uri.get_all_buckets():
      print bucket.name
      
  def list_objects(self):
    pass
      
  def upload_objects(self):
    pass
  
  def download_and_copy_objects(self):
    pass
  
  def change_object_acls(self):
    pass
  
  def read_bucket_and_object_metadata(self):
    pass
  
  def delete_objects_and_buckets(self):
    pass

# debug/test
a = Googlestorage()
a.list_buckets()