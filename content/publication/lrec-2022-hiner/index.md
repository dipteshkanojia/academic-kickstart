---
title: "HiNER: A Large Hindi Named Entity Recognition Dataset"
date: 2022-06-24
authors: ["Rudra Murthy", "Pallab Bhattacharjee", "Rahul Sharnagat", "Jyotsana Khatri", "Diptesh Kanojia", "Pushpak Bhattacharyya"]
publication_types: ["1"]
abstract: "Named Entity Recognition (NER) is a foundational NLP task that aims to provide class labels like Person, Location, Organisation, Time, and Number to words in free text. Named Entities can also be multi-word expressions where the additional I-O-B annotation information helps label them during the NER annotation process. While English and European languages have considerable annotated data for the NER task, Indian languages lack on that front- both in terms of quantity and following annotation standards. This paper releases a significantly sized standard-abiding Hindi NER dataset containing 109,146 sentences and 2,220,856 tokens, annotated with 11 tags. We discuss the dataset statistics in all their essential detail and provide an in-depth analysis of the NER tag-set used with our data. The statistics of tag-set in our dataset show a healthy per-tag distribution, especially for prominent classes like Person, Location and Organisation. Since the proof of resource-effectiveness is in building models with the resource and testing the model on benchmark data and against the leader-board entries in shared tasks, we do the same with the aforesaid data. We use different language models to perform the sequence labelling task for NER and show the efficacy of our data by performing a comparative evaluation with models trained on another dataset available for the Hindi NER task. Our dataset helps achieve a weighted F1 score of 88.78 with all the tags and 92.22 when we collapse the tag-set, as discussed in the paper. To the best of our knowledge, no available dataset meets the standards of volume (amount) and variability (diversity), as far as Hindi NER is concerned. We fill this gap through this work, which we hope will significantly help NLP for Hindi. We release this dataset with our code and models for further research."

featured: false
publication: "*Proceedings of the 13th Conference on Language Resources and Evaluation (LREC 2022)*"
url_pdf: "files/lrec-2022-hiner.pdf"
url_preprint: "https://arxiv.org/abs/2204.13743"
tags: ["named entity recognition", "transfer learning", "NER", "Hindi NER", "dataset", "empirical", "evaluation"]
url_poster: "files/poster-lrec-2022-hiner.pdf"
url_code: "https://github.com/cfiltnlp/HiNER"
url_dataset: "https://github.com/cfiltnlp/HiNER"
# url_slides: ""
url_video: "files/vidoe-lrec-2022-hiner.mp4"
---

