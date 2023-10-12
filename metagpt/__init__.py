#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 22:26
# @Author  : alexanderwu
# @File    : __init__.py

from metagpt import _compat as _  # noqa: F401
import openai
from agentops import Client

ao_client = Client(api_key="<API KEY GOES HERE>",
                   tags=['MetaGPT', '2048'])
