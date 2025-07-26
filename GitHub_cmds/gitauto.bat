:: Full Batch Script for Git Repository Automation
:: Here's a comprehensive batch script that automates the entire Git workflow including:
:: 1. Repository initialization
:: 2. Adding files
:: 3. Committing changes
:: 4. Tagging versions
:: 5. Pushing to remote
:: 6. Creating GitHub releases (via GitHub CLI)

@echo off
setlocal enabledelayedexpansion

:: Git Repository Automation Script
:: Automates init, commit, tagging, pushing, and releases

:: Configuration Section
set "REPO_PATH=C:\path\to\your\repo"
set "REMOTE_URL=https://github.com/username/repository.git"
set "DEFAULT_BRANCH=main"
set "GITHUB_CLI=gh.exe" :: Path to GitHub CLI if not in PATH

:: Check if git is available
where git >nul 2>&1
if %errorlevel% neq 0 (
    echo Git is not installed or not in PATH
    pause
    exit /b 1
)

:: Navigate to repository directory
if not exist "%REPO_PATH%" (
    echo Repository path does not exist: %REPO_PATH%
    pause
    exit /b 1
)
cd /d "%REPO_PATH%"

:: Menu System
:menu
cls
echo Git Repository Automation
echo ========================
echo 1. Initialize new repository
echo 2. Add files and commit changes
echo 3. Create tag and push to remote
echo 4. Create GitHub release
echo 5. Full workflow (add, commit, tag, push, release)
echo 6. Exit
echo.
set /p choice="Enter your choice: "

if "%choice%"=="1" goto init_repo
if "%choice%"=="2" goto add_commit
if "%choice%"=="3" goto tag_push
if "%choice%"=="4" goto create_release
if "%choice%"=="5" goto full_workflow
if "%choice%"=="6" exit /b 0

echo Invalid choice, please try again
timeout /t 2 >nul
goto menu

:: Initialize new repository
:init_repo
echo Initializing new Git repository...
git init
if %errorlevel% neq 0 (
    echo Failed to initialize repository
    pause
    goto menu
)

echo Adding remote origin...
git remote add origin %REMOTE_URL%
if %errorlevel% neq 0 (
    echo Failed to add remote
    pause
    goto menu
)

echo Creating initial commit...
echo # Project Title > README.md
git add README.md
git commit -m "Initial commit"
if %errorlevel% neq 0 (
    echo Failed to create initial commit
    pause
    goto menu
)

echo Pushing to remote...
git push -u origin %DEFAULT_BRANCH%
if %errorlevel% neq 0 (
    echo Failed to push to remote
    pause
    goto menu
)

echo Repository initialized successfully!
pause
goto menu

:: Add files and commit changes
:add_commit
set /p commit_msg="Enter commit message: "
if "%commit_msg%"=="" (
    echo Commit message cannot be empty
    pause
    goto menu
)

echo Adding all changed files...
git add .
if %errorlevel% neq 0 (
    echo Failed to add files
    pause
    goto menu
)

echo Committing changes...
git commit -m "%commit_msg%"
if %errorlevel% neq 0 (
    echo Failed to commit changes
    pause
    goto menu
)

echo Changes committed successfully!
pause
goto menu

:: Create tag and push to remote
:tag_push
git fetch --tags
if %errorlevel% neq 0 (
    echo Failed to fetch tags
    pause
    goto menu
)

:: Get current highest tag
for /f "delims=" %%a in ('git describe --tags --abbrev^=0 2^>nul') do set "latest_tag=%%a"
if "%latest_tag%"=="" (
    echo No existing tags found, starting with v0.1.0
    set "new_tag=v0.1.0"
) else (
    echo Latest tag found: %latest_tag%
    :: Extract version numbers
    for /f "tokens=1-3 delims=." %%i in ("%latest_tag:~1%") do (
        set major=%%i
        set minor=%%j
        set patch=%%k
    )
    
    :: Tag versioning options
    echo.
    echo 1. Major version (v%major%.0.0)
    echo 2. Minor version (v%major%.%minor%.0)
    echo 3. Patch version (v%major%.%minor%.%patch%)
    echo.
    set /p version_choice="Select version increment [1-3]: "
    
    if "%version_choice%"=="1" (
        set /a new_major=!major! + 1
        set "new_tag=v!new_major!.0.0"
    ) else if "%version_choice%"=="2" (
        set /a new_minor=!minor! + 1
        set "new_tag=v%major%.!new_minor!.0"
    ) else if "%version_choice%"=="3" (
        set /a new_patch=!patch! + 1
        set "new_tag=v%major%.%minor%.!new_patch!"
    ) else (
        echo Invalid choice, using patch version by default
        set /a new_patch=!patch! + 1
        set "new_tag=v%major%.%minor%.!new_patch!"
    )
)

set /p confirm_tag="Create tag %new_tag%? [Y/n]: "
if /i "%confirm_tag%"=="n" (
    echo Tag creation canceled
    pause
    goto menu
)

echo Creating tag %new_tag%...
git tag -a %new_tag% -m "Version %new_tag%"
if %errorlevel% neq 0 (
    echo Failed to create tag
    pause
    goto menu
)

echo Pushing tag to remote...
git push origin %new_tag%
if %errorlevel% neq 0 (
    echo Failed to push tag
    pause
    goto menu
)

echo Tag %new_tag% created and pushed successfully!
pause
goto menu

:: Create GitHub release
:create_release
for /f "delims=" %%a in ('git describe --tags --abbrev^=0 2^>nul') do set "latest_tag=%%a"
if "%latest_tag%"=="" (
    echo No tags found in repository
    pause
    goto menu
)

echo Latest tag: %latest_tag%
set /p release_title="Release title [%latest_tag%]: "
if "%release_title%"=="" set "release_title=%latest_tag%"

set /p release_notes="Release notes: "
if "%release_notes%"=="" set "release_notes=Release %latest_tag%"

where %GITHUB_CLI% >nul 2>&1
if %errorlevel% neq 0 (
    echo GitHub CLI not found. Install it or provide path in script configuration.
    pause
    goto menu
)

echo Creating GitHub release...
%GITHUB_CLI% release create %latest_tag% --title "%release_title%" --notes "%release_notes%"
if %errorlevel% neq 0 (
    echo Failed to create GitHub release
    pause
    goto menu
)

echo GitHub release created successfully!
pause
goto menu

:: Full workflow
:full_workflow
call :add_commit
if %errorlevel% neq 0 exit /b 1

call :tag_push
if %errorlevel% neq 0 exit /b 1

call :create_release
if %errorlevel% neq 0 exit /b 1

echo Full workflow completed successfully!
pause
goto menu


::Features
:: 1. Interactive Menu System:
::    Initialize new repositories
::    Add files and commit changes
::    Create version tags and push them
::    Create GitHub releases
::    Run the full workflow automatically

:: 2. Smart Tagging:
::    Automatically detects the latest tag
::    Offers semantic versioning options (major/minor/patch)
::    Defaults to patch version increment

:: 3. GitHub Integration:
::   Uses GitHub CLI to create releases
::   Includes release titles and notes

:: 4. Error Handling:
::    Checks for Git installation
::    Validates repository existence
::    Handles failed commands gracefully

:: Requirements
::  Git installed and in PATH
::  For GitHub releases: GitHub CLI (gh) installed
::  Windows system (for batch script)

:: Customization
::  Edit the configuration section at the top:
::  REPO_PATH: Your repository location
::  REMOTE_URL: Your remote repository URL
::  DEFAULT_BRANCH: Your default branch name
::  GITHUB_CLI: Path to GitHub CLI if not in PATH

:: NB: For Linux/macOS users, convert this to a shell script using similar logic but with bash syntax.
