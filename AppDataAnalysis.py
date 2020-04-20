import os
from collections import defaultdict


app_permissions=defaultdict(list)
basepath='/Users/mumanika/Semester2/CNS/HW4/'
basedir=os.listdir(basepath)

count=0
for i in basedir:
    if (not os.path.isfile(basepath+i)) and (i.startswith('co') or i.startswith('com') or i.startswith('tv')):
        try:
            f=open(basepath+i+'/result/AppData.txt', 'r')
            count+=1
        except FileNotFoundError:
            continue
        fileData=f.read().split('\n\n')
        f.close()

        # Reading the application permissions
        AppPerm=fileData[0].split('\n')
        AppPerm[0]=AppPerm[0][AppPerm[0].index(":")+1:].strip()
        AppPerm[1] = AppPerm[1][AppPerm[1].index(":") + 1:].strip()
        temp=[]
        for j in AppPerm[1].split(','):
            temp.append(j.strip())
        for k in temp:
            app_permissions[k].append(AppPerm[0])


with open("ApplicationPermissions.txt",'w+') as f:
    for i,j in app_permissions.items():
        f.write(i+"\t"+str(j)+"\n")




