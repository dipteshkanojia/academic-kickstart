---
title: "TANDEM: Temporal-Aware Neural Detection for Multimodal Hate Speech"
date: 2026-01-16T00:00:00
authors: ["Girish A. Koushik", "Helen Treharne", "Diptesh Kanojia"]
publication_types: ["3"]
abstract: "Social media platforms are increasingly dominated by long-form multimodal content, where harmful narratives are constructed through a complex interplay of audio, visual, and textual cues. While automated systems can flag hate speech with high accuracy, they often function as 'black boxes' that fail to provide the granular, interpretable evidence, such as precise timestamps and target identities, required for effective human-in-the-loop moderation. In this work, we introduce TANDEM, a unified framework that transforms audio-visual hate detection from a binary classification task into a structured reasoning problem. Our approach employs a novel tandem reinforcement learning strategy where vision-language and audio-language models optimize each other through self-constrained cross-modal context, stabilizing reasoning over extended temporal sequences without requiring dense frame-level supervision. Experiments across three benchmark datasets demonstrate that TANDEM significantly outperforms zero-shot and context-augmented baselines, achieving 0.73 F1 in target identification on HateMM (a 30% improvement over state-of-the-art) while maintaining precise temporal grounding. We further observe that while binary detection is robust, differentiating between offensive and hateful content remains challenging in multi-class settings due to inherent label ambiguity and dataset imbalance. More broadly, our findings suggest that structured, interpretable alignment is achievable even in complex multimodal settings, offering a blueprint for the next generation of transparent and actionable online safety moderation tools."
featured: false
publication: "*arXiv preprint arXiv:2601.11178* | Accepted to *AAAI-ICWSM 2027*"
url_pdf: "https://arxiv.org/pdf/2601.11178.pdf"
url_preprint: "https://arxiv.org/abs/2601.11178"
links:
- name: "Local PDF"
  url: "files/koushik-2026-tandem.pdf"
tags: ["multimodal hate speech", "temporal grounding", "reinforcement learning", "online safety", "audio-visual"]
---
