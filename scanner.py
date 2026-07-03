import os
import sys
from google import genai

# Initialize the client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def scan_terraform(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print("Error: main.tf not found.")
        return False

    prompt = f"""
    You are a Senior Security Architect. Analyze the following Terraform code for security risks.
    Look specifically for public S3 buckets or open security groups (0.0.0.0/0).
    If the code has security risks, output 'FAIL' followed by a brief explanation.
    If it is secure, output 'PASS'.
    
    Terraform Code:
    {code}
    """
    
    # Using the updated client syntax
    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=prompt,
    )
    
    print(response.text)
    return "FAIL" not in response.text

if __name__ == "__main__":
    if scan_terraform('main.tf'):
        sys.exit(0)
    else:
        sys.exit(1)
