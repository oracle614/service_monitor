/*
Navicat MySQL Data Transfer

Source Server         : 测试环境_自建机房_admin
Source Server Version : 50081
Source Host           : test.mysql.apitops.com:4310
Source Database       : topsqa_rf_monitor

Target Server Type    : MYSQL
Target Server Version : 50081
File Encoding         : 65001

Date: 2017-07-05 16:13:25
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for rf_product
-- ----------------------------
DROP TABLE IF EXISTS `rf_product`;
CREATE TABLE `rf_product` (
  `product_id` int(10) NOT NULL AUTO_INCREMENT COMMENT '项目ID',
  `product_name` varchar(32) NOT NULL COMMENT '项目名称',
  `qa` varchar(32) DEFAULT NULL COMMENT 'QA人员',
  `product_leader` varchar(32) DEFAULT NULL COMMENT '主程',
  `sys_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
