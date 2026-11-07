---
title: "Parameter-Efficient Quality Estimation via Frozen Recursive Models"
date: 2026-03-28T00:00:00
authors: ["Umar Abubacar", "Roman Bauer", "Diptesh Kanojia"]
publication_types: ["1"]
abstract: "Tiny Recursive Models (TRM) achieve strong results on reasoning tasks through iterative refinement of a shared network. We investigate whether these recursive mechanisms transfer to Quality Estimation (QE) for low-resource languages using a three-phase methodology. Experiments on 8 language pairs on a low-resource QE dataset reveal three findings. First, TRM's recursive mechanisms do not transfer to QE. External iteration hurts performance, and internal recursion offers only narrow benefits. Next, representation quality dominates architectural choices, and lastly, frozen pretrained embeddings match fine-tuned performance while reducing trainable parameters by 37x."
featured: false
publication: "*Proceedings of the Second Workshop on Language Models for Low-Resource Languages (LoResLM 2026)*"
url_pdf: "https://aclanthology.org/2026.loreslm-1.52.pdf"
url_dataset: "https://huggingface.co/datasets/surrey-nlp/Low-resource-QE-DA-dataset"
doi: "10.18653/v1/2026.loreslm-1.52"
links:
- name: "Local PDF"
  url: "files/abubacar-2026-parameter.pdf"
tags: ["quality estimation", "parameter-efficient fine-tuning", "recursive models", "low-resource languages"]
---
