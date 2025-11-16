"""
Generate JSONL training file for OpenAI fine-tuning
"""
import json
import sys
import os

# Import the conversations
from mental_health_conversations import MENTAL_HEALTH_CONVERSATIONS

def create_training_jsonl():
    """Create JSONL file for OpenAI fine-tuning"""
    
    print("🌱 Neurobud Fine-Tuning Data Generator")
    print("=" * 60)
    
    examples = MENTAL_HEALTH_CONVERSATIONS
    
    print(f"📊 Total examples loaded: {len(examples)}")
    
    # Validate format
    print("\n🔍 Validating format...")
    valid_count = 0
    
    for i, example in enumerate(examples):
        if 'messages' not in example:
            print(f"❌ Example {i+1}: Missing 'messages' key")
            continue
            
        messages = example['messages']
        
        if len(messages) < 2:
            print(f"❌ Example {i+1}: Less than 2 messages")
            continue
        
        valid = True
        for msg in messages:
            if 'role' not in msg or 'content' not in msg:
                print(f"❌ Example {i+1}: Invalid message format")
                valid = False
                break
        
        if valid:
            valid_count += 1
    
    print(f"✅ Valid examples: {valid_count}/{len(examples)}")
    
    # Write to JSONL
    output_file = 'neurobud_training.jsonl'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for example in examples:
            f.write(json.dumps(example, ensure_ascii=False) + '\n')
    
    file_size = os.path.getsize(output_file)
    
    print("\n" + "=" * 60)
    print("✅ TRAINING FILE CREATED!")
    print("=" * 60)
    print(f"📁 File: {output_file}")
    print(f"📊 Examples: {len(examples)}")
    print(f"💾 Size: {file_size:,} bytes ({file_size/1024:.2f} KB)")
    print(f"\n🎯 Next: Upload to OpenAI and start fine-tuning!")
    print(f"💰 Estimated Cost: $1-5")
    
    return output_file

if __name__ == "__main__":
    create_training_jsonl()