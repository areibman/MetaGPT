#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Desc   : default request & response data for provider unittest


from dashscope.api_entities.dashscope_response import (
    DashScopeAPIResponse,
    GenerationOutput,
    GenerationResponse,
    GenerationUsage,
)
from openai.types.chat.chat_completion import (
    ChatCompletion,
    ChatCompletionMessage,
    Choice,
)
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk
from openai.types.chat.chat_completion_chunk import Choice as AChoice
from openai.types.chat.chat_completion_chunk import ChoiceDelta
from openai.types.completion_usage import CompletionUsage
from qianfan.resources.typing import QfResponse

from metagpt.provider.base_llm import BaseLLM

prompt = "who are you?"
messages = [{"role": "user", "content": prompt}]

resp_cont_tmpl = "I'm {name}"
default_resp_cont = resp_cont_tmpl.format(name="GPT")


# part of whole ChatCompletion of openai like structure
def get_part_chat_completion(name: str) -> dict:
    part_chat_completion = {
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": resp_cont_tmpl.format(name=name),
                },
                "finish_reason": "stop",
            }
        ],
        "usage": {"completion_tokens": 22, "prompt_tokens": 19, "total_tokens": 41},
    }
    return part_chat_completion


def get_openai_chat_completion(name: str) -> ChatCompletion:
    openai_chat_completion = ChatCompletion(
        id="cmpl-a6652c1bb181caae8dd19ad8",
        model="xx/xxx",
        object="chat.completion",
        created=1703300855,
        choices=[
            Choice(
                finish_reason="stop",
                index=0,
                message=ChatCompletionMessage(role="assistant", content=resp_cont_tmpl.format(name=name)),
                logprobs=None,
            )
        ],
        usage=CompletionUsage(completion_tokens=110, prompt_tokens=92, total_tokens=202),
    )
    return openai_chat_completion


def get_openai_chat_completion_chunk(name: str, usage_as_dict: bool = False) -> ChatCompletionChunk:
    usage = CompletionUsage(completion_tokens=110, prompt_tokens=92, total_tokens=202)
    usage = usage if not usage_as_dict else usage.model_dump()
    openai_chat_completion_chunk = ChatCompletionChunk(
        id="cmpl-a6652c1bb181caae8dd19ad8",
        model="xx/xxx",
        object="chat.completion.chunk",
        created=1703300855,
        choices=[
            AChoice(
                delta=ChoiceDelta(role="assistant", content=resp_cont_tmpl.format(name=name)),
                finish_reason="stop",
                index=0,
                logprobs=None,
            )
        ],
        usage=usage,
    )
    return openai_chat_completion_chunk


# For gemini
gemini_messages = [{"role": "user", "parts": prompt}]


# For QianFan
qf_jsonbody_dict = {
    "id": "as-4v1h587fyv",
    "object": "chat.completion",
    "created": 1695021339,
    "result": "",
    "is_truncated": False,
    "need_clear_history": False,
    "usage": {"prompt_tokens": 7, "completion_tokens": 15, "total_tokens": 22},
}


def get_qianfan_response(name: str) -> QfResponse:
    qf_jsonbody_dict["result"] = resp_cont_tmpl.format(name=name)
    return QfResponse(code=200, body=qf_jsonbody_dict)


# For DashScope
def get_dashscope_response(name: str) -> GenerationResponse:
    return GenerationResponse.from_api_response(
        DashScopeAPIResponse(
            status_code=200,
            output=GenerationOutput(
                **{
                    "text": "",
                    "finish_reason": "",
                    "choices": [
                        {
                            "finish_reason": "stop",
                            "message": {"role": "assistant", "content": resp_cont_tmpl.format(name=name)},
                        }
                    ],
                }
            ),
            usage=GenerationUsage(**{"input_tokens": 12, "output_tokens": 98, "total_tokens": 110}),
        )
    )


# For llm general chat functions call
async def llm_general_chat_funcs_test(llm: BaseLLM, prompt: str, messages: list[dict], resp_cont: str):
    resp = await llm.aask(prompt, stream=False)
    assert resp == resp_cont

    resp = await llm.aask(prompt)
    assert resp == resp_cont

    resp = await llm.acompletion_text(messages, stream=False)
    assert resp == resp_cont

    resp = await llm.acompletion_text(messages, stream=True)
    assert resp == resp_cont
