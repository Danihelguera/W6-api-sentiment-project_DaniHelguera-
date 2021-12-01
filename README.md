# W6-api-sentiment-project_DaniHelguera-
# Emotions check on Amazon Products Reviews

This project tries to develop a method for "objective emotional" evaluation of amazon products review.
The final aim is to be able to evaluate the emotions that a product generates in the purchasers by the analysis of the text writen as review, not only seeing the number of stars given to that product.


## Project steps:
The project consists on several steps that are also documented by the following succesive scripts:
    01_Data_loading_cleaning_exporting.ipynb
    02_SQL_DB_Structure_creation.sql
    02_SQL_DB_Structure_Schema_after_Reverse_Engineering.png
    03_Feeding_the_SQL_DataBase.ipynb
    04_Api_calls.ipynb
    05_Sentiment_analysis.ipynb

### 1) Find and clean a suitable data that includes texts to be analyzed under an emotional perpective.
A CSV data including around 34.000 Amazon Product Reviews has been found at Kaagle.
After cleaning and reorganizing the data in Python, the data base has been reduced to a total of 27405 different ratings.
Following columns have been identified as relevant ones in order to analyse the reviews:
    -   Product_name       37 unique values
    -   rating              5 unique values (1,2,3,4,5)
    -   rating_text     27405 unique values
    -   rating_title    15659 unique valuesj
    -   recommended         2 unique values (True or False)
    -   username        21478 unique values
    -   date              919 unique values
    -   year                4 unique values
    -   month              12 unique values
    -   day                31 unique values
A new CSV datafile with the cleaned reviews has been exported and saved in data directory.
The script "01_Data_loading_cleaning_exporting.ipynb" includes all necesary operations.

### 2) Design the structure of your own database depending on the type of info you want to store.
A SQL database with following structure has be created using the script "02_SQL_DB_Structure_creation.sql"
Data Basis: amazon_rating:
    - Table: product_names: 
                Fields: ID, productname
    - Table: user_names:
                Fields: ID, username
    - Table: ratings:
                Fields: ID, mark, text, title, date, recommended, id_product, id_user

### 3) Feed all reviews, products and users from dataframe into SQL Database
The jupyter notebook script "03_Feeding_the_SQL_DataBase.ipynb" includes all required operations.
Firstly, it is mandatory to connect to the DataBase (including secret password) and to launch the engine.
The connection configuration is storaged in the file "config/configuration.py".
Secondly, four functions have been defined in order to be able to insert all information in the BD:
    - check: Funtion that checks if any asked element (user, product or rating) exists already in the data base.
             This function return a list with True or False and the corresponding ID or None of the asked element
    - insert_user:    inserts a new user in the database and return the assigned ID.
                      if the user already exists, it makes nothing and return the previously assigned ID.
    - insert_product: inserts a new product in the database and return the assigned ID.
                      if the product already exists, it makes nothing and return the previously assigned ID.
    - insert_rating:  inserts a new rating in the database and return the assigned ID.
                      it find (or inserts if any) the ID of product and ID of user in the corresponding tables.
                      if the rating already exists, it makes nothing and return the previously assigned ID.
Those four function can be loaded from the file "config/sql_tools.py".
Thirdly, after loading the cleaned dataframe, it has to be iterated row by row to insert each row in the BD.
Some rows are giving codification errors while inserting in the Database from python in SQL.
Those problematic 63 rows are skipped with try-except and identified in a list for later analysis.
A JSON file has been exporte including index, error type and error message of those problematic 63 rows. 

### 4) Write an API using flask to receive and/or store ratings in the database (mysql).
Following endpoints have been defined in the Flask API.
    /                   [GET]
    /user_list          [GET]
    /product_list       [GET]
    /newuser            [POST]
    /newproduct         [POST]
    /newrating          [POST]
    /ratingsbyuser      [GET]
    /ratingsbyproduct   [GET]
The API server is launched with the file "main.py" executed directly in the Terminal.
The file "config/sql_tools.py" has been extended with further four functions:
    - users_list()
    - products_list()
    - ratings_by_user(user)
    - ratings_by_product(product)
These new four functions are used to give answer to the api calls.
The jupyter notebook script "04_Api_calls.ipynb" follow several steps showing how the api works:
    a) required libraries importation
    b) Checking that all endpoints gives a 200 response
    c) Checking the content of every endpoint
    d) Checking that the responses of every are JSON'izables
    e) Transforming the JSONs to Pandas DataFrames for further processes.

### 5) Extract the emotional value of the amazon reviews.
The jupyter Notebook "05_Sentiment_analysis.ipynb" includes all required operations.
It uses the library spacy and the function SentimentIntensityAnalyzer from library nltk, and generates the
new columns
    - rating_text_tokenized	
    - sentiment_title	
    - sentiment_text	
    - sentiment_text_tokenized

### 6) Do it useful for your own product interests.
    To download the reviews, it is possible to make web-scrapping in the amazon webpage of a determined product and to automatically download all reviews. THIS PART IS STILL PENDING.
    The downloaded reviews can be uploaded to our SQL Database by using the api endpoints or just to run the script to have also the emotional analyse of those reviews.


    Por último te faltaría el technology stack. Es decir un apartado en el que digas que librerías has utilizado y el link a la documentación de cada una. Puedes hacer algo así:

## Technology stack:
    - [Kaggle](https://www.kaggle.com/)
    - [pandas](https://pandas.pydata.org/docs/)
    - [datetime](https://docs.python.org/3/library/datetime.html)
    - [sqlalchemy](https://www.sqlalchemy.org/)
    - [json](https://docs.python.org/3/library/json.html)
    - [requests](https://docs.python-requests.org/en/latest/)
    - [spacy](https://spacy.io/)
    - [SentimentIntensityAnalyzer from nltk.sentiment.vader](https://www.nltk.org/api/nltk.sentiment.html)
    - [seaborn](https://seaborn.pydata.org/)
    - [flask](https://flask.palletsprojects.com/en/2.0.x/)
    