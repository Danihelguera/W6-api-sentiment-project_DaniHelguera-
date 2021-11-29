#############################
#                           #
#       PROJECT W6:         #
#       Api-sentiment       #
#       DaniHelguera        #
#                           #
#   CREATE THE DB IN SQL    #
#                           #
#############################


DROP DATABASE IF EXISTS amazon_rating;
CREATE DATABASE amazon_rating;
USE amazon_rating;

#############################
#      CREATE THE TABLES    #
#############################
-- -----------------------------------------------------
-- Table 'product_names'
-- -----------------------------------------------------
CREATE TABLE product_names(
  ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  productname TINYTEXT
  );

-- -----------------------------------------------------
-- Table 'user_names'
-- -----------------------------------------------------
CREATE TABLE user_names (
  ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  username VARCHAR(30)
  );

-- -----------------------------------------------------
-- Table 'ratings'
-- -----------------------------------------------------
CREATE TABLE ratings (
  ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  mark ENUM ('1','2','3','4','5') ,
  texto TEXT,
  title VARCHAR(60),
  date_ DATE,
  recommended BOOLEAN, 
  ID_product INT,
  ID_user INT,
  FOREIGN KEY (ID_product) REFERENCES product_names(ID) ON DELETE SET NULL, 
  FOREIGN KEY (ID_user)    REFERENCES user_names(ID)    ON DELETE SET NULL
  );

    
  
