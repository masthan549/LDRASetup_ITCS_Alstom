from tkinter import Label, Button, Entry, Radiobutton 
import tkinter as tk
from tkinter import messagebox, filedialog, StringVar, SUNKEN, W, X, BOTTOM
from os import path
import threading, sys
import os
from tkinter.filedialog import askopenfilename
import LDRAProjectSetup

class GUI_COntroller:
    '''
	   This class initialize the required controls for TkInter GUI
	'''
    def __init__(self,TkObject):

        #Load company image
        Imageloc=tk.PhotoImage(file='../Images/alstom_logo.gif')		
        label3=Label(image=Imageloc,)
        label3.image = Imageloc		
        label3.place(x=200,y=20)

        global TkObject_ref, entryText_LDRAToolPath, entryText_vvPath, entryText_SourceFilePath, entryText_commonSourceFilePath, entryText_sysearchFilePath, entryText_TestbedINI, AnalyseDirRunBatchButton, swLevelRadioButton

        #1. select LDRA Tool suite directory
        TkObject_ref = TkObject
        LDRAToolsuitePath=Button(TkObject_ref,activebackground='green',borderwidth=3, anchor="w", text='1. Select LDRA Tool suite path:',width=30, command=lambda:GUI_COntroller.selectResDirectory("LDRAPath"), cursor="hand2")
        LDRAToolsuitePath.place(x=30,y=120)
        LDRAToolsuitePath.config(font=('helvetica',10,'bold'))	

        #1. This is text box where LDRA tool suite directory will be shown to user
        entryText_LDRAToolPath = tk.StringVar()		
        Entry_LDRAToolSuitePath= Entry(TkObject_ref, width=78, textvariable=entryText_LDRAToolPath, bd=1)
        Entry_LDRAToolSuitePath.place(x=290,y=124)					
        Entry_LDRAToolSuitePath.config(font=('helvetica',10), state="readonly")	

        #2. select VV directory
        vvPath=Button(TkObject_ref,activebackground='green',borderwidth=3, anchor="w", text='2. Select VV path:',width=30, command=lambda:GUI_COntroller.selectResDirectory("VVPath"), cursor="hand2")
        vvPath.place(x=30,y=180)
        vvPath.config(font=('helvetica',10,'bold'))	

        #2. This is text box where VV directory will be shown to user
        entryText_vvPath = tk.StringVar()		
        Entry_vvPath= Entry(TkObject_ref, width=78, textvariable=entryText_vvPath, bd=1)
        Entry_vvPath.place(x=290,y=184)					
        Entry_vvPath.config(font=('helvetica',10), state="readonly")	

        #3. select Source file directory
        SourceFilePath=Button(TkObject_ref,activebackground='green',borderwidth=3, anchor="w", text='3. Select Source files path:',width=30, command=lambda:GUI_COntroller.selectResDirectory("SourceFilesPath"), cursor="hand2")
        SourceFilePath.place(x=30,y=240)
        SourceFilePath.config(font=('helvetica',10,'bold'))	

        #3. This is text box where source file directory will be shown to user
        entryText_SourceFilePath = tk.StringVar()		
        Entry_SourceFilePath= Entry(TkObject_ref, width=78, textvariable=entryText_SourceFilePath, bd=1)
        Entry_SourceFilePath.place(x=290,y=244)					
        Entry_SourceFilePath.config(font=('helvetica',10), state="readonly")

        #4. select common Source file directory
        CommonSourceFilePath=Button(TkObject_ref,activebackground='green',borderwidth=3, anchor="w", text='4. Select common Source files path:',width=30, command=lambda:GUI_COntroller.selectResDirectory("CommonSourceFilesPath"), cursor="hand2")
        CommonSourceFilePath.place(x=30,y=300)
        CommonSourceFilePath.config(font=('helvetica',10,'bold'))	

        #4. This is text box where source file directory will be shown to user
        entryText_commonSourceFilePath = tk.StringVar()		
        Entry_CommonSourceFilePath= Entry(TkObject_ref, width=78, textvariable=entryText_commonSourceFilePath, bd=1)
        Entry_CommonSourceFilePath.place(x=290,y=304)			
        Entry_CommonSourceFilePath.config(font=('helvetica',10), state="readonly")	

        #5. select sysearch file
        sysearchFilePath=Button(TkObject_ref,activebackground='green',borderwidth=3, anchor="w", text='5. Select a sysearch file:',width=30, command=lambda:GUI_COntroller.selectResDirectory("SysearchFile"), cursor="hand2")
        sysearchFilePath.place(x=30,y=360)
        sysearchFilePath.config(font=('helvetica',10,'bold'))    

        #5. This is text box where source file directory will be shown to user
        entryText_sysearchFilePath = tk.StringVar()        
        Entry_sysearchFilePath= Entry(TkObject_ref, width=78, textvariable=entryText_sysearchFilePath, bd=1)
        Entry_sysearchFilePath.place(x=290,y=364)            
        Entry_sysearchFilePath.config(font=('helvetica',10), state="readonly")    
        
        
        # Select creticality of the software
        swCriticalityLabel = Label(TkObject_ref, text="Select the criticality of the software: ", background = "#b7bbc7")
        swCriticalityLabel.place(x=30,y=420)
        swCriticalityLabel.config(font=('helvetica',10,'bold'))          
 
        #Set the Radio button to select software complexity level
        swLevelRadioButton = tk.IntVar()        
        swCriticalityLevel_VitalRadioButton = Radiobutton(TkObject_ref, text="Vital software",background = "#b7bbc7", variable=swLevelRadioButton, value=1)
        swCriticalityLevel_VitalRadioButton.place(x=290, y=424)
        swCriticalityLevel_VitalRadioButton.config(font=('helvetica',10,'bold')) 
 
        swCriticalityLevel_NonVitalRadioButton = Radiobutton(TkObject_ref, text="Non-Vital software",background = "#b7bbc7", variable=swLevelRadioButton, value=2)
        swCriticalityLevel_NonVitalRadioButton.place(x=430, y=424)
        swCriticalityLevel_NonVitalRadioButton.config(font=('helvetica',10,'bold'))  
 
        #6. select testbed.ini file directory
        TestbedINI=Button(TkObject_ref,activebackground='green',borderwidth=3, anchor="w", text='6. Select TESTBED.ini file:',width=30, command=lambda:GUI_COntroller.selectResDirectory("TESTBEDINI"), cursor="hand2")
        TestbedINI.place(x=30,y=480)
        TestbedINI.config(font=('helvetica',10,'bold'))	

        #6. This is text box where spare directory will be shown to user
        entryText_TestbedINI = tk.StringVar()		
        Entry_TestbedINI= Entry(TkObject_ref, width=78, textvariable=entryText_TestbedINI, bd=1)
        Entry_TestbedINI.place(x=290,y=484)			
        Entry_TestbedINI.config(font=('helvetica',10), state="readonly")	


        #Exit Window		
        closeButton=Button(TkObject_ref,activebackground='green',borderwidth=4, text='Close Window', command=GUI_COntroller.exitWindow)
        closeButton.place(x=570,y=580)	
        closeButton.config(font=('helvetica',11,'bold'))	


        #select sequence files directory
        AnalyseDirRunBatchButton=Button(TkObject_ref,activebackground='green',borderwidth=4, text='Configure LDRA Project',width=25, command=GUI_COntroller.RunTest)
        AnalyseDirRunBatchButton.place(x=200,y=580)
        AnalyseDirRunBatchButton.config(font=('helvetica',11,'bold'))		           
            
        #read the data from saved preference if it is saved already
        GUI_COntroller.readDataFromSavedPref()  

    def writeDataIntoSavedPref():

        dictSavedPref = {}
        fPtr = open("../Images/savedPref.txt","w")
        dictSavedPref["LDRAToolsuite"] = entryText_LDRAToolPath.get()
        dictSavedPref["VVPath"] = entryText_vvPath.get()
        dictSavedPref["SourcePath"] = entryText_SourceFilePath.get()
        dictSavedPref["CommonFilesPath"] = entryText_commonSourceFilePath.get()
        dictSavedPref["TeststandINI"] = entryText_TestbedINI.get()
        dictSavedPref["Sysearch"] = entryText_sysearchFilePath.get()                                        
        fPtr.write(str(dictSavedPref))
        fPtr.close()

    def readDataFromSavedPref():
        if os.path.exists('../Images/savedPref.txt'):
            fPtr = open("../Images/savedPref.txt")
            for lineText in fPtr:
                dictInfoOfSavedPrefDir = eval(lineText)
                if 'LDRAToolsuite' in dictInfoOfSavedPrefDir.keys():                      
                    entryText_LDRAToolPath.set(dictInfoOfSavedPrefDir['LDRAToolsuite'])   
                if 'VVPath' in dictInfoOfSavedPrefDir.keys():                      
                    entryText_vvPath.set(dictInfoOfSavedPrefDir['VVPath']) 
                if 'SourcePath' in dictInfoOfSavedPrefDir.keys():                      
                    entryText_SourceFilePath.set(dictInfoOfSavedPrefDir['SourcePath']) 
                if 'CommonFilesPath' in dictInfoOfSavedPrefDir.keys():                      
                    entryText_commonSourceFilePath.set(dictInfoOfSavedPrefDir['CommonFilesPath']) 
                if 'TeststandINI' in dictInfoOfSavedPrefDir.keys():                      
                    entryText_TestbedINI.set(dictInfoOfSavedPrefDir['TeststandINI']) 
                if 'Sysearch' in dictInfoOfSavedPrefDir.keys():                      
                    entryText_sysearchFilePath.set(dictInfoOfSavedPrefDir['Sysearch'])                                                                                                                               

    def selectResDirectory(dirSelectionType): 
        global entryText_LDRAToolPath, entryText_sysearchFilePath, entryText_vvPath, entryText_SourceFilePath, entryText_commonSourceFilePath, entryText_TestbedINI
        currdir = os.getcwd()

        if dirSelectionType == "LDRAPath":
            selectedDir_res = filedialog.askdirectory(initialdir=currdir, title='Please select a LDRA tool suite directory')
            
            if len(selectedDir_res)> 0:
                if not path.isdir(selectedDir_res):
                    entryText_LDRAToolPath.set("")			
                    messagebox.showerror('Error','Please select a valid directory!')
                else:
                    entryText_LDRAToolPath.set(str(selectedDir_res))
        elif dirSelectionType == "VVPath":
                selectedDir_res = filedialog.askdirectory(initialdir=currdir, title='Please select VV directory')
                
                if len(selectedDir_res)> 0:
                    if not path.isdir(selectedDir_res):
                        entryText_vvPath.set("")			
                        messagebox.showerror('Error','Please select a valid directory!')
                    else:
                        entryText_vvPath.set(str(selectedDir_res))
        elif dirSelectionType == "SourceFilesPath":
                selectedDir_res = filedialog.askdirectory(initialdir=currdir, title='Please select Source file directory')
                
                if len(selectedDir_res)> 0:
                    if not path.isdir(selectedDir_res):
                        entryText_SourceFilePath.set("")			
                        messagebox.showerror('Error','Please select a valid directory!')
                    else:
                        entryText_SourceFilePath.set(str(selectedDir_res))	
        elif dirSelectionType == "CommonSourceFilesPath":
                selectedDir_res = filedialog.askdirectory(initialdir=currdir, title='Please select common Source file directory')
                
                if len(selectedDir_res)> 0:
                    if not path.isdir(selectedDir_res):
                        entryText_commonSourceFilePath.set("")			
                        messagebox.showerror('Error','Please select a valid directory!')
                    else:
                        entryText_commonSourceFilePath.set(str(selectedDir_res))
        elif dirSelectionType == "TESTBEDINI":
                selectedFile_res = askopenfilename(initialdir=currdir, title='Please select Testbed ini file', filetypes=(("sysearch files", "*.ini"), ("all files", "*.*")))
                
                if len(selectedFile_res)> 0:
                    if not path.exists(selectedFile_res):
                        entryText_TestbedINI.set("")			
                        messagebox.showerror('Error','Please select a valid testbed.ini file!')
                    else:
                        entryText_TestbedINI.set(str(selectedFile_res))						
        elif dirSelectionType == "SysearchFile":
                selectedFile_res = askopenfilename(initialdir=currdir, title='Please select a sysearch file', filetypes=(("sysearch files", "*.dat"), ("all files", "*.*")))
                
                if len(selectedFile_res)> 0:
                    if not path.exists(selectedFile_res):
                        entryText_TestbedINI.set("")			
                        messagebox.showerror('Error','Please select a valid directory!')
                    else:
                        entryText_sysearchFilePath.set(str(selectedFile_res))	

    def exitWindow():
            TkObject_ref.destroy()

    def RunTest():

        debug = False        
        if debug is True:
            ProjectDirAnalysis.RunAnalysis()

        if len(entryText_LDRAToolPath.get()) > 0:
            if len(entryText_vvPath.get()) > 0:
                if len(entryText_SourceFilePath.get()) > 0:
                    if len(entryText_commonSourceFilePath.get()) > 0:
                        if len(entryText_sysearchFilePath.get()) > 0:
                            if (swLevelRadioButton.get() == 1) or (swLevelRadioButton.get() == 2): 
                                if (len(entryText_TestbedINI.get()) > 0): 
                                    ProjectDirAnalysis.RunAnalysis()
                                else:
                                    messagebox.showerror('Error','Please select Testbed.ini file!')                                 
                            else:
                                messagebox.showerror('Error','Please select Software criticality level!')                                
                        else:
                            messagebox.showerror('Error','Please select sysearch dat file!')
                    else:
                        messagebox.showerror('Error','Please select common directory for source files!')
                else:
                    messagebox.showerror('Error','Please select Source files path!')
            else:
                messagebox.showerror('Error','Please select V&V path!')
        else:
            messagebox.showerror('Error','Please select LDRA tool path!')    

class ProjectDirAnalysis:
    def RunAnalysis(): 

        global statusBarText
        AnalyseDirRunBatchButton.config(state="disabled")

        statusBarText = StringVar()		
        StatusLabel = Label(TkObject_ref, textvariable=statusBarText, fg="green", bd=1,relief=SUNKEN,anchor=W) 
        StatusLabel.config(font=('helvetica',11,'bold'))
        StatusLabel.pack(side=BOTTOM, fill=X)

        GUI_COntroller.writeDataIntoSavedPref();
        if swLevelRadioButton.get() == 1:
            thread = threading.Thread(target=LDRAProjectSetup.script_exe, args = (entryText_LDRAToolPath.get(), entryText_vvPath.get(), entryText_SourceFilePath.get(), entryText_commonSourceFilePath.get(), entryText_TestbedINI.get(), entryText_sysearchFilePath.get(), "Vital.bat", TkObject_ref, statusBarText))                                
        elif swLevelRadioButton.get() == 2:
            thread = threading.Thread(target=LDRAProjectSetup.script_exe, args = (entryText_LDRAToolPath.get(), entryText_vvPath.get(), entryText_SourceFilePath.get(), entryText_commonSourceFilePath.get(), entryText_TestbedINI.get(), entryText_sysearchFilePath.get(), "Non_Vital.bat", TkObject_ref, statusBarText))
            
        thread.start()

if __name__ == '__main__':	

    root = tk.Tk()
       
    #Change the background window color
    root.configure(background='#b7bbc7')     
       
    #Set window parameters
    root.geometry('850x680')
    root.title('LDRA Project setup')
       
    #Removes the maximizing option
    root.resizable(0,0)
       
    ObjController = GUI_COntroller(root)
       
    #keep the main window is running
    root.mainloop()
    sys.exit()
