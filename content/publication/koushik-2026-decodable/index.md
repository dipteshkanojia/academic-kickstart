---
title: "Decodable but Misrouted: Sparse Features Uncover a Readout Gap in Vision-Language Models for Harmful Meme Detection"
date: 2026-09-16T00:00:00
authors: ["Girish A. Koushik", "Diptesh Kanojia", "Helen Treharne"]
publication_types: ["3"]
abstract: "When large vision-language models misclassify harmful memes, the failure may reflect missing internal evidence or an inability to route represented evidence to their outputs. We distinguish these cases in Gemma-3 and Qwen3.5 using sparse autoencoders, role-conditioned probes, causal interventions, and recovery experiments across six harmful content benchmarks, with additional Spanish and Hindi-English code-mixed evaluations. Sparse readouts outperform native prediction on all six primary binary tasks: Qwen averages 0.740 versus 0.432 for native macro-F1, residual reconstruction reaches 0.486, and Gemma improves from 0.532 to 0.714. These gains measure how accessible the label is to a supervised readout; they do not show that the model's native generation already applies such a decision rule. Under the evaluated scales, Qwen silent-feature ablation is 24-63 times more probe-sensitive, whereas routed-feature patching on literal yes/no tasks is 16-140 times more output-sensitive. Native-only threshold calibration explains much, but not all of the gap: on five tasks with matched probe scores, it recovers 69.8% of the raw native-to-probe difference, while direct routing adds 0.094 mean macro-F1 beyond calibrated native scoring. Joint gold-label, probe-KL, and pairwise LoRA supervision improves dedicated FHM prediction, but a gold-only adapter performs better on the shared seven-task mean. A case study of Gemma-3-12B on the Facebook Hateful Memes dataset finds a distributed rank-32 image-prompt interaction, reaching 0.756 versus 0.685 native macro-F1. Robustness controls show that the signal is not explained solely by accompanying OCR and depends on paired visual evidence, and that it extends beyond English. In many of the errors we study, the evidence is represented but does not reach the answer; therefore, routing is a common bottleneck in harmful meme classification."
featured: false
publication: "*arXiv preprint arXiv:2609.18860*"
url_pdf: "https://arxiv.org/pdf/2609.18860.pdf"
url_preprint: "https://arxiv.org/abs/2609.18860"
links:
- name: "Local PDF"
  url: "files/koushik-2026-decodable.pdf"
tags: ["harmful meme detection", "vision-language models", "sparse autoencoders", "mechanistic interpretability"]
---
