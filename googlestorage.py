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
    uri = boto.storage_uri('seungjin', self.GOOGLE_STORAGE)
    for obj in uri.get_bucket():
      print '%s://%s/%s' % (uri.scheme, uri.bucket_name, obj.name)
      #print '  "%s"' % obj.get_contents_as_string()
      
  def upload_objects(self):
    # Make some temporary files.
    temp_dir = tempfile.mkdtemp(prefix='googlestorage')
    tempfiles = {
      'labrador.txt': 'Who wants to play fetch? Me!',
      'collie.txt': 'Timmy fell down the well!'
    }
    for filename, contents in tempfiles.iteritems():
      fh = file(os.path.join(temp_dir, filename), 'w')
      fh.write(contents)
      fh.close()

    # Upload these files to DOGS_BUCKET.
    for filename in tempfiles:
      contents = file(os.path.join(temp_dir, filename), 'r')

    dst_uri = boto.storage_uri(DOGS_BUCKET + '/' + filename, GOOGLE_STORAGE)
    # The key-related functions are a consequence of boto's
    # interoperability with Amazon S3 (which employs the
    # concept of a key mapping to contents).
    dst_uri.new_key().set_contents_from_file(contents)
    contents.close()
    print 'Successfully created "%s/%s"' % (dst_uri.bucket_name, dst_uri.object_name)
    shutil.rmtree(temp_dir)  # Don't forget to clean up!
  
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
a.list_objects()