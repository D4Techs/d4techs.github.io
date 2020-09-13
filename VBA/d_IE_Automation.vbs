'***********************************************************************
'Author: Durgesh Vishwakarma (https://github.com/D4Techs)
'***********************************************************************
Set IE = CreateObject("InternetExplorer.Application")
Set Excel = WScript.CreateObject("Excel.Application")
Set WshShell = WScript.CreateObject("WScript.Shell")
Set dMacro = Excel.workbooks.open("D:\dMarcoExcel.xlsm")

'MacroNames: DoubleClick() & RightClick() & SingleClick() in Excel file

Dim Excel, x, y
x = "740"
y = "195"

IE.Navigate "https://apps2.level3.com/vpn/index.html"
IE.Visible = True
IE.FullScreen=True

WScript.Sleep (3000)

Excel.ExecuteExcel4Macro ( "CALL(""user32"",""SetCursorPos"",""JJJ""," & x & "," & y & ")" )

dMacro.application.run("SingleClick")
WshShell.SendKeys "Welcome Durgesh"

WScript.Sleep (100)
dMacro.Close

' Remove/ Replace ' (Apostrophe) from below VBA code in Excel
'***********************************************************************
'Author: Durgesh Vishwakarma (https://github.com/D4Techs)
'******** File Name: "D:\dMarcoExcel.xlsm" to call click marcos ********
'
'Public Declare PtrSafe Function SetCursorPos Lib "user32" (ByVal x As Long, ByVal y As Long) As Long
'Public Declare PtrSafe Sub mouse_event Lib "user32" (ByVal dwFlags As Long, ByVal dx As Long, ByVal dy As Long, ByVal cButtons As Long, ByVal dwExtraInfo As Long)
'
'Public Const MOUSEEVENTF_LEFTDOWN = &H2
'Public Const MOUSEEVENTF_LEFTUP = &H4
'Public Const MOUSEEVENTF_RIGHTDOWN As Long = &H8
'Public Const MOUSEEVENTF_RIGHTUP As Long = &H10
'
'Private Sub SingleClick()
'  mouse_event MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0
'  mouse_event MOUSEEVENTF_LEFTUP, 0, 0, 0, 0
'End Sub
'
'Private Sub DoubleClick()
'  mouse_event MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0
'  mouse_event MOUSEEVENTF_LEFTUP, 0, 0, 0, 0
'  mouse_event MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0
'  mouse_event MOUSEEVENTF_LEFTUP, 0, 0, 0, 0
'End Sub
'
'Private Sub RightClick()
'  mouse_event MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0
'  mouse_event MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0
'End Sub
'******** END Here => File Name: "D:\dMarcoExcel.xlsm" to call click marcos ********
