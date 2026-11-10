---
title: "In the Blind: Building Pseudo-References for MT Evaluation"
date: 2026-10-24T00:00:00
authors: ["Diptesh Kanojia", "Chi-kiu Lo", "Archchana Sindhujan", "Samuel Larkin", "Greg Hanneman", "Alon Lavie"]
publication_types: ["1"]
abstract: "The WMT26 General MT task evaluates systems on 10 language pairs that have no human references (neither translated from scratch nor post-edited from MT output by humans). We describe how we built the pseudo-references for these pairs and six other language pairs (in which some forms of human references are available): seven models translate the 3,277 official documents under up to five prompt conditions, giving a total of 26 system–prompt combinations; then three reference-free quality estimation (QE) models score every candidate; and a per-document selector picks one translation, which GPT-5.5 post-edits where needed. Working without references exposed a failure mode of QE-guided selection: the metrics rank fluent output in the wrong language above correct translations. Adding a confidence-scaled language identification penalty to the score fusion drives the wrong-language count to zero, and the resulting selector still scores better on MetricX than the rank-fusion baseline it replaces. Since no references were available for these pairs while we were building them, we calibrate every selection decision on last year's WMT25 human judgments. The human evaluation, released after construction, shows the cost of getting selection wrong: our references stand with the strongest participating systems when the selector kept a frontier-model candidate, and fall up to 17 ESA points below them when it did not. We release the selection method and the provenance of every reference."
featured: false
publication: "*Proceedings of the Eleventh Conference on Machine Translation*"
url_pdf: "https://aclanthology.org/2026.wmt-main.69.pdf"
url_preprint: "https://arxiv.org/abs/2609.13611"
url_code: "https://github.com/surrey-nlp/PseudoRef"
doi: "10.18653/2026.wmt-main.69"
links:
- name: "Local PDF"
  url: "files/kanojia-2026-blind.pdf"
tags: ["machine translation", "MT evaluation", "pseudo-references", "quality estimation", "WMT"]
---
