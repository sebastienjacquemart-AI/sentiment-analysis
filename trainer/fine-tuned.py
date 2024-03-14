from datasets import load_dataset
from transformers import AutoTokenizer

imdb = load_dataset("imdb")

train_dataset = imdb["train"].shuffle(seed=42).select([i for i in list(range(3000))])
test_dataset = imdb["test"].shuffle(seed=42).select([i for i in list(range(300))])

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

def preprocess(examples):
    return tokenizer(examples["text"], truncation=True)


print(train_dataset[0])

