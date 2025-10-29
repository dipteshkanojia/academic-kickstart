---
title: "What do Large Language Models Need for Machine Translation Evaluation?"
date: 2024-11-12T00:00:00
authors: ["Shenbin Qian", "Archchana Sindhujan", "Minnie Kabra", "Diptesh Kanojia", "Constantin Orasan", "Tharindu Ranasinghe", "Fred Blain"]
publication_types: ["1"]
abstract: "Leveraging large language models (LLMs) for various natural language processing tasks has led to superlative claims about their performance. For the evaluation of machine translation (MT), existing research shows that LLMs are able to achieve results comparable to fine-tuned multilingual pre-trained language models. In this paper, we explore what translation information, such as the source, reference, translation errors and annotation guidelines, is needed for LLMs to evaluate MT quality. In addition, we investigate prompting techniques such as zero-shot, Chain of Thought (CoT) and few-shot prompting for eight language pairs covering high-, medium- and low-resource languages, leveraging varying LLM variants. Our findings indicate the importance of reference translations for an LLM-based evaluation. While larger models do not necessarily fare better, they tend to benefit more from CoT prompting, than smaller models. We also observe that LLMs do not always provide a numerical score when generating evaluations, which poses a question on their reliability for the task. Our work presents a comprehensive analysis for resource-constrained and training-less LLM-based evaluation of machine translation. We release the accrued prompt templates, code and data publicly for reproducibility."
featured: false
publication: "*Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing*"
url_pdf: "https://aclanthology.org/2024.emnlp-main.214.pdf"
url_preprint: "https://arxiv.org/abs/2410.03278"
url_code: "https://github.com/surrey-nlp/LLM4MT_eval"
tags: ["machine translation", "large language models", "evaluation", "prompting"]
---