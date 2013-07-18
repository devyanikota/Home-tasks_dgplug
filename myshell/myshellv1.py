from cmd2 import Cmd
from getpass import getuser
import sys
import requests
 
__version__ = '0.1'
 
class Application(Cmd):
    """
   The main Application class
 
   """
 
    def __init__(self):
        Cmd.__init__(self)
 
    def do_hello(self, line):
        print "Hello:", line

    def do_greet(self,line):
        print "Hi %s :)" %(getuser())

    def do_stock(self,line):
        r=requests.get('http://download.finance.yahoo.com/d/quote.csv?s='+line+'&f=l1')
        data=r.text
        value=float(data)
        print value
 
if __name__ == '__main__':
    app = Application()
    app.cmdloop()
