# Check for all the requirements libraries if already installed or not and 
# install it if not installed.

import importlib.util
import sys
import subprocess
import os

# Fix Windows console encoding
if os.name == 'nt':  # Windows
    os.system('chcp 65001 >nul')

packages = [
    'langchain', 'langchain-core',
    'langchain-openai', 'openai',
    'langchain-anthropic',
    'langchain-google-genai', 'google-generativeai',
    'langchain-huggingface', 'transformers', 'huggingface-hub',
    'python-dotenv',
    'numpy', 'scikit-learn'
]

def is_installed(package):
    return importlib.util.find_spec(package) is not None

def install_package(package):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', package],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"[INSTALLED] {package}")
        return True
    except subprocess.CalledProcessError:
        print(f"[FAILED] {package}")
        return False

print("Checking and installing LangChain dependencies...\n")
for pkg in packages:
    if is_installed(pkg):
        print(f"[OK] Already installed: {pkg}")
    else:
        print(f"[INSTALLING] {pkg}")
        install_package(pkg)

print("\nDone! Run 'pip list | findstr langchain' to verify.")
