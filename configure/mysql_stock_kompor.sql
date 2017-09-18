/*
Navicat MySQL Data Transfer

Source Server         : 192.168.199.136
Source Server Version : 50637
Source Host           : 192.168.199.136:3306
Source Database       : stock_kompor

Target Server Type    : MYSQL
Target Server Version : 50637
File Encoding         : 65001

Date: 2017-09-18 18:34:37
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for 10jqka_hs_00_bar
-- ----------------------------
DROP TABLE IF EXISTS `10jqka_hs_00_bar`;
CREATE TABLE `10jqka_hs_00_bar` (
  `code` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `type` varchar(16) DEFAULT NULL,
  `open` double DEFAULT NULL,
  `high` double DEFAULT NULL,
  `low` double DEFAULT NULL,
  `close` double DEFAULT NULL,
  `vol` double DEFAULT NULL,
  `val_01` varchar(255) DEFAULT NULL,
  `val_02` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`code`,`date`),
  CONSTRAINT `10jqka_hs_00_bar_ibfk_1` FOREIGN KEY (`code`) REFERENCES `stock_basic_from_10jqka` (`symbol`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for 10jqka_hs_01_bar
-- ----------------------------
DROP TABLE IF EXISTS `10jqka_hs_01_bar`;
CREATE TABLE `10jqka_hs_01_bar` (
  `code` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `type` varchar(16) DEFAULT NULL,
  `open` double DEFAULT NULL,
  `high` double DEFAULT NULL,
  `low` double DEFAULT NULL,
  `close` double DEFAULT NULL,
  `vol` double DEFAULT NULL,
  `val_01` varchar(255) DEFAULT NULL,
  `val_02` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`code`,`date`),
  CONSTRAINT `10jqka_hs_01_bar_ibfk_1` FOREIGN KEY (`code`) REFERENCES `stock_basic_from_10jqka` (`symbol`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for 10jqka_usa_00_bar
-- ----------------------------
DROP TABLE IF EXISTS `10jqka_usa_00_bar`;
CREATE TABLE `10jqka_usa_00_bar` (
  `code` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `type` varchar(16) DEFAULT NULL,
  `open` double DEFAULT NULL,
  `high` double DEFAULT NULL,
  `low` double DEFAULT NULL,
  `close` double DEFAULT NULL,
  `vol` double DEFAULT NULL,
  `val_01` varchar(255) DEFAULT NULL,
  `val_02` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`code`,`date`),
  CONSTRAINT `10jqka_usa_00_bar_ibfk_1` FOREIGN KEY (`code`) REFERENCES `stock_basic_from_10jqka` (`symbol`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for 10jqka_usa_01_bar
-- ----------------------------
DROP TABLE IF EXISTS `10jqka_usa_01_bar`;
CREATE TABLE `10jqka_usa_01_bar` (
  `code` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `type` varchar(16) DEFAULT NULL,
  `open` double DEFAULT NULL,
  `high` double DEFAULT NULL,
  `low` double DEFAULT NULL,
  `close` double DEFAULT NULL,
  `vol` double DEFAULT NULL,
  `val_01` varchar(255) DEFAULT NULL,
  `val_02` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`code`,`date`),
  CONSTRAINT `10jqka_usa_01_bar_ibfk_1` FOREIGN KEY (`code`) REFERENCES `stock_basic_from_10jqka` (`symbol`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for diff_hs_bar
-- ----------------------------
DROP TABLE IF EXISTS `diff_hs_bar`;
CREATE TABLE `diff_hs_bar` (
  `code` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `open` double DEFAULT NULL,
  `high` double DEFAULT NULL,
  `low` double DEFAULT NULL,
  `close` double DEFAULT NULL,
  `vol` double DEFAULT NULL,
  `adj_open` double DEFAULT NULL,
  `adj_high` double DEFAULT NULL,
  `adj_low` double DEFAULT NULL,
  `adj_close` double DEFAULT NULL,
  `adj_vol` double DEFAULT NULL,
  PRIMARY KEY (`code`,`date`),
  CONSTRAINT `diff_hs_bar_ibfk_1` FOREIGN KEY (`code`) REFERENCES `stock_basic_from_10jqka` (`symbol`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for diff_usa_bar
-- ----------------------------
DROP TABLE IF EXISTS `diff_usa_bar`;
CREATE TABLE `diff_usa_bar` (
  `code` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `open` double DEFAULT NULL,
  `high` double DEFAULT NULL,
  `low` double DEFAULT NULL,
  `close` double DEFAULT NULL,
  `vol` double DEFAULT NULL,
  `adj_open` double DEFAULT NULL,
  `adj_high` double DEFAULT NULL,
  `adj_low` double DEFAULT NULL,
  `adj_close` double DEFAULT NULL,
  `adj_vol` double DEFAULT NULL,
  PRIMARY KEY (`code`,`date`),
  CONSTRAINT `diff_usa_bar_ibfk_1` FOREIGN KEY (`code`) REFERENCES `stock_basic_from_10jqka` (`symbol`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for diff_variance_hs_bar
-- ----------------------------
DROP TABLE IF EXISTS `diff_variance_hs_bar`;
CREATE TABLE `diff_variance_hs_bar` (
  `code` varchar(255) NOT NULL,
  `year` year(4) NOT NULL,
  `open` double DEFAULT NULL,
  `high` double DEFAULT NULL,
  `low` double DEFAULT NULL,
  `close` double DEFAULT NULL,
  `vol` double DEFAULT NULL,
  `adj_open` double DEFAULT NULL,
  `adj_high` double DEFAULT NULL,
  `adj_low` double DEFAULT NULL,
  `adj_close` double DEFAULT NULL,
  `adj_vol` double DEFAULT NULL,
  PRIMARY KEY (`code`,`year`),
  CONSTRAINT `diff_variance_hs_bar_ibfk_1` FOREIGN KEY (`code`) REFERENCES `stock_basic_from_10jqka` (`symbol`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for diff_variance_usa_bar
-- ----------------------------
DROP TABLE IF EXISTS `diff_variance_usa_bar`;
CREATE TABLE `diff_variance_usa_bar` (
  `code` varchar(255) NOT NULL,
  `year` year(4) NOT NULL,
  `open` double DEFAULT NULL,
  `high` double DEFAULT NULL,
  `low` double DEFAULT NULL,
  `close` double DEFAULT NULL,
  `vol` double DEFAULT NULL,
  `adj_open` double DEFAULT NULL,
  `adj_high` double DEFAULT NULL,
  `adj_low` double DEFAULT NULL,
  `adj_close` double DEFAULT NULL,
  `adj_vol` double DEFAULT NULL,
  PRIMARY KEY (`code`,`year`),
  CONSTRAINT `diff_variance_usa_bar_ibfk_1` FOREIGN KEY (`code`) REFERENCES `stock_basic_from_10jqka` (`symbol`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for quote_hs_bar
-- ----------------------------
DROP TABLE IF EXISTS `quote_hs_bar`;
CREATE TABLE `quote_hs_bar` (
  `code` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `open` double DEFAULT NULL,
  `high` double DEFAULT NULL,
  `low` double DEFAULT NULL,
  `close` double DEFAULT NULL,
  `vol` double DEFAULT NULL,
  `adj_open` double DEFAULT NULL,
  `adj_high` double DEFAULT NULL,
  `adj_low` double DEFAULT NULL,
  `adj_close` double DEFAULT NULL,
  `adj_vol` double DEFAULT NULL,
  PRIMARY KEY (`code`,`date`),
  CONSTRAINT `quote_hs_bar_ibfk_1` FOREIGN KEY (`code`) REFERENCES `stock_basic_from_10jqka` (`symbol`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for quote_usa_bar
-- ----------------------------
DROP TABLE IF EXISTS `quote_usa_bar`;
CREATE TABLE `quote_usa_bar` (
  `code` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `open` double DEFAULT NULL,
  `high` double DEFAULT NULL,
  `low` double DEFAULT NULL,
  `close` double DEFAULT NULL,
  `vol` double DEFAULT NULL,
  `adj_open` double DEFAULT NULL,
  `adj_high` double DEFAULT NULL,
  `adj_low` double DEFAULT NULL,
  `adj_close` double DEFAULT NULL,
  `adj_vol` double DEFAULT NULL,
  PRIMARY KEY (`code`,`date`),
  CONSTRAINT `quote_usa_bar_ibfk_1` FOREIGN KEY (`code`) REFERENCES `stock_basic_from_10jqka` (`symbol`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for stock_basic_from_10jqka
-- ----------------------------
DROP TABLE IF EXISTS `stock_basic_from_10jqka`;
CREATE TABLE `stock_basic_from_10jqka` (
  `symbol` varchar(255) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `type` enum('hs','usa') DEFAULT NULL,
  `effective` enum('T','F') DEFAULT NULL,
  `rt` varchar(255) DEFAULT NULL,
  `start` varchar(64) DEFAULT NULL,
  `year` varchar(512) CHARACTER SET utf8 DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- View structure for 10jqka_hs_bar
-- ----------------------------
DROP VIEW IF EXISTS `10jqka_hs_bar`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `10jqka_hs_bar` AS select `10jqka_hs_00_bar`.`code` AS `code`,`10jqka_hs_00_bar`.`date` AS `date`,`10jqka_hs_00_bar`.`open` AS `open`,`10jqka_hs_00_bar`.`high` AS `high`,`10jqka_hs_00_bar`.`low` AS `low`,`10jqka_hs_00_bar`.`close` AS `close`,`10jqka_hs_00_bar`.`vol` AS `vol`,`10jqka_hs_01_bar`.`open` AS `adj_open`,`10jqka_hs_01_bar`.`high` AS `adj_high`,`10jqka_hs_01_bar`.`low` AS `adj_low`,`10jqka_hs_01_bar`.`close` AS `adj_close`,`10jqka_hs_01_bar`.`vol` AS `adj_vol` from (`10jqka_hs_00_bar` join `10jqka_hs_01_bar`) where ((`10jqka_hs_00_bar`.`code` = `10jqka_hs_01_bar`.`code`) and (`10jqka_hs_00_bar`.`date` = `10jqka_hs_01_bar`.`date`)) ;

-- ----------------------------
-- View structure for 10jqka_usa_bar
-- ----------------------------
DROP VIEW IF EXISTS `10jqka_usa_bar`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `10jqka_usa_bar` AS select `10jqka_usa_00_bar`.`code` AS `code`,`10jqka_usa_00_bar`.`date` AS `date`,`10jqka_usa_00_bar`.`open` AS `open`,`10jqka_usa_00_bar`.`high` AS `high`,`10jqka_usa_00_bar`.`low` AS `low`,`10jqka_usa_00_bar`.`close` AS `close`,`10jqka_usa_00_bar`.`vol` AS `vol`,`10jqka_usa_01_bar`.`open` AS `adj_open`,`10jqka_usa_01_bar`.`high` AS `adj_high`,`10jqka_usa_01_bar`.`low` AS `adj_low`,`10jqka_usa_01_bar`.`close` AS `adj_close`,`10jqka_usa_01_bar`.`vol` AS `adj_vol` from (`10jqka_usa_00_bar` join `10jqka_usa_01_bar`) where ((`10jqka_usa_00_bar`.`code` = `10jqka_usa_01_bar`.`code`) and (`10jqka_usa_00_bar`.`date` = `10jqka_usa_01_bar`.`date`)) ;

-- ----------------------------
-- View structure for view_all_code
-- ----------------------------
DROP VIEW IF EXISTS `view_all_code`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `view_all_code` AS select `stock_kompor`.`code`.`code` AS `code`,`stock_kompor`.`code`.`name` AS `name`,`stock_kompor`.`code`.`type` AS `type` from `code` ;

-- ----------------------------
-- View structure for view_hs_all_bar
-- ----------------------------
DROP VIEW IF EXISTS `view_hs_all_bar`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `view_hs_all_bar` AS select `qu`.`code` AS `code`,`qu`.`date` AS `date`,`qu`.`open` AS `qu_open`,`qu`.`high` AS `qu_high`,`qu`.`low` AS `qu_low`,`qu`.`close` AS `qu_close`,`qu`.`vol` AS `qu_vol`,`qu`.`adj_open` AS `qu_adj_open`,`qu`.`adj_high` AS `qu_adj_high`,`qu`.`adj_low` AS `qu_adj_low`,`qu`.`adj_close` AS `qu_adj_close`,`qu`.`adj_vol` AS `qu_adj_vol`,`jq`.`open` AS `jq_open`,`jq`.`high` AS `jq_high`,`jq`.`low` AS `jq_low`,`jq`.`close` AS `jq_close`,`jq`.`vol` AS `jq_vol`,`jq`.`adj_open` AS `jq_adj_open`,`jq`.`adj_high` AS `jq_adj_high`,`jq`.`adj_low` AS `jq_adj_low`,`jq`.`adj_close` AS `jq_adj_close`,`jq`.`adj_vol` AS `jq_adj_vol` from (`quote_hs_bar` `qu` join `10jqka_hs_bar` `jq`) where ((`qu`.`code` = `jq`.`code`) and (`qu`.`date` = `jq`.`date`)) ;

-- ----------------------------
-- View structure for view_usa_all_bar
-- ----------------------------
DROP VIEW IF EXISTS `view_usa_all_bar`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `view_usa_all_bar` AS select `qu`.`code` AS `code`,`qu`.`date` AS `date`,`qu`.`open` AS `qu_open`,`qu`.`high` AS `qu_high`,`qu`.`low` AS `qu_low`,`qu`.`close` AS `qu_close`,`qu`.`vol` AS `qu_vol`,`qu`.`adj_open` AS `qu_adj_open`,`qu`.`adj_high` AS `qu_adj_high`,`qu`.`adj_low` AS `qu_adj_low`,`qu`.`adj_close` AS `qu_adj_close`,`qu`.`adj_vol` AS `qu_adj_vol`,`jq`.`open` AS `jq_open`,`jq`.`high` AS `jq_high`,`jq`.`low` AS `jq_low`,`jq`.`close` AS `jq_close`,`jq`.`vol` AS `jq_vol`,`jq`.`adj_open` AS `jq_adj_open`,`jq`.`adj_high` AS `jq_adj_high`,`jq`.`adj_low` AS `jq_adj_low`,`jq`.`adj_close` AS `jq_adj_close`,`jq`.`adj_vol` AS `jq_adj_vol` from (`quote_usa_bar` `qu` join `10jqka_usa_bar` `jq`) where ((`qu`.`code` = `jq`.`code`) and (`qu`.`date` = `jq`.`date`)) ;
SET FOREIGN_KEY_CHECKS=1;
