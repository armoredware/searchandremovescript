#servers 10.16.114.184 , 163.151.20.11
import os
import mmap
#rootdir = '/root'
livedir = '/var/www/html'
import re


def file_seek(rootdir):
        for subdir, dirs, files in os.walk(rootdir):
                for file in files:
                        #print os.path.join(subdir, file)
                        title = os.path.join(file)

                        try:
                                if os.stat(os.path.join(subdir,file)).st_size != 0:
                                        f = open(os.path.join(subdir,file))
                                        #if os.stat(os.path.join(subdir,file)).st_size == 0:
                                        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                                        #removes all comments
                                        #comments = re.sub("<!--.*?-->", "", s, flags=re.MULTILINE)
                                        comments = re.findall("<!--.*?-->",s, flags=re.MULTILINE)
                                        #print comments
                                        is_RobComment = False
                                        for comment in comments:
                                        #future upgrade remove rob comment
                                                if 'Astorino' in comment or 'astorino' in comment:
                                                        print comment
                                                        is_RobComment = True
                                        if 'Astorino' in title or 'acechallenge' in title or 'Rob' in title or 'ACE' in title or 'Ace' in title or 'Robert' in title or 'asto' in title or 'robert' in title:
                                                print('found RA in title')
                                                flog = open('raBot_log.txt', 'a+')
                                                flog.write('Detected RA in file title:'+os.path.join(subdir, file)+'\n')
                                                #os.remove(os.path.join(subdir,file))
                                        if s.find('Astorino') != -1 or s.find('astorino') !=-1 and not is_RobComment:
                                                print('found RA in page')
                                                flog = open('raBot_log.txt', 'a+')
                                                flog.write('Detected RA in page code: '+os.path.join(subdir, file)+'\n')
                                                #os.remove(os.path.join(subdir,file))
                        except Exception as e:
                                print(e)

#file_seek(rootdir)
file_seek(livedir)
