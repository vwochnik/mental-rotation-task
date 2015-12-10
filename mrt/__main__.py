import sys, traceback
from __init__ import *

def main():
    inst = Main(640, 480, "Mental Rotation Task")
    inst.init()
    try:
        inst.loop()
    except Exception, e:
        tb = sys.exc_info()[2]
        traceback.print_exception(e.__class__, e, tb)
    inst.quit()

if __name__ == '__main__':
    main()
