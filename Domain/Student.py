
#Clasa Student defineste cum arata un student, sablon,
class Student:
    def __init__(self, id_student: int, nume: str):
        """
            Constructorul clasei. Se apeleaza la crearea unui nou obiect Student.
        :param id_student: preconditii: ID-ul (trebuie sa fie int)
        :param nume: Numele Studentului (trebuie sa fie string)
        """
        #Atribute private, marcate cu (__)
        #Conceptie care inseamna ca nu ar trebui sa fie accesate direct
        self.__id_student = id_student
        self.__nume = nume
#=============GETTERS=============================================
    def get_id_student(self):
        """
        Returneaza id-ul studentului
        :return: int -ID
        """
        return self.__id_student

    def get_nume(self):
        """
        Returneaza numele studentului
        """
        return self.__nume
#===============SETTERS=====================================
    def set_nume(self, nume_nou: str):
        """
        Modifica nunmele studentului
        """
        self.__nume = nume_nou
    #id-ul nu il poti schimba(este definitiv), singura metoda ar fi stergerea si adaguarea unui nou student
    def set_id_student(self, id_nou):
        self.__id_student = id_nou

    def __str__(self):
        """
        Defineste cum arata obiectul cand este convertit in string, cand se printeaza in python totul este convertit in string si afisat
        :return:  string - reprezentarea in string a studentului
        """
        return f"ID:{self.__id_student} Nume: {self.__nume}"

    def __eq__(self, other):
        """
        Defineste egalitatea intre doua obiecte Student. Doi studenti sunt considerati egali daca au acelasi ID
        :param other:
        :return: True daca studentii sunt egali, iar False daca nu
        """
        if isinstance(other, Student):
            return self.get_id_student() == other.get_id_student()
        else:
            return False