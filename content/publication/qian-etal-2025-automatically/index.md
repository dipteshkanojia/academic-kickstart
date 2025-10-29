---
title: "Automatically Generating Chinese Homophone Words to Probe Machine Translation Estimation Systems"
date: 2025-05-01T00:00:00
authors: ["Shenbin Qian", "Constantin Orasan", "Diptesh Kanojia", "Félix Do Carmo"]
publication_types: ["1"]
abstract: "Evaluating machine translation (MT) of user-generated content (UGC) involves unique challenges such as checking whether the nuance of emotions from the source are preserved in the target text. Recent studies have proposed emotion-related datasets, frameworks and models to automatically evaluate MT quality of Chinese UGC, without relying on reference translations. However, whether these models are robust to the challenge of preserving emotional nuances has been left largely unexplored. To this end, we introduce a novel method inspired by information theory which generates challenging Chinese homophone words related to emotions, by leveraging the concept of *self-information*. Our approach generates homophones that were observed to cause translation errors in emotion preservation, and exposes vulnerabilities in MT models struggling to preserve relevant emotions. We evaluate the efficacy of our method using human evaluation and compare it with an existing one, showing that our method achieves higher correlation with human judgments. The generated Chinese homophones, along with their manual translations, are utilized to generate perturbations and to probe the robustness of existing quality evaluation models, including models trained using multi-task learning, fine-tuned variants of multilingual language models, as well as large language models (LLMs). Our results indicate that LLMs with larger size exhibit higher stability and robustness to such perturbations. We release our data and code for reproducibility and further research."
featured: false
publication: "*Proceedings of the Tenth Workshop on Noisy and User-generated Text*"
url_pdf: "https://aclanthology.org/2025.wnut-1.11.pdf"
url_preprint: "https://arxiv.org/abs/2503.16158"
url_code: "https://github.com/surrey-nlp/homo_gen"
tags: ["machine translation", "homophones", "quality estimation", "Chinese", "emotions"]
---