---
title: "Improving Search Suggestions for Alphanumeric Queries"
date: 2026-03-24T00:00:00
authors: ["Samarth Agrawal", "Jayanth Yetukuri", "Diptesh Kanojia", "Qunzhi Zhou", "Zhe Wu"]
publication_types: ["1"]
abstract: "Alphanumeric identifiers such as manufacturer part numbers (MPNs), SKUs, and model codes are ubiquitous in e-commerce catalogs and search. These identifiers are sparse, non-linguistic, and highly sensitive to tokenization and typographical variation, rendering conventional lexical and embedding-based retrieval methods ineffective. We propose a training-free, character-level retrieval framework that encodes each alphanumeric sequence as a fixed-length binary vector. This representation enables efficient similarity computation via Hamming distance and supports nearest-neighbor retrieval over large identifier corpora. An optional re-ranking stage using edit distance refines precision while preserving latency guarantees. The method offers a practical and interpretable alternative to learned dense retrieval models, making it suitable for production deployment in search suggestion generation systems. Significant gains in business metrics in the A/B test further prove utility of our approach."
featured: false
publication: "*Advances in Information Retrieval: 48th European Conference on Information Retrieval (ECIR 2026)*"
url_pdf: "https://doi.org/10.1007/978-3-032-21321-1_12"
url_preprint: "https://arxiv.org/abs/2604.07364"
doi: "10.1007/978-3-032-21321-1_12"
links:
- name: "Local PDF"
  url: "files/agrawal-2026-improving.pdf"
tags: ["information retrieval", "e-commerce search", "alphanumeric queries", "search suggestions"]
---
