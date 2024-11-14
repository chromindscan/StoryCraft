import os
import dspy

lm = dspy.LM(
    model="xai/grok-beta",
    provider="xai", 
    api_base="https://api.x.ai/v1",
    api_key=os.getenv("XAI_API_KEY")
)
dspy.configure(lm=lm)