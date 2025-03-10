@set mypath=%cd%

cd %mypath%

python -m PyInstaller search-machine.py --add-data="1M-bq-results-20250310-165622-1741625891242.csv:." --add-data="history.txt:." --console --onefile --noconfirm

@Pause