---
title: "Centrality-aware Product Retrieval and Ranking"
date: 2024-11-12T00:00:00
authors: ["Hadeel Saadany", "Swapnil Bhosale", "Samarth Agrawal", "Diptesh Kanojia", "Constantin Orasan", "Zhe Wu"]
publication_types: ["1"]
abstract: "This paper addresses the challenge of improving user experience on e-commerce platforms by enhancing product ranking relevant to user's search queries. Ambiguity and complexity of user queries often lead to a mismatch between user's intent and retrieved product titles or documents. Recent approaches have proposed the use of Transformer-based models which need millions of annotated query-title pairs during the pre-training stage, and this data often does not take user intent into account. To tackle this, we curate samples from existing datasets at eBay, manually annotated with buyer-centric relevance scores, and centrality scores which reflect how well the product title matches the user's intent. We introduce a User-intent Centrality Optimization (UCO) approach for existing models, which optimizes for the user intent in semantic product search. To that end, we propose a dual-loss based optimization to handle hard negatives, i.e., product titles that are semantically relevant but do not reflect the user's intent. Our contributions include curating challenging evaluation sets and implementing UCO, resulting in significant improvements in product ranking efficiency, observed for different evaluation metrics. Our work aims to ensure that the most buyer-centric titles for a query are ranked higher, thereby, enhancing the user experience on e-commerce platforms."
featured: false
publication: "*Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track*"
url_pdf: "https://aclanthology.org/2024.emnlp-industry.17.pdf"
url_poster: "https://aclanthology.org/attachments/2024.emnlp-industry.17.poster.pdf"
url_slides: "https://aclanthology.org/attachments/2024.emnlp-industry.17.presentation.pdf"
tags: ["product retrieval", "ranking", "e-commerce", "user intent"]
---