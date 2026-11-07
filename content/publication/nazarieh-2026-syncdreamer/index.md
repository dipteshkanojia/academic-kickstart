---
title: "SyncDreamer: Controllable and Expressive Avatar Generation Beyond the Talking Head"
date: 2026-06-18T00:00:00
authors: ["Fatemeh Nazarieh", "Zhenhua Feng", "Diptesh Kanojia", "Josef Kittler", "Muhammad Awais"]
publication_types: ["1"]
abstract: "Generating realistic and expressive audio-driven talking avatars remains a central challenge in digital human synthesis. Existing methods often depend on intermediate representations such as pose estimations for natural body motion, which restricts flexibility and adds visual distortions. Moreover, most audio-driven approaches rely on discrete emotion classifiers or text labels to regulate facial expression, reducing complex affective dynamics to coarse categories such as happy, sad, or angry. Such categorical supervision fails to capture the continuous and fine-grained speech dynamics (rhythm, energy, intensity) resulting in limited synchronization and emotionally shallow motion. To overcome these limitations, we present SyncDreamer, a unified Diffusion Transformer framework that generates identity-preserving and emotionally expressive talking avatars from only a single image, speech audio, and text prompt. We propose a visual adapter with Attention Localization Loss to maintain identity fidelity, further incorporating an audio dynamics encoder for rhythm- and emotion-aware motion, and an RL-based Cross-Modal Prompt Enhancer grounding textual cues in visual context for fine-grained motion control. Extensive experiments on portrait and full-body benchmarks demonstrate state-of-the-art performance in realism, synchronization accuracy, and semantic controllability, establishing a scalable foundation for expressive digital avatars in interactive and creative applications."
featured: false
publication: "*Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*"
url_pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Nazarieh_SyncDreamer_Controllable_and_Expressive_Avatar_Generation_Beyond_the_Talking_Head_CVPR_2026_paper.pdf"
url_project: "https://fnazarieh.github.io/SyncDreamerWeb/"
links:
- name: "Local PDF"
  url: "files/nazarieh-2026-syncdreamer.pdf"
tags: ["avatar generation", "talking head", "diffusion transformer", "multimodal generation", "CVPR"]
---
