import os
import sys
with open('read.txt','w') as f:
    f.write(os.name)
    f.write(sys.version)
    f.close()

    with open('read,txt','r') as e:
        a= e.read()
        print(a)
        e.close()