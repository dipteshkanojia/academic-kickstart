---
title: "A Multi-task Learning Framework for Evaluating Machine Translation of Emotion-loaded User-generated Content"
date: 2024-11-19T00:00:00
authors: ["Shenbin Qian", "Constantin Orăsan", "Diptesh Kanojia", "Félix Do Carmo"]
publication_types: ["1"]
abstract: "Machine translation (MT) of user-generated content (UGC) poses unique challenges, including handling slang, emotion, and literary devices like irony and sarcasm. Evaluating the quality of these translations is challenging as current metrics do not focus on these ubiquitous features of UGC. To address this issue, we utilize an existing emotion-related dataset that includes emotion labels and human-annotated translation errors based on Multi-dimensional Quality Metrics. We extend it with sentence-level evaluation scores and word-level labels, leading to a dataset suitable for sentence- and word-level translation evaluation and emotion classification, in a multi-task setting. We propose a new architecture to perform these tasks concurrently, with a novel combined loss function, which integrates different loss heuristics, like the Nash and Aligned losses. Our evaluation compares existing fine-tuning and multi-task learning approaches, assessing generalization with ablative experiments over multiple datasets. Our approach achieves state-of-the-art performance and we present a comprehensive analysis for MT evaluation of UGC."
featured: false
publication: "*Proceedings of the Ninth Conference on Machine Translation*"
url_pdf: "https://aclanthology.org/2024.wmt-1.113.pdf"
url_preprint: "https://arxiv.org/abs/2410.03277"
url_code: "https://github.com/surrey-nlp/MTL4QE"
url_dataset: "https://github.com/surrey-nlp/MTL4QE/tree/main/data"
tags: ["machine translation", "emotion", "user-generated content", "multi-task learning"]
---