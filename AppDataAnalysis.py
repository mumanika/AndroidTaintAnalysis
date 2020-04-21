import os
from collections import defaultdict
from prettytable import PrettyTable
import sys

app_permissions=defaultdict(list)
app_sinks_sources=defaultdict(dict)
grouped_sinks=defaultdict(list)
grouped_source=defaultdict(list)

basepath='/Users/mumanika/Semester2/CNS/HW4/'
basedir=os.listdir(basepath)

count=0
for i in basedir:
    if (not os.path.isfile(basepath+i)) and (i.startswith('co') or i.startswith('com') or i.startswith('tv')):
        try:
            f=open(basepath+i+'/result/AppData.txt', 'r')
            count+=1
        except FileNotFoundError:
            print("AppData.txt is not found in directory: "+i, file=sys.stderr)
            continue
        fileData=f.read()
        f.close()

        # Reading the application permissions
        AppPerm=fileData.split('\n\n')[0].split('\n')
        AppPerm[0]=AppPerm[0][AppPerm[0].index(":")+1:].strip()
        AppPerm[1] = AppPerm[1][AppPerm[1].index(":") + 1:].strip()
        temp=[]
        for j in AppPerm[1].split(','):
            temp.append(j.strip())
        for k in temp:
            app_permissions[k].append(AppPerm[0])

        # Counting the number of sources and sinks
        apiSinkCount=0
        iccSinkCount=0
        callbackSourceCount=0
        iccSourceCount=0
        apiSourceCount=0
        for i in fileData.split('\n'):
            if i.startswith("    <Descriptors: api_sink:"):
                apiSinkCount+=1
            elif i.startswith("    <Descriptors: icc_sink:"):
                iccSinkCount+=1
            elif i.startswith("    <Descriptors: icc_source:"):
                iccSourceCount+=1
            elif i.startswith("    <Descriptors: api_source:"):
                apiSourceCount+=1
            elif i.startswith("    <Descriptors: callback_source:"):
                callbackSourceCount+=1
        app_sinks_sources[AppPerm[0]]["API Sinks"]=apiSinkCount
        app_sinks_sources[AppPerm[0]]["ICC Sinks"] = iccSinkCount
        app_sinks_sources[AppPerm[0]]["Callback Sources"] = callbackSourceCount
        app_sinks_sources[AppPerm[0]]["ICC Sources"] = iccSourceCount
        app_sinks_sources[AppPerm[0]]["API Sources"] = apiSourceCount

        # counting groups of sink and source
        for i in fileData.split('\n'):
            if i.startswith('    <Descriptors: api_source: Ljava/net/URLConnection'):
                grouped_source['Network based Source'].append(AppPerm[0])
                break

        for i in fileData.split('\n'):
            if i.startswith('    <Descriptors: api_source: Landroid/telephony/TelephonyManager'):
                grouped_source['Telephony based Source'].append(AppPerm[0])
                break

        for i in fileData.split('\n'):
            if i.startswith('    <Descriptors: icc_source: Landroid/content/Intent'):
                grouped_source['Intent based Source'].append(AppPerm[0])
                break

        for i in fileData.split('\n'):
            if i.startswith('    <Descriptors: api_sink: Landroid/util/Log'):
                grouped_sinks['Utility Log based Sink'].append(AppPerm[0])
                break

        for i in fileData.split('\n'):
            if i.startswith('    <Descriptors: api_sink: Ljava/io/FileOutputStream'):
                grouped_sinks['File Output based Sink'].append(AppPerm[0])
                break

        for i in fileData.split('\n'):
            if i.startswith('    <Descriptors: api_sink: Ljava/net/URL;.openConnection'):
                grouped_sinks['Network based Sink'].append(AppPerm[0])
                break



with open("ApplicationPermissions.txt",'w+') as f:
    for i,j in app_permissions.items():
        f.write('{:100}'.format(i)+'\n'+str(j)+"\n\n\n")


with open("SourcesAndSinks.txt",'w+') as f:
    for i,j in app_sinks_sources.items():
        f.write("Application name: "+i+"\n")
        table = PrettyTable(['Source/Sink', 'Count'])
        for x,y in j.items():
            table.add_row([x,y])
            #f.write('{:20}'.format(x)+"\t"+str(y)+"\n")
        f.write(table.get_string())
        f.write("\n\n")

with open("GroupedSources.txt",'w+') as f:
    table=PrettyTable(['Category','Application list'])
    for i,j in grouped_source.items():
        table.add_row([i,str(j).lstrip('[').rstrip(']')])
    f.write(table.get_string())
    f.write("\n\n")

with open("GroupedSinks.txt",'w+') as f:
    table=PrettyTable(['Category','Application list'])
    for i,j in grouped_sinks.items():
        table.add_row([i,str(j).lstrip('[').rstrip(']')])
    f.write(table.get_string())
    f.write("\n\n")


