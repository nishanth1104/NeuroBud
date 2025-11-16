"""
Start fine-tuning job on OpenAI
"""
import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

# Load .env file from backend directory
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

# Initialize OpenAI client
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    print("❌ ERROR: OPENAI_API_KEY not found!")
    print(f"Looking for .env at: {env_path}")
    exit(1)

client = OpenAI(api_key=api_key)

def start_fine_tuning(file_id):
    print("🚀 Starting fine-tuning job...")
    print("=" * 60)
    print(f"✅ API Key loaded: {api_key[:20]}...")
    print(f"📁 Using File ID: {file_id}\n")
    
    try:
        response = client.fine_tuning.jobs.create(
            training_file=file_id,
            model="gpt-4o-mini-2024-07-18",
            hyperparameters={
                "n_epochs": 3  # Number of training passes
            },
            suffix="neurobud-v1"  # Your custom model suffix
        )
        
        job_id = response.id
        
        print("✅ FINE-TUNING JOB STARTED!")
        print("=" * 60)
        print(f"🆔 Job ID: {job_id}")
        print(f"📊 Status: {response.status}")
        print(f"🤖 Base Model: {response.model}")
        print(f"\n⏳ Estimated time: 10-30 minutes")
        print(f"💰 Estimated cost: $1-3")
        print("=" * 60)
        
        # Save job ID
        with open('job_id.txt', 'w') as f:
            f.write(job_id)
        
        print("\n💾 Job ID saved to job_id.txt")
        print("\n🔍 Check status with: python check_status.py")
        print("⏰ Check back in 10-15 minutes!")
        
        return job_id
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    # Read file ID
    try:
        with open('file_id.txt', 'r') as f:
            file_id = f.read().strip()
        
        if not file_id:
            print("❌ file_id.txt is empty!")
            print("Run upload_training.py first!")
            exit(1)
        
        job_id = start_fine_tuning(file_id)
        
        if job_id:
            print("\n✅ SUCCESS! Fine-tuning job is running.")
        else:
            print("\n❌ Failed to start fine-tuning. Check errors above.")
            
    except FileNotFoundError:
        print("❌ file_id.txt not found!")
        print("Run upload_training.py first to upload your training file.")