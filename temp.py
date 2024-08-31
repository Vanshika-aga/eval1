# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def add_task(task):
    a=[2,"sit","ongoing"]
    task.append(a)
    
def display():
    for tasks in task:
        print(tasks)
def remove_task(task,t):
    l=[]
    for tasks in task:
        if(tasks!=t):
            l.append(tasks)
    task=l 
def delete_by_name(tasks,name):
    for task in tasks:
        a=task[1]
        if(a==name):
            tasks.remove(task)
def update_task(tasks,task,no,upd):
    for t in tasks:
        if(t==task):
            if(no==0):
                t[0]=upd
            else:
                t[1]=upd
            
def search_task(t,task):
    flag=0
    for tasks in task:
        if(tasks==t):
           print("found")
           flag=1
    if(flag==0):     
        print("not found")
def search_task_with_name(task,name,no):
    for tasks in task:
        a=name[no]
        if(a==name):
            print("FOUND BY NAME")
def search_task_with_letter(task,letter):
    flag=0
    for tasks in task:
        a=tasks[1]
        if(a[len(a)-1]==letter):
                print("Found")
                flag=1
    if(flag==0):
        print("Not found")
    
t =[1,"play","ompleted"];
task=[[1,"work","completed"]]
remove_task(task,t)
display()
search_task_with_letter(t,'a')
