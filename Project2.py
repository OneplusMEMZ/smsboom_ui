#coding=utf-8
#import libs 
import sys
import Project2_cmd
import Project2_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Project2:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        Fun.Register(uiName,'root',root)
        style = Project2_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            root.overrideredirect(True)
            Fun.WindowDraggable(root,0,'#00ffff')
            root.resizable(False,False)
            root.wm_attributes("-transparentcolor","#00ffff")
            Fun.CenterDlg(uiName,root,305,319)
            root['background'] = '#efefef'
            root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(fill=BOTH,expand=True)
        Form_1.configure(bg = "#00ffff")
        Fun.SetRootRoundRectangle(Form_1,0,0,305,319,radius=50,fill='#efefef',outline='#00ffff',width=0)
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Label_3 = tkinter.Label(Form_1,text="短信轰炸")
        Fun.Register(uiName,'Label_3',Label_3)
        Fun.SetControlPlace(uiName,'Label_3',82,21,118,49)
        Label_3.configure(relief = "flat")
        Label_3_Ft=tkinter.font.Font(family='微软雅黑', size=16,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_3.configure(font = Label_3_Ft)
        CheckButton_4_Variable = Fun.AddTKVariable(uiName,'CheckButton_4')
        CheckButton_4_Variable.set(False)
        CheckButton_4 = tkinter.Checkbutton(Form_1,variable=CheckButton_4_Variable,text="异步并发",anchor=tkinter.W)
        Fun.Register(uiName,'CheckButton_4',CheckButton_4)
        Fun.SetControlPlace(uiName,'CheckButton_4',45,75,70,20)
        CheckButton_4.configure(command=lambda:Project2_cmd.CheckButton_4_onCommand(uiName,"CheckButton_4"))
        Fun.AddUserData(uiName,'CheckButton_4','yibu','string','False',0)
        CheckButton_5_Variable = Fun.AddTKVariable(uiName,'CheckButton_5')
        CheckButton_5_Variable.set(False)
        CheckButton_5 = tkinter.Checkbutton(Form_1,variable=CheckButton_5_Variable,text="使用代理",anchor=tkinter.W)
        Fun.Register(uiName,'CheckButton_5',CheckButton_5)
        Fun.SetControlPlace(uiName,'CheckButton_5',120,76,71,20)
        CheckButton_5.configure(command=lambda:Project2_cmd.CheckButton_5_onCommand(uiName,"CheckButton_5"))
        Fun.AddUserData(uiName,'CheckButton_5','daili','string','False',0)
        Label_8 = tkinter.Label(Form_1,text="手机号")
        Fun.Register(uiName,'Label_8',Label_8)
        Fun.SetControlPlace(uiName,'Label_8',34,107,39,20)
        Label_8.configure(relief = "flat")
        Entry_9_Variable = Fun.AddTKVariable(uiName,'Entry_9','')
        Entry_9 = tkinter.Entry(Form_1,textvariable=Entry_9_Variable)
        Fun.Register(uiName,'Entry_9',Entry_9)
        Fun.SetControlPlace(uiName,'Entry_9',82,107,155,20)
        Entry_9.configure(relief = "sunken")
        Button_10 = tkinter.Button(Form_1,text="手动更新接口")
        Fun.Register(uiName,'Button_10',Button_10)
        Fun.SetControlPlace(uiName,'Button_10',37,160,100,28)
        Button_10.configure(command=lambda:Project2_cmd.Button_10_onCommand(uiName,"Button_10"))
        Button_11 = tkinter.Button(Form_1,text="开始轰炸")
        Fun.Register(uiName,'Button_11',Button_11)
        Fun.SetControlPlace(uiName,'Button_11',150,160,100,28)
        Button_11.configure(command=lambda:Project2_cmd.Button_11_onCommand(uiName,"Button_11"))
        Button_12 = tkinter.Button(Form_1,text="退出")
        Fun.Register(uiName,'Button_12',Button_12)
        Fun.SetControlPlace(uiName,'Button_12',91,212,100,28)
        Button_12.configure(command=lambda:Project2_cmd.Button_12_onCommand(uiName,"Button_12"))
        Label_14 = tkinter.Label(Form_1,text="等待时间")
        Fun.Register(uiName,'Label_14',Label_14)
        Fun.SetControlPlace(uiName,'Label_14',74,133,51,20)
        Label_14.configure(relief = "flat")
        ComboBox_15_Variable = Fun.AddTKVariable(uiName,'ComboBox_15')
        ComboBox_15 = tkinter.ttk.Combobox(Form_1,textvariable=ComboBox_15_Variable, state="readonly")
        Fun.Register(uiName,'ComboBox_15',ComboBox_15)
        Fun.SetControlPlace(uiName,'ComboBox_15',125,133,100,20)
        ComboBox_15["values"]=['10s','30s','60s','120s']
        ComboBox_15.current(0)
        Fun.AddUserData(uiName,'ComboBox_15','dengdaishijian','int',10,0)
        ComboBox_15.bind("<<ComboboxSelected>>",Fun.EventFunction_Adaptor(Project2_cmd.ComboBox_15_onSelect,uiName=uiName,widgetName="ComboBox_15"))
        CheckButton_16_Variable = Fun.AddTKVariable(uiName,'CheckButton_16')
        CheckButton_16_Variable.set(False)
        CheckButton_16 = tkinter.Checkbutton(Form_1,variable=CheckButton_16_Variable,text="循环",anchor=tkinter.W)
        Fun.Register(uiName,'CheckButton_16',CheckButton_16)
        Fun.SetControlPlace(uiName,'CheckButton_16',197,76,48,19)
        CheckButton_16.configure(command=lambda:Project2_cmd.CheckButton_16_onCommand(uiName,"CheckButton_16"))
        Fun.AddUserData(uiName,'CheckButton_16','xunhuan','string','False',0)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)



        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True:
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
    def Exit(self):
        if self.isTKroot == True:
            self.root.destroy()

    def Configure(self,event):
        if self.root == event.widget:
            pass
#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Project2(root)
    root.mainloop()
