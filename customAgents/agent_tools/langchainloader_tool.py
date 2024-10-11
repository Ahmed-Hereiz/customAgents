from langchain.tools import BaseTool
from typing import Type, Any

class LangchainToolLoader(BaseTool):
    def __init__(self, tool_class: Type[BaseTool], *args, **kwargs):
        self.tool = tool_class(*args, **kwargs)
        super().__init__(
            name=self.tool.name,
            description=self.tool.description,
            return_direct=self.tool.return_direct,
            verbose=self.tool.verbose,
            callbacks=self.tool.callbacks,
            callback_manager=self.tool.callback_manager,
            tags=self.tool.tags,
            metadata=self.tool.metadata,
        )

    def _run(self, *args: Any, **kwargs: Any) -> Any:
        return self.tool.run(*args, **kwargs)

    def _arun(self, *args: Any, **kwargs: Any) -> Any:
        return self.tool.arun(*args, **kwargs)

    def execute_func(self, *args: Any, **kwargs: Any) -> Any:
        return self._run(*args, **kwargs)


