from tkinter import Label, Button, Entry
import tkinter as tk
from tkinter import messagebox, filedialog, PhotoImage, StringVar, SUNKEN, W, X, BOTTOM
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

        global TkObject_ref, entryText_LDRAToolPath, entryText_vvPath, entryText_SourceFilePath, entryText_commonSourceFilePath, entryText_sparePath, AnalyseDirRunBatchButton
		
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


        #5. select spare directory
        SparePath=Button(TkObject_ref,activebackground='green',borderwidth=3, anchor="w", text='5. Select spare path (optional):',width=30, command=lambda:GUI_COntroller.selectResDirectory("SparePath"), cursor="hand2")
        SparePath.place(x=30,y=360)
        SparePath.config(font=('helvetica',10,'bold'))	

        #5. This is text box where spare directory will be shown to user
        entryText_sparePath = tk.StringVar()		
        Entry_sparePath= Entry(TkObject_ref, width=78, textvariable=entryText_sparePath, bd=1)
        Entry_sparePath.place(x=290,y=364)			
        Entry_sparePath.config(font=('helvetica',10), state="readonly")	


        #Exit Window		
        closeButton=Button(TkObject_ref,activebackground='green',borderwidth=4, text='Close Window', command=GUI_COntroller.exitWindow)
        closeButton.place(x=570,y=460)	
        closeButton.config(font=('helvetica',11,'bold'))	

				
        #select sequence files directory
        AnalyseDirRunBatchButton=Button(TkObject_ref,activebackground='green',borderwidth=4, text='Configure LDRA Project',width=25, command=GUI_COntroller.RunTest)
        AnalyseDirRunBatchButton.place(x=200,y=460)
        AnalyseDirRunBatchButton.config(font=('helvetica',11,'bold'))			

    def selectResDirectory(dirSelectionType): 
        global entryText_LDRAToolPath, entryText_vvPath, entryText_SourceFilePath, entryText_commonSourceFilePath, entryText_sparePath
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
        elif dirSelectionType == "SparePath":
                selectedDir_res = filedialog.askdirectory(initialdir=currdir, title='Please select Spare directory')
                
                if len(selectedDir_res)> 0:
                    if not path.isdir(selectedDir_res):
                        entryText_sparePath.set("")			
                        messagebox.showerror('Error','Please select a valid directory!')
                    else:
                        entryText_sparePath.set(str(selectedDir_res))						

		
    def exitWindow():
            TkObject_ref.destroy()
			

    def RunTest():

        if len(entryText_LDRAToolPath.get()) > 0:
            if len(entryText_vvPath.get()) > 0:
                if len(entryText_SourceFilePath.get()) > 0:
                    if len(entryText_commonSourceFilePath.get()) > 0:
                        ProjectDirAnalysis.RunAnalysis()
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
		
        thread = threading.Thread(target=LDRAProjectSetup.script_exe, args = (entryText_LDRAToolPath.get(), entryText_vvPath.get(), entryText_SourceFilePath.get(), entryText_commonSourceFilePath.get(), entryText_sparePath.get(), TkObject_ref, statusBarText))
        
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
