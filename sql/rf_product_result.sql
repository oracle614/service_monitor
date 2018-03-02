/*
Navicat MySQL Data Transfer

Source Server         : 测试环境_自建机房_admin
Source Server Version : 50081
Source Host           : test.mysql.apitops.com:4310
Source Database       : topsqa_rf_monitor

Target Server Type    : MYSQL
Target Server Version : 50081
File Encoding         : 65001

Date: 2017-07-05 16:13:39
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for rf_product_result
-- ----------------------------
DROP TABLE IF EXISTS `rf_product_result`;
CREATE TABLE `rf_product_result` (
  `result_id` int(10) NOT NULL AUTO_INCREMENT COMMENT '结果id',
  `tc_id` int(10) DEFAULT NULL,
  `product_id` int(10) NOT NULL COMMENT '项目ID',
  `passed_count` int(10) DEFAULT '0' COMMENT '通过次数',
  `failed_count` int(10) DEFAULT '0' COMMENT '失败次数',
  `date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '日期',
  `sys_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`result_id`)
) ENGINE=InnoDB AUTO_INCREMENT=118 DEFAULT CHARSET=utf8 COMMENT='记录自动化测试结果';
