# sentiment-analysis

https://huggingface.co/blog/sentiment-analysis-python

Sentiment analysis is the automated process of tagging data according to their sentiment, such as positive, negative and neutral.

## Build model using transformers
Transformers library provides pre-trained models for various NLP tasks, including sentiment analysis.

On the Hugging Face Hub, we are building the largest collection of models and datasets publicly available in order to democratize machine learning 🚀. In the Hub, you can find more than 27,000 models shared by the AI community with state-of-the-art performances on different tasks.

This code snippet uses the pipeline class to make predictions from models available in the Hub. You can use a specific sentiment analysis model that is better suited to your language or use case by providing the name of the model.

The following are some popular models for sentiment analysis models available on the Hub that we recommend checking out:
* Twitter-roberta-base-sentiment is a roBERTa model trained on ~58M tweets and fine-tuned for sentiment analysis. Fine-tuning is the process of taking a pre-trained large language model (e.g. roBERTa in this case) and then tweaking it with additional training data to make it perform a second similar task (e.g. sentiment analysis).
* Bert-base-multilingual-uncased-sentiment is a model fine-tuned for sentiment analysis on product reviews in six languages: English, Dutch, German, French, Spanish and Italian.
* Distilbert-base-uncased-emotion is a model fine-tuned for detecting emotions in texts, including sadness, joy, love, anger, fear and surprise.

The complete list of sentiment analysis models: https://huggingface.co/models?pipeline_tag=text-classification&sort=downloads&search=sentiment

## Building your own sentiment analysis model

Using pre-trained models publicly available on the Hub is a great way to get started right away with sentiment analysis. These models use deep learning architectures such as transformers that achieve state-of-the-art performance on sentiment analysis and other machine learning tasks. However, you can fine-tune a model with your own data to further improve the sentiment analysis results and get an extra boost of accuracy in your particular use case.

In this section, we'll go over two approaches on how to fine-tune a model for sentiment analysis with your own data and criteria. The first approach uses the Trainer API from the 🤗Transformers, an open source library with 50K stars and 1K+ contributors and requires a bit more coding and experience. The second approach is a bit easier and more straightforward, it uses AutoNLP, a tool to automatically train, evaluate and deploy state-of-the-art NLP models without code or ML experience.
