---
title: "TRACE: Textual Relevance Augmentation and Contextual Encoding for Multimodal Hate Detection"
date: 2026-03-14T00:00:00
authors: ["Girish A. Koushik", "Helen Treharne", "Aditya Joshi", "Diptesh Kanojia"]
publication_types: ["1"]
abstract: "Social media memes are a challenging domain for hate detection because they intertwine visual and textual cues into culturally nuanced messages. To tackle these challenges, we introduce TRACE, a hierarchical multimodal framework that leverages visually grounded context augmentation, along with a novel caption-scoring network to emphasize hate-relevant content, and parameter-efficient fine-tuning of CLIP's text encoder. Our experiments demonstrate that selectively fine-tuning deeper text encoder layers significantly enhances performance compared to simpler projection-layer fine-tuning methods. Specifically, our framework achieves state-of-the-art accuracy (0.807) and F1-score (0.806) on the widely-used Hateful Memes dataset, matching the performance of considerably larger models while maintaining efficiency. Moreover, it achieves superior generalization on the MultiOFF offensive meme dataset (F1-score 0.673), highlighting robustness across meme categories. Additional analyses confirm that robust visual grounding and nuanced text representations significantly reduce errors caused by benign confounders. We publicly release our code to facilitate future research. **Note:** An earlier preprint version of this work was titled 'CAMU: Context Augmentation for Meme Understanding' ([arXiv:2504.17902v1](https://arxiv.org/abs/2504.17902v1))."
featured: false
publication: "*Proceedings of the AAAI Conference on Artificial Intelligence*"
url_pdf: "https://ojs.aaai.org/index.php/AAAI/article/view/41220"
url_preprint: "https://arxiv.org/abs/2504.17902"
url_code: "https://github.com/surrey-nlp/TRACE"
doi: "10.1609/aaai.v40i45.41220"
links:
- name: "Local PDF"
  url: "files/koushik-2026-trace.pdf"
aliases: ["/publication/koushik-etal-2025-camu/"]
tags: ["multimodal hate detection", "hateful memes", "visual grounding", "parameter-efficient fine-tuning", "AAAI"]
---
