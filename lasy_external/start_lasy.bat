@echo on

rem \----LASY_DATA_ROOT -- Add the path where you want the databases to be saved on your storage
set "LASY_DATA_ROOT=D:\SynologyDrive\LASY_DATABASE"

rem \----LASY_ROOT -- Add the path where Lasy Me app exists on your storage (this helps with this line: "%LASY_ROOT%\lasy_me.exe")
set "LASY_ROOT=D:\My_Apps_Repo\lasy_me_1.0"

"%LASY_ROOT%\lasy_me.exe"