+++
title = "ALOPE: Adaptive Layer Optimization for Translation Quality Estimation using Large Language Models"
date = 2025-10-23T00:00:00  # Schedule page publish date.
draft = false

# Talk start and end times.
# End time can optionally be hidden by prefixing the line with `#`.
time_start = 2025-10-23T14:00:00
time_end = 2025-10-23T15:00:00

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["Archchana Sindhujan", "Diptesh Kanojia"]

# Abstract and optional shortened version.
abstract = "Large Language Models (LLMs) have shown remarkable performance across a wide range of natural language processing tasks. Quality Estimation (QE) for Machine Translation (MT), which assesses the quality of a source-MT pair without relying on reference translations, remains a challenging cross-lingual task for LLMs. The challenges stem from the inherent limitations of existing LLM-based QE systems, which are pre-trained for causal language modelling rather than regression-specific tasks, further elevated by the presence of low-resource languages given pre-training data distribution. This paper introduces ALOPE, an adaptive layer-optimization framework designed to enhance LLM-based QE by restructuring Transformer representations through layer-wise adaptation for improved regression-based prediction. Our framework integrates low-rank adapters (LoRA) with regression task headers, leveraging select pre-trained Transformer layers for improved cross-lingual alignment. In addition to the layer-specific adaptation, ALOPE introduces two strategies—dynamic weighting, which adaptively combines representations from multiple layers, and multi-head regression, which aggregates regression losses from multiple heads for improved prediction. Our framework shows improvements over various existing LLM-based QE approaches. Empirical evidence suggests that intermediate Transformer layers in LLMs provide contextual representations that are more aligned with the cross-lingual nature of the QE task. Our resultant models and framework code is publicly available for further research, also allowing to scale any existing LLM-based MT frameworks to be equipped with QE capabilities."
abstract_short = "NLP Café Talk | ALOPE | Quality Estimation | LLMs"

# Name of event and optional event URL.
event = "NLP Café @ CTS, University of Surrey"
event_url = "https://nlp-at-cts.dinel.org.uk/"

# Location of event.
location = "Centre for Translation Studies, University of Surrey"

# Is this a selected talk? (true/false)
selected = true

# Projects (optional).
#   Associate this talk with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["deep-learning"]` references 
#   `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects = []

# Tags (optional).
#   Set `tags = []` for no tags, or use the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["talks", "nlp-cafe", "quality-estimation", "large-language-models", "machine-translation"]

# Links (optional).
url_pdf = ""
url_slides = "files/NLPCafe-ALOPE.pdf"
url_video = ""
url_code = ""

# Does the content use math formatting?
math = false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
[image]
  # Caption (optional)
  caption = ""

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = "Right"
+++