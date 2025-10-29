---
title: "Predict and Use: Harnessing Predicted Gaze to Improve Multimodal Sarcasm Detection"
date: 2023-12-06T00:00:00
authors: ["Divyank Tiwari", "Diptesh Kanojia", "Anupama Ray", "Apoorva Nunna", "Pushpak Bhattacharyya"]
publication_types: ["1"]
abstract: "Sarcasm is a complex linguistic construct with incongruity at its very core. Detecting sarcasm depends on the actual content spoken and tonality, facial expressions, the context of an utterance, and personal traits like language proficiency and cognitive capabilities. In this paper, we propose the utilization of synthetic gaze data to improve the task performance for multimodal sarcasm detection in a conversational setting. We enrich an existing multimodal conversational dataset, i.e., MUStARD++ with gaze features. With the help of human participants, we collect gaze features for 20% of data instances, and we investigate various methods for gaze feature prediction for the rest of the dataset. We perform extrinsic and intrinsic evaluations to assess the quality of the predicted gaze features. We observe a performance gain of up to 6.6% points by adding a new modality, i.e., collected gaze features. When both collected and predicted data are used, we observe a performance gain of 2.3% points on the complete dataset. Interestingly, with only predicted gaze features, too, we observe a gain in performance (1.9% points). We retain and use the feature prediction model, which maximally correlates with collected gaze features. Our model trained on combining collected and synthetic gaze data achieves SoTA performance on the MUStARD++ dataset. To the best of our knowledge, ours is the first predict-and-use model for sarcasm detection. We publicly release the code, gaze data, and our best models for further research."
featured: false
publication: "*Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing*"
url_pdf: "https://aclanthology.org/2023.emnlp-main.988.pdf"
url_video: "https://aclanthology.org/2023.emnlp-main.988.mp4"
tags: ["sarcasm detection", "multimodal", "gaze prediction", "machine learning"]
---