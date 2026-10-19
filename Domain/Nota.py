
class Nota:
    def __init__(self, id_nota, student, disciplina, nota):
        """
        Constructorul clasei. Se apeleaza la crearea unui nou obiect a notei
        :param student:
        :param disciplina:
        :param nota:
        """
        self.__id_nota = id_nota
        self.__student = student
        self.__disciplina = disciplina
        self.__nota = nota

    def get_id_nota(self):
        return self.__id_nota

    def get_student(self):
        return self.__student

    def get_disciplina(self):
        return self.__disciplina

    def get_nota(self):
        return self.__nota


    def set_nota(self, nota_noua):
        self.__nota = nota_noua

    def set_id_nota(self, id_nou):
        self.__id_nota = id_nou

    def __eq__(self, other):
        """
        Defineste egalitatea intre doua obiecte din clasa Nota. Construita pe baza id ului
        :param other:
        :return:
        """
        if isinstance(other, Nota):
            return self.get_id_nota() == other.get_id_nota()
        else:
            return False
    def __str__(self):
        return f"{self.__student} \n {self.__disciplina} \n ID:{self.__id_nota} Nota:{self.__nota} "
















