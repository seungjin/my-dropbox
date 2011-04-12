#!/usr/bin/env python

from fsevents import Observer
from fsevents import Stream



from googlestorage import Googlestorage

"""
Bit                Description
IN_ACCESS          File was accessed (read) (*)
IN_ATTRIB          Metadata changed (permissions, timestamps, extended attributes, etc.) (*)
IN_CLOSE_WRITE     File opened for writing was closed (*)
IN_CLOSE_NOWRITE   File not opened for writing was closed (*)
IN_CREATE          File/directory created in watched directory (*)
IN_DELETE          File/directory deleted from watched directory (*)
IN_DELETE_SELF     Watched file/directory was itself deleted
IN_MODIFY          File was modified (*)
IN_MOVE_SELF       Watched file/directory was itself moved
IN_MOVED_FROM      File moved out of watched directory (*)
IN_MOVED_TO        File moved into watched directory (*)
IN_OPEN            File was opened (*)
"""


"""
==mask value==
512:
2:
256: looks like new file comming
"""


# TODO
# DATABASE, METADATA
# NOT BIG DEAL!!!


def main():

  observer = Observer()
  observer.start()
  path = '/Users/seungjin/Desktop'

  def callback(event):
    #print "mask: " + str(event.mask)
    #print "cookie: " + str(event.cookie)
    #print "name: " + str(event.name)
    print event
    if event.mask == 256:  #looks like new file comming
      newFile(str(event.name))
    elif event.mask == 512:  #looks line file deleted
      rmFile(str(event.name))
    elif event.mask == 2:  #looks like overwriting?
      print "hihihihi"

  def newFile(filename):
    print "new file is comming"
    #pushing this file into cloud
    gs = Googlestorage()
    #print gs.list_objects()
    gs.upload_objects(filename)
  
  def rmFile(filename):
    #print "%s is removed" % filename
    gs = Googlestorage() # this is evil.. do i need to make global goolgestorage object??? idk
    gs.delete_objects_and_buckets(filename)
    

  stream = Stream(callback,path,file_events=True)
  observer.schedule(stream)

if __name__ == "__main__":
  watch_folder = ""
  main()


