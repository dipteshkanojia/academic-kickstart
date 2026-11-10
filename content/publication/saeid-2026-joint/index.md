---
title: "Joint Multiplicative-Additive Low-Rank Adaptation for Cyberbullying Detection"
date: 2026-10-23T00:00:00
authors: ["Aisha Saeid", "Ferrante Neri", "Diptesh Kanojia"]
publication_types: ["2"]
abstract: "Cyberbullying detection requires models to distinguish targeted harassment from general hostility and other forms of abusive language. Although large language models can perform this task through prompting, supervised adaptation generally achieves better performance. This study proposes a low-rank adaptation framework, W̄ = W(I + UV) + AB, which jointly optimises multiplicative and additive update paths, termed joint multiplicative-additive low-rank adaptation (JMA-LoRA). The multiplicative component preserves the rank of the pretrained weight matrix under an invertible near-identity transformation, while the additive component improves representational flexibility and optimisation stability. A four-stage experimental protocol compares zero-shot and few-shot prompting, additive and multiplicative low-rank adaptation, and the proposed joint framework across six decoder-only large language models on a six-class and a binary cyberbullying dataset. The proposed method achieves Macro F1 scores of 0.9044 on CB1 and 0.8959 on CB2. Its best configuration uses approximately 47% fewer trainable parameters than standard low-rank adaptation, while the additive path is associated with a Macro F1 that is 0.1359 higher where multiplicative adaptation alone collapses. These results support JMA-LoRA as an efficient strategy for specialised text classification."
featured: false
publication: "*International Journal of Neural Systems*"
url_pdf: "https://doi.org/10.1142/S0129065727500377"
url_code: "https://github.com/surrey-nlp/JMA-LoRA"
doi: "10.1142/S0129065727500377"
tags: ["cyberbullying detection", "low-rank adaptation", "parameter-efficient fine-tuning", "LLMs", "social media"]
---
