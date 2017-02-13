import os
import time

source = [r'F:\test\python\test1', r'F:\test\python\test2']

target_dir = r'F:\test\python\backup\\'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr %s %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup Faild'
