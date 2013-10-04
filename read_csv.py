# -*- coding: utf-8 -*-
#csv之reader用法测试
import csv;
def write_head(tcp_list,my_dic):
  head_list=['ip'];
  for item in tcp_list:
    head_list.append(item+'/'+my_dic[item]);
  #print tuple(head_list);
  return tuple(head_list);
  
def gen_tuple(tuple_list,lenth):
  for i in range(lenth):
    tuple_list.append('N');
  return tuple_list;
  
tcp_list=[];
dictionary_list=[];
with open('/home/dell/network_pro/new20100.csv','rb') as csvfile:
  content=csv.reader(csvfile,delimiter=',');
  for row in content:
    #dicts=row[1].split('/');
    if row[1] not in tcp_list:
      tcp_list.append(row[1]);
      dictionary_list.append((row[1],row[3]));
    

tcp_list.remove('PORT');
tcp_list.sort(key=int);
my_dic=dict(dictionary_list);
print tcp_list;
print '字典为';
print my_dic;
print '一共tcp端口开放个数为:'
print len(tcp_list);
#tuple_list=[''];
#for i in range(len(tcp_list)):
  #tuple_list.append('N');
  
#print len(tuple_list),tuple_list;
#print tuple(tuple_list);
print 'csv头文件';

current_ip='0';
current_list=[];
tuple_list=[];
with open('/home/dell/network_pro/refnew20100.csv','a+') as writefile:
  writer=csv.writer(writefile);
  writer.writerow(write_head(tcp_list,my_dic));
  with open('/home/dell/network_pro/new20100.csv','rb') as csvfile:
    content=csv.reader(csvfile,delimiter=',');
    for row in content:
      if current_ip==row[0]:
	current_list[tcp_list.index(row[1])+1]='Y('+row[2]+')';
      else:
	row_tuple=tuple(current_list);
	if len(row_tuple)!=0 and row[0]!='ip':
	  #print row_tuple;
	  #print current_ip;
	  writer.writerow(row_tuple);
	if row[0]!='ip':
	  current_ip,tuple_list=str(row[0]),[row[0]];
	  current_list=gen_tuple(tuple_list,len(tcp_list));
    writer.writerow(tuple(current_list));
      