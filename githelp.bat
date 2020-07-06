
@echo off
SET /A "index = 1"
SET /A "count = 5"
:while
if %index% neq %count% (
   echo Pulling...
   git pull
   echo Pushing...
   git push
   goto :while
)