# -*- coding: utf-8 -*-

#date:2013/10/3
#author:idevcod@163.com
#description:扫描tcp开放端口

import re;
import csv;
import os;
import threading;
import time

count_percentage=0;
def write_info(lock,ip_begin,ip_end):
  global count_percentage;
  tcp_list=[];
  re_string='PORT\s*STATE\s*SERVICE(?P<port>.*?)Nmap';
  for current_ip in range(ip_begin,ip_end):
    commandLine='sudo nmap 202.201.1.'+str(current_ip);
    exe_cmd=os.popen(commandLine,'r').read();
    found=re.search(re_string,exe_cmd,re.S);
    if not found:
      lock.acquire();
      count_percentage+=1;
      lock.release();
      continue;
    else:
      found=found.group("port");
      mylist=[];
      head_tuple=('ip','PORT','STATE','SERVICE');
      mylist.append(head_tuple);
      for item in found.splitlines():
	dicts=item.split();
	if len(dicts)!=0:
	  row=dicts[0].split('/');
	  mylist.append(('202.201.1.'+str(current_ip),row[0],dicts[1],dicts[2]));
	  tcp_list.append(dicts[1]);
      #lock.acquire();
      try:
	csv_file=open('/home/dell/network_pro/new20101.csv','a+');
	writer=csv.writer(csv_file);
	lock.acquire();
	count_percentage+=1;
	lock.release();
	writer.writerows(mylist);
      finally:
	csv_file.close();
	#print '正在解锁';
	#lock.release();
  print "thread %shas finished"%(threading.currentThread().getName());
  #print tcp_list.sort();
	
def report_progress():
  global count_percentage;
  while count_percentage<255:
    #percentage=count_percentage/255.0;
    print 'have scann %d port '%count_percentage;
    #print 'have finished %d%%'%(percentage);
    time.sleep(30);#每30秒报告一次进度
  print 'total ports is%s' %count_percentage;
    
def scan_main():
  os.system('sudo echo "start scaning..."');
  #print 'ok';
  lock=threading.Lock();
  #write_info(lock,150,160);
  #for i in range(5):
    #t=threading.Thread(target=write_info,args=(lock,i*51+1,(i+1)*51+1,));
    #t.start();
  t=threading.Thread(target=write_info,args=(lock,0,256,));
  t.start();
  t=threading.Thread(target=report_progress,args=());
  t.start();

  
if __name__=='__main__':
  scan_main();