tasks=[]

def main_menu():
    print('===TO-DO-LIST===')
    print('1.Add task')
    print('2.Show tasks')
    print('3.search task')
    print('4.Mark task as done ')
    print('5.remove task')
    print('6.EXIT')
   

def add_task():
    task=input('Add new task: ')
    tasks.append({'name':task,'status':'pending'})
    print(f"task [{task}] added .")

def show_tasks():
    if not tasks:
        print('No tasks added.')
        return 
    for index , task in enumerate(tasks , start=1):
       
        print(f"{index}-{task['name']} is {task['status']}")

def mark_task_done():
    show_tasks()
    if not tasks:
       print('no tasks found.')
       return
    
    try:
      task_num=int(input('enter a number:'))
      if task_num<=0 or task_num > len(tasks):
          print('invalid number !')
      else:
       tasks[task_num-1]['status']='DONE!'
       print('task mark as done ')
    except ValueError:
        print('enter valid number ')

def search_task():
   if not tasks:
        print('no tasks found.')
        return
   
   search=input('enter task name : ')
   
   if search.isdigit():
        print('enter valid task name, not index')
        return
   for t in tasks:
        if search == t['name']:
            print(f"task is {search} and Status: {t['status']}")
            return

   print('task not found.')
   
      
def remove_task():   
   
    if not tasks:
        print('no tasks found.')
        return
    show_tasks()
    
    task_name = input('enter task name to remove: ')

    found=False
    for task in tasks:
        if task['name'] == task_name:
           tasks.remove(task)
           print('task has been removed')
           found=True
           break
    if not found :
          print ('task name not found')
    

while True:
  main_menu()
  choice=input('choose an option (1-6) : ')
  if choice=='1':
     add_task()
  elif choice=='2':
     show_tasks()
  elif choice=='3':
     search_task()
  elif choice=='4':
     mark_task_done()
  elif choice=='5':
     remove_task()
  elif choice=='6':
       print('finished')
       break
  else :
     print('invalid number , try again ')

