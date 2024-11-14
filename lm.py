
import os
import dspy

class XAILanguageModel(dspy.LM):
    def __init__(self, base_url, api_key):
        super().__init__(
            model="xai/grok-beta",
            api_base=base_url,
            api_key=api_key
        )

    def __call__(self, *args, **kwargs):

        kwargs.pop('response_format', None)
        return super().__call__(*args, **kwargs)

def get_lm_provider(provider="openai"):
    providers = {
        "openai": dspy.LM(
            model="openai/gpt-4o-mini",
            provider="openai",
            api_key=os.getenv("OPENAI_API_KEY")
        ),
        "xai": XAILanguageModel(
            base_url="https://api.x.ai/v1",
            api_key=os.getenv("XAI_API_KEY")
        ),
        "chromind": XAILanguageModel(
            base_url="https://api.chromind.ai/v1", 
            api_key=os.getenv("CHROMINDSCAN_API_KEY")
        )
    }
    return providers.get(provider)

lm = get_lm_provider("xai")
dspy.configure(lm=lm)