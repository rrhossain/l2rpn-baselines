__all__ = [
    "TemplateBaseline",
    "TemplateBaseline_eval",
    "TemplateBaseline_train"
]

from l2rpn_baselines.Template.TemplateBaseline import TemplateBaseline
from l2rpn_baselines.Template.evaluate import evaluate as TemplateBaseline_eval
from l2rpn_baselines.Template.train import train as TemplateBaseline_train

"""
In the __init__ file, it is expected to export 3 classes with names that depends on the name you gave to your baseline.
For example, say you chose to write a baseline with the awesome name "XXX" (what an imagination!) you should export
in this __init__.py file:

- `XXXBaseline` [**mandatory**] contains the definition of your baseline. It must follow the directives
   given in "TemplateBaseline.py"
- `XXXBaseline_eval` [**mandatory**] contains the script to evaluate the performance of this baseline. It must
  follow the directive in "evaluate.py"
- `XXXBaseline_train` [**optional**] contains the script to train your baseline. If provided, it must follow
  the directives given in "train.py"
  
See the import above for an example on how to export your scripts properly.
"""
