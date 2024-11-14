import os
import dspy

def get_lm_provider(provider="openai"):
    providers = {
        "openai": dspy.LM(
            model="openai/gpt-4o-mini",
            provider="openai",
            api_key=os.getenv("OPENAI_API_KEY")
        ),
        "xai": dspy.LM(
            model="xai/grok-beta",
            provider="xai", 
            api_base="https://api.x.ai/v1",
            api_key=os.getenv("XAI_API_KEY")
        )
    }
    return providers.get(provider)

lm = get_lm_provider(provider="openai")

dspy.configure(lm=lm)