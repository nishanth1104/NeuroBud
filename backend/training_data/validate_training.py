"""
Validate training file format before uploading to OpenAI
"""
import json

def validate_jsonl(file_path):
    print("🔍 Validating training file...")
    print("=" * 60)
    
    errors = []
    warnings = []
    examples = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            try:
                example = json.loads(line)
                examples.append(example)
                
                # Check structure
                if 'messages' not in example:
                    errors.append(f"Line {i}: Missing 'messages' key")
                    continue
                
                messages = example['messages']
                
                # Check message count
                if len(messages) < 2:
                    errors.append(f"Line {i}: Need at least 2 messages")
                    continue
                
                # Check message format
                for j, msg in enumerate(messages):
                    if 'role' not in msg:
                        errors.append(f"Line {i}, Message {j}: Missing 'role'")
                    if 'content' not in msg:
                        errors.append(f"Line {i}, Message {j}: Missing 'content'")
                    
                    # Check roles
                    if msg.get('role') not in ['system', 'user', 'assistant']:
                        errors.append(f"Line {i}, Message {j}: Invalid role '{msg.get('role')}'")
                    
                    # Check content length
                    content_len = len(msg.get('content', ''))
                    if content_len == 0:
                        warnings.append(f"Line {i}, Message {j}: Empty content")
                    elif content_len > 4096:
                        warnings.append(f"Line {i}, Message {j}: Very long content ({content_len} chars)")
                
            except json.JSONDecodeError as e:
                errors.append(f"Line {i}: Invalid JSON - {e}")
    
    # Print results
    print(f"📊 Total examples: {len(examples)}")
    print(f"✅ Valid examples: {len(examples) - len(errors)}")
    
    if errors:
        print(f"\n❌ ERRORS: {len(errors)}")
        for error in errors[:10]:  # Show first 10
            print(f"  - {error}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")
    
    if warnings:
        print(f"\n⚠️  WARNINGS: {len(warnings)}")
        for warning in warnings[:5]:  # Show first 5
            print(f"  - {warning}")
        if len(warnings) > 5:
            print(f"  ... and {len(warnings) - 5} more")
    
    if not errors:
        print("\n" + "=" * 60)
        print("✅ FILE IS VALID!")
        print("🎯 Ready to upload to OpenAI!")
        print("=" * 60)
        return True
    else:
        print("\n" + "=" * 60)
        print("❌ FILE HAS ERRORS - FIX BEFORE UPLOADING")
        print("=" * 60)
        return False

if __name__ == "__main__":
    is_valid = validate_jsonl('neurobud_training.jsonl')
    exit(0 if is_valid else 1)