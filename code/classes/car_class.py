class Car:
    def __init__(self, name: str, orientation: str, col: int, row: int, length: int) -> None:
        # set demographics
        self.name = name
        self.col = col
        self.row = row
        self.length = length
        
        if orientation.upper() not in ("H", "V"):
            raise ValueError("Orientation must be 'H' or 'V'")
        
        self.orientation = orientation.upper()

        # initialize current position
        self.current_coördinates: list[list] = self.get_initial_coördinates()

            
    def get_initial_coördinates(self) -> list[list]:
        """
        Return initial coördinates of car
        """
        coördinates = []

        if self.orientation == 'H':
            for i in range(self.length):
                coördinates.append([self.row, self.col + i])
        else:
            for i in range(self.length):
                coördinates.append([self.row + i, self.col])       

        return coördinates
    
    def get_current_coördinates(self):
        return(self.current_coördinates)
