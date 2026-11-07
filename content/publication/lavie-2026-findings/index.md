---
title: "Findings of the WMT26 Shared Task on Automated Translation Quality Evaluation Systems: Compact Open Models are Competitive Quality Evaluators"
date: 2026-10-23T00:00:00
authors: ["Alon Lavie", "Greg Hanneman", "Stefano Perrella", "Shuoyang Ding", "Eleftherios Avramidis", "Lorenzo Proietti", "Chi-kiu Lo", "Ammon Shurtz", "Chrysoula Zerva", "Archchana Sindhujan", "Vilém Zouhar", "Diptesh Kanojia", "Frédéric Blain", "Brian Thompson", "Giorgos Filandrianos", "Orfeas Menis Mastromichalakis", "Tom Kocmi", "Pranav Gupta"]
publication_types: ["1"]
abstract: "We present the findings of the WMT26 Shared Task on Automated Translation Quality Evaluation Systems, continuing last year's unification of the earlier separate WMT Metrics and Quality Estimation shared tasks. This year we evaluated three complementary views of segment-level translation quality on a common test set: fine-grained error-span detection, continuous quality-score prediction, and a new task on identifying error-free translations. Submissions to upstream tasks were also converted automatically to downstream predictions. The evaluation covered 21 translation directions using human cESA judgments from the WMT26 General Machine Translation task, with optional reference translations generated as either native, post-edited, or pseudo-references, depending on the translation direction. Official evaluation data was complemented by five submitted challenge sets. Across all three primary tasks, unsupervised LLM-as-a-judge approaches outperformed all traditional and supervised metrics, while open-weight models such as Gemma 4 were found to be largely competitive with proprietary frontier models. Reference-free LLM judges are highly competitive, and the benefit of adding a reference largely depends on its provenance and on the evaluator model family."
featured: false
publication: "*Proceedings of the Eleventh Conference on Machine Translation*"
url_pdf: "https://aclanthology.org/2026.wmt-main.49.pdf"
url_code: "https://github.com/wmt-conference/wmt26-mteval"
doi: "10.18653/2026.wmt-main.49"
links:
- name: "Local PDF"
  url: "files/lavie-2026-findings.pdf"
tags: ["machine translation", "quality estimation", "shared task", "evaluation systems", "LLM-as-a-judge"]
---
