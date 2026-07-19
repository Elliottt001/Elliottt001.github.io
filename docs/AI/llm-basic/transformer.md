### 第一步：输入表示（Input & Embedding）

模型的第一步是将离散的文本符号转化为计算机可以处理的连续向量。

**1. 词嵌入（Word Embedding）**
假设输入序列包含 $n$ 个词（Token），每个词被映射为一个维度为 $d_{model}$ 的向量（通常 $d_{model} = 512$）。
输入序列的矩阵表示为：


$$X \in \mathbb{R}^{n \times d_{model}}$$

**2. 位置编码（Positional Encoding）**
由于Transformer同时处理所有词（没有RNN的顺序机制），为了让模型感知词在句子中的相对或绝对位置，必须加上位置信息。Transformer使用了基于正弦和余弦函数的绝对位置编码：
对于位置 $pos$ 和维度 $i$：


$$PE_{(pos, 2i)} = \sin(pos / 10000^{2i/d_{model}})$$

$$PE_{(pos, 2i+1)} = \cos(pos / 10000^{2i/d_{model}})$$


最终进入编码器的实际输入是词嵌入与位置编码的逐元素相加：


$$X_{input} = X + PE$$

---

### 第二步：自注意力机制（Self-Attention）

这是Transformer最具革命性的数学设计。它的目的是让序列中的每一个词都能与序列中的其他所有词进行交互，计算出它们之间的关联程度。

**1. 构造 Q、K、V 矩阵**
对于输入矩阵 $X$，我们通过三个可学习的权重参数矩阵 $W^Q$, $W^K$, $W^V$ 进行线性变换，得到查询（Query）、键（Key）和值（Value）矩阵：


$$Q = X W^Q$$

$$K = X W^K$$

$$V = X W^V$$


其中，$W^Q, W^K \in \mathbb{R}^{d_{model} \times d_k}$，$W^V \in \mathbb{R}^{d_{model} \times d_v}$。

**2. 缩放点积注意力计算（Scaled Dot-Product Attention）**
注意力的数学表达式为：


$$Attention(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

这步计算的物理意义极其重要：

* **$QK^T$ (点积相似度)**：计算每一个Query和所有Key的点积。点积越大，说明两个词的向量方向越一致，相关性越强。结果是一个 $n \times n$ 的注意力得分矩阵。
* **$\frac{1}{\sqrt{d_k}}$ (缩放因子)**：当维度 $d_k$ 很大时，点积结果的方差会变得很大，导致softmax函数的梯度极小（梯度消失）。除以 $\sqrt{d_k}$ 可以将方差拉回 $1$，保持梯度稳定。
* **$\text{softmax}(\cdot)$**：将每一行的得分归一化为概率分布，所有权重相加等于 $1$。
* **$\times V$ (加权求和)**：将得到的概率分布矩阵与值矩阵 $V$ 相乘。相当于根据其他词与当前词的相关性，把所有词的信息（Value）进行加权融合。

---

### 第三步：多头注意力（Multi-Head Attention）

如果只用一组 $Q, K, V$，模型只能从一个角度关注信息。多头注意力的思想是将 $Q, K, V$ 投影到 $h$ 个不同的子空间中（通常 $h=8$），在不同的子空间独立计算注意力，最后拼接起来。

对于第 $i$ 个头：


$$head_i = Attention(QW_i^Q, KW_i^K, VW_i^V)$$


然后将所有头的输出拼接（Concat），再经过一个线性变换 $W^O$ 得到最终输出：


$$MultiHead(Q, K, V) = \text{Concat}(head_1, ..., head_h)W^O$$


这样做的数学好处是允许模型同时关注序列中不同位置、不同表示子空间的信息（例如，有的头关注语法，有的头关注主谓宾关系）。

---

### 第四步：残差连接与层归一化（Add & Norm）

在经过多头注意力层之后，Transformer为了防止深层网络中的梯度消失，引入了残差连接（Residual Connection）和层归一化（Layer Normalization）。

对于每一个子层（Sublayer，比如Attention层或前馈层），其输出公式为：


$$Output = \text{LayerNorm}(x + \text{Sublayer}(x))$$

* **$x + \text{Sublayer}(x)$**：将输入 $x$ 直接加到输出上，保证了底层特征可以直接传递到高层。
* **$\text{LayerNorm}$**：对每个样本在特征维度上进行标准化，使其均值为 $0$，方差为 $1$，加速模型收敛并提高稳定性。

---

### 第五步：前馈神经网络（Feed-Forward Network, FFN）

在Attention层提取了全局上下文信息后，需要一个非线性变换来单独处理每个位置的特征。FFN 包含两个线性变换和一个 ReLU 激活函数：


$$FFN(x) = \max(0, xW_1 + b_1)W_2 + b_2$$


这里的计算是**Position-wise**的，意味着同一个参数矩阵 $W_1, W_2$ 作用于序列中的每一个词（相当于 $1 \times 1$ 的卷积）。通常 $W_1$ 会将维度放大 $4$ 倍（如 $512 \to 2048$），$W_2$ 再将其降维回 $512$，这极大地增加了模型的非线性表达能力。

*(至此，编码器（Encoder）的单层数学过程结束，通常会堆叠 $N$ 层（如 $N=6$）。)*

---

### 第六步：解码器特有机制（Decoder Specifics）

解码器的结构与编码器类似，同样堆叠 $N$ 层，但包含两个关键的数学修改：

**1. 掩码多头注意力（Masked Multi-Head Attention）**
在生成文本时，模型是自回归的（从左到右逐个生成），因此在预测第 $t$ 个词时，不能看到 $t$ 时刻之后的词。
数学实现上，在计算 $QK^T$ 时，会加上一个掩码矩阵 $M$：


$$Attention(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}} + M\right)V$$


其中，矩阵 $M$ 是一个上三角矩阵，未来位置的元素值为 $-\infty$。这样在经过 softmax 函数后（$e^{-\infty} = 0$），未来位置的注意力权重被强制归零。

**2. 编码器-解码器注意力（Encoder-Decoder Attention）**
这是解码器如何利用原文信息的桥梁。在这个子层中：

* **Query ($Q$)**：来自解码器自身的上一层输出（代表当前正在生成的词需要什么信息）。
* **Key ($K$) 和 Value ($V$)**：来自**编码器的最终输出**（代表原文的所有信息）。
这使得解码器在生成每一个词时，都能计算出它对原文所有词的注意力权重，从而提取相关的翻译或回答内容。

---

### 第七步：输出层（Linear & Softmax）

解码器最后一层的输出是一个序列矩阵。为了得到具体的词汇，需要通过一个线性层将其映射到词表大小（Vocabulary Size）的维度：


$$Logits = X_{decoder\_output} W^{vocab}$$


最后，应用 Softmax 函数将其转化为各个词生成的概率分布：


$$P(y_t \vert{} y_{<t}, X) = \text{softmax}(Logits)$$


模型在训练阶段通过交叉熵损失（Cross-Entropy Loss）来优化所有权重矩阵，使得正确词汇的预测概率最大化。