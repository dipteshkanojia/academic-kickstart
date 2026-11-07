---
title: "TeMuDance: Contrastive Alignment-Based Textual Control for Music-Driven Dance Generation"
date: 2026-04-18T00:00:00
authors: ["Xinran Liu", "Diptesh Kanojia", "Wenwu Wang", "Zhenhua Feng"]
publication_types: ["1"]
abstract: "Existing music-driven dance generation approaches have achieved strong realism and effective audio-motion alignment. However, they generally lack semantic controllability, making it difficult to guide specific movements through natural language descriptions. This limitation primarily stems from the absence of large-scale datasets that jointly align music, text, and motion for supervised learning of text-conditioned control. To address this challenge, we propose TeMuDance, a framework that enables text-based control for music-conditioned dance generation without requiring any manually annotated music-text-motion triplet dataset. TeMuDance introduces a motion-centred bridging paradigm that leverages motion as a shared semantic anchor to align disjoint music-dance and text-motion datasets within a unified embedding space, enabling cross-modal retrieval of missing modalities for end-to-end training. A lightweight text control branch is then trained on top of a frozen music-to-dance diffusion backbone, preserving rhythmic fidelity while enabling fine-grained semantic guidance. To further suppress noise inherent in the retrieved supervision, we design a dual-stream fine-tuning strategy with confidence-based filtering. We also propose a novel task-aligned metric that quantifies whether textual prompts induce the intended kinematic attributes under music conditioning. Extensive experiments demonstrate that TeMuDance achieves competitive dance quality while substantially improving text-conditioned control over existing methods."
featured: false
publication: "*Proceedings of the 34th ACM International Conference on Multimedia (ACM MM 2026)*"
url_pdf: "https://arxiv.org/pdf/2604.17005.pdf"
url_preprint: "https://arxiv.org/abs/2604.17005"
url_code: "https://github.com/surrey-nlp/TeMuDance"
url_project: "https://xinranliu7715.github.io/temudance-page/"
links:
- name: "Local PDF"
  url: "files/liu-2026-temudance.pdf"
tags: ["dance generation", "music-driven", "textual control", "contrastive alignment", "ACM Multimedia"]
---
