# 导入必要的模块
import argparse  # 用于解析命令行参数

# 导入用于加载和处理网页文档的模块
from langchain.document_loaders import WebBaseLoader  # 用于从网页加载文档
from langchain.text_splitter import RecursiveCharacterTextSplitter  # 用于将文档分割为更小的片段

# 导入向量存储和嵌入处理相关的模块
from langchain.vectorstores import Chroma  # 向量存储库
from langchain.embeddings import GPT4AllEmbeddings  # GPT4All嵌入方法
from langchain.embeddings import OllamaEmbeddings  # Ollama嵌入方法，提供另一种嵌入选项

# 导入语言模型和回调函数管理器相关的模块
from langchain.llms import Ollama  # 语言模型
from langchain.callbacks.manager import CallbackManager  # 回调函数管理器
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler  # 输出流回调处理器


def main():
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description='提取并过滤出URL参数。')
    parser.add_argument('--url', type=str, default='https://www.baidu.com/s?wd=中国联通', required=True, help='要进行提取的URL。')

    # 解析命令行输入的参数
    args = parser.parse_args()
    url = args.url
    print(f"当前使用的URL: {url}")

    # 初始化网页加载器，并加载指定URL的内容
    loader = WebBaseLoader(url)
    data = loader.load()

    # 初始化文本分割器，并将加载的文档内容分割成小块
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=100)
    all_splits = text_splitter.split_documents(data)
    print(f"文档被分割成了 {len(all_splits)} 块")

    # 初始化向量存储，并使用分割后的文档块和嵌入模型来填充它
    vectorstore = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())

    # 输出加载的文档数量
    print(f"加载了 {len(data)} 个文档")

    # 从LangChain Hub中拉取RAG提示
    from langchain import hub
    QA_CHAIN_PROMPT = hub.pull("rlm/rag-prompt-llama")

    # 初始化语言模型，设置回调函数管理器用于处理输出
    llm = Ollama(model="llama2",
                 verbose=True,
                 callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
    print(f"加载了LLM模型：{llm.model}")

    # 设置问答链，使用从向量存储中检索的信息和LLM模型来构建答案
    from langchain.chains import RetrievalQA
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
    )

    # 提出问题并获取答案
    question = f"最新的 {url} 头条新闻是什么？"
    result = qa_chain({"query": question})

    # 打印出获取的答案
    #print(result)


if __name__ == "__main__":
    main()
