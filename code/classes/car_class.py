class Car:
    def __init__(self, name: str, orientation: str, col: int, row: int, length: int) -> None:
        """
        Set all attributes of a car.
        """
        # set name, column, row, length
        self.name = name
        self.col = col
        self.row = row
        self.length = length
        
        # set orientation (horizontal ot vertical)
        if orientation.upper() not in ("H", "V"):
            raise ValueError("Orientation must be 'H' or 'V'")
        
        self.orientation = orientation.upper()

        # set current position
        self.current_coördinates: list[list] = self.get_initial_coördinates()

            
    def get_initial_coördinates(self) -> list[list]:
        """
        method to return initial coördinates of a car.
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
