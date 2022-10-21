class CountingStopwatch():
    
    def __init__(self):
        # Allow superclass to do its initialization of the
        # inherited fields
        super().__init__()
        # Set number of starts to zero
        self.__count = 0
        
    def start(self):
        # Let superclass do its start code
        super().start()
        # Count this start message
        self.__count += 1
        
    def reset(self):
        # Let superclass reset the inherited fields
        super().reset()
        # Reset new field that the base class method does not know about
        self.__count = 0
        
    def count(self):
        return self.__count
