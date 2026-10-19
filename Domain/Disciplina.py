
class Disciplina:


    def __init__(self, id_disciplina, nume, profesor):
        """
        Constructorul clasei. Se apeleaza la crearea unui nou obiect disciplina,
        :param id_disciplina:
        :param nume:
        :param profesor:
        """
        self.__id_disciplina = id_disciplina
        self.__nume = nume
        self.__profesor = profesor

    def __str__(self):
        """
        Defineste cum arata obiectul cand este convertit in string.
        :return: string - reprezentarea in string a disciplinei
        """
        return f"ID:{self.__id_disciplina} Disciplina:{self.__nume} Profesor:{self.__profesor}"

    def get_id_disciplina(self):
        return self.__id_disciplina

    def get_nume(self):
        return self.__nume

    def get_profesor(self):
        return  self.__profesor

    def set_nume(self, nume_nou):
        self.__nume = nume_nou

    def set_profesor(self, profesor_nou):
        self.__profesor = profesor_nou

    def set_id_disciplina(self, id_nou):
        self.__id_disciplina = id_nou

    def __eq__(self, other):
        """
        Defineste egalitatea intre doua obiecte din clasa Disciplina. Construita pe baza id ului
        :param other:
        :return: True daca cele doua obiecte au acelasi id. False daca nu
        """
        if isinstance(other, Disciplina):
            return self.get_id_disciplina() == other.get_id_disciplina()

        else:
            return False

