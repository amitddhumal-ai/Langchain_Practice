import os
import google.generativeai as genai

os.environ["GOOGLE_API_KEY"] = "AIzaSyCJtS-1MBEB_wxTZaF_QH5_Wo0sZmsAZ44"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

print("✅ Your Available Gemini Models:")
print("-" * 50)

for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"✅ {model.name} - {model.display_name}")

print("\nCopy the model.name (first line) for your apitest.py!")
