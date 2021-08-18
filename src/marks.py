class Marks:

    def __init__(self) -> None:
        self.__marks = []
        self.marksPercentage = []
    
    @classmethod
    def input():
        pass

    def calculate_average(self, marks: list):
        suma = 0 
        self.__marks = marks
        for i in range(len(self.__marks)):
            #self.__marks.append(float(input("nota: ")))
            self.marksPercentage.append(float(input("Porcentaje de la nota {}: ".format(i))))
            notaFinal = self.__marks[i] * self.marksPercentage[i]
            suma = suma + notaFinal
        total = suma / len(self.__marks)
        return total

    def marks_total_value(self) -> str:
        pass