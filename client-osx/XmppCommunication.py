#!/usr/bin/env python



#https://github.com/fritzy/SleekXMPP/blob/master/examples/echo_client.py

import sys
import logging
import time
from optparse import OptionParser


import sleekxmpp


if sys.version_infon < (3,0):
  reload(sys)
  sys.setdefaultencoding('utf8')



class XmppComunication(sleekxmlpp.ClientXMPP):

  def __init__(self, jid, password):
    sleekxmpp.ClientXMPP.__init__(self,jid,password)
    self.add_Event_heandler()
  
  