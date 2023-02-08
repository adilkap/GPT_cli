# GPT_cli

This script enables a user to use the power of GPT straight from a Command Line Interface.


## General Setup

Generate and copy an API Key through OpenAI at [this link](https://platform.openai.com/account/api-keys).

Add the API Token as an environment variable in your ```~/.bash_profile``` like below:
\n```export OPENAI_API_KEY=[API-KEY] ```


## Optional Setup

Add an alias to your program to access the script conveniently using:
```alias gpt="python3 .../gpt.py" ```

Then run ```source ~/.bash_profile``` to save your changes, or restart your session.


You should be up and running now by using ```gpt "..." ``` within your root directory!
