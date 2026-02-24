+++

title = "Optimizing Large Language Models for Low-resource Quality Estimation"
date = 2025-12-24T12:00:00  # Schedule page publish date.
draft = false

# Talk start and end times.
# End time can optionally be hidden by prefixing the line with `#`.
time_start = 2025-12-24T12:00:00

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["Diptesh Kanojia"]

# Abstract and optional shortened version.
abstract = "Large Language Models (LLMs) are positioned as generalist models often claiming superlative performance on many Natural Language Processing (NLP) tasks. However, they tend to fail at Quality Estimation (QE) of Machine Translation (MT), particularly for low-resource languages. The talk investigates root causes of this disparity, such as tokenization inconsistencies arising from morphological richness in natural languages. To bridge this gap, the talk introduces strategies to embed annotation guidelines-based reasoning constraints directly in-context. Furthermore, our investigation on optimal cross-lingual alignment shows that intermediate Transformer layers help produce performant adapters. By attaching Low-Rank Adapter (LoRA) based regression heads to intermediate layers, we bypass the generation-specific biases of the final layer, efficiently outperforming standard instruction fine-tuning and SoTA encoders like COMETKiwi. Finally, via results from the WMT Unified Shared subtask on QE-informed Correction, we demonstrate that these precise estimations can guide LLMs to produce reliable corrections. We discuss how these signals help address the \"diminishing returns\" challenge, enabling models to improve fluent outputs without diverging from human references."
abstract_short = "Invited Talk | WAT 2025 | LLMs for Quality Estimation | Low-resource Languages"

# Name of event and optional event URL.
event = "Invited Talk @ The 12th Workshop on Asian Translation (WAT 2025)"
event_url = "#"

# Location of event.
location = "The 12th Workshop on Asian Translation 2025"

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
tags = ["talks", "invited-talk", "quality-estimation", "automatic-post-editing", "translation-quality", "large-language-models", "evaluation-and-correction"]

# Links (optional).
url_pdf = ""
url_slides = "files/LLMS4QE-WAT-2025.pdf"
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
