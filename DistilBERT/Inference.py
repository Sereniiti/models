### Inference function ###
import os
import boto3
import tarfile
from utilities import files_utils

# Typing
from typing import List

# Huggingface transformers
from transformers import DistilBertConfig,  DistilBertTokenizer

# Tensorflow
import tensorflow as tf

# Function
def distilbert_inference(sentences: List[str], from_s3 = True, root_directory = "./"):
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
  ## Define what saved model file to use
  path = os.path.join(root_directory,"models/distilBERT/prod")
  if from_s3:
    path = os.path.join(root_directory,"prod")
  ## Load the model
  model = tf.keras.models.load_model(path)

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


def download_BERT():
    # Download from s3
    s3 = boto3.client('s3')
    s3.download_file('sereniiti-inference', 'distilBERT', 'distilBERT.tar.gz')
    # unpack
    files_utils.unpack_tarfile("distilBERT.tar.gz","./")
    
