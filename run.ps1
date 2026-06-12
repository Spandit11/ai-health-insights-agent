# Activate the virtual environment and start Streamlit
$activatePath = Join-Path $PSScriptRoot 'venv\Scripts\Activate.ps1'
if (-Not (Test-Path $activatePath)) {
    Write-Error "Virtual environment activate script not found at $activatePath"
    exit 1
}

& $activatePath

Write-Host "Starting Streamlit..."
streamlit run src/main.py
