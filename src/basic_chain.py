from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


llm = Ollama(model="llama2",
             callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
             # tempreture=0.9,
             )

from langchain.prompts import PromptTemplate


prompt = PromptTemplate(
    input_variables=["topic"],
    template="采用简体中文写一个关于 {topic} 的文章。注意，一定要采用中文，不要用英文。",
    #template="Give me 5 insterting facts about {topic}",
)

from langchain.chains import LLMChain

chain = LLMChain(llm=llm,
                 prompt=prompt,
                 verbose=False)

data = input("您想要写什么话题的文章？\n\t")

print(chain.run(data))