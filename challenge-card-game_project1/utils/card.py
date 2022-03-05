class Symbol:
    """Class defining a Symbol characterized by :
    - its color
    - its icon(♥, ♦, ♣, ♠)"""
    color = ["red", "black"]
    icon = ['\u2666', '\u2665', '\u2663','\u2660'] 
    def __init__(self, color: str, icon: str):
        """Constructor our class"""
        self.color = color
        self.icon = icon

    def __str__(self):
        """Method called during a conversion of the object into a chain"""
        return f"{self.color} {self.icon}"



class Card(Symbol): 
    """
    This class has a special attribute which is called value.
    value is the value of each card. 
    This class Inherits from Symbol and also this subclass has new attribute which is added to super class

    
    """
    value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    def __init__(self, color: str, icon: str, value: str) -> str:

        super().__init__(color, icon)
        self.value = value
        
    def __str__(self):
        """Method called during a conversion of the object into a chain"""
        return f"{Card.color[self.color]} {Card.icon[self.icon]} {Card.value[self.value]}"

