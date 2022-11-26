+++
title = "Quality Estimation"
date = 2022-11-15T00:00:00  # Schedule page publish date.
draft = false

# Talk start and end times.
# End time can optionally be hidden by prefixing the line with `#`.
time_start = 2022-11-15T09:00:00
time_end = 2022-11-15T10:00:00

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["Diptesh Kanojia"]

# Abstract and optional shortened version.
abstract = "In this talk, I discuss the Quality Estimation (QE) for Machine Translation (MT). I discuss the basics of the QE task, and the QE shared task organized every year. Further, the discussion get into how current MT systems achieve very good results on a growing variety of language pairs and datasets. However, they are known to produce fluent translation outputs that can contain important meaning errors, thus undermining their reliability in practice. Quality Estimation (QE) is the task of automatically assessing the performance of MT systems at test time. Thus, in order to be useful, QE systems should be able to detect such errors. However, this ability is yet to be tested in the current evaluation practices, where QE systems are assessed only in terms of their correlation with human judgements. In this talk, we will discuss how we attempted to bridge this gap by proposing a general methodology for the adversarial testing of QE for MT. In this discussion, we first see that despite a high correlation with human judgements achieved by the recent SOTA, certain types of meaning errors are still problematic for QE to detect. We also discuss how the ability of a given model to discriminate between meaning-preserving and meaning-altering perturbations is predictive of its overall performance, thus potentially allowing us to compare the QE systems without relying on manual quality annotation."

abstract_short = "Quality Estimation | Natural Language Processing | Guest Lecture"

# Name of event and optional event URL.
event = "Guest Lecture @ KIT's College of Engineering, Maharashtra, India"
event_url = "#"

# Location of event.
location = "University of Surrey, United Kingdom (Online)"

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
tags = ["talks", "quality estimation", "machine translation", "adversarial evaluation", "probing systems"]

# Links (optional).
url_pdf = ""
url_slides = "files/kitcoe-guestlec-qe4mt.pdf"
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
