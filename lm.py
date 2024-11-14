
import os
import dspy

class XAILanguageModel(dspy.LM):
    def __init__(self):
        super().__init__(
            model="xai/grok-beta",
            api_base="https://api.x.ai/v1",
            api_key=os.getenv("XAI_API_KEY")
        )

    def __call__(self, *args, **kwargs):

        kwargs.pop('response_format', None)
        return super().__call__(*args, **kwargs)

lm = XAILanguageModel()
dspy.configure(lm=lm)