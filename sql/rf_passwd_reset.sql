/*
Navicat MySQL Data Transfer

Source Server         : 测试环境_自建机房_admin
Source Server Version : 50081
Source Host           : test.mysql.apitops.com:4310
Source Database       : topsqa_rf_monitor

Target Server Type    : MYSQL
Target Server Version : 50081
File Encoding         : 65001

Date: 2017-07-05 16:13:13
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for rf_passwd_reset
-- ----------------------------
DROP TABLE IF EXISTS `rf_passwd_reset`;
CREATE TABLE `rf_passwd_reset` (
  `phone` varchar(32) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL,
  `keyid` varchar(32) DEFAULT NULL,
  `sys_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='jenkins线上密码修改记录';
