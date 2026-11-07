---
title: "Beyond Relevance: Structured Semantic Supervision for Product Search with LLM-Augmented Annotations"
date: 2026-09-20T00:00:00
authors: ["Girish A. Koushik", "Swapnil Bhosale", "Samarth Agrawal", "Hadeel Saadany", "Constantin Orăsan", "Xiatian Zhu", "Diptesh Kanojia"]
publication_types: ["3"]
abstract: "E-commerce search requires distinguishing products that are merely related to a query from those that directly satisfy the user's shopping intent. We augment query-product pairs with structured LLM-generated query and product attributes and human-validated relevance, explanations, and centrality judgments, and evaluate these signals using a simple dual-encoder retriever and MLP re-ranker. On an augmented subset of ESCI, a human-feature oracle reaches 0.9382 nDCG@10, while a human-free trained Q+P configuration reaches 0.9258. Synthetic approximations of the human signals reach 0.9150 overall but provide substantial gains for difficult, low-performing queries. Ablations show that most of the oracle improvement comes from post-edited explanations and annotator comments rather than the scalar centrality feature, suggesting that LLMs are most useful for exposing and approximating structured semantic supervision rather than replacing human judgment directly."
featured: false
publication: "*arXiv preprint arXiv:2609.23646*"
url_pdf: "https://arxiv.org/pdf/2609.23646.pdf"
url_preprint: "https://arxiv.org/abs/2609.23646"
links:
- name: "Local PDF"
  url: "files/koushik-2026-beyond.pdf"
tags: ["product search", "e-commerce", "information retrieval", "LLMs", "semantic supervision"]
---
