
import os
import dspy

class XAILanguageModel(dspy.LM):
    def __init__(self, model, api_base, api_key):
        super().__init__(
            model=model,
            api_base=api_base,
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
            model="xai/grok-beta",
            api_base="https://api.x.ai/v1",
            api_key=os.getenv("XAI_API_KEY")
        ),
        "chromindscan": dspy.LM(
            model="openai/grok-beta",
            api_base="https://api.chromindscan.com/v1",
            api_key=os.getenv("CHROMINDSCAN_API_KEY"),
            provider="chromindscan"
        )
    }
    return providers.get(provider)

lm = get_lm_provider("chromindscan")
dspy.configure(lm=lm)