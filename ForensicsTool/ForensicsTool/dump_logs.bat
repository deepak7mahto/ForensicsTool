mkdir C:\Windows_Event_logs
Powershell -Command "& { Start-Process xcopy -ArgumentList \"C:\Windows\System32\winevt C:\Windows_Event_logs /E\" -Verb RunAs }"