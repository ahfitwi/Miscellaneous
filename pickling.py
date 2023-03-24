# Module
# Python pickle module is used for serializing and de-serializing python object structures
import pickle
import numpy as np

# Save Pickled Data To Disk
mylist = ['a', 'b', 'c', 'd']
with open('datafile.txt', 'wb') as fp:
   pickle.dump(mylist, fp)
fp.close(
    
# Read Pickled Data From Disk Unpickled
import pickle
with open ("datafile.txt", "rb") as fp:
  emp = pickle.load(fp)
fp.close()

# Pickled Data On Memory
  arr = np.array([[1,2][3,4]])
  pickled_arr = pickle.dumps(arr)

# Unpickle Data On Memory
  unpickled_arr = pickle.loads(arr)
