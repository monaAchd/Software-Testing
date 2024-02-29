import unittest
import rock_paper_scissors

# Mona Achaaoud

class rockpaperTesting(unittest.TestCase):

    def test_Data(self): 
        #Arrange
        x = "a"
        y = 1

        #Act
        receive = rock_paper_scissors.Game(x, y)

        #Assert
        self.assertEqual("Number must be between 1-3", receive)

    def test_Number(self): 
        #Arrange
        x = 5
        y = 1

        #Act
        receive = rock_paper_scissors.Game(x, y)

        #Assert
        self.assertEqual("Number must be between 1-3", receive)

    def test_Lost(self): 
        #Arrange
        x = 2
        y = 3

        #Act
        receive = rock_paper_scissors.Game(x, y)

        #Assert
        self.assertEqual("You loose", receive)

    def test_Win(self): 
        #Arrange
        x = 2
        y = 1

        #Act
        receive = rock_paper_scissors.Game(x, y)

        #Assert
        self.assertEqual("You win", receive)

        

if __name__ == "__main__":
   unittest.main()

