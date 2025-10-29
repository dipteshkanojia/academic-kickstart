---
title: "Using character-level models for efficient abbreviation and long-form detection"
date: 2024-05-20T00:00:00
authors: ["Leonardo Zilio", "Shenbin Qian", "Diptesh Kanojia", "Constantin Orasan"]
publication_types: ["1"]
abstract: "Abbreviations and their associated long forms are important textual elements that are present in almost every scientific communication, and having information about these forms can help improve several NLP tasks. In this paper, our aim is to fine-tune language models for automatically identifying abbreviations and long forms. We used existing datasets which are annotated with abbreviations and long forms to train and test several language models, including transformer models, character-level language models, stacking of different embeddings, and ensemble methods. Our experiments showed that it was possible to achieve state-of-the-art results by stacking RoBERTa embeddings with domain-specific embeddings. However, the analysis of our first run showed that one of the datasets had issues in the BIO annotation, which led us to propose a revised dataset. After re-training selected models on the revised dataset, results show that character-level models achieve comparable results, especially when detecting abbreviations, but both RoBERTa large and the stacking of embeddings presented better results on biomedical data. When tested on a different subdomain (segments extracted from computer science texts), an ensemble method proved to yield the best results for the detection of long forms, and a character-level model had the best performance in detecting abbreviations."
featured: false
publication: "*Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)*"
url_pdf: "https://aclanthology.org/2024.lrec-main.270.pdf"
url_code: "https://github.com/surrey-nlp/PLODv2-CLM4AbbrDetection"
url_dataset: "https://huggingface.co/collections/surrey-nlp/plod-v2"
tags: ["abbreviation detection", "character-level models", "NLP", "biomedical text"]
---