---
title: "Quality-Aware Self-Correcting Speech Translation on an Edge Device"
date: 2026-10-06T00:00:00
authors: ["Zubair Ajmal Farooq", "Diptesh Kanojia"]
publication_types: ["3"]
abstract: "We present a fully offline speech-to-speech translation pipeline that runs on a Jetson Nano (4 GB) and corrects its own weak translations without retraining. A Whisper-tiny ASR feeds an Opus-MT translator; multilingual BERT cosine similarity acts as a Quality Estimation (QE) gate, triggering a secondary-pass when confidence falls below a pre-defined threshold. We compare three correction methods: QE reranking (M1), Minimum Bayes-Risk decoding (M2), and constrained beam search (M3). On 1,012 FLORES-200 sentences (English-Spanish), M2 produces statistically significant improvements over greedy decoding on BLEU (+0.67, p<0.001), ChrF (+0.51, p<0.001), and COMET (+0.0020 at N=3, p=0.002); M1 yields no significant gains, and M3 is significantly worse than baseline (p>0.99). Our central finding is that QE functions effectively as a gate but poorly as a ranker: removing the QE model from candidate selection (M1 to M2) does not hurt quality and frees 680 MB from the critical path. Using a gain-to-edit ratio adapted from the post-editing-effort literature, we further show that smaller candidate pools (N=3) yield more surgical corrections with better semantic adequacy, while larger pools (N=10) maximise lexical reward. We release the system and demonstrate live translation across six language pairs."
featured: false
publication: "*arXiv preprint arXiv:2610.07545*"
url_pdf: "https://arxiv.org/pdf/2610.07545.pdf"
url_preprint: "https://arxiv.org/abs/2610.07545"
url_code: "https://github.com/surrey-nlp/speech-translation_edge_device"
links:
- name: "Local PDF"
  url: "files/farooq-2026-quality.pdf"
tags: ["speech translation", "edge computing", "quality estimation", "minimum Bayes-risk decoding"]
---
