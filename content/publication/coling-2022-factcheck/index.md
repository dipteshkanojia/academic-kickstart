---
title: "Harnessing Abstractive Summarization for Fact-Checked Claim Detection"
date: 2022-09-11
authors: ["Varad Bhatnagar", "Diptesh Kanojia", "Kameswari Chebrolu"]
publication_types: ["1"]
abstract: "Social media platforms have become new battlegrounds for anti-social elements, with misinformation being the weapon of choice. Fact-checking organizations try to debunk as many claims as possible while staying true to their journalistic processes but cannot cope with its rapid dissemination. We believe that the solution lies in partial automation of the fact-checking life cycle, saving human time for tasks which require high cognition. We propose a new workflow for efficiently detecting previously fact-checked claims that uses abstractive summarization to generate crisp queries. These queries can then be executed on a general-purpose retrieval system associated with a collection of previously fact-checked claims. We curate an abstractive text summarization dataset comprising noisy claims from Twitter and their gold summaries. It is shown that retrieval performance improves 2x by using popular out-of-the-box summarization models and 3x by fine-tuning them on the accompanying dataset compared to verbatim querying. Our approach achieves Recall@5 and MRR of 35% and  0.3, compared to baseline values of 10% and 0.1, respectively. Our dataset, code, and models are
available publicly [here](https://github.com/varadhbhatnagar/FC-Claim-Det/).
"

featured: false
publication: "*Proceedings of The 29th International Conference on Computational Linguistics (COLING 2022)*"
url_pdf: "files/coling-2022-factcheck.pdf"
tags: ["fact-checking", "google fact check", "automatic pipeline", "abstractive summarization", "twitter data", "social media", "misinformation"]
# url_poster: "files/poster-eacl-2021-cognate.pdf"
url_code: "https://github.com/varadhbhatnagar/FC-Claim-Det"
# url_slides: "files/ppt-eacl-2021-cognate.pdf"
# url_video: "https://slideslive.com/38954530/cognitionaware-cognate-detection"
# url_preprint: "https://arxiv.org/abs/2112.08087"
---

