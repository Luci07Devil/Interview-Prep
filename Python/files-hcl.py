#script to create file and folders based on input value 

import os 

def createFiles(filesCount):
 
 if os.path.exists(os.getcwd()):
  for i in range(1,filesCount+1):
    folder=f"folder{i}"
    if not os.path.exists(os.path.join(os.getcwd(),folder)):
     os.mkdir(folder)  
     if not os.path.exists(os.path.join(os.getcwd(),f"file{i}")):
      for j in range(1,filesCount+1) :
       with open(f'file{j}','w+') as f:
        f.write(f"I am file{j}")
     else:
      print("file exists skipping")
    else:
      continue
 else:
  print("file already found")

createFiles(3)
