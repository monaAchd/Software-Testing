import unittest
import triangle

# Mona Achaaoud
class triangleTesting(unittest.TestCase):
 def test_IsEquilateral(self):
      #Arrange
      a = 5
      b = 5
      c = 5

      #Act
      receive = triangle.IsEquilateral(a, b, c)

      #Assert
      self.assertEqual('Triangle is Equilateral.', receive)

 def test_IsIsosceles(self):
      #Arrange
      a = 6
      b = 6
      c = 12

      #Act
      receive = triangle.IsIsosceles(a, b, c)

      #Assert
      self.assertEqual('Triangle is Isosceles.', receive)

 def test_Scalane(self):
      #Arrange
      a = 4
      b = 8
      c = 6

      #Act
      receive = triangle.Scalane(a, b, c)

      #Assert
      self.assertEqual('Triangle is Scalane', receive)

if __name__ == "__main__":
   unittest.main()


  