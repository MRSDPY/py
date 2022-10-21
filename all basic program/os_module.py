import os
import datetime

path = "test.txt"
file = os.open(path, os.O_RDWR)
retval = os.fstat(file)

m_time = datetime.timezone(retval.st_ctime)

print(retval)