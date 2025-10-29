---
title: "APE-then-QE: Correcting then Filtering Pseudo Parallel Corpora for MT Training Data Creation"
date: 2023-12-21T00:00:00
authors: ["Akshay Batheja", "Sourabh Deoghare", "Diptesh Kanojia", "Pushpak Bhattacharyya"]
publication_types: ["3"]
abstract: "Automatic Post-Editing (APE) is the task of automatically identifying and correcting errors in the Machine Translation (MT) outputs. We propose a repair-filter-use methodology that uses an APE system to correct errors on the target side of the MT training data. We select the sentence pairs from the original and corrected sentence pairs based on the quality scores computed using a Quality Estimation (QE) model. To the best of our knowledge, this is a novel adaptation of APE and QE to extract quality parallel corpus from the pseudo-parallel corpus. By training with this filtered corpus, we observe an improvement in the Machine Translation system's performance by 5.64 and 9.91 BLEU points, for English-Marathi and Marathi-English, over the baseline model. The baseline model is the one that is trained on the whole pseudo-parallel corpus. Our work is not limited by the characteristics of English or Marathi languages; and is language pair-agnostic, given the necessary QE and APE data."
featured: false
publication: "*arXiv preprint arXiv:2312.11312*"
url_pdf: "https://arxiv.org/abs/2312.11312"
url_preprint: "https://arxiv.org/abs/2312.11312"
tags: ["automatic post-editing", "quality estimation", "machine translation", "pseudo-parallel corpora"]
---