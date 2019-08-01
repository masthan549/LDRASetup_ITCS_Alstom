import os, sys, time
import subprocess
from subprocess import *
from tkinter import messagebox


def script_exe(LDRAToolsuitePath, vvpath, sourceFilesDir, sourceFilesCommonDir, sparePath, TkObject_ref, statusBarText):

    global statusBar

    statusBar = statusBarText

    #LDRAToolsuitePath = "C:\LDRA_Toolsuite"
    #sourceFilesDir = "C:\SCM\IWP\VPM-3 DO-WCM\Software Engineering\VPM_3 AB Exec"
    #sourceFilesCommonDir = "C:\SCM\IWP\VPM-3 DO-WCM\Software Engineering\VPM_3 Common"
    #vvpath = "C:\SCM\IWP\VPM-3 DO-WCM\Software Engineering\\V&V\\Unit Test"

    
    #Set the curret directory
    os.chdir(sourceFilesDir)
    
    #Run batch file
    statusBar.set("Directories are listing from given path...")
    
    #Fetch all source files sub directories in given path
    SourceDirectoriesInSelectedPath = []
    for root, directories, filenames in os.walk(sourceFilesDir):
        for directory in directories:
            SourceDirectoriesInSelectedPath.append(os.path.join(root, directory))
    
    #Fetch all source files common sub directories in given path
    CommonDirectoriesInSelectedPath = []
    for root, directories, filenames in os.walk(sourceFilesCommonDir):
        for directory in directories:
            CommonDirectoriesInSelectedPath.append(os.path.join(root, directory))
    
    #This is the additional files path where modified code files are placed
    additionFilesDir = []
    additionFilesDir.append(vvpath)

    listOfDir = additionFilesDir + SourceDirectoriesInSelectedPath + CommonDirectoriesInSelectedPath
    
    #Write directories to file
    fPtr = open("DirInSelectedPath.txt",'w')
    
    statusBar.set("Listed directories are writing into text file \"DirInSelectedPath.txt\"...")
    
    #Add these source code directories to Environment variables
    allDir = ';'.join(listOfDir)
    fPtr.write(allDir)
    fPtr.close()
    
    statusBar.set("Batch file execution in progress, please wait...")
    

    p = subprocess.Popen(['C:/SCM/VEG/Wayside/Formal Testing/EIXS Formal Testing/Software Tests/Unit Test/Unit test Automation/setup.bat', LDRAToolsuitePath, vvpath, allDir], stdout = subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout, stderr = p.communicate()

    print("\n Number of Errors seen during batch file execution: "+len(str(stderr)))

    if(len(str(stderr))) > 0:
        print("\n\n ****** ERRORs seen white executing batch *****\n\n"+str(stdout))

    time.sleep(10)

    statusBar.set("DONE!!")	
    #messagebox.showinfo('DONE!!',"Project configuration is complete!")
    #TkObject_ref.destroy()
    #sys.exit()
