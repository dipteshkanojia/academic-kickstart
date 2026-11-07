---
title: "Beyond Scalar Scores: Reinforcement Learning for Error-Aware Quality Estimation of Machine Translation"
date: 2026-02-09T00:00:00
authors: ["Archchana Sindhujan", "Girish A. Koushik", "Shenbin Qian", "Diptesh Kanojia", "Constantin Orăsan"]
publication_types: ["3"]
abstract: "Quality Estimation (QE) aims to assess the quality of machine translation (MT) outputs without relying on reference translations, making it essential for real-world, large-scale MT evaluation. Large Language Models (LLMs) have shown significant promise in advancing the field of quality estimation of machine translation. However, most of the QE approaches solely rely on scalar quality scores, offering no explicit information about the translation errors that should drive these judgments. Moreover, for low-resource languages where annotated QE data is limited, existing approaches struggle to achieve reliable performance. To address these challenges, we introduce the first segment-level QE dataset for English to Malayalam, a severely resource-scarce language pair in the QE domain, comprising human-annotated Direct Assessment (DA) scores and Translation Quality Remarks (TQR), which are short, contextual, free-form annotator comments that describe translation errors. We further introduce ALOPE-RL, a policy-based reinforcement learning framework that trains efficient adapters based on policy rewards derived from DA score and TQR. Integrating error-aware rewards with ALOPE-RL enables LLMs to reason about translation quality beyond numeric scores. Despite being trained on a small-scale QE dataset, ALOPE-RL achieves state-of-the-art performance on English to Malayalam QE using compact LLMs (<=4B parameters) fine-tuned with LoRA and 4-bit quantization, outperforming both larger LLM-based baselines and leading encoder-based QE models. Our results demonstrate that error-aware, policy-based learning can deliver strong QE performance under limited data and compute budgets. We release our dataset, code, and trained models to support future research."
featured: false
publication: "*arXiv preprint arXiv:2602.08600*"
url_pdf: "https://arxiv.org/pdf/2602.08600.pdf"
url_preprint: "https://arxiv.org/abs/2602.08600"
url_code: "https://github.com/surrey-nlp/ALOPE-RL"
url_dataset: "https://huggingface.co/datasets/surrey-nlp/ALOPE-RL-Dataset"
links:
- name: "Local PDF"
  url: "files/sindhujan-2026-beyond.pdf"
tags: ["quality estimation", "reinforcement learning", "machine translation", "low-resource languages", "LLMs"]
---
