import json
import os

import runpod
from llama_cpp import Llama

#TEST
#os.environ["LLAMA_ARGS"] = '{"model_path": "./models/openhermes-2.5-neural-chat-7b-v3-1-7b.Q4_K_M.gguf", "n_gpu_layers": -1, "n_ctx": 28000, "max_tokens": 8000, "temperature": 0.2, "stream": "true"}'

args = json.loads(os.environ.get("LLAMA_ARGS", "{}"))
llm = Llama(**args)

def handler(event):
    inp = event["input"]    
    return llm(**inp)

runpod.serverless.start({
    "handler": handler,
    "return_aggregate_stream": True
})