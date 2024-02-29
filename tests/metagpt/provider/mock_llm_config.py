#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/1/8 17:03
@Author  : alexanderwu
@File    : mock_llm_config.py
"""

from metagpt.configs.llm_config import LLMConfig

mock_llm_config = LLMConfig(
    llm_type="mock",
    api_key="mock_api_key",
    base_url="mock_base_url",
    app_id="mock_app_id",
    api_secret="mock_api_secret",
    domain="mock_domain",
)


mock_llm_config_proxy = LLMConfig(
    llm_type="mock",
    api_key="mock_api_key",
    base_url="mock_base_url",
    proxy="http://localhost:8080",
)


mock_llm_config_azure = LLMConfig(
    llm_type="azure",
    api_version="2023-09-01-preview",
    api_key="mock_api_key",
    base_url="mock_base_url",
    proxy="http://localhost:8080",
)


mock_llm_config_zhipu = LLMConfig(
    llm_type="zhipu",
    api_key="mock_api_key.zhipu",
    base_url="mock_base_url",
    model="mock_zhipu_model",
    proxy="http://localhost:8080",
)


mock_llm_config_spark = LLMConfig(
    api_type="spark",
    app_id="xxx",
    api_key="xxx",
    api_secret="xxx",
    domain="generalv2",
    base_url="wss://spark-api.xf-yun.com/v3.1/chat",
)

mock_llm_config_qianfan = LLMConfig(api_type="qianfan", access_key="xxx", secret_key="xxx", model="ERNIE-Bot-turbo")

mock_llm_config_dashscope = LLMConfig(api_type="dashscope", api_key="xxx", model="qwen-max")
