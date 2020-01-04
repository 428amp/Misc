from ArrayQueue import ArrayQueue
import os
import sys

def disk_usage(path):
  total = os.path.getsize(path)
  if os.path.isdir(path):
    for filename in os.listdir(path):
      childpath = os.path.join(path, filename)
      total += disk_usage(childpath)
  
  print('{0:<7}'.format(total), path)
  return total

def searchDirectory(directory, fileName):
  q = ArrayQueue()
  q.enqueue(directory)
  while not q.is_empty():
    prefix = q.dequeue()
    for name in os.listdir(prefix):
      if name == fileName:
        return True
      if os.path.isdir(prefix+'/'+name):
        q.enqueue(prefix+'/'+name)
  return False


if __name__ == '__main__':
  directory = sys.argv[1]
  fileName = sys.argv[2]
  print(searchDirectory(directory, fileName))