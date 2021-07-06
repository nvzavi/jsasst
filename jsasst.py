#!/usr/bin/env python3
#
# This is a little tool to automate some of the manual tasks of reviewing obfuscated JavaScript files. It is intended to assist by making the script easier to read.
# Still testing and removing a few bugs. Kindly note that I am not responsible for any damages to code (if any).
# Use at your own risk.  
# Thanks.
#
# BY @nvzavi
#
# Date:  2021/07/04
#
# TODO:  Clean up/streamline code
# TODO:  Complete testing

import argparse
import time
import re
from pathlib import Path

Descr = "This is a little tool to automate some of the manual tasks of reviewing obfuscated JavaScript files. It is intended to assist by making the script easier to read.  Still testing and removing a few bugs. Kindly note that I am not responsible for any damages to code (if any). Use at your own risk.  Thanks."

parser = argparse.ArgumentParser(description = Descr)
parser.add_argument("-f", "--File", help = "This is the file from which to read the contents", required=True)
parser.add_argument("-s", "--QuickSummary", action='store_true', help = "Displays a quick summary of misleading tuples / suspicious elements / URLs and files names")
parser.add_argument("-d", "--Dump", help = "Used with -v (ResolveVariableNames) to dump results to a new file")
parser.add_argument("-t", "--IdentifyTupleStatments", action='store_true', help = "Identify misleading tuple structures")
parser.add_argument("-v", "--ResolveVariableNames", help = "Update variable name to enable easier recognition.  Add variable name after -v e.g. -v Arg")
parser.add_argument("-e", "--IdentifySuspiciousElements", action='store_true', help = "Identify suspicious elements")
parser.add_argument("-u", "--IdentifyURLs_Files", action='store_true', help = "Identifies URLs and files within the script")

Received_Args = parser.parse_args()

def Display_Tuples():
    try:
        print("----------------------------------------------------------------------")
        print("---            Detected misleading tuple structures                ---")
        print("----------------------------------------------------------------------")
        print(" Starting Position\t | Code Snippet                                   ")
        print("----------------------------------------------------------------------")
        FileTR = open(Received_Args.File, "r")
        DataTR = FileTR.read()
        FoundSPOS=0
        FoundEPOS=0
        FoundSPOS=DataTR.find(chr(40))   
        FirstLOC=FoundSPOS
        DiDDCounter=0
        while (FoundSPOS !=-1):
            FoundEPOS=DataTR.find(chr(41),FoundSPOS+1) 
            if (FoundEPOS==-1):
                break
            if (DataTR.find(chr(44),FoundSPOS,FoundEPOS)!=-1):        
                CountL=0
                LoopPOS=FirstLOC-1
                while (LoopPOS >= 0 and CountL < 4): 
                    if (DataTR[LoopPOS]==chr(32)): 
                        CountL+=1
                    elif (DataTR[LoopPOS]==chr(61)): 
                        ExtractSPOS=0
                        if (FoundSPOS>=6):
                            ExtractSPOS=FoundSPOS-6
                        LocatedTS=DataTR[ExtractSPOS:ExtractSPOS + 50]
                        LocatedTS=LocatedTS.replace("\n",chr(32))
                        print(chr(32) + chr(32) + str(FirstLOC) + "\t\t\t | " + str(LocatedTS.strip()))
                        DiDDCounter+=1
                        break
                    else:
                        break
                    LoopPOS-=1               
            FoundSPOS=DataTR.find(chr(40),FoundEPOS+1) 
            FirstLOC=FoundSPOS
        FileTR.close()     
        if (DiDDCounter==0):
           print(chr(32) + chr(32) + "No misleading tuple structures were found...\n")
    except Exception as e:
        print(e)

def DisplaySuspiciousElements():
    try:
        print("----------------------------------------------------------------------")
        print("---    Detected JavaScript elements that may require attention     ---")
        print("----------------------------------------------------------------------")
        SeFile = open("//usr//local//bin//se_list.txt", "r") #Change this path if se_list.txt is moved to a different location
        DiDDCounter=0
        for SeLine in SeFile:
            if (SeLine[0]!=chr(42)): 
                FoundEPOS=SeLine.find(chr(58)) 
                WToS=SeLine[0:FoundEPOS]
                FileTR = open(Received_Args.File, "r")
                DataTR = FileTR.read() 
                LDataTR = DataTR.lower()
                FoundWToSSPOS=LDataTR.find(str(WToS.lower()))
                FoundWToSEPOS= FoundWToSSPOS + len(str(WToS)) - 1
                while (FoundWToSSPOS!=-1):
                    SeSnippet=DataTR[FoundWToSSPOS:FoundWToSEPOS+20]
                    SeSnippet=SeSnippet.replace("\n",chr(32))
                    print(" Element\t:  " + SeLine[0:FoundEPOS]) 
                    print(" Description\t:  " + SeLine[FoundEPOS+1:].strip())
                    print(" Code Snippet\t:  " + str(SeSnippet))
                    print("----------------------------------------------------------------------")
                    FoundWToSSPOS=LDataTR.find(str(WToS.lower()),FoundWToSEPOS+1)
                    FoundWToSEPOS= FoundWToSSPOS + len(str(WToS)) - 1
                    DiDDCounter+=1
                FileTR.close()
        SeFile.close()
        if (DiDDCounter==0):
               print(chr(32) + chr(32) + "Strange...No elements were found...\n")
    except Exception as e:
        print(e)

def Resolve_FreindlyVar():
    try:
        FileTR = open(Received_Args.File, "r")
        DataTR = FileTR.read()
        FoundPOS=DataTR.find(chr(61)) - 1 
        ArrIndex=0
        VarArray=[]
        while (FoundPOS > -1): 
            CountL = 0
            Var_Located = False
            LastStrIndex = 0
            LoopPOS = FoundPOS
            while (LoopPOS >= 0 and CountL < 4): 
                if DataTR[LoopPOS]==chr(32): 
                    CountL+=1
                else:
                    Var_Located = True
                    LastStrIndex = LoopPOS
                    break
                LoopPOS-=1 
            if  Var_Located == True:
                CheckChr = IsUnwantedChr(DataTR[LastStrIndex]) 
                BeginStrIndex = LastStrIndex 
                while (CheckChr != True and BeginStrIndex != -1):  
                    CheckChr = IsUnwantedChr(DataTR[BeginStrIndex]) 
                    BeginStrIndex-=1
                if (ord(DataTR[BeginStrIndex+1])!=43 and ord(DataTR[BeginStrIndex+1])!=47):
                    if (ord(DataTR[BeginStrIndex+1])!=46):
                        if (BeginStrIndex == -1): 
                            TempVar=DataTR[BeginStrIndex+1:LastStrIndex+1] 
                        else: 
                            TempVar=DataTR[BeginStrIndex+2:LastStrIndex+1] 
                        if (len(TempVar)>0): 
                            if TempVar.isnumeric()==False:
                                if TempVar.strip() not in VarArray:
                                    VarArray.insert(ArrIndex,TempVar.strip())
                                    ArrIndex+=1            
            FoundPOS=DataTR.find(chr(61), FoundPOS + 3) - 1
        TempNameCounter=1
        for VarT in VarArray:
            DataTR = re.sub(r"\b%s\b" % str(VarT), Received_Args.ResolveVariableNames + str(TempNameCounter), DataTR)
            TempNameCounter+=1
        print(str(TempNameCounter-1) + " variables were updated...")
        FileTR.close()  
        FileTR = open(Received_Args.Dump, "w")
        FileTR.write(DataTR)
        FileTR.close() 
        print("Saved results to " + str(Received_Args.Dump))
    except Exception as e:
        print(e)

def IsUnwantedChr(ChrS):
    ValidChrArr=[48,49,50,51,52,53,54,55,56,57,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80, + \
        81,82,83,84,85,86,87,88,89,90,95,97,98,99,100,101,102,103,104,105,106,107,108,109,110, + \
        111,112,113,114,115,116,117,118,119,120,121,122]

    if ord(ChrS) not in ValidChrArr:
        return True
    else:
        return False

def ID_Urls_Files():
    print("----------------------------------------------------------------------")
    print("---                  Detected URLs and Files                       ---")
    print("----------------------------------------------------------------------")
    DiDDCounter=0
    FileTR = open(Received_Args.File, "r")
    DataTR = FileTR.read()
    urls = re.findall('(?:(?:(?:ftp|http)[s]*:\/\/|www\.)[^\.]+\.[^ \n]+)', DataTR)
    for item in urls:
        print(" URL:  " + item)
    ArrIndexE=0
    VarArrayE=[]
    for Files in range(1,5):
        FilesWI = re.findall('\.[A-Za-z0-9]{%s}\s' % str(Files), DataTR)
        for FWI in FilesWI:
            if str(FWI).strip() not in VarArrayE:
                VarArrayE.insert(ArrIndexE,str(FWI).strip())
                ArrIndexE+=1
        FilesAE = re.findall('\.[A-Za-z0-9]{%s}$' % str(Files), DataTR)
        for FAE in FilesAE:
            if str(FAE).strip() not in VarArrayE:
                VarArrayE.insert(ArrIndexE,str(FAE).strip())
                ArrIndexE+=1
        FilesWL = re.findall('\.[A-Za-z0-9]{%s}[);"\',]' % str(Files), DataTR)
        for FWL in FilesWL:
            if str(FWL).strip() not in VarArrayE:
                VarArrayE.insert(ArrIndexE,str(FWL).strip())
                ArrIndexE+=1
    for AItem in VarArrayE:
        DFilePOS = DataTR.rfind(AItem) - 1
        BeginChar=DFilePOS
        CheckChar=IsUnwantedChr(DataTR[DFilePOS]) 
        while (BeginChar != -1 and CheckChar != True): 
           BeginChar-=1 
           CheckChar=IsUnwantedChr(DataTR[BeginChar])
        if (DataTR[BeginChar]!=chr(46) and DataTR[BeginChar]!=chr(47)):
            print(" File:  " + DataTR[BeginChar:DFilePOS+1].strip() + AItem)
        DiDDCounter+=1
    FileTR.close()
    if (DiDDCounter==0):
           print(chr(32) + chr(32) + "No URLs or files were found...")

if Received_Args.ResolveVariableNames:
    SProcess = time.time()
    print("*****************************************************************")
    print("***                  JavaScript Assist v1.0                   ***")
    print("*****************************************************************")
    print("Running -v/--ResolveVariableNames...")
    Resolve_FreindlyVar() 
    print("Completed in " + str(round(time.time() - SProcess,3)) + " seconds ...")

if Received_Args.IdentifyTupleStatments:
    SProcess = time.time()
    print("*********************************************************************")
    print("***                     JavaScript Assist v1.0                    ***")
    print("*********************************************************************")
    print(" Summary of: " + Received_Args.File + "\n")
    print(" NOTE:  The data displayed below includes any detected misleading tuple\n"\
       " statements that can be used for nefarious activites. Further\n investigation"\
      " is required in order to confirm the true nature of the\n contents.\n")
    Display_Tuples()
    print("Completed in " + str(round(time.time() - SProcess,3)) + " seconds ...")

if Received_Args.IdentifySuspiciousElements:
    SProcess = time.time()
    print("*********************************************************************")
    print("***                      JavaScript Assist v1.0                   ***")
    print("*********************************************************************")
    print(" Summary of: " + Received_Args.File + "\n")
    print(" NOTE:  The data displayed below includes any detected elements that\n"\
       " can be used for nefarious activites. Further investigation is\n required"\
      " in order to confirm the true nature of the contents.\n")
    DisplaySuspiciousElements()
    print("Completed in " + str(round(time.time() - SProcess,3)) + " seconds ...")

if Received_Args.QuickSummary:
    SProcess = time.time()
    print("*********************************************************************")
    print("***                      JavaScript Assist v1.0                   ***")
    print("*********************************************************************")
    print(" Summary of: " + Received_Args.File + "\n")
    print(" NOTE:  The data displayed below includes any detected misleading tuple\n"\
       " statements, as well as any detected elements that can be used for\n nefarious "\
       "activites. Further investigation is required in order to\n confirm the true"\
      " nature of the contents.\n")
    Display_Tuples()
    print("\n\n")
    DisplaySuspiciousElements()
    print("\n\n")
    ID_Urls_Files()
    print("Completed in " + str(round(time.time() - SProcess,3)) + " seconds ...")

if Received_Args.IdentifyURLs_Files:
    SProcess = time.time()
    print("*********************************************************************")
    print("***                      JavaScript Assist v1.0                   ***")
    print("*********************************************************************")
    print(" Summary of: " + Received_Args.File + "\n")
    print(" NOTE:  The data displayed below includes any detected URLs\n"\
       " and files.  Further investigation is required in order to\n confirm the true"\
      " nature of the contents.\n")
    ID_Urls_Files()
    print("\nCompleted in " + str(round(time.time() - SProcess,3)) + " seconds ...")
