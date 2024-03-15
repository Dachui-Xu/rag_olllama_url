# Test Result with rag.py

我是采用win轻薄本测试，没有用独显，所以推理速度慢，推理准确性也不高。

## 测试百度搜索

```bash
(AiFinance) PS C:\Users\woo~\PycharmProjects\AiTest> python .\rag.py --url https://www.baidu.com/s?wd=中国联通
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\document_loaders\__init__.py:36: LangChainDeprecationWarning: Importing document loaders from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.document_loaders import WebBaseLoader`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\vectorstores\__init__.py:35: LangChainDeprecationWarning: Importing vector stores from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.vectorstores import Chroma`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\embeddings\__init__.py:29: LangChainDeprecationWarning: Importing embeddings from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.embeddings import GPT4AllEmbeddings`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\embeddings\__init__.py:29: LangChainDeprecationWarning: Importing embeddings from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.embeddings import OllamaEmbeddings`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\llms\__init__.py:548: LangChainDeprecationWarning: Importing LLMs from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:


To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
当前使用的URL: https://www.baidu.com/s?wd=中国联通
文档被分割成了 3 块
bert_load_from_file: gguf version     = 2
bert_load_from_file: gguf alignment   = 32
bert_load_from_file: gguf data offset = 695552
bert_load_from_file: model name           = BERT
bert_load_from_file: model architecture   = bert
bert_load_from_file: model file type      = 1
bert_load_from_file: bert tokenizer vocab = 30522
加载了 1 个文档
加载了LLM模型：llama2
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain_core\_api\deprecation.py:117: LangChainDeprecationWarning: The function `__call__` was deprecated in LangChain 0.1.0 and will be removed in 0.2.0. Use invoke instead.
  warn_deprecated(
Number of requested results 4 is greater than number of elements in index 3, updating n_results = 3

中国联通2023年三季报财报：

公司名称：中国联通
股票代码：600050
年报|第三季度|中报|第一季度

下面是中国联通2023年三季度财报的主要信息：

1. 收益产生方式：利润能力改善，以及减少负面现象。
2. 营业收入：365.38亿元人民币，增长9.7%年同期。
3. 利润：104.13亿元人民币，增长13.1%年同期。
4. 资产总额：1,583.69亿元人民币。
5. 负债总额：670.27亿元人民币，负债率为40.6%。
6. 营业利用率：38.1%。
7. 资产利用率：14.5%。
8. 减值：22.3亿元人民币，减值率为60.9%。
9. 流动性评价：高、可靠性评价：中等。
10. 投资回报率：23.5%。

根据这些信息，我们可以看出中国联通2023年三季度财报的主要特点为：

1. 收益产生方式改善：中国联通通过改进其业务模式和经营管理，成功地提高了利润能力。
2. 营业收入增长：中国联通在三季度内实现了营业收入的增长，这也反映了其经营效果。
3. 利润增长明显：中国联通在2023年三季度内实现了利润的增长，这也是由于改进业务模式和经营管理而导致。
4. 资产总额增加：中国联通在2023年三季度内实现了资产总额的增加，这也反映了其经营效果。
5. 流动性评价高：中国联通在2023年三季度内实现了流动性评价的提高，这也是由于改进业务模式和经营管理而导致。

总体来说，中国联通2023年三季度财报表现出色，具有良好的收益产生方式、营业收入增长、利润增长和流动性评价等特点。

```

## 测试微博热搜

```b
(AiFinance) PS C:\Users\woo~\PycharmProjects\AiTest> python .\rag.py --url https://s.weibo.com/top/summary    
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\document_loaders\__init__.py:36: LangChainDeprecationWarning: Importing document loaders from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.document_loaders import WebBaseLoader`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\vectorstores\__init__.py:35: LangChainDeprecationWarning: Importing vector stores from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.vectorstores import Chroma`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\embeddings\__init__.py:29: LangChainDeprecationWarning: Importing embeddings from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.embeddings import GPT4AllEmbeddings`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\embeddings\__init__.py:29: LangChainDeprecationWarning: Importing embeddings from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.embeddings import OllamaEmbeddings`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\llms\__init__.py:548: LangChainDeprecationWarning: Importing LLMs from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:


To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
当前使用的URL: https://s.weibo.com/top/summary
文档被分割成了 1 块
bert_load_from_file: gguf version     = 2
bert_load_from_file: gguf alignment   = 32
bert_load_from_file: gguf data offset = 695552
bert_load_from_file: model name           = BERT
bert_load_from_file: model architecture   = bert
bert_load_from_file: model file type      = 1
bert_load_from_file: bert tokenizer vocab = 30522
加载了 1 个文档
加载了LLM模型：llama2
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain_core\_api\deprecation.py:117: LangChainDeprecationWarning: The function `__call__` was deprecated in LangChain 0.1.0 and will be removed in 0.2.0. Use invoke instead.
  warn_deprecated(
Number of requested results 4 is greater than number of elements in index 1, updating n_results = 1
 Based on the context provided, the latest news on the https://s.weibo.com/top/summary top page is not available as it is a real-time feed of updates from various sources and may not be archived or saved. Therefore, I don't know the answer to your question.

```

## 测试BBC新闻

```bash
(AiFinance) PS C:\Users\woo~\PycharmProjects\AiTest> python .\rag.py --url https://www.bbc.co.uk/         
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\document_loaders\__init__.py:36: LangChainDeprecationWarning: Importing document loaders from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.document_loaders import WebBaseLoader`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\vectorstores\__init__.py:35: LangChainDeprecationWarning: Importing vector stores from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.vectorstores import Chroma`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\embeddings\__init__.py:29: LangChainDeprecationWarning: Importing embeddings from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.embeddings import GPT4AllEmbeddings`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\embeddings\__init__.py:29: LangChainDeprecationWarning: Importing embeddings from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.embeddings import OllamaEmbeddings`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\llms\__init__.py:548: LangChainDeprecationWarning: Importing LLMs from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:
当前使用的URL: https://www.bbc.co.uk/
当前使用的URL: https://www.bbc.co.uk/
文档被分割成了 6 块
bert_load_from_file: gguf version     = 2
bert_load_from_file: gguf alignment   = 32
bert_load_from_file: gguf data offset = 695552
bert_load_from_file: model name           = BERT
bert_load_from_file: model architecture   = bert
bert_load_from_file: model file type      = 1
bert_load_from_file: bert tokenizer vocab = 30522
加载了 1 个文档
加载了LLM模型：llama2
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain_core\_api\deprecation.py:117: LangChainDeprecationWarning: The function `__call__` was deprecated in LangChain 0.1.0 and will be removed in 0.2.0. Use invoke instead.
  warn_deprecated(
The latest news on the BBC Homepage includes a story about a whistleblower found dead in the US, as well as articles on the National Lottery draws, Comic Relief, and a roundup of the top stories from around the UK. Additionally, there are video clips featuring a head teacher who saved his pupils from a knifeman, a playlist shared by Mollie King for the Comic Relief Pedal Power challenge, and a look back at the 1984 miners' strike. There are also articles on the Trump administration's Scottish golfing dream gone wrong, four famous women facing Comic Relief's coldest challenge in the Arctic, and highly acclaimed award-winning films available on BBC iPlayer.

```

## 测试澎湃新闻

原网页：[刚刚 | 记者亲赴燕郊爆炸点位！当量或为100公斤TNT！现场情况→_澎湃号·媒体_澎湃新闻-The Paper](https://www.thepaper.cn/newsDetail_forward_26673886)

网页PDF：./thepaper-燕郊.pdf

```bas
(AiFinance) PS C:\Users\woo~\PycharmProjects\AiTest> python .\rag.py --url https://www.thepaper.cn/newsDetail_forward_26673886
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\document_loaders\__init__.py:36: LangChainDeprecationWarning: Importing document loaders from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.document_loaders import WebBaseLoader`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\vectorstores\__init__.py:35: LangChainDeprecationWarning: Importing vector stores from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.vectorstores import Chroma`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\embeddings\__init__.py:29: LangChainDeprecationWarning: Importing embeddings from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.embeddings import GPT4AllEmbeddings`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\embeddings\__init__.py:29: LangChainDeprecationWarning: Importing embeddings from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.embeddings import OllamaEmbeddings`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\llms\__init__.py:548: LangChainDeprecationWarning: Importing LLMs from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.llms import Ollama`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
当前使用的URL: https://www.thepaper.cn/newsDetail_forward_26673886
文档被分割成了 4 块
bert_load_from_file: gguf version     = 2
bert_load_from_file: gguf alignment   = 32
bert_load_from_file: gguf data offset = 695552
bert_load_from_file: model name           = BERT
bert_load_from_file: model architecture   = bert
bert_load_from_file: model file type      = 1
bert_load_from_file: bert tokenizer vocab = 30522
加载了 1 个文档
加载了LLM模型：llama2
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain_core\_api\deprecation.py:117: LangChainDeprecationWarning: The function `__call__` was deprecated in LangChain 0.1.0 and will be removed in 0.2.0. Use invoke instead.
  warn_deprecated(

On March 13th, a massive explosion occurred in the North Europe residential area of Xinhe City, causing widespread damage and injuries. According to reports, the explosion occurred at around 2:00 pm local time and was heard and felt several kilometers away. The epicenter of the blast is believed to be a commercial building in the North Europe residential area, where several businesses were operating at the time of the incident.

Eyewitnesses described a massive fireball that shot out of the commercial building and exploded into a second blast, causing widespread damage to nearby buildings and infrastructure. The explosion was so powerful that it shattered windows and doors of neighboring buildings, and debris from the explosion was found scattered over a wide area.

The authorities have confirmed that 7 commercial buildings and 13 residential buildings were affected by the explosion, with many of them suffering significant damage. The blast also caused power outages in the area, leaving hundreds of residents without electricity.

The cause of the explosion is still unknown, but it is believed to be related to a gas leak. The local fire department has launched an investigation into the incident, and emergency responders have been deployed to the scene to assist with rescue and recovery efforts.

The explosion has left many residents in the area shaken and frightened, with some reporting hearing and feeling the blast from several kilometers away. The incident has also raised concerns about the safety of gas infrastructure in the city and the need for more stringent safety protocols to prevent such incidents in the future.

In conclusion, the massive explosion in Xinhe City on March 13th was a devastating event that caused widespread damage and injuries. While the cause of the explosion is still unknown, it is believed to be related to a gas leak. The incident has raised concerns about the safety of gas infrastructure in the city and the need for more stringent safety protocols to prevent such incidents in the future.
```

llama2推理出现了问题，它将河北三河市认为成了北欧的城市。

## 测试淘宝网

```bash
Finance) PS C:\Users\woo~\PycharmProjects\AiTest> python .\rag.py --url https://tb.alicdn.com/                                   
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\document_loaders\__init__.py:36: LangChainDeprecationWarning: Importing document loaders from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.document_loaders import WebBaseLoader`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\vectorstores\__init__.py:35: LangChainDeprecationWarning: Importing vector stores from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.vectorstores import Chroma`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\embeddings\__init__.py:29: LangChainDeprecationWarning: Importing embeddings from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.embeddings import GPT4AllEmbeddings`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\embeddings\__init__.py:29: LangChainDeprecationWarning: Importing embeddings from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.embeddings import OllamaEmbeddings`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain\llms\__init__.py:548: LangChainDeprecationWarning: Importing LLMs from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:

`from langchain_community.llms import Ollama`.

To install langchain-community run `pip install -U langchain-community`.
  warnings.warn(
当前使用的URL: https://tb.alicdn.com/
文档被分割成了 1 块
bert_load_from_file: gguf version     = 2
bert_load_from_file: gguf alignment   = 32
bert_load_from_file: gguf data offset = 695552
bert_load_from_file: model name           = BERT
bert_load_from_file: model architecture   = bert
bert_load_from_file: model file type      = 1
bert_load_from_file: bert tokenizer vocab = 30522
加载了 1 个文档
加载了LLM模型：llama2
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain_core\_api\deprecation.py:117: LangChainDeprecationWarning: The function `__call__` was deprecated in LangChain 0.1.0 and will be removed in 0.2.0. Use invoke instead.
  warn_deprecated(
Number of requested results 4 is greater than number of elements in index 1, updating n_results = 1
 Based on the context provided, the latest headline news on Tb.alicdn.com is "New Arrivals: Four-Piece Set of Trendy Tops and Bottoms for Women".
```

