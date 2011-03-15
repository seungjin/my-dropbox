#!/usr/bin/env python

from fsevents import Observer
from fsevents import Stream

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

def main():

  observer = Observer()
  observer.start()
  path = '/Users/seungjin/Desktop'

  def callback(event):
    print "mask: " + str(event.mask)
    print "cookie: " + str(event.cookie)
    print "name: " + str(event.name)

  stream = Stream(callback,path,file_events=True)
  observer.schedule(stream)


if __name__ == "__main__":
    main()

