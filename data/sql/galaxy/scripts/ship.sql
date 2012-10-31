-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.1.63-community - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL version:             7.0.0.4053
-- Date/time:                    2012-10-14 17:59:00
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;

-- Dumping structure for table galaxy.ship
DROP TABLE IF EXISTS `ship`;
CREATE TABLE IF NOT EXISTS `ship` (
  `id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `FK_FA30EB24BF396750` FOREIGN KEY (`id`) REFERENCES `object` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table galaxy.ship: ~0 rows (approximately)
/*!40000 ALTER TABLE `ship` DISABLE KEYS */;
/*!40000 ALTER TABLE `ship` ENABLE KEYS */;
/*!40014 SET FOREIGN_KEY_CHECKS=1 */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
