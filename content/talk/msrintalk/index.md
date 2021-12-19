+++
title = "Quality Estimation for Machine Translation"
date = 2021-12-19T00:00:00  # Schedule page publish date.
draft = false

# Talk start and end times.
# End time can optionally be hidden by prefixing the line with `#`.
time_start = 2021-12-21T08:30:00
time_end = 2021-12-21T09:30:00

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["Diptesh Kanojia"]

# Abstract and optional shortened version.
abstract = "Current Machine Translation (MT) systems achieve very good results on a growing variety of language pairs and datasets. However, they are known to produce fluent translation outputs that can contain important meaning errors, thus undermining their reliability in practice. Quality Estimation (QE) is the task of automatically assessing the performance of MT systems at test time. Thus, in order to be useful, QE systems should be able to detect such errors. However, this ability is yet to be tested in the current evaluation practices, where QE systems are assessed only in terms of their correlation with human judgements. In this talk, we will discuss how we attempted to bridge this gap by proposing a general methodology for the adversarial testing of QE for MT. In this discussion, we first see that despite a high correlation with human judgements achieved by the recent SOTA, certain types of meaning errors are still problematic for QE to detect. We also discuss how the ability of a given model to discriminate between meaning-preserving and meaning-altering perturbations is predictive of its overall performance, thus potentially allowing us to compare the QE systems without relying on manual quality annotation. We also see possible future applications of this work and discuss various directions we are investigating to improve the performance of QE systems."

abstract_short = "Quality Estimation | Probing QE Systems | Adversarial Evaluation | NLP"

# Name of event and optional event URL.
event = "Invited talk @ Microsoft Research, Bangalore, India"
event_url = "#"

# Location of event.
location = "Bangalore, India (Online)"

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
tags = ["talks", "cognate detection", "semantics", "distributional semantics"]

# Links (optional).
url_pdf = ""
url_slides = ""
url_video = ""
url_code = ""

# Does the content use math formatting?
math = true

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
[image]
  # Caption (optional)
  caption = ""

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = "Right"
+++
