import json
import os

import runpod
from llama_cpp import Llama

#TEST
#os.environ["LLAMA_ARGS"] = '{"model_path": "./models/openhermes-2.5-neural-chat-7b-v3-1-7b.Q4_K_M.gguf", "n_gpu_layers": -1, "n_ctx": 28000}'

args = json.loads(os.environ.get("LLAMA_ARGS", "{}"))
llm = Llama(**args)

def handler(event):
    #TEST
    #with open('test_input.json') as file:       
    #     event = json.load(file)
    
    inp = event["input"]  
    stream: bool = inp.get("stream", False)

    if stream: 
        response = llm.create_completion(**inp)
        for chunk in response:
           yield str(chunk["choices"][0]["text"])
    else:
        return llm.create_completion(**inp)
          
runpod.serverless.start({
   "handler": handler,
   "return_aggregate_stream": True
})
