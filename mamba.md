| 论文                                                                                                 | 代码仓库                                                 |              源代码             |            数据集         |
| --------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | :-----------------------------------: | :----------------------------: |
| LXT: Layer-wise Relevance Propagation for Transformers                                          | [rachtibat/LRP-eXplains-Transformers][1]             |             PyTorch 实现             |         SST-2 / GLUE        |
| GlobEnc: Quantifying Global Token Attribution                                                   | [mohsenfayyaz/GlobEnc][2]                            |               PyTorch              |          GLUE 任务脚本          |
| Addressing Token Uniformity via Singular Value Transformation                                   | [hanqi-qi/tokenUni][3]                               | PyTorch / HuggingFace Transformers |     BERT 上验证，使用标准 NLP 数据    |
| TokenTune: Memory-Efficient Fine-Tuning via Token Selection                                     | [facebookresearch/tokentune][4]                      |               Python               |   HuggingFace datasets 脚本   |
| AdapLeR: Adaptive Length Reduction                                                              | [amodaresi/AdapLeR][5]                               |               PyTorch              |   QA / Text Classification  |
| Routing Transformer                                                                             | [lucidrains/routing-transformer][6]                  |               PyTorch              |    WikiText-103 / Enwik8    |
| TokenMixup: Attention-guided Token-level Mixup                                                  | [mlvlab/TokenMixup][7]                               |               PyTorch              |       CIFAR / ImageNet      |
| state-spaces / Mamba (Selective SSM 模型)                                                         | [state-spaces/mamba][8]                              |       纯 Python + CUDA kernel       | Long Range Arena / The Pile |
| NVlabs / MambaVision: 混合 Mamba-Transformer 视觉骨干网络                                               | [NVlabs/MambaVision][9]                              |               PyTorch              |        ImageNet 训练脚本        |
| 混合 / 路由 Transformer + SSM / 路径选择 的工作 (Switch Transformer)                                       | [Hugging Face Switch Transformer 文档][10]             |       transformers库中 Python实现      |     HuggingFace datasets    |
| Tracr: Compiled Transformers as a Laboratory for Interpretability                               | [Google DeepMind tracr][11]                          |            Python / JAX            |           仅内置合成数据          |
| Transformer Interpretability Beyond Attention Visualization                                     | [hila-chefer/Transformer-Explainability][12]         |               PyTorch              |       ImageNet / COCO       |
| Attention Visualizer Package: Revealing Word Importance for Encoder-Only Transformers           | [AlaFalaki/AttentionVisualizer][13]                  |         Python / Streamlit         |         仅可视化，无训练数据         |
| InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques | [NIPS 2024 Poster][14]                               |               Python               |      半合成 Transformer 数据     |
| Towards Mechanistic Interpretability of Graph Transformers via Attention Graphs                 | [batu-el/understanding-inductive-biases-of-gnns][15] |          PyTorch Geometric         |   Cora / Citeseer / PubMed  |

[1]: https://github.com/rachtibat/LRP-eXplains-Transformers "rachtibat/LRP-eXplains-Transformers: Layer-wise ..."
[2]: https://arxiv.org/abs/2205.03286 "GlobEnc: Quantifying Global Token Attribution by Incorporating the Whole Encoder Layer in Transformers"
[3]: https://arxiv.org/abs/2208.11790 "Addressing Token Uniformity in Transformers via Singular Value Transformation"
[4]: https://github.com/facebookresearch/tokentune "TokenTune: Memory-Efficient Fine-Tuning of Transformers ..."
[5]: https://arxiv.org/abs/2203.08991 "AdapLeR: Speeding up Inference by Adaptive Length Reduction"
[6]: https://github.com/lucidrains/routing-transformer "Fully featured implementation of Routing Transformer"
[7]: https://arxiv.org/abs/2210.07562 "TokenMixup: Efficient Attention-guided Token-level Data Augmentation for Transformers"
[8]: https://github.com/state-spaces/mamba "state-spaces/mamba: Mamba SSM architecture - GitHub"
[9]: https://github.com/NVlabs/MambaVision "A Hybrid Mamba-Transformer Vision Backbone - GitHub"
[10]: https://huggingface.co/docs/transformers/v4.46.0/en/model_doc/switch_transformers "SwitchTransformers"
[11]: https://arxiv.org/pdf/2301.05062 "Tracr: Compiled Transformers as a Laboratory for ..."
[12]: https://github.com/hila-chefer/Transformer-Explainability "hila-chefer/Transformer-Explainability: [CVPR 2021] Official ..."
[13]: https://arxiv.org/abs/2308.14850 "Attention Visualizer Package: Revealing Word Importance for Deeper Insight into Encoder-Only Transformer Models"
[14]: https://nips.cc/virtual/2024/poster/97689 "InterpBench: Semi-Synthetic Transformers for Evaluating ..."
[15]: https://arxiv.org/abs/2502.12352 "Towards Mechanistic Interpretability of Graph Transformers via Attention Graphs"




