/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : jobs

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2017-11-27 14:49:36
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for ip_proxy
-- ----------------------------
DROP TABLE IF EXISTS `ip_proxy`;
CREATE TABLE `ip_proxy` (
  `host` varchar(20) NOT NULL,
  `port` varchar(10) DEFAULT NULL,
  `http_type` varchar(10) DEFAULT 'HTTP',
  PRIMARY KEY (`host`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
