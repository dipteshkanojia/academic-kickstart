---
title: "Quality Estimation-Assisted Automatic Post-Editing"
date: 2023-12-06T00:00:00
authors: ["Sourabh Deoghare", "Diptesh Kanojia", "Fred Blain", "Tharindu Ranasinghe", "Pushpak Bhattacharyya"]
publication_types: ["1"]
abstract: "Automatic Post-Editing (APE) systems are prone to over-correction of the Machine Translation (MT) outputs. While Word-level Quality Estimation (QE) system can provide a way to curtail the over-correction, a significant performance gain has not been observed thus far by utilizing existing APE and QE combination strategies. In this paper, we propose joint training of a model on APE and QE tasks to improve the APE. Our proposed approach utilizes a multi-task learning (MTL) methodology, which shows significant improvement while treating both tasks as a 'bargaining game' during training. Moreover, we investigate various existing combination strategies and show that our approach achieves state-of-the-art performance for a 'distant' language pair, viz., English-Marathi. We observe an improvement of 1.09 TER and 1.37 BLEU points over a baseline QE-Unassisted APE system for English-Marathi, while also observing 0.46 TER and 0.62 BLEU points for English-German. Further, we discuss the results qualitatively and show how our approach helps reduce over-correction, thereby improving the APE performance. We also observe that the degree of integration between QE and APE directly correlates with the APE performance gain. We release our code and models publicly."
featured: false
publication: "*Findings of the Association for Computational Linguistics: EMNLP 2023*"
url_pdf: "https://aclanthology.org/2023.findings-emnlp.115.pdf"
tags: ["automatic post-editing", "quality estimation", "machine translation", "multi-task learning"]
---