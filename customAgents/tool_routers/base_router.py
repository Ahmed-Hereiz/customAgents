import time


class BaseRouter:
    def __init__(self, exec_after: float = 0):
        self.exec_after = exec_after
        self.execution_time = None
        
    def exec_router(self):
        time.sleep(self.exec_after)
        self.execution_time = time.time()  # Record the execution time
        return self.execution_time
    
    def get_execution_time(self):
        """Returns the time at which the router was executed."""
        return self.execution_time
    
    def reset_execution(self):
        """Resets the execution time and exec_after value."""
        self.execution_time = None
        self.exec_after = 0
        
    def set_exec_after(self, exec_after: float):
        """Sets a new delay for execution."""
        self.exec_after = exec_after
        
    def __str__(self) -> str:
        return f"router will execute after {self.exec_after} seconds"
    
    def __repr__(self) -> str:
        return f"BaseRouter(exec_after={self.exec_after})"