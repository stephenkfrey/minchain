# minchain


Automatically help humans find codebases/tools to solve the task at hand.

Problem: There are so many tools and repositories coming out. If I could access them in the moment, or eventually if an agent could access the right tool at the right time to include in its own code, that would help. 

This tool: 
- takes in a description of a problem that the user is trying to solve
- generates a broad list of search queries that may find related tools
- compiles the READMEs of all the repositories that come up from those search queries
- evaluates each README for its potential to help with the problem
- returns a list of the repositories most relevant to the problem, with steps for how the user or agent could use that tool

![image](github_tool/github_search_auto.png)
