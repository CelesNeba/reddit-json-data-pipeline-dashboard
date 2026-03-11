@echo off
REM Activate virtual environment
call env\Scripts\activate.bat

REM Start Reddit collector in a separate window
start cmd /k "python reddit_collector.py"

REM Start Streamlit dashboard in a separate window
start cmd /k "streamlit run dashboard.py"

REM Keep this window open
pause