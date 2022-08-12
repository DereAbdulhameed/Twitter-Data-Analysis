# Twitter-Data-Analysis
   This project aims to showcase a complete Machine Learning Workflow with the aim of Understanding the current political sitiuations of the world powers including 
United States, china and Taiwan. This project intends to understand, analyze and gain meaningful insights from the data. In order to complete this task,
we will use Topic Modelling and Sentiment Analysis whilst followung the data science workflow.

# Data Science / Machine Learning Workflow

## Data Understanding
   In this project, two JSON files are given. These files contain dataset of tweets that are gotten from a scraping process done on twitter regrading current poliical situation. The datasets are global_twitter_data.json and africa_twitter_data.json. Each file has numerous columns including but not limited to "followers_count", "original_text", "polarity", "hashtags". From the names of these columns, there should be some intuitions in the mind regarding the nature of the dataset.

## Data Preparation/Processing
   As a data scientist, majority of work lies in processing the data needed for proper modelling. There is need to clean and preprocess the raw data in order to make it ready for modelling. Processing includes but not limited to managing missing data, duplicate data, handling noises and outliers, handling different language in the data as well as other characters that are not strings. The preprocessing step also include splitting of the dataset into training, validation and testing.

## Model Building
   A model will be built on the processed data. In this step, we would explore the concept of NO FREE LUNCH THEOREM where we cannot just pick a single model without trying the others, that is, different models will be built and compared. Training dataset will be used to train/fit while validation and test data will be used to evaluate the model.

## Evaluation
   Performance evaluation will be done using accuracy, f1-score, precision to determine the best performing model

## Deployment
   After the accuracy of the model has beinmg ascertained, the best performing model will then be deployed and canm be used to make predictions by end users.


## Folder Structure
data: contains the dataset
notebooks: contains the jupytrer notebooks
test: contains the test files

