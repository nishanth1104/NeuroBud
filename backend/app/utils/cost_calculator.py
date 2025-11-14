from app.config import settings
from typing import Dict

class CostCalculator:
    """Calculate OpenAI API costs"""
    
    @staticmethod
    def calculate_chat_cost(input_tokens: int, output_tokens: int, model: str = "gpt-4o-mini") -> Dict:
        """
        Calculate cost for chat completion
        
        Returns:
            dict with input_cost, output_cost, total_cost
        """
        
        # Determine pricing based on model
        if model.startswith("ft:"):  # Fine-tuned model
            input_price = settings.FINE_TUNED_INPUT_PRICE
            output_price = settings.FINE_TUNED_OUTPUT_PRICE
        else:  # Base model (gpt-4o-mini)
            input_price = settings.GPT4O_MINI_INPUT_PRICE
            output_price = settings.GPT4O_MINI_OUTPUT_PRICE
        
        # Calculate costs (price is per 1M tokens, so divide by 1,000,000)
        input_cost = (input_tokens / 1_000_000) * input_price
        output_cost = (output_tokens / 1_000_000) * output_price
        total_cost = input_cost + output_cost
        
        return {
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": input_tokens + output_tokens,
            "input_cost": round(input_cost, 6),
            "output_cost": round(output_cost, 6),
            "total_cost": round(total_cost, 6),
            "model": model
        }
    
    @staticmethod
    def calculate_embedding_cost(tokens: int) -> Dict:
        """
        Calculate cost for embeddings
        
        Returns:
            dict with token count and cost
        """
        cost = (tokens / 1_000_000) * settings.EMBEDDING_PRICE
        
        return {
            "tokens": tokens,
            "cost": round(cost, 6),
            "feature": "embedding"
        }
    
    @staticmethod
    def calculate_fine_tuning_cost(training_tokens: int) -> Dict:
        """
        Calculate cost for fine-tuning
        
        Returns:
            dict with token count and cost
        """
        cost = (training_tokens / 1_000_000) * settings.FINE_TUNE_TRAINING_PRICE
        
        return {
            "training_tokens": training_tokens,
            "cost": round(cost, 6),
            "feature": "fine_tuning"
        }
    
    @staticmethod
    def estimate_tokens(text: str) -> int:
        """Rough estimation: 4 characters ≈ 1 token"""
        return len(text) // 4