---
title: "When LLMs Struggle: Reference-less Translation Evaluation for Low-resource Languages"
date: 2025-01-01T00:00:00
authors: ["Archchana Sindhujan", "Diptesh Kanojia", "Constantin Orasan", "Shenbin Qian"]
publication_types: ["1"]
abstract: "This paper investigates the reference-less evaluation of machine translation for low-resource language pairs, known as quality estimation (QE). Segment-level QE is a challenging cross-lingual language understanding task that provides a quality score (0 -100) to the translated output. We comprehensively evaluate large language models (LLMs) in zero/few-shot scenarios and perform instruction fine-tuning using a novel prompt based on annotation guidelines. Our results indicate that prompt-based approaches are outperformed by the encoder-based fine-tuned QE models. Our error analysis reveals tokenization issues, along with errors due to transliteration and named entities, and argues for refinement in LLM pre-training for cross-lingual tasks. We release the data, and models trained publicly for further research."
featured: false
publication: "*Proceedings of the First Workshop on Language Models for Low-Resource Languages*"
url_pdf: "https://aclanthology.org/2025.loreslm-1.33.pdf"
url_dataset: "https://huggingface.co/datasets/ArchSid/QE-DA-datasets"
tags: ["quality estimation", "machine translation", "low-resource languages", "LLMs"]
---