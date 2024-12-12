@echo off

:: Get the directory of the script where it is run
set "ROOT_DIR=%~dp0"

:: Specify the relative directory to zip (e.g., a subdirectory named "assets")
set "SOURCE_DIR=%ROOT_DIR%assets"

:: Specify the relative path for the output zip file
set "ZIP_FILE=%ROOT_DIR%odyssey-resource-pack.zip"

:: Specify the README file and Pack to include from source
set "README_FILE=%ROOT_DIR%README.md"
set "MCMETA_FILE=%ROOT_DIR%pack.mcmeta"
set "PACKPNG_FILE=%ROOT_DIR%pack.png"

:: Create a temporary directory to hold filtered files
set "TEMP_DIR=%TEMP%\filtered_files"
if exist "%TEMP_DIR%" rd /s /q "%TEMP_DIR%"
mkdir "%TEMP_DIR%"

:: Create exclude.txt file containing patterns to ignore
echo .pyc>exclude.txt
echo __pycache__>>exclude.txt

:: Copy files excluding .pyc and __pycache__
xcopy "%SOURCE_DIR%" "%TEMP_DIR%" /E /I /EXCLUDE:exclude.txt >nul

:: Copy README file into the temporary directory
copy "%README_FILE%" "%TEMP_DIR%" >nul
copy "%MCMETA_FILE%" "%TEMP_DIR%" >nul
copy "%PACKPNG_FILE%" "%TEMP_DIR%" >nul

:: Use PowerShell to zip the filtered files
PowerShell -Command "Compress-Archive -Path '%TEMP_DIR%\*' -DestinationPath '%ZIP_FILE%'"

:: Cleanup
if exist "%TEMP_DIR%" rd /s /q "%TEMP_DIR%"
del exclude.txt

@echo Zip file created successfully: %ZIP_FILE%
:: certutil -hashfile "odyssey-resource-pack-test.zip" SHA1