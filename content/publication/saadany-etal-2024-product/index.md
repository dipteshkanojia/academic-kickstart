---
title: "Product Retrieval and Ranking for Alphanumeric Queries"
date: 2024-10-21T00:00:00
authors: ["Hadeel Saadany", "Swapnil Bhosale", "Samarth Agrawal", "Zhe Wu", "Constantin Orasan", "Diptesh Kanojia"]
publication_types: ["1"]
abstract: "This talk addresses the challenge of improving user experience on e-commerce platforms by enhancing product ranking relevant to user's search queries. Queries such as S2716DG consist of alphanumeric characters where a letter or number can signify important detail for the product/model. Speaker describes recent research where we curate samples from existing datasets at eBay, manually annotated with buyer-centric relevance scores, and centrality scores which reflect how well the product title matches the user's intent. We introduce a User-intent Centrality Optimization (UCO) approach for existing models, which optimizes for the user intent in semantic product search. To that end, we propose a dual-loss based optimization to handle hard negatives, i.e., product titles that are semantically relevant but do not reflect the user's intent. Our contributions include curating a challenging evaluation set and implementing UCO, resulting in significant improvements in product ranking efficiency, observed for different evaluation metrics. Our work aims to ensure that the most buyer-centric titles for a query are ranked higher, thereby, enhancing the user experience on e-commerce platforms."
featured: false
publication: "*Proceedings of the 33rd ACM International Conference on Information and Knowledge Management*"
url_pdf: "https://doi.org/10.1145/3627673.3679080"
tags: ["product retrieval", "ranking", "alphanumeric queries", "e-commerce"]
---