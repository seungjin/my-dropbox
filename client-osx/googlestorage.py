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

    
    config = ConfigParser.RawConfigParser()
    config.read(os.path.dirname(os.path.realpath(__file__))+'/config')
    #gs_access_key_id = config.get('google storage','gs_access_key_id')
    #gs_secret_access_key = config.get('google storage','gs_secret_access_key')
    
    # URI scheme for Google Storage
    self.GOOGLE_STORAGE = 'gs'
    # URI scheme for accessing local files
    self.LOCAL_FILE = 'file'
    
    self.GOOGLE_STORAGE_MY_BUCKET = config.get('google storage my bucket','my_bucket')

  def create_buckets(self):
    # TODO
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
    # TODO
    uri = boto.storage_uri('',self.GOOGLE_STORAGE)
    for bucket in uri.get_all_buckets():
      print bucket.name

  def list_objects(self):
    uri = boto.storage_uri(self.GOOGLE_STORAGE_MY_BUCKET, self.GOOGLE_STORAGE)
    object_list = []
    for obj in uri.get_bucket():
      object = {'scheme': uri.scheme, 'bucket_name': uri.bucket_name, 'name': obj.name}
      object_list.append(object)
    return object_list

  def upload_objects(self, myFile):
    print myFile
    # TODO
    # Make some temporary files.
    temp_dir = tempfile.mkdtemp(prefix='googlestorage')
    
    """
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
    """
    filename = myFile
    contents = file(myFile,'r')
    
    dst_uri = boto.storage_uri("seungjin-mydropbox" + '/' + filename, 'gs')
    # The key-related functions are a consequence of boto's
    # interoperability with Amazon S3 (which employs the
    # concept of a key mapping to contents).
    dst_uri.new_key().set_contents_from_file(contents)
    contents.close()
    print 'Successfully created "%s/%s"' % (dst_uri.bucket_name, dst_uri.object_name)
    shutil.rmtree(temp_dir)  # Don't forget to clean up!
  
  def download_and_copy_objects(self):
    #TODO
    dest_dir = os.getenv('HOME')
    for filename in ('collie.txt', 'labrador.txt'):
      src_uri = boto.storage_uri(
        DOGS_BUCKET + '/' + filename, GOOGLE_STORAGE)
    # Create a file-like object for holding the object contents.
    object_contents = StringIO.StringIO()
    # The unintuitively-named get_file() doesn't return the objects's
    # contents; instead, it actually writes the contents to
    # object_contents.
    src_uri.get_key().get_file(object_contents)
    local_dst_uri = boto.storage_uri(os.path.join(dest_dir, filename), LOCAL_FILE)
    bucket_dst_uri = boto.storage_uri(CATS_BUCKET + '/' + filename, GOOGLE_STORAGE)
    for dst_uri in (local_dst_uri, bucket_dst_uri):
      object_contents.seek(0)
      dst_uri.new_key().set_contents_from_file(object_contents)
    object_contents.close()
  
  def change_object_acls(self):
    # TODO
    uri = boto.storage_uri(DOGS_BUCKET + '/labrador.txt', GOOGLE_STORAGE)
    print str(uri.get_acl())
    uri.add_email_grant('FULL_CONTROL', 'valid-email-address')
    print str(uri.get_acl())
  
  def read_bucket_and_object_metadata(self):
    # TODO
    # Print ACL entries for DOGS_BUCKET.
    bucket_uri = boto.storage_uri(DOGS_BUCKET, GOOGLE_STORAGE)
    for entry in bucket_uri.get_bucket().get_acl().entries.entry_list:
      entry_id = entry.scope.id
      if not entry_id:
        entry_id = entry.scope.email_address
      print 'SCOPE: %s' % entry_id
      print 'PERMISSION: %s\n' % entry.permission
    # Print object metadata and ACL entries.
    object_uri = boto.storage_uri(DOGS_BUCKET + '/labrador.txt', GOOGLE_STORAGE)
    print ' Object size:\t%s' % key.size
    print ' Last mod:\t%s' % key.last_modified  
    print ' MIME type:\t%s' % key.content_type
    print ' MD5:\t%s' % key.etag.strip('"\'') # Remove surrounding quotes
    for entry in key.get_acl().entries.entry_list:
      entry_id = entry.scope.id
      if not entry_id:
        entry_id = entry.scope.email_address
      print 'SCOPE: %s' % entry_id
      print 'PERMISSION: %s\n' % entry.permission
  
  def delete_objects_and_buckets(self, myFile):
    # TODO
    """
    for bucket in (CATS_BUCKET, DOGS_BUCKET):
      uri = boto.storage_uri(bucket, GOOGLE_STORAGE)
    for obj in uri.get_bucket():
      print 'Deleting object: %s...' % obj.name
      obj.delete()
    print 'Deleting bucket: %s...' % uri.bucket_name
    uri.delete_bucket()
    """
    uri = boto.storage_uri('seungjin-mydropbox', 'gs')
    for obj in uri.get_bucket():
      if "/"+str(obj.key) == myFile :
        print "sd"
        obj.delete()
    

# debug/test
#a = Googlestorage()
#print a.list_objects()