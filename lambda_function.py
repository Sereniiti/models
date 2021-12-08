
import json
import logging
import boto3
import datetime
import random
import time
import os
from utilities import files_utils, text_utils
from botocore.exceptions import ClientError
from DistilBERT import inference

def lambda_handler(event, context):
    # get the body of the API call
    body=json.loads(event['body'])
    # Let's suppose it contains text for inference
    text=body['text']
    # Split the text into sentences
    sentences = text_utils.NLTK_sentence_split(text)
    # Download BERT if it tge first used?
    if not os.path.exists("./prod"):
        inference.download_BERT()
    # Calculate the inference
    result = inference.distilbert_inference(sentences)
    # Return the results to the outside
    return {
        'status': 200,
        'body' : result
    }