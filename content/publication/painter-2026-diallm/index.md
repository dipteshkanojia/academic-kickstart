---
title: "DiaLLM: An Investigation into the Robustness-Generation Gap in English Dialect Adaptation"
date: 2026-10-20T00:00:00
authors: ["Jordan Painter", "Dipankar Srirag", "Adarsh Kappiyath", "Diptesh Kanojia", "Aditya Joshi", "Lu Yin"]
publication_types: ["1"]
abstract: "Large language models increasingly understand dialectal English, yet still produce only standard, US-leaning English, leaving dialectal generation, the harder half of the problem, largely unaddressed. We introduce DiaLLM, which continually pretrains three open-weight language model families on the International Corpus of English and applies implicit and explicit post-training paradigms, each combined with three model alignment strategies, giving the first controlled comparison of these components across Australian, Indian, and Northern British English. Our results reveal a robustness–generation gap: benchmarks are shaped by continual pretraining and SFT, while alignment visibly reshapes generation in ways benchmarks do not capture. Explicit variety-targeted adaptation produces output reliably recognised as dialectal and judged more dialectal than broad alignment, yet where human judgement was directly assessed, the method that most aggressively optimises the dialectal reward is not the one judged most dialectal. Independent linguistic analysis corroborates this reward-quality gap, most clearly on two of the three families. No single alignment method dominates, and closing the gap will require richer reward designs and continued investment in dialectal resources. We release all code, checkpoints, and preference datasets."
featured: true
publication: "*Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing*"
url_pdf: "https://aclanthology.org/2026.emnlp-main.2321.pdf"
url_preprint: "https://arxiv.org/abs/2607.07669"
url_code: "https://github.com/surrey-nlp/DiaLLM"
url_dataset: "https://huggingface.co/datasets/surrey-nlp/dialect-preferences"
url_poster: "files/poster-emnlp-2026-diallm.pdf"
doi: "10.18653/2026.emnlp-main.2321"
links:
- name: "Local PDF"
  url: "files/painter-2026-diallm.pdf"
tags: ["English dialects", "dialect adaptation", "LLMs", "preference alignment", "reinforcement learning"]
---
