import os
import sys
import time
from google import genai
from google.genai.errors import ClientError, ServerError

# Initialize the client using the environment variable
# Ensure GOOGLE_API_KEY is set in your Jenkins Credentials
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("Error: GOOGLE_API_KEY environment variable not set.")
    sys.exit(1)

client = genai.Client(api_key=api_key)

def scan_terraform(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return False

    prompt = f"""
    You are a Senior Security Architect. Analyze the following Terraform code for security risks.
    Look specifically for public S3 buckets, open security groups (0.0.0.0/0), or hardcoded secrets.
    If the code has security risks, output 'FAIL' followed by a brief, professional explanation of the vulnerability.
    If it is secure, output 'PASS'.
    
    Terraform Code:
    {code}
    """
    
    # Retry logic to handle API rate limits and temporary service unavailability
    max_retries = 5
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model='gemini-flash-latest', # Using the 'latest' alias for best availability
                contents=prompt,
            )
            
            print("--- AI Analysis Result ---")
            print(response.text)
            print("--------------------------")
            
            # If the AI response contains FAIL, we return False to fail the pipeline
            return "FAIL" not in response.text

        except (ServerError, ClientError) as e:
            wait_time = (attempt + 1) * 30
            print(f"API Error (Attempt {attempt + 1}/{max_retries}): {e}. Retrying in {wait_time}s...")
            time.sleep(wait_time)
            
    print("Error: Scanner failed after multiple attempts due to API unavailability.")
    return False 

if __name__ == "__main__":
    # Point to your terraform file
    if scan_terraform('main_secure.tf'):
        print("Security Scan Passed.")
        sys.exit(0) # Exit 0 = Success
    else:
        print("Security Scan Failed.")
        sys.exit(1) # Exit 1 = Fail (Jenkins will stop the pipeline)
