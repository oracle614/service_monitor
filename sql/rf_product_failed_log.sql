/*
Navicat MySQL Data Transfer

Source Server         : 测试环境_自建机房_admin
Source Server Version : 50081
Source Host           : test.mysql.apitops.com:4310
Source Database       : topsqa_rf_monitor

Target Server Type    : MYSQL
Target Server Version : 50081
File Encoding         : 65001

Date: 2017-07-05 16:13:32
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for rf_product_failed_log
-- ----------------------------
DROP TABLE IF EXISTS `rf_product_failed_log`;
CREATE TABLE `rf_product_failed_log` (
  `log_id` int(10) NOT NULL AUTO_INCREMENT,
  `tc_id` int(11) DEFAULT NULL COMMENT '测试用例ID',
  `tc_name` varchar(64) DEFAULT NULL COMMENT '测试用例名称',
  `result_id` int(10) NOT NULL COMMENT '结果ID',
  `failed_content` varchar(200) DEFAULT NULL COMMENT '失败信息',
  `sys_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8;
