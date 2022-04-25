import os
command = "ls"  #The command needs to be a string
os.system(command) #The command can also be passed as a string, instead of a variable

os.system('cmd /k "date"') 
os.system('cmd /k "color a & date"')
os.system('cmd /c "color a"')
os.system('cmd /k "Your Command Prompt Command"')
os.system("start cmd /c {command here}")     # Launches in new command prompt, closes when done

from subprocess import check_output
check_output("dir C:", shell=True)

from subprocess import check_output
check_output("dir C:", shell=True).decode()

import os
os.system("python test.py")