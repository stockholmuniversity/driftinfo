-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: wordpress
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `driftinfo`
--

DROP TABLE IF EXISTS `driftinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `driftinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `big` varchar(100) DEFAULT NULL,
  `small` varchar(100) DEFAULT NULL,
  `sms` varchar(100) DEFAULT NULL,
  `reg_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `wordpress_process` tinyint(1) DEFAULT '0',
  `twitter_process` tinyint(1) DEFAULT '0',
  `sms_process` tinyint(1) DEFAULT '0',
  `rubrick` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `driftinfo`
--

LOCK TABLES `driftinfo` WRITE;
/*!40000 ALTER TABLE `driftinfo` DISABLE KEYS */;
INSERT INTO `driftinfo` VALUES (40,'hej','','on','2019-02-04 09:23:44',1,0,0,'hej'),(41,'hej','','on','2019-02-04 11:25:05',NULL,0,0,'hej');
/*!40000 ALTER TABLE `driftinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `infos`
--

DROP TABLE IF EXISTS `infos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `infos` (
  `id` int(11) NOT NULL,
  `wordpress_lista` varchar(100) DEFAULT NULL,
  `sms_lista` varchar(100) DEFAULT NULL,
  `twitter_lista` varchar(100) DEFAULT NULL,
  `driftinfo_lista` varchar(100) DEFAULT NULL,
  `wordpress` tinyint(1) DEFAULT '0',
  `sms` tinyint(1) DEFAULT '0',
  `twitter` tinyint(1) DEFAULT '0',
  `driftinfo` tinyint(1) DEFAULT '0',
  `register_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `infos`
--

LOCK TABLES `infos` WRITE;
/*!40000 ALTER TABLE `infos` DISABLE KEYS */;
/*!40000 ALTER TABLE `infos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-04  6:30:45
