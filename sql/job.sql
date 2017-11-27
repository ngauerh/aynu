/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : jobs

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2017-11-27 14:50:31
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for job
-- ----------------------------
DROP TABLE IF EXISTS `job`;
CREATE TABLE `job` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id号',
  `job_url` varchar(255) NOT NULL COMMENT '职位详情链接',
  `job_comp` varchar(50) DEFAULT NULL COMMENT '公司名',
  `job_name` varchar(50) DEFAULT NULL COMMENT '职位名',
  `job_degree` varchar(30) DEFAULT NULL COMMENT '学历',
  `job_smoney` int(6) DEFAULT NULL COMMENT '最低薪资',
  `job_emoney` int(6) DEFAULT NULL COMMENT '最高薪资',
  `job_address` varchar(255) DEFAULT NULL COMMENT '公司地址',
  `job_comp_type` varchar(255) DEFAULT '民企' COMMENT '公司类型（民营，国企）',
  `job_comp_snum` int(6) DEFAULT NULL COMMENT '公司规模（人数）',
  `job_comp_enum` int(6) DEFAULT NULL COMMENT '公司规模（人数）',
  `job_business` varchar(30) DEFAULT NULL COMMENT '公司主营',
  `job_syear` int(4) DEFAULT NULL COMMENT '工作经验',
  `job_eyear` int(4) DEFAULT NULL COMMENT '工作经验',
  `job_date_pub` varchar(20) DEFAULT NULL COMMENT '发布日期',
  `job_datetime` datetime(6) DEFAULT NULL,
  `job_welfafe` varchar(255) DEFAULT NULL COMMENT '公司福利',
  `job_people` int(4) DEFAULT '0' COMMENT '招的人数',
  `job_desc` text COMMENT '岗位职责',
  `job_request` text COMMENT '岗位要求',
  `job_tag` varchar(50) DEFAULT '0' COMMENT '职业标签',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=345298 DEFAULT CHARSET=utf8;
