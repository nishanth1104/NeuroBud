"""
Upload training file to OpenAI
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from parent directory
load_dotenv('../.env')  # or '../.env' depending on structure

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def upload_file():
    print("📤 Uploading training file to OpenAI...")
    print("=" * 60)
    
    # Verify API key is loaded
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY not found!")
        print("Make sure your .env file exists and contains OPENAI_API_KEY")
        return None
    
    print(f"✅ API Key loaded: {api_key[:20]}...")
    
    try:
        with open('neurobud_training.jsonl', 'rb') as f:
            response = client.files.create(
                file=f,
                purpose='fine-tune'
            )
        
        file_id = response.id
        
        print("✅ FILE UPLOADED!")
        print("=" * 60)
        print(f"📁 File ID: {file_id}")
        print(f"📊 Status: {response.status}")
        print(f"💾 Bytes: {response.bytes:,}")
        print(f"\n🎯 Save this File ID - you'll need it for fine-tuning!")
        print("=" * 60)
        
        # Save file ID for later use
        with open('file_id.txt', 'w') as f:
            f.write(file_id)
        
        print("\n💾 File ID saved to file_id.txt")
        
        return file_id
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return None

if __name__ == "__main__":
    file_id = upload_file()