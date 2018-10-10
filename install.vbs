currentpath = createobject("Scripting.FileSystemObject").GetFolder(".").Path
hydra = currentpath + "\hydra_api"
nmap = currentpath + "\nmap_api"
'MsgBox(currentpath)
'MsgBox(hydra)
'MsgBox(nmap)

Dim wsh
Set wsh = WScript.CreateObject("WScript.Shell")

wsh.Environment("system").Item("Path")= wsh.Environment("system").Item("Path") + ";"+hydra+ ";"+nmap
