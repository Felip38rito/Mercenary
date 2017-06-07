# # Tasks functionality + filesystem storage
# 
import json
import os
from datetime import datetime as date

def _load_queue():
  with open(os.path.expanduser('~/.mercenary/tasks.json'), 'r') as queue:
    return json.load(queue)

def _write_queue(queue):
  with open(os.path.expanduser('~/.mercenary/tasks.json'), 'w') as q:
    json.dump(queue, q)

def _now():
  return date.strftime(date.now(), "%d-%m-%y %H:%M:%S")

def _get_current_task():
  q = _load_queue()
  if len(q["tasks"]) == 0:
    return None
  else:
    return q["tasks"][-1]

# Start working in a task
# Receive records - a tasks queue
def start(task):
  q = _load_queue()
  # stop the current task if active
  stop()
  # start new task
  q["tasks"].append({
    "name": task,
    "start": _now(),
    "stop": None
  })

  _write_queue(q)
  return "Started the task %s" % task

# Stop working in a task
def stop():
  q = _load_queue()
  c = _get_current_task()
  
  # stop the current task if active
  if c != None and c["stop"] == None:
    q["tasks"][-1]["stop"] = _now()
  else: 
    return "No active task at the moment"

  _write_queue(q)

  return "Stopped the task %s" % c["name"]

# Status of my actual work
def status():
  queue = _load_queue()
  
  if len(queue["tasks"]) == 0:
    return "There are no current tasks"
  
  current_task = queue["tasks"][-1]
  return "Working on %s since %s" % (current_task["name"], current_task["start"].split(" ")[1])

# Show the list of the tasks of today
def resume():
  return "list of tasks of today"

# Build the records queue based on txt saved
def _read_saved_tasks():
  pass
