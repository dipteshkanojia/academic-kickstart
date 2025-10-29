---
title: "DiffSED: Sound Event Detection with Denoising Diffusion"
date: 2024-03-24T00:00:00
authors: ["Swapnil Bhosale", "Sauradip Nag", "Diptesh Kanojia", "Jiankang Deng", "Xiatian Zhu"]
publication_types: ["1"]
abstract: "Sound Event Detection (SED) aims to predict the temporal boundaries of all the events of interest and their class labels, given an unconstrained audio sample. Taking either the split-and-classify (i.e., frame-level) strategy or the more principled event-level modeling approach, all existing methods consider the SED problem from the discriminative learning perspective. In this work, we reformulate the SED problem by taking a generative learning perspective. Specifically, we aim to generate sound temporal boundaries from noisy proposals in a denoising diffusion process, conditioned on a target audio sample. During training, our model learns to reverse the noising process by converting noisy latent queries to the ground-truth versions in the elegant Transformer decoder framework. Doing so enables the model generate accurate event boundaries from even noisy queries during inference. Extensive experiments on the Urban-SED and EPIC-Sounds datasets demonstrate that our model significantly outperforms existing alternatives, with 40+% faster convergence in training. Code: https://github.com/Surrey-UPLab/DiffSED"
featured: false
publication: "*Proceedings of the AAAI Conference on Artificial Intelligence*"
url_pdf: "https://ojs.aaai.org/index.php/AAAI/article/view/27837"
url_code: "https://github.com/Surrey-UPLab/DiffSED"
url_slides: "files/DiffSED-slides.pdf"
url_poster: "https://underline.io/lecture/93027-diffsed-sound-event-detection-with-denoising-diffusion"
tags: ["sound event detection", "denoising diffusion", "generative learning"]
---