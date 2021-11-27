# W6-api-sentiment-project_DaniHelguera-


# Project steps:

## a) Design the structure of your own database depending on the type of info you want to store.
A CSV data from Kaggle including around 34.000 Amazon Product Reviews has been found at Kaagle.
After cleaning and reorganizing the data in Python, the data base has been reduced to a total of 27405 different ratings.
Following columns have been identified as relevant ones in order to analyse the reviews:
    -   Product_name       37 unique values
    -   rating              5 unique values (1,2,3,4,5)
    -   rating_text     27405 unique values
    -   rating_title    15659 unique values
    -   recommended         2 unique values (True or False)
    -   username        21478 unique values
    -   date              919 unique values
    -   year                4 unique values
    -   month              12 unique values
    -   day                31 unique values

A CSV datafile has been exported and saved in data directory.
A SQL database with following structure has be created:
    - Table: product_names: 
                Fields: ID, productname
    - Table: user_names:
                Fields: ID, username
    - Table: ratings:
                Fields: ID, mark, text, title, date, recommended, id_product, id_user

## a.2) Connect with the SQL Database from Python

## a.3) Upload all ratings to the SQL Data Base


## b) Write an API using flask to receive chat messages and store them in a database (mysql).


## c) Read and serve data from the chats database using different endpoints.

## d) Extract the emotional value of messages per user/chats and make it queryable through an endpoit.

## e) Do it real, use slack API to get messages and analyze the messages of our data-bootcamp channel.

