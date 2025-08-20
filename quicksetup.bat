@echo off
if exist .env (
    echo .env file already exists. Skipping creation.
) else (
    echo Creating .env file...
    echo GEMINI_API_KEY=your_api_key_here > .env
    echo .env file created successfully!
)
@echo off
echo Creating virtual environment...
if exist venv (
    echo Virtual environment already exists. Skipping creation.
) else (
    echo Creating virtual environment...
    python -m venv venv
    echo Activating virtual environment...
)
call venv\Scripts\activate
echo Installing required packages...
pip install -r requirements.txt
echo Virtual environment setup complete!
echo You can now run the application using 'python app.py'.