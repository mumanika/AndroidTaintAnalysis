# AndroidTaintAnalysis

**Author:** Mukul Manikandan *(mmanika@ncsu.edu)*

Environment: Python 3

## Steps to run script:
1. Run amandroid on the application set and place all the results in a particular directory. 
2. Place the executable script in a suitable directory. 

## Command to run the script 
> \# ./AppDataAnalysis <<'path to amandroid ouput'>>

Note: If the /results/AppData.txt file is not present, the script will continue its execution, ignoring the subdirectory. 

## Outputs:

The script will generate the following output files: 
1. ApplicationPermissions.txt: This file contains all the permissions reported by Amandroid that are used by the application.
2. GroupedSinks.txt: This file contains all the applications that are categorised as Utility based sinks, Network based sinks and File output based sinks. 
3. GroupedSources.txt: This file contains all the applications that are categorised as Network based sources, Intent based sources and Telephony based sources. 
4. SourcesAndSinks.txt: This file contains tha tally of all the types of sources and sinks that are part of the applicaiton. 
5. ValidTaintPaths.txt: This file lists the applications that have valid taint paths that are reported by Amandroid. 
6. ValidNetworkSinkPaths.txt: This file lists the applications that have network based sinks that make URL connections. 

