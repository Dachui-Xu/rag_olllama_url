# 环境

```ba
python版本为3.11
```

## 安装langchain库：

因为langchain很大，可以根据需要安装，例如：

```bash
pip install langchain[ollama]
```

## 下载安装Ollama

[Ollama](https://ollama.com/)

利用Ollama拉取llama2模型。

```bash
ollama run llama2
```

# 运行以及测试

## basic

basic.py是核心方法的测试模块，直接运行即可:

```bash
python basic.py
```

每次回答结果会有些不同，但格式都为1—5条的格式阐述：

```bash
Of course! Here are five interesting facts about Roman history:

1. The Roman Empire was the largest empire in the world at its peak, covering an area of approximately 5.9 million square miles and spanning three continents.
2. The Roman language, Latin, is still widely studied today and has influenced many modern languages, including English. In fact, around 20% of all English words are derived from Latin.
3. Ancient Rome was a republic before it became an empire. The Roman Republic lasted for over 400 years, during which time the government was run by elected officials and citizens had the right to vote.
4. The Roman Colosseum, also known as the Flavian Amphitheatre, was completed in 80 AD and could hold up to 50,000 spectators. It was used for gladiatorial contests, animal hunts, and other public events.
5. Julius Caesar was assassinated on the Ides of March (March 15) in 44 BC by a group of senators who were afraid he was becoming too powerful. This event marked the end of the Roman Republic and the beginning of the Roman Empire under Caesar's adopted son, Octavian (later known as Augustus).

I hope you find these facts interesting! Is there anything else you would like to know about Roman history?
```

## basic_chain

basic_chain.py可以进行提问，并按照简体中文回答，但因为本人是用轻薄本测试，算力不太行，会出现中英杂糅的现象，本例的回答都采用文章的格式：

```bash
您想要写什么话题的文章？
        卖火箭的小女孩
C:\Users\woo~\AppData\Roaming\Python\Python311\site-packages\langchain_core\_api\deprecation.py:117: LangChainDeprecationWarning: The function `run` was deprecated in LangChain 0.1.0 and will be removed in 0.2.0. Use invoke instead.
  warn_deprecated(

 Title: 小女孩烧火箭：成就自己的梦想

 Introduction:

在我们小时候，有许多人喜欢玩烧火箭。但是，只有一些幸运的人能够真正实现自己的梦想。当我们发现了这个小女孩时，我们就意识到她的成功 Story 非常有趣。

 Body:

小女孩叫做李华，她生活在一个中等大小的城市，家庭 Background 是一个中等收入家庭。从小就喜欢玩烧火箭，但是不一定有机会。直到她13岁的时候，她的父母送她去了一个烧火箭的夏令营。在那里，她遇到了一些具有才华和毅力的人，他们告诉她，只要努力学习和坚持功，她也可以实现自己的梦想。

从那个时候起，李华开始了她的努力和坚持。她不仅学习烧火箭的技术，还学习了一些关于烧火箭的知识，包括烧火箭的历史、科学原理和安全标准等。她不断地提高自己的技能和知识，并在每个阶段都取得了进展。

结果：

李华的努力和坚持 finalmente paid off. When she was 16 years old, she successfully launched her own rocket and became the youngest person in the world to do so at that time. Her achievement not only surprised her parents but also inspired many other young people around the world.

Conclusion:

小女孩的成功 Story 证明了，如果你有梦想和坚持的心理，就可以实现自己的目标。不管你在哪里出生，享有什么 Background，只要努力学习和坚持功夫，你也能像小女孩一样实现自己的梦想。
```

内容明显编的逻辑不流畅，但内容还是挺正能量的。

对比下ChatGPT:

```bash
《星梦启航：卖火箭的小女孩》
在一个遥远的小村庄里，住着一个名叫艾米的小女孩。艾米的父亲是一个退役的火箭工程师，家里堆满了各种各样的火箭模型和太空器件。虽然艾米的家很穷，但她的心中充满了对太空的梦想和好奇。

艾米的父亲教她制作简单的小火箭，并讲述太空的奇妙故事。艾米渐渐地被这些故事吸引，梦想着有一天能将这些美妙的火箭带给更多的人。

有一天，艾米得到了一个想法。她决定在村庄的年度节日上设置一个小摊位，卖她和父亲制作的小火箭。她用彩纸和油漆装饰这些火箭，使它们看起来五彩缤纷、光彩夺目。

节日来临了，艾米的摊位前挤满了好奇的村民和孩子们。她热情地向他们展示如何启动小火箭，每当一枚小火箭嗖的一声飞上天空，人群中就会爆发出阵阵惊叹和掌声。

艾米的小火箭不仅仅是玩具，她在每枚火箭中都附上了一张小纸条，上面写着关于太空的知识和她的梦想。孩子们被这些神奇的小火箭深深吸引，而大人们则被艾米的智慧和热情所感动。

就这样，艾米不仅卖出了所有的火箭，还在村里点燃了对太空探索的热情。她的小摊位变成了一个交流梦想和启发想象的小天地。

从那以后，艾米被人们亲切地称为“卖火箭的小女孩”。她的故事激励着村里的孩子们追逐自己的梦想，无论它们看起来多么遥不可及。而艾米本人，也在每天夜晚仰望星空时，更加坚信了自己有朝一日成为一名真正的太空人的梦想。
```

## rag

rag.py可以用于分析网页中的内容，并用大模型分析并进行输出。

> RAG代表的是“检索式生成器”(Retrieval-Augmented Generation)，这是一个结合了信息检索和文本生成的自然语言处理技术。在RAG体系结构中，首先使用一个检索组件（通常是一个大规模的文档数据库或知识库）来查找与输入问题相关的信息或文档。然后，这些检索到的文档被送入一个生成组件，通常是一个预训练的语言模型，如GPT或BART。这个生成组件利用检索到的文档中的信息来生成回答或其他相关文本。
>
> RAG结合了检索和生成两种策略的优点：检索部分提供了相关的、事实性的信息，帮助确保生成的文本准确无误；而生成部分则提供了流畅性和灵活性，使输出更自然、更符合人类语言习惯。这种方法特别适合于需要大量专业知识或事实信息的应用场景，如问答、文章写作或内容创作等。

运行格式:

```bash
python rag.py --url https:\\example.com
```

[测试内容](./test/ragTest.md)