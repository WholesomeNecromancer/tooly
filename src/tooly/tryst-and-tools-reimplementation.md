# Problems with current `tryst` approach

If I want to dynamically load `main()` from some tool, I may that tool to have a class.

This begs the question: why didn't I just make `tryst` more like something someone would **inherit from and override** rather than a procedural side-along to use occasionally? Why did I go backward, rather than using fairly obvious OOP?

It might be time to re-engineer tryst as a class, so that implementing a new tool might take on a form more like this:

```
from tryst import Tryst

class mytool(Tryst):
    def main(self, inputs = None):
        # Do your main here
    
```
which might reduce boilerplate code.

In the end, users would simply add `if __name__ == "__main__": mytool().main()` to the bottom of their file and boom, done.

This would allow us to call `mytool.main(tooltryst, requestinputs)` from our Flask app, tooly.
