::------------------------------------------------------------------------------------------------
:: Git Automation Created By Alem Fitwi
::------------------------------------------------------------------------------------------------
@echo off
::------------------------------------------------------------------------------------------------
REM Set Params
set BRANCH=main
set REMOTE_URL=git@https://github.com/ahfitwi/Miscellaneous.git
set COMMIT_MSG=Add Commit Message Here
set TAG_ID=v01.00.00
set TAG_MSG=Release Version v01.00.00
::------------------------------------------------------------------------------------------------
REM Initialize git repo if need be
if not exist ".git"(
     git init
     git remote add origin "%REMOTE_URL%
)
::------------------------------------------------------------------------------------------------
REM Show Status
git status
::------------------------------------------------------------------------------------------------
REM Stage All Changes or Specify a specific file name
git add .
::------------------------------------------------------------------------------------------------
REM Commit Changes
git commit -m "%COMMIT_MSG%"
::------------------------------------------------------------------------------------------------
REM Tsg The Commit
git tag -a %TAG_ID% -m "%TAG_MSG%"
::------------------------------------------------------------------------------------------------
REM Push Branch and Tags
git push origin %BRANCH%
git push origin %TAG_ID%
::------------------------------------------------------------------------------------------------
REM [Optional] Create A Github Release Using GitHub CLI(gh), must be installed on PC
REM Uncomment The Next Line If You Have GitHub CLI Installed & Authenticated
REM gh release create %TAG_ID% --title "%TAG_MSG%"
::------------------------------------------------------------------------------------------------
REM Add Tag To Already Committed And Pushed Repo
set COMMIT_ID=zxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxggggggggggggggggyyyyyyyyyyy
set TAG_ID=v01.01.02
set TAG_MSG=Release Version v01.01.02
git tag -a %TAG_ID%  %COMMIT_ID% -m "%TAG_MSG%"

::------------------------------------------------------------------------------------------------
echo All Done!
pause

REM End
::------------------------------------------------------------------------------------------------
