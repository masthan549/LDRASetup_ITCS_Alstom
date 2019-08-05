import os, sys, time, re
from os import path
import subprocess
from subprocess import *
from tkinter import messagebox

def getVSPaths(line_read):
    VSPaths = []
    splitLines = line_read.split(';')
    for listIndx in splitLines:
        if 'Visual Studio' in listIndx:
            if 'INCLUDE=' in listIndx:
                listIndx = listIndx.replace("INCLUDE=","")
            VSPaths.append(listIndx)
    return VSPaths

def script_exe(LDRAToolsuitePath, vvpath, sourceFilesDir, sourceFilesCommonDir, TestbedINIFileLoc, sysearchFileLoc, swCriticality, TkObject_ref, statusBarText):

    global statusBar
    
    #Set the curret directory
    os.chdir('.')    

    statusBar = statusBarText
    batchFile = os.getcwd()+"\\"+swCriticality
    
    ################# 1. Read directories names from user given path ####################### 
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
    

    ################# 2. Read Microsoft Visual studio TESTBED.ini file #######################
    
    patternVSName = re.compile("\[.*Microsoft Visual(.*)Build Environment.*\]")    
    fileNameMatchLineNumer = 0
    exitLoop = False
    vsPaths = ''
            
    for i, line in enumerate(open(TestbedINIFileLoc)):
        for match in re.finditer(patternVSName, line):
            fileNameMatchLineNumer = i
        
    line = open(TestbedINIFileLoc, "r").readlines()[fileNameMatchLineNumer]        
    substr = re.findall(r'INCLUDE=',line)  
    while ((not exitLoop) and (fileNameMatchLineNumer > 0)):         
        line_read = open(TestbedINIFileLoc, "r").readlines()[fileNameMatchLineNumer+1]      
        if "INCLUDE=" in line_read:
            exitLoop = True # Required line found. So stop reading furthur lines from text file.
            vsPaths = getVSPaths(line_read)
            
        fileNameMatchLineNumer = fileNameMatchLineNumer+1        

    if len(vsPaths) == 0:
        statusBar.set("Error!!")    
        messagebox.showerror('Error','Microsoft Visual studio paths are not present at #INCLUDE section in Testbed.ini!')
        TkObject_ref.destroy()
        sys.exit()            
    
    #This is the additional files path where modified code files are placed
    additionFilesDir = []
    additionFilesDir.append(vvpath)
    listOfDir = vsPaths+additionFilesDir + SourceDirectoriesInSelectedPath + CommonDirectoriesInSelectedPath
    
    #Write directories to file
    
    fPtr = open(os.getcwd()+"/DirInSelectedPath.txt",'w')
    
    statusBar.set("Listed directories are writing into text file \"DirInSelectedPath.txt\"...")
    
    #Add these source code directories to Environment variables
    allDir = ';'.join(listOfDir)
    allDir = allDir.replace('/', '\\')
    allDir = allDir+';'
    fPtr.write(allDir)
    fPtr.close()
    
    ################# 3. Configure source file directories in selected sysearch.dat file #######################
    
    #sourceFileDirNewline: This varibale will have source files directories to be included
    sourceFileDir = SourceDirectoriesInSelectedPath + CommonDirectoriesInSelectedPath
    sourceFileDirNewline = '\n'.join(sourceFileDir)
    sourceFileDirNewline = sourceFileDirNewline.replace('/', '\\')  
    sourceFileDirNewline = "  1 " + sourceFileDirNewline
    sourceFileDirNewline = sourceFileDirNewline.replace("\n","\n  1 ")
    sourceFileDirNewline = sourceFileDirNewline+"\n"  

    #Get the position where source files directories needs to be inserted
    patternStringName = re.compile("Type 1   -")    
    stringMatchLineNumber = 0

    for i, line in enumerate(open(sysearchFileLoc)):
        for match in re.finditer(patternStringName, line):
            stringMatchLineNumber = i
    stringMatchLineNumber = stringMatchLineNumber+14 # This is the position where source directory paths needs to be inserted


    #Insert the data into file
    fPtr_sysearch = open(sysearchFileLoc, "r")
    contents = fPtr_sysearch.readlines()
    fPtr_sysearch.close()

    contents.insert(stringMatchLineNumber, sourceFileDirNewline)

    fPtr_sysearchRedo = open(sysearchFileLoc, "w")
    contents = "".join(contents)
    fPtr_sysearchRedo.write(contents)
    fPtr_sysearchRedo.close()
    
    ################# 4. Execute the batch file ####################### 
    
    #Check if batch file present in given location
    if not path.exists(batchFile):           
        messagebox.showerror('Error','Please make sure vital and non_vital batch files are present in application folder!')
        TkObject_ref.destroy()
        sys.exit()            
        
    statusBar.set("Batch file execution in progress, please wait...")
    
    TestbedINIFileLocDir = TestbedINIFileLoc.split("\\")
    TestbedINIFileLocDir = '\\'.join(TestbedINIFileLocDir[:-1])

    p = subprocess.Popen([batchFile, TestbedINIFileLocDir, LDRAToolsuitePath, vvpath, allDir], stdout = subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    stdout, stderr = p.communicate()
    
    #This makes the wait possible
    p_status = p.wait()

    print("\n Number of Errors seen during batch file execution: "+str(stderr))

    if(len(str(stderr))) > 0:
        print("\n\n ****** ERRORs seen white executing batch *****\n\n"+str(stdout))

    #time.sleep(10)

    statusBar.set("DONE!!")	
    messagebox.showinfo('DONE!!',"Project configuration is complete!")
    TkObject_ref.destroy()
    sys.exit()
