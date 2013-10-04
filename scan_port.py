# -*- coding: utf-8 -*-

import re;
import csv;
import os;
import threading;
import time;
count_percentage=0;
def write_info(lock,ip_begin,ip_end):
  global count_percentage;
  re_string='PROTOCOL\s*STATE\s*SERVICE(?P<port>.*?)Nmap';
<<<<<<< HEAD
  for current_ip in range(ip_begin,ip_end):
    commandLine='sudo nmap 202.201.0.'+str(current_ip);
=======
  csv_file=open('/home/dell/network_pro/test20101.csv','a+');
  writer=csv.writer(csv_file);
  for current_ip in range(ip_begin,ip_end):
    commandLine='sudo nmap -sO 202.201.1.'+str(current_ip);
>>>>>>> b74fd10fe68e4c4912c5bf727553975bc50ba59d
    #commandLine='sudo nmap -sO localhost';
    exe_cmd=os.popen(commandLine,'r').read();
    #print exe_cmd;
    found=re.search(re_string,exe_cmd,re.S);
    if not found:
      #print 'null';
<<<<<<< HEAD
      lock.acquire();
      count_percentage+=1;
      lock.release();
=======
>>>>>>> b74fd10fe68e4c4912c5bf727553975bc50ba59d
      continue;
    else:
      found=found.group("port");
      mylist=[]
      head_tuple=(str(current_ip),'PROTOCOL','STATE','SERVICE');
      mylist.append(head_tuple);
      for item in found.splitlines():
	dicts=item.split();
	if len(dicts)!=0:
	  mylist.append((' ',dicts[0],dicts[1],dicts[2]));
      #print '正在获取锁';
      lock.acquire();
      try:
<<<<<<< HEAD
	csv_file=open('/home/dell/network_pro/port20100.csv','a+');
	writer=csv.writer(csv_file);
	count_percentage+=1;
	writer.writerows(mylist);
      finally:
	csv_file.close();
	#print '正在解锁';
	lock.release();
=======
	count_percentage+=1;
	writer.writerows(mylist);
      finally:
	#print '正在解锁';
	lock.release();
  csv_file.close();
>>>>>>> b74fd10fe68e4c4912c5bf727553975bc50ba59d
  print "thread %shas finished"%(threading.currentThread().getName());
	
def report_progress():
  global count_percentage;
  while count_percentage<255:
<<<<<<< HEAD
    #percentage=count_percentage/255.0;
    print 'have scann %d port '%count_percentage;
    #print 'have finished %d%%'%(percentage);
    time.sleep(300);#每五分钟报告一次进度
  print 'total ports is%s' %count_percentage;
=======
    percentage=count_percentage/255;
    print 'have finished %d%%'%(percentage);
    time.sleep(300);#每五分钟报告一次进度
>>>>>>> b74fd10fe68e4c4912c5bf727553975bc50ba59d
    
def scan_main():
  os.system('sudo echo "start scaning..."');
  #print 'ok';
  lock=threading.Lock();
  for i in range(5):
    t=threading.Thread(target=write_info,args=(lock,i*51+1,(i+1)*51+1,));
    t.start();
<<<<<<< HEAD
=======
  #write_info(lock,1,2);
  #print 'ok';
>>>>>>> b74fd10fe68e4c4912c5bf727553975bc50ba59d
  t=threading.Thread(target=report_progress,args=());
  t.start();

  
if __name__=='__main__':
<<<<<<< HEAD
  scan_main();
=======
  scan_main();
>>>>>>> b74fd10fe68e4c4912c5bf727553975bc50ba59d
