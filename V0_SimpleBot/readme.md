1. `Get-Command python`
2. `Get-Command pip`
3. Get all installed versions of python: `py -0`
4. `py3.11 -m venv venv`
5. `venv/Scripts/activate`
6. `pip cache purge`
7. `python -m pip install pip --upgrade`
8. `python -m pip install -r requirements.txt`
   > Note: You can install dependencies one by one as well\
   > `python -m pip install __your_space_separated_dependencies ....`
9. Download Ollama from https://ollama.com/download
10. Add ollama.exe PATH in windows environment variable
11. windows cmd `ollama --version`
12. pull model from ollama `ollama pull __your_model_name__`
13. `streamlit run __your_file_name__`