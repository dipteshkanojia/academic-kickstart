---
title: "Are Large Language Models State-of-the-art Quality Estimators for Machine Translation of User-generated Content?"
date: 2024-11-19T00:00:00
authors: ["Shenbin Qian", "Constantin Orăsan", "Diptesh Kanojia", "Félix Do Carmo"]
publication_types: ["1"]
abstract: "This paper investigates whether large language models (LLMs) are state-of-the-art quality estimators for machine translation of user-generated content (UGC) that contains emotional expressions, without the use of reference translations. To achieve this, we employ an existing emotion-related dataset with human-annotated errors and calculate quality evaluation scores based on the Multi-dimensional Quality Metrics. We compare the accuracy of several LLMs with that of our fine-tuned baseline models, under in-context learning and parameter-efficient fine-tuning (PEFT) scenarios. We find that PEFT of LLMs leads to better performance in score prediction with human interpretable explanations than fine-tuned models. However, a manual analysis of LLM outputs reveals that they still have problems such as refusal to reply to a prompt and unstable output while evaluating machine translation of UGC."
featured: false
publication: "*Proceedings of the Eleventh Workshop on Asian Translation (WAT 2024)*"
url_pdf: "https://aclanthology.org/2024.wat-1.4.pdf"
url_preprint: "https://arxiv.org/abs/2410.06338"
url_code: "https://github.com/surrey-nlp/LLMs4MTQE-UGC"
url_dataset: "https://github.com/surrey-nlp/LLMs4MTQE-UGC/tree/main/data"
tags: ["large language models", "machine translation", "quality estimation", "user-generated content"]
---