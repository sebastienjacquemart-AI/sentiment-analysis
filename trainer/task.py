from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")
data = ["I love you", "I hate you", "I eat apple"]
results_default_model = sentiment_pipeline(data)

print(results_default_model)

specific_model = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")
results_specific_model = specific_model(data)

print(results_specific_model)