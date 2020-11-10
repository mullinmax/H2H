This programming language is designed for a few key traits:
  - small file size: tokens are typically just one character
  - deterministic: running a program twice with the same inputs will always yeild the same output
  - pipe-oreinted: the only io available to the language is stdin and stdout


In addition to these contraints the language also strives to be:
  - fast: leveraging the C++ compiler ensures good if not great speed
  - testable: each operation should be tested to ensure reliable performance
  - human readable: this is very much at odds with the small file sizes; however legible code is required for testing
