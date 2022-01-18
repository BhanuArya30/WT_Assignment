# WT_Assignment

____________
Task1 : NLP
____________

Summary:
I have focussed on the exploratory data analysis and building a sentiment classifcation of tweets using BERT based model.

Files:
01_EDA.ipynb - Exploratory data analysis of the the tweets
02_roBERTa_SentimentClassification.ipynb - BERT based pre-trained model used for sentiment classification
top_30_cloud.png - Word cloud of top 30 most frequest tweets
wt_env.yml - Yaml file containing the dependencies required to run the files

Future improvements:
  1. Model - Fine Tune model with more data
  2. Text Preprocesing - Comperhenensive text processing
  3. Influencer indentification - This dataset can also be used for selecting the best influencer a given topic
  4. Entity extraction - Analysis of sentiment across Organizations and People


__________________________
Task2 : Data Reformatting
__________________________

Summary:
I have used Object Objected Approach to define the schema for reformatting. During the process, I did not consider duplicate tweets. There were tweets with same text and metrics but different 'Unnamed' first column.

Files:
result.json - is the file which contains the formatted output
data_reformatting.py - contains Python code for reformatting the json file


