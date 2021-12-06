### Inference function ###

# Typing
from typing import List

# Huggingface transformers
from transformers import DistilBertConfig,  DistilBertTokenizer

# Tensorflow
import tensorflow as tf

# Function
def distilbert_inference(sentences: List[str]):
  """
  Launch an inference on a set of sentences.
  Uses distilbert classification and regression heads.
  """
  
  # Name of the BERT model to use
  model_name = 'distilbert-base-uncased'

  # Max length of the sentences
  max_length = 120

  # Load transformers config and set output_hidden_states to False
  config = DistilBertConfig.from_pretrained(model_name)
  config.output_hidden_states = False

  # Load BERT tokenizer
  tokenizer = DistilBertTokenizer.from_pretrained(pretrained_model_name_or_path = model_name, config = config)

  # Load the model from disk
  model = tf.keras.models.load_model('../models/distilBERT/prod')

  # Tokenize
  embedded_sentences = tokenizer(
    text=sentences,
    add_special_tokens=True,
    max_length=max_length,
    truncation=True,
    padding='max_length', 
    return_tensors='tf',
    return_token_type_ids = True,
    return_attention_mask = True,
    verbose = True)

  return model.call(embedded_sentences)