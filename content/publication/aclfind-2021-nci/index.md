---
title: "FrameNet-assisted Noun Compound Interpretation"
date: 2021-08-01T00:00:00
authors: ["Girishkumar Ponkiya", "Diptesh Kanojia", "Pushpak Bhattacharyya", "Girish Palshikar"]
publication_types: ["1"]
abstract: "Given a noun compound (NC), we address the problem of predicting the appropriate semantic label linking the constituents of the NC. This problem is called Noun Compound Interpretation (NCI). We use FrameNet as a semantic label repository. For example, given the noun compound (board approval), we predict the frame (DENY OR GRANT PERMISSION, as per FrameNet) as appropriate and the semantic role of the modifier word (AUTHORITY) as the semantic label linking board and approval; the resulting label is DENY OR GRANT PERMISSION:AUTHORITY. Our semantic label repository is very large (≈11k labels) compared to the NC data available for training (approx 1900). Thus, learning in this case, especially for unseen semantic labels, is hard. We propose to solve this problem by predicting semantic labels in a continuous label embedding space, which is novel. This embedding space is created by learning label embeddings using the FrameNet data. The embeddings are then used to train two separate models – one for predicting Frames and the other for FEs. As the label embedding space captures the semantics of the labels, using these embeddings enables generalizing well on unseen labels, thus achieving zero-shot learning. Our preliminary investigations show that the proposed approach performs well for unseen labels, achieving 5% and 2% points improvements over baselines for the frame and FE prediction, respectively. The study shows the promise of the use of continuous space embeddings for noun compound interpretation and points to the need for further investigation."

featured: false
publication: "*Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021*"
url_pdf: "files/aclfind-2021-nci.pdf"
tags: ["noun-compound", "deep learning", "framenet", "theoretical"]
url_pdf: "files/aclfind-2021-nci.pdf"
url_dataset: "https://www.cse.iitb.ac.in/~girishp/nc-dataset/"

---

