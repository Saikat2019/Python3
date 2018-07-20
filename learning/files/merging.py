import glob2
from datetime import datetime
filenames=glob2.glob("*.txt")
with open(datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")+".txt","w+") as mergedFile:
    for myfile in filenames:
        print(myfile)
        with open(myfile) as target:
            mergedFile.write(target.read()+"\n")
