---
title: "ALOPE: Adaptive Layer Optimization for Translation Quality Estimation using Large Language Models"
date: 2025-10-01T00:00:00
authors: ["Archchana Sindhujan", "Shenbin Qian", "Chan Chi Chun Matthew", "Constantin Orăsan", "Diptesh Kanojia"]
publication_types: ["1"]
abstract: "Large Language Models (LLMs) have shown remarkable performance across a wide range of natural language processing tasks. Quality Estimation (QE) for Machine Translation (MT), which assesses the quality of a source-target pair without relying on reference translations, remains a challenging cross-lingual task for LLMs. The challenges stem from the inherent limitations of existing LLM-based QE systems, which are pre-trained for causal language modelling rather than regression-specific tasks, further elevated by the presence of low-resource languages given pre-training data distribution. This paper introduces ALOPE, an adaptive layer-optimization framework designed to enhance LLM-based QE by restructuring Transformer representations through layer-wise adaptation for improved regression-based prediction. Our framework integrates low-rank adapters (LoRA) with regression task heads, leveraging selected pre-trained Transformer layers for improved cross-lingual alignment. In addition to the layer-specific adaptation, ALOPE introduces two strategies-dynamic weighting, which adaptively combines representations from multiple layers, and multi-head regression, which aggregates regression losses from multiple heads for QE. Our framework shows improvements over various existing LLM-based QE approaches. Empirical evidence suggests that intermediate Transformer layers in LLMs provide contextual representations that are more aligned with the cross-lingual nature of the QE task. We make resultant models and framework code publicly available for further research, also allowing existing LLM-based MT frameworks to be scaled with QE capabilities."
featured: true
publication: "*Proceedings of the 2nd Conference on Language Modeling*"
url_pdf: "https://arxiv.org/abs/2508.07484"
url_preprint: "https://arxiv.org/abs/2508.07484"
url_code: "https://github.com/surrey-nlp/ALOPE"
url_dataset: "https://huggingface.co/collections/surrey-nlp/alope-models"
url_poster: "files/poster-colm-25-alope.pdf"
url_slides: "files/NLPCafe-ALOPE.pdf"
tags: ["quality estimation", "machine translation", "LLMs", "layer optimization", "low-resource languages"]
---