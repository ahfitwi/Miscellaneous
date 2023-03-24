# Module
# Python pickle module is used for serializing and de-serializing python object structures
import json
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
   
#-----------------------------------------------
# Save Data To Disk As JSON
dct = {"Alem":40}
with open('datafile.json', 'w') as fp:
   json.dump(dct, fp)
fp.close(
    
# Read json Data From Disk Unpickled
with open ("datafile.json", "r") as fp:
  alem = json.load(fp)
fp.close()

# Convert dict to json On Memory
  dct = {"Alem":40}
  jsondata = pickle.dumps(arr)

# Convert json to dict On Memory
  dct = pickle.loads(jsondata)
#-----------------------------------------------
