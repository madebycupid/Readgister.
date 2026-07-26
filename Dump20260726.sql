-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: localhost    Database: readgister
-- ------------------------------------------------------
-- Server version	9.4.0

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
-- Table structure for table `admin_acc`
--

DROP TABLE IF EXISTS `admin_acc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_acc` (
  `id_admin` int NOT NULL AUTO_INCREMENT,
  `name_admin` varchar(255) DEFAULT NULL,
  `user_admin` varchar(45) DEFAULT NULL,
  `email_admin` varchar(255) DEFAULT NULL,
  `phone_admin` varchar(25) DEFAULT NULL,
  `pass_admin` varchar(255) DEFAULT NULL,
  `profile_admin` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_admin`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_acc`
--

LOCK TABLES `admin_acc` WRITE;
/*!40000 ALTER TABLE `admin_acc` DISABLE KEYS */;
INSERT INTO `admin_acc` VALUES (1,'Charlie','ikuyuk','charliebalsomo@gmail.com','0','ilovebread',NULL);
/*!40000 ALTER TABLE `admin_acc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_list`
--

DROP TABLE IF EXISTS `book_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_list` (
  `id_book` int NOT NULL AUTO_INCREMENT,
  `title_book` varchar(255) DEFAULT NULL,
  `author_book` varchar(455) DEFAULT NULL,
  `year_book` varchar(255) DEFAULT NULL,
  `desc_book` varchar(999) DEFAULT NULL,
  `quantity_book` int DEFAULT NULL,
  `course_book` varchar(255) DEFAULT NULL,
  `status_book` enum('available','unavailable') DEFAULT NULL,
  `photo_book` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_book`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_list`
--

LOCK TABLES `book_list` WRITE;
/*!40000 ALTER TABLE `book_list` DISABLE KEYS */;
INSERT INTO `book_list` VALUES (11,'An Introduction to Data Structures and Algorithms','James A. Storer','2020','ok',1,'BSIT','available','profile_p/data_structures.png'),(13,'Introduction to Computing','ikuyuk','2018','okay',2,'BSIT','available','profile_p/introduction_to_computing.png'),(16,'Accounting Information Systems','James A. Hall','2019','Description',1,'BSAIS','available','profile_p/BSAIS_Accounting_Information.png'),(17,'Introduction to Surveying','Koos Landman, Terry Hunter & Jay Jackson','2012','=',4,'BSCE','available','profile_p/BSCE_Introduction_to_Surveying.jpg'),(18,'Geotechnical Engineering','N. Sivakugan & Braja M. Das','2010','=',1,'BSCE','available','profile_p/BSCE_Geotechnical_Engineering.jpg'),(19,'Introduction to Criminology','Balsomo','2023','~~~~',3,'BSCRIM','available','profile_p/BSCRIM_IntroToCrim.jpg'),(20,'General Education Essentials','Paul Hanstedt','2021','~~~~',3,'BSED','available','profile_p/BSED_General_Education_Essentials.jpg'),(21,'Database Management Systems','Sotirios Zygiaris','2019','Hello',3,'BSIT','available','profile_p/BSIT_DBMS.png'),(27,'Fundamental Of Accounting V2','Patricia M. Empleo','2023','HI',5,'BSAIS','available','profile_p/BSAIS_Foundational.jpeg'),(28,'Fundamental Of Business Analytics ','R N Prasad, Seema Acharya','2000','HI',5,'BSBA','available','profile_p/BSAIS_Fundamentals_of_Business_Analytics.jpg'),(29,'Inside The Criminal Mind','Stanton E. Samenow, P h. D.','2005','HI',5,'BSCRIM','available','profile_p/BSCRIM_InsideTheCriminal.jpg'),(30,'Basics Of MicroEconomics','Francis B. Banaag','2006','Hi',5,'BSBA','available','profile_p/BSBA_BasicOfMicro.png'),(31,'Operations Management ','Jay Heizer, Barry Render, Chuck Munson','2010','Hi',5,'BSBA','available','profile_p/BSBA_OperationManagement.png'),(32,'Introduction to Structural Analysis&Design ','S. D. Rajan','2009','HI',5,'BSCE','available','profile_p/BSCE_Introduction_to_Structural.jpg'),(33,'The Revised Penal Code ','Arthur L. Abudiedte','1990','HI',5,'BSCRIM','available','profile_p/BSCRIM_TheRevised.jpg'),(34,'Innovation In Professional Education ','David A. Kolb','2000','Hi',5,'BSED','available','profile_p/BSED_Innovation_in_Professional.jpg'),(35,'Language Culture And Society','James Stanlaw','2020','hi hi',4,'BSED','available','profile_p/BSED_Language_Culture.jpg'),(36,'Management In The Hospatily Industry ','Tom Powers ','2019','Hi',4,'BSHM','available','profile_p/BSHM_IntroToManagement.jpg'),(37,'Managing Front Office Operation ','Micheal L. Kasavana','2011','hi',5,'BSHM','available','profile_p/BSHM_ManagingFrontOfficeOperations.jpg'),(38,'The Heart Of Hospitaly ','Micah Solomon','2006','Hi',5,'BSHM','available','profile_p/BSHM_TheHeartOfHospitality.jpg'),(39,'Anatomy And Physiology','Paulo Manuel l. Macapagal','2013','HI',5,'BSN','available','profile_p/BSN_Anatomy&Physiology.png'),(40,'Community And Public Health Nursing Evidence for Practice ','Carl Johnson ','2006','Hi',5,'BSN','available','profile_p/BSN_Community&PH.png'),(44,'Fundamentals of Nursing','Audrey','2019','description jdsadasasda',1,'BSN','available','profile_p/BSN_Fundamentals.png');
/*!40000 ALTER TABLE `book_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sensor_data`
--

DROP TABLE IF EXISTS `sensor_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sensor_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `soil_moisture` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensor_data`
--

LOCK TABLES `sensor_data` WRITE;
/*!40000 ALTER TABLE `sensor_data` DISABLE KEYS */;
/*!40000 ALTER TABLE `sensor_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_acc`
--

DROP TABLE IF EXISTS `staff_acc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff_acc` (
  `id_staff` int NOT NULL AUTO_INCREMENT,
  `name_staff` varchar(45) DEFAULT NULL,
  `email_staff` varchar(255) DEFAULT NULL,
  `phone_staff` varchar(25) DEFAULT NULL,
  `pass_staff` varchar(255) DEFAULT NULL,
  `status_staff` enum('pending','approved','rejected') DEFAULT 'pending',
  `profile_staff` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_staff`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_acc`
--

LOCK TABLES `staff_acc` WRITE;
/*!40000 ALTER TABLE `staff_acc` DISABLE KEYS */;
INSERT INTO `staff_acc` VALUES (1,'Princess','Mistood@gmail.com','09926307641','12345','approved','profile_p/princesa.jpeg'),(2,'Carl Klient','crlcapanas@gmail.com','0','12345','rejected',''),(3,'Charlie','charliebalsomo@gmail.com','0','ilovebread','pending',''),(13,'apple','apple@gmail.com',NULL,'12345','approved',NULL);
/*!40000 ALTER TABLE `staff_acc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_list`
--

DROP TABLE IF EXISTS `student_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_list` (
  `id_student` int NOT NULL AUTO_INCREMENT,
  `namelast_student` varchar(255) DEFAULT NULL,
  `namefirst_student` varchar(255) DEFAULT NULL,
  `course_student` varchar(255) DEFAULT NULL,
  `email_student` varchar(255) DEFAULT NULL,
  `phone_no` bigint DEFAULT NULL,
  `date_borrow` varchar(255) DEFAULT NULL,
  `return_borrow` varchar(255) DEFAULT NULL,
  `book_borrow` varchar(255) DEFAULT NULL,
  `status_borrow` varchar(20) DEFAULT 'Borrowed',
  PRIMARY KEY (`id_student`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_list`
--

LOCK TABLES `student_list` WRITE;
/*!40000 ALTER TABLE `student_list` DISABLE KEYS */;
INSERT INTO `student_list` VALUES (19,'Balsomo','Charlie','BSAIS','@gmail.com',9,'2025-10-26','2025-10-29','Accounting Information Systems','Borrowed'),(25,'Nequia','Ann Margret','BSAIS','@gmail.com',9,'2025-10-27','2025-10-29','Introduction to Surveying','Borrowed'),(27,'CAPANAS','CARL','BSIT','ccrlcapanas@gmail.com',999534736434,'2025-10-27','2025-10-29','Accounting Information Systems','Borrowed');
/*!40000 ALTER TABLE `student_list` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-07-26 20:42:14
