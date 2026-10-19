from Domain.Student import Student
from Repository.repository_student import StudentRepository
from Domain.validator import StudentValidator
import random

class ServiceStudenti:
    """

    """
    def __init__(self, repo: StudentRepository , validator: StudentValidator):
        self.__repo = repo
        self.__validator = validator

    def adaugare_student(self, nume_student: str):
        """
        Adauga un student
        :param nume_student:
        :return: -
        :raises:RepoError daca studentul exista deja (dar cum am implementat id automat, nu o sa fie cazul)
                ValueError daca studentul este invalid
        """
        student = Student(None, nume_student)
        self.__validator.validate(student)
        self.__repo.adauga(student)

    def sterge_student(self, id_student):
        """
        Sterge studentul dupa ID
        :param id_student:
        :return: studetnul sters
        raises: RepoError, daca nu exista studentul cu ID ul specificat
        """
        return self.__repo.sterge_dupa_id(id_student)

    def modifica_student(self, id_student, nume_nou):
        """
        Modifica un student deja existent
        :param id_student:
        :param nume_nou:
        :return: studenul vechi
        :raises: RepoError daca nu exista studentul cu ID ul specificat
                 ValueError daca studentul este invalid
        """

        student_nou = Student(id_student, nume_nou)
        self.__validator.validate(student_nou)
        student_vechi = self.__repo.cauta_dupa_id(id_student)
        self.__repo.modifica(student_nou)
        return student_vechi
    def cauta_dupa_id(self, id_student):
        """
        Cauta daca exista un student cu id ul dat
        :param id_student:
        :return:Studentul cu id ul aferent
        :raises: RepoError: Daca id ul nu exista
        """
        return self.__repo.cauta_dupa_id(id_student)

    def get_studenti(self):
        """
        Returneaza lista de studenti
        :return:
        """
        return self.__repo.get_all_studenti()

    def get_numar_studenti(self):
        """
        Returneaza numarul de studenti
        :return:
        """
        return self.__repo.size()

    def adaugare_studenti_random(self, numar:int):
        """

        :param numar:
        :return:
        :raises:RepoError daca studentul exista deja (dar cum am implementat id automat, nu o sa fie cazul)
                ValueError daca studentul este invalid (Daca e generat nu are cum)
        """
        while numar:
            nume = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k =7))
            separator = " "
            prenume = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k =7))
            nume_intreg = nume + separator + prenume
            self.adaugare_student(nume_intreg)
            numar = numar - 1







