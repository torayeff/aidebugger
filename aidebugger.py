import gradio as gr
import openai


class AIDebugger:
    def __init__(self) -> None:
        self.build_interface()

    def debug(self, openai_key: str, debug_prompt: str, source_code: str) -> str:
        """Debugs the source code using Open AI GPT-3 model.

        Args:
            openai_key (str): OPEN AI API KEY.
            debug_prompt (str): Prompt for debugging.
            source_code (str): Source code to debug.

        Returns:
            str: Debugging suggestions.
        """
        prompt = debug_prompt + source_code

        openai.api_key = openai_key
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            temperature=0,
            max_tokens=256,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )

        resp = response["choices"][0]["text"].strip("\n")
        return resp

    def launch(self):
        self.interface.launch()
    
    def build_interface(self):
        self.interface = gr.Interface(
            fn=self.debug,
            inputs=[
                gr.Textbox(lines=1, label="OpenAI API Key", placeholder="OPENAI_KEY"),
                gr.Textbox(
                    lines=1,
                    label="Debug prompt",
                    value="Find the bugs in the below code and suggest recommendations:",
                ),
                gr.Textbox(
                    lines=18,
                    label="Source code",
                    placeholder="Paste your source code here...",
                ),
            ],
            outputs=[gr.Textbox(lines=26, label="Debug result:")],
            allow_flagging="never",
            title="Simple AI Debugger based on OpenAI GPT-3"
        )


if __name__ == "__main__":
    aidebugger = AIDebugger()
    aidebugger.launch()
