---
title: "AV-GS: Learning Material and Geometry aware Priors for Novel View Acoustic Synthesis"
date: 2024-12-10T00:00:00
authors: ["Swapnil Bhosale", "Haosen Yang", "Diptesh Kanojia", "Jiankang Deng", "Xiatian Zhu"]
publication_types: ["1"]
abstract: "Novel view acoustic synthesis (NVAS) aims to render binaural audio at any target viewpoint, given a mono audio emitted by a sound source at a 3D scene. Existing methods have proposed NeRF-based implicit models to exploit visual cues as a condition for synthesizing binaural audio. However, in addition to low efficiency originating from heavy NeRF rendering, these methods all have a limited ability of characterizing the entire scene environment such as room geometry, material properties, and the spatial relation between the listener and sound source. To address these issues, we propose a novel Audio-Visual Gaussian Splatting (AV-GS) model. To obtain a material-aware and geometry-aware condition for audio synthesis, we learn an explicit point-based scene representation with an audio-guidance parameter on locally initialized Gaussian points, taking into account the space relation from the listener and sound source. To make the visual scene model audio adaptive, we propose a point densification and pruning strategy to optimally distribute the Gaussian points, with the per-point contribution in sound propagation (e.g., more points needed for texture-less wall surfaces as they affect sound path diversion). Extensive experiments validate the superiority of our AV-GS over existing alternatives on the real-world RWAS and simulation-based SoundSpaces datasets."
featured: false
publication: "*Advances in Neural Information Processing Systems*"
url_pdf: "https://proceedings.neurips.cc/paper_files/paper/2024/file/8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b-Paper-Conference.pdf"
url_preprint: "https://arxiv.org/abs/2406.08920"
url_slides: "https://neurips.cc/media/neurips-2024/Slides/96666.pdf"
url_poster: "https://neurips.cc/media/PosterPDFs/NeurIPS%202024/96666.png?t=1733151540.7388813"
tags: ["acoustic synthesis", "gaussian splatting", "novel view synthesis", "audio-visual"]
---