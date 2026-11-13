---
title: "IndicQE-APE: A Consolidated Benchmark for Quality Estimation and Automatic Post-Editing over Indic Languages"
date: 2026-10-25T00:00:00
authors: ["Diptesh Kanojia", "Archchana Sindhujan", "Sourabh Deoghare", "Daria Sokova", "Shenbin Qian", "Girish A. Koushik", "Tharindu Ranasinghe", "Constantin Orăsan", "Chrysoula Zerva", "Ricardo Rei", "Frédéric Blain", "André Martins", "Marco Turchi", "Matteo Negri", "Anoop Kunchukuttan", "Mitesh M. Khapra", "Pushpak Bhattacharyya"]
publication_types: ["1"]
abstract: "Indic quality estimation (QE) and automatic post-editing (APE) data is spread across separate releases, so no single resource supports training and evaluation across tasks and language pairs on one footing. We consolidate the WMT 2020-2024 shared-task lineage with an extended English-Malayalam resource into IndicQE-APE: 126,754 instances over nine directional pairs, with up to four label types aligned on the same segment, a direct assessment, a human post-edit, word-level tags and an error explanation, and a test set stratified over four difficulty axes. We benchmark six prompted LLMs and three COMET metrics on segment-level QE, and three systems on APE. Two of the axes are defined partly on direct assessment and select a compressed slice of it. Segments whose segment-level and token-level signals disagree are ranked below equally scored segments of the same language. Four-shot prompting costs every model at or below 3.4B both correlation and output-format compliance. Unedited MT beats every APE system we run on three of the four pairs. The benchmark and code are released."
featured: true
publication: "*Proceedings of the Eleventh Conference on Machine Translation*"
url_pdf: "https://aclanthology.org/2026.wmt-main.19.pdf"
url_preprint: "https://arxiv.org/abs/2608.16344"
url_code: "https://github.com/surrey-nlp/IndicQE-APE"
url_dataset: "https://huggingface.co/datasets/surrey-nlp/IndicQE-APE"
url_poster: "files/poster-wmt-2026-indicqe.pdf"
doi: "10.18653/2026.wmt-main.19"
links:
- name: "Local PDF"
  url: "files/kanojia-2026-indicqe.pdf"
tags: ["quality estimation", "automatic post-editing", "Indic languages", "machine translation", "benchmark"]
---
