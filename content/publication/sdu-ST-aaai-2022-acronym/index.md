---
title: "Ensemble Approach to Acronym Extraction using Transformers"
date: 2021-12-11T00:00:00
authors: ["Prashant Sharma", "Hadeel Saadany", "Leonardo Zilio", "Diptesh Kanojia", "Constantin Orăsan"]
publication_types: ["1"]
abstract: "Acronyms are abbreviated units of a phrase constructed by using initial components of the phrase in a text. Automatic extraction of acronyms from a text can help various Natural Language Processing tasks like machine translation, information retrieval, and text summarisation. This paper discusses an ensemble approach for the task of Acronym Extraction, which utilises two different methods to extract acronyms and their corresponding long forms. The first method utilises a multilingual contextual language model and fine-tunes the model to perform the task. The second method relies on a convolutional neural network architecture to extract acronyms and append them to the output of the previous method. We also augment the official training dataset with additional training samples extracted from a series of open-access journals to help improve the task performance. Our dataset analysis also highlights the noise within the current task dataset. Our approach achieves the following macro-F1 scores on test data released with the task: Danish (0.74), English-Legal (0.72), English-Scientific (0.73), French (0.63), Persian (0.57), Spanish (0.65), Vietnamese (0.65). We release our code and models publicly."

featured: false
publication: "*Proceedings of the Thirty-sixth AAAI Conference on Artificial Intelligence (AAAI 2022) as a part of the SDU Workshop Shared Task*"
tags: ["acronym extraction", "shared task", "data analysis", "data augmentation", "ensemble approach"]
url_pdf: "files/sdu-ST-aaai-2022-acronym.pdf"
url_code: "https://github.com/dipteshkanojia/PR-AAAI22-SDU-ST1-AE"
#url_slides: ""
#url_video: ""
---
