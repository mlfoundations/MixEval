from mix_eval.models.base import BaseModel
from mix_eval.api.registry import register_model


@register_model("qwen_15_72b")
class Qwen_15_72B(BaseModel):
    def __init__(self, args):
        super().__init__(args)
        self.model_name = "Qwen/Qwen1.5-72B"
        self.attn_implementation = "flash_attention_2"  # If use default, set to None

        self.model = self.build_model()
        self.model_max_len = self.model.config.max_position_embeddings
        self.tokenizer = self.build_tokenizer()
        self.max_input_length_closeend = min(self.model_max_len, self.max_input_length) - self.closeended_max_new_tokens
