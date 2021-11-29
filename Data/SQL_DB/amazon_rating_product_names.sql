-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: amazon_rating
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `product_names`
--

DROP TABLE IF EXISTS `product_names`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_names` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `productname` tinytext,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_names`
--

LOCK TABLES `product_names` WRITE;
/*!40000 ALTER TABLE `product_names` DISABLE KEYS */;
INSERT INTO `product_names` VALUES (1,'All-New Fire HD 8 Tablet 8 HD Display Wi-Fi 16 GB - Includes Special Offers Magenta'),(2,'Kindle Oasis E-reader with Leather Charging Cover - Merlot 6 High-Resolution Display (300 ppi) Wi-Fi - Includes Special Offers'),(3,'All-New Fire HD 8 Tablet 8 HD Display Wi-Fi 32 GB - Includes Special Offers Magenta'),(4,'Fire HD 8 Tablet with Alexa 8 HD Display 32 GB Tangerine - with Special Offers'),(5,'Amazon 5W USB Official OEM Charger and Power Adapter for Fire Tablets and Kindle eReaders'),(6,'Amazon Kindle Fire Hd (3rd Generation) 8gb'),(7,'Fire Tablet 7 Display Wi-Fi 8 GB - Includes Special Offers Magenta'),(8,'Kindle Oasis E-reader with Leather Charging Cover - Black 6 High-Resolution Display (300 ppi) Wi-Fi - Includes Special Offers'),(9,'Amazon - Kindle Voyage - 4GB - Wi-Fi + 3G - Black'),(10,'Fire HD 8 Tablet with Alexa 8 HD Display 16 GB Tangerine - with Special Offers'),(11,'Amazon Standing Protective Case for Fire HD 6 (4th Generation) - Black'),(12,'Certified Refurbished Amazon Fire TV (Previous Generation - 1st)'),(13,'Brand New Amazon Kindle Fire 16gb 7 Ips Display Tablet Wifi 16 Gb Blue'),(14,'Amazon Kindle Touch Leather Case (4th Generation - 2011 Release) Olive Green'),(15,'Fire Kids Edition Tablet 7 Display Wi-Fi 16 GB Green Kid-Proof Case'),(16,'Amazon Kindle Paperwhite - eBook reader - 4 GB - 6 monochrome Paperwhite - touchscreen - Wi-Fi - black'),(17,'Kindle Voyage E-reader 6 High-Resolution Display (300 ppi) with Adaptive Built-in Light PagePress Sensors Wi-Fi - Includes Special Offers'),(18,'Certified Refurbished Amazon Fire TV Stick (Previous Generation - 1st)'),(19,'Kindle Paperwhite'),(20,'Amazon Fire Kids Edition Tablet 7 Display Wi-Fi 16 GB Blue Kid-Proof Case - Blue'),(21,'Kindle Paperwhite E-reader - White 6 High-Resolution Display (300 ppi) with Built-in Light Wi-Fi - Includes Special Offers'),(22,'Amazon Echo and Fire TV Power Adapter'),(23,'Amazon Fire Hd 8 8in Tablet 16gb Black B018szt3bk 6th Gen (2016) Android'),(24,'Certified Refurbished Amazon Fire TV with Alexa Voice Remote'),(25,'Amazon - Fire 16GB (5th Gen 2015 Release) - Black'),(26,'Fire Tablet 7 Display Wi-Fi 8 GB - Includes Special Offers Black'),(27,'Echo (White)'),(28,'Echo (Black)'),(29,'Amazon 9W PowerFast Official OEM USB Charger and Power Adapter for Fire Tablets and Kindle eReaders'),(30,'Amazon Fire Hd 6 Standing Protective Case(4th Generation - 2014 Release) Cayenne Red'),(31,'Amazon Fire Hd 10 Tablet Wi-Fi 16 Gb Special Offers - Silver Aluminum'),(32,'Amazon - Amazon Tap Portable Bluetooth and Wi-Fi Speaker - Black'),(33,'Coconut Water Red Tea 16.5 Oz (pack of 12)'),(34,'Amazon Fire Tv'),(35,'Kindle Dx Leather Cover Black (fits 9.7 Display Latest and 2nd Generation Kindle Dxs)'),(36,'Amazon Kindle Fire 5ft USB to Micro-USB Cable (works with most Micro-USB Tablets)'),(37,'New Amazon Kindle Fire Hd 9w Powerfast Adapter Charger + Micro Usb Angle Cable');
/*!40000 ALTER TABLE `product_names` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-28 23:31:27
