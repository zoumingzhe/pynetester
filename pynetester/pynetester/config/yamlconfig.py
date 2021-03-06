#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
import yaml
# ----------------------------------------------------------------------------------------------------
# 类 yamlconfig
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2021-05-19 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | yamlload(...)                | 导入配置
# 已测试 | yamldump(...)                | 导出配置
# 未测试 | yamlmerge(...)               | 合并配置
# ----------------------------------------------------------------------------------------------------
class yamlconfig:
    """
    yamlconfig类。
    """
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def yamlload(config_path):
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def yamldump(config_path, cfgs):
        with open(config_path, 'w') as f:
            return yaml.safe_dump(cfgs, f)
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def yamlmerge(config1, config2):
        config = {}
        for key in config1:
            config[key] = config1[key]
        for key in config2:
            conf = config2[key]
            if key not in config:
                config[key] = conf
            # elif type(config[key]) == type(conf):
            #     config[key] = merge(config[key], conf)
            # else:
            #     print("error")
        return config
# ----------------------------------------------------------------------------------------------------
