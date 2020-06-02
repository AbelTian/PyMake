on error resume next 
Set objArgs=WScript.Arguments 
For I=0 to objArgs.Count-1 
strArgs=strArgs & " " & objArgs(I)
Next
strArgs = Trim(strArgs)

currentpath = createobject("Scripting.FileSystemObject").GetFile(Wscript.ScriptFullName).ParentFolder.Path
currentCommand = "py " & currentpath & "\pyedit.py"
rem msgbox "strArgs:" & strArgs
rem msgbox "strArgs:" & currentCommand
if strArgs<>"" then HideRun(strArgs) 

function HideRun(h) 
set oWSl=WScript.CreateObject("WScript.Shell") 
rem msgbox "strArgs:" & h
rem msgbox "strArgs:" & strArgs
rem msgbox "strArgs:" & currentCommand
rtn=oWSl.run(h,0,false) 
end function 