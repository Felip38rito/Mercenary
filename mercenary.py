# I'm here to track the time you spent on every task
# Look, I'm not trying to get you working, I'm lazy
# Just want to make something useful with my time
import tasks as t
import sys
import os

# Create the folder which we save the data
def start_app():
  # verify if folder already exists
  if os.path.exists( os.path.expanduser('~/.mercenary/tasks.json') ):
    args = sys.argv
    
    if "stop" in args:
      print(t.stop())
    
    elif "on" in args:
      # Only start task if the task is informed
      try:
        print(t.start(args[2]))
      except IndexError:
        print("Invalid usage. use -h for help")
    
    elif "list" in args:
      print(t.resume())

    else:
      print(t.status())
  else :
    # create the folder if it not exists
    os.system('mkdir %s' % os.path.expanduser('~/.mercenary'))
    os.system('echo \'{"tasks": []}\' > %s' % os.path.expanduser('~/.mercenary/tasks.json'))
    # Let's try again, right?
    start_app()

start_app()
