# agentfromscratch

*************    code_for_class.py ****************

In this file, i have created a class with two functions:

We are passing two variables one after the other.
First variable is passed as system prompt.
secong variable is actual query to the LLM.

The agent class has a variable which is passed as system prompt
The call function has another variable (product)

The agent function can be initialized with system prompt: ex- provide a list of xxxx and that xxx can be passed in the call function.

This helps to reuse the class for different purposes. By changing the prompt we can get the LLM to answer based on the system prompt.