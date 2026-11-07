---
title: "Domain-Specific Quality Estimation for Machine Translation in Low-Resource Scenarios"
date: 2026-03-28T00:00:00
authors: ["Namrata Bhalchandra Patil Gurav", "Akashdeep Ranu", "Archchana Sindhujan", "Diptesh Kanojia"]
publication_types: ["1"]
abstract: "Quality Estimation (QE) is essential for assessing machine translation quality in reference-less settings, particularly for domain-specific and low-resource language scenarios. In this paper, we investigate sentence-level QE for English to Indic machine translation across four domains (Healthcare, Legal, Tourism, and General) and five language pairs. We systematically compare zero-shot, few-shot, and guideline-anchored prompting across selected closed-weight and open-weight LLMs. Findings indicate that while closed-weight models achieve strong performance via prompting alone, prompt-only approaches remain fragile for open-weight models, especially in high-risk domains. To address this, we adopt ALOPE, a framework for LLM-based QE which uses Low-Rank Adaptation with regression heads attached to selected intermediate Transformer layers. We also extend ALOPE with the recently proposed Low-Rank Multiplicative Adaptation (LoRMA) for this work. Our results show that intermediate-layer adaptation consistently improves QE performance, with gains in semantically complex domains, indicating a way ahead for robust QE in practical scenarios. We release code and domain-specific QE datasets publicly for further research."
featured: false
publication: "*Proceedings of the Second Workshop on Language Models for Low-Resource Languages (LoResLM 2026)*"
url_pdf: "https://aclanthology.org/2026.loreslm-1.55.pdf"
url_code: "https://github.com/surrey-nlp/ALOPE/tree/main/Domain-based-QE-with-ALOPE"
doi: "10.18653/v1/2026.loreslm-1.55"
links:
- name: "Local PDF"
  url: "files/gurav-2026-domain.pdf"
tags: ["quality estimation", "domain adaptation", "low-resource languages", "Indic languages", "LLMs"]
---
