---
title: "The Mind's Eye: A Multi-Faceted Reward Framework for Guiding Visual Metaphor Generation"
date: 2025-08-25T00:00:00
authors: ["Girish A Koushik", "Fatemeh Nazarieh", "Katherine Birch", "Shenbin Qian", "Diptesh Kanojia"]
publication_types: ["3"]
abstract: "Visual metaphor generation is a challenging task that aims to generate an image given an input text metaphor. Inherently, it needs language understanding to bind a source concept with a target concept, in a way that preserves meaning while ensuring visual coherence. We propose a self-evaluating visual metaphor generation framework that focuses on metaphor alignment. Our self-evaluation approach combines existing metrics with our newly proposed metaphor decomposition score and a meaning alignment (MA) metric. Within this setup, we explore two novel approaches: a training-free pipeline that explicitly decomposes prompts into source-target-meaning (S-T-M) mapping for image synthesis, and a complementary training-based pipeline that improves alignment using our proposed self-evaluation reward schema, without any large-scale retraining. On the held-out test set, the training-free approach surpasses strong closed baselines (GPT-4o, Imagen) on decomposition, CLIP, and MA scores, with the training-based approach close behind. We evaluate our framework output using a user-facing study, and observed that participants preferred GPT-4o overall, while our training-free pipeline led open-source methods and edged Imagen on abstract metaphors. Our analyses show S-T-M prompting helps longer or more abstract metaphors, with closed models excelling on short, concrete cases; we also observe sensitivity to sampler settings. Overall, structured prompting and lightweight RL perform metaphor alignment well under modest compute, and remaining gaps to human preference appear driven by aesthetics and sampling."
featured: false
publication: "*arXiv preprint arXiv:2508.18569*"
url_pdf: "https://arxiv.org/abs/2508.18569"
url_preprint: "https://arxiv.org/abs/2508.18569"
tags: ["visual metaphor generation", "reward framework", "image synthesis", "metaphor alignment"]
---