"""
Check fine-tuning job status
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

def check_status(job_id):
    print("🔍 Checking fine-tuning status...")
    print("=" * 60)
    print(f"🆔 Job ID: {job_id}\n")
    
    try:
        response = client.fine_tuning.jobs.retrieve(job_id)
        
        print(f"📊 Status: {response.status}")
        print(f"🤖 Base Model: {response.model}")
        
        # Show training progress if available
        if hasattr(response, 'trained_tokens') and response.trained_tokens:
            print(f"🎯 Tokens Trained: {response.trained_tokens:,}")
        
        if response.fine_tuned_model:
            print(f"\n✅ Fine-tuned Model ID: {response.fine_tuned_model}")
            
            # Save model name
            with open('model_name.txt', 'w') as f:
                f.write(response.fine_tuned_model)
            print("💾 Model ID saved to model_name.txt")
        
        print("\n" + "=" * 60)
        
        if response.status == 'succeeded':
            print("🎉 FINE-TUNING COMPLETE!")
            print("=" * 60)
            print("\n🎯 Next Steps:")
            print("1. Copy your model ID from above")
            print("2. Add to backend/.env:")
            print(f"   FINE_TUNED_MODEL={response.fine_tuned_model}")
            print("   USE_FINE_TUNED=true")
            print("\n3. Restart your backend server")
            print("4. Test your fine-tuned model!")
            
        elif response.status == 'running':
            print("⏳ STILL TRAINING...")
            print("=" * 60)
            print("\nCheck back in 5-10 minutes.")
            print("Run: python check_status.py")
            
        elif response.status == 'validating_files':
            print("🔍 VALIDATING FILES...")
            print("=" * 60)
            print("\nOpenAI is checking your training file.")
            print("This usually takes 1-2 minutes.")
            
        elif response.status == 'queued':
            print("⏰ QUEUED...")
            print("=" * 60)
            print("\nWaiting for training to start.")
            print("This usually takes a few minutes.")
            
        elif response.status == 'failed':
            print("❌ TRAINING FAILED!")
            print("=" * 60)
            if hasattr(response, 'error') and response.error:
                print(f"\nError: {response.error}")
            print("\nCheck your training file format and try again.")
            
        elif response.status == 'cancelled':
            print("🛑 TRAINING CANCELLED")
            print("=" * 60)
        
        print("=" * 60)
        
        return response.status
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    try:
        with open('job_id.txt', 'r') as f:
            job_id = f.read().strip()
        
        if not job_id:
            print("❌ job_id.txt is empty!")
            exit(1)
        
        status = check_status(job_id)
        
    except FileNotFoundError:
        print("❌ job_id.txt not found!")
        print("Run start_fine_tuning.py first to start a fine-tuning job.")