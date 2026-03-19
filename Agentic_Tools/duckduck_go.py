from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()
result = search_tool.invoke('ipl news')
print(result)
print(search_tool.name)
print(search_tool.description)
print(search_tool.args)
from langchain_community.tools import ShellTool
shell_tool = ShellTool()

results = shell_tool.invoke('ls')