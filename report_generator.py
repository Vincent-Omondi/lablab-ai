from transformers import AutoTokenizer, T5ForConditionalGeneration
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Use smaller model
MODEL_NAME = "google/flan-t5-small"

def load_model():
    try:
        logger.info(f"Loading tokenizer and model from {MODEL_NAME}...")
        
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)
        
        logger.info("Model loaded successfully!")
        return tokenizer, model
    
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        raise

# Load model and tokenizer at module level
try:
    tokenizer, model = load_model()
except Exception as e:
    logger.error(f"Failed to initialize model: {str(e)}")
    tokenizer, model = None, None

def generate_report(metrics):
    if tokenizer is None or model is None:
        return "Error: Model not properly initialized"
        
    prompt = f"""
    You are a network monitoring system. Generate a detailed and professional network status report based on the following metrics:
    
    - CPU Load: {metrics['cpu_load']}%
    - Packet Loss: {metrics['packet_loss']}%
    - Predicted Failure: {'Yes' if metrics['failure'] else 'No'}
    
    The report should include:
    1. A summary of the current network status.
    2. An analysis of the CPU load and packet loss.
    3. Recommendations based on the predicted failure status.
    
    Report:
    """
    
    try:
        # Tokenize input
        inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
        
        # Generate text
        outputs = model.generate(
            inputs.input_ids,
            max_length=300,  # Increase max_length for a more detailed report
            do_sample=True,
            temperature=0.7
        )
        
        # Decode and return the generated text
        report = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return report
        
    except Exception as e:
        logger.error(f"Error generating report: {str(e)}")
        return f"Error generating report: {str(e)}"