@echo off
:a
color 2
echo 1 1 1 0 1 0 0 0 1 1 1 1 0 0 0 1 1 0 0 1 0 0 0 1 1 0 1 0 1 0 0 0 1 1 1 1 1 0 1 0 0 1 0 1 0 
ping localhost -n 1 > nul
echo 1 1 0 1 1 1 0 0 0 1 0 1 a f h 0 0 0 1 0 1 1 0 0 1 1 1 0 0 1 0 1 0 0 1 1 0 010 0 1 1 0 0 1 
ping localhost -n 1 > nul
echo 0 1 0 0 0 1 0 0 0 1 0 0 0 1 0 1 0 0 1 0 1 0 1 1 0 1 0 0 0 0 1 0 1 0 0 1 0 1 0 1 0 9 1 0 1
ping localhost -n 1 > nul
echo 1 0 1 1 1 0 1 1 0 9 1 1 2 1 1 0 9 1 0 5 7 7 8 7 8 1 3 2 1 2 1 2 3 2 1 3 4 1 0 0 1 0 0 0 1 
ping localhost -n 1 > nul
echo 1 1 1 0 1 0 0 1 0 0 0 1 1 1 0 0 1 1 1 4 1 2 1 1 2 0 1 0 1 2 2 1 0 1 1 0 1 1 0 1 0 1 0 1 0
goto a