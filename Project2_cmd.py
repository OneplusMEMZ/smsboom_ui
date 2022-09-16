#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

def CheckButton_4_onCommand(uiName,widgetName):
    yibu = Fun.GetUserData(uiName,"CheckButton_4","yibu")
    if yibu == "False":
        yibu = "True"
        Fun.SetUserData(uiName,"CheckButton_4","yibu",yibu)
    else:
        yibu = "False"
        Fun.SetUserData(uiName,"CheckButton_4","yibu",yibu)
def CheckButton_5_onCommand(uiName,widgetName):
    daili = Fun.GetUserData(uiName,"CheckButton_5","daili")
    if daili == "False":
        daili = "True"
        Fun.SetUserData(uiName,"CheckButton_5","daili",daili)
    else:
        daili = "False"
def Button_10_onCommand(uiName,widgetName):
    os.system("smsboom.exe update")
def Button_11_onCommand(uiName,widgetName):
    smsboom = open("smsboom.cmd",mode = "w")
    smsboom.write("""smsboom.exe update
smsboom.exe """)
    smsboom.close()
    smsboom_yibu = Fun.GetUserData(uiName,"CheckButton_4","yibu")
    smsboom_daili = Fun.GetUserData(uiName,"CheckButton_5","daili")
    smsboom_xunhuan = Fun.GetUserData(uiName,"CheckButton_16","xunhuan")
    smsboom_dengdai = Fun.GetUserData(uiName,"ComboBox_15","dengdaishijian")
    smsboom_phone = Fun.GetText(uiName,"Entry_9")
    smsboom_a = open("smsboom.cmd",mode = "a")
    if smsboom_yibu == "True":
        smsboom_a.write("asyncrun -p "+smsboom_phone)
        os.system("smsboom.cmd")
        smsboom_a.close()
    else:
        smsboom_a.write("run -t 64 -p "+smsboom_phone)
        if smsboom_xunhuan == "True":
            smsboom_a.write(" -f 60 -i "+str(smsboom_dengdai))
        if smsboom_daili == "True":
            smsboom_a.write(" -e")
        smsboom_a.close()
        os.system("smsboom.cmd")
def Button_12_onCommand(uiName,widgetName):
    sys.exit()
def ComboBox_15_onSelect(event,uiName,widgetName):
    dengdai = Fun.GetText(uiName,"ComboBox_15")
    if dengdai == "10s":
        dengdai = 10
    if dengdai == "30s":
        dengdai = 30
    if dengdai == "60s":
        dengdai = 60
    if dengdai == "120s":
        dengdai = 120
    Fun.SetUserData(uiName,"ComboBox_15","dengdaishijian",dengdai)
def CheckButton_16_onCommand(uiName,widgetName):
    xunhuan = Fun.GetUserData(uiName,"CheckButton_16","xunhuan")
    if xunhuan == "False":
        xunhuan = "True"
        Fun.SetUserData(uiName,"CheckButton_16","xunhuan",xunhuan)
    else:
        xunhuan = "False"

