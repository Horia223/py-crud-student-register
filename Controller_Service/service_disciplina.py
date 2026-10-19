from Repository.repository_diciplina import DisciplinaRepository
from Domain.validator import DisciplinaValidator
from Domain.Disciplina import Disciplina
class ServiceDisciplina:
    def __init__(self, repo:DisciplinaRepository, validator:DisciplinaValidator):
        self.__repo =  repo
        self.__validator =  validator

    def adaugare_disciplina(self, nume_disciplina, nume_profesor):
        """
        :param nume_disciplina:
        :param nume_profesor:
        :return:
        :raises: ValueError: Daca informatiile nu sunt corecte pentru disciplina
        """
        disciplina = Disciplina(None, nume_disciplina, nume_profesor)
        self.__validator.validate(disciplina)
        self.__repo.adauga(disciplina)

    def sterge_disciplina(self, id_disciplina):
        """

        :param id_disciplina:
        :return:Disciplina stearsa
        :raises:RepoError: Daca nu exista disciplina cu id ul dat
        """
        return self.__repo.sterge_dupa_id(id_disciplina)

    def modifica_disciplina(self, id_disciplina, nume_disciplina_nou, nume_profesor_nou):
        """
        Modifica o disciplina existent
        :param: id_disciplina
        :param: nume_disciplina_noi
        :param: nume_profesor_nou
        :return:Disciplina veche, care a fost modificata
        :raises: RepoError:Daca nu exista disciplina cu id ul dat
                 ValueError: Daca datele disciplinei noi nu sunt valide
        """
        disciplina_noua = Disciplina(id_disciplina, nume_disciplina_nou, nume_profesor_nou)
        self.__validator.validate(disciplina_noua)
        disciplina_veche = self.__repo.cauta_dupa_id(id_disciplina)
        self.__repo.modifica(disciplina_noua)
        return disciplina_veche
    def cauta_dupa_id(self, id_disciplina):
        """
        Cauta daca exista o disciplina cu id ul dat
        :param id_disciplina:
        :return:Studentul cu id ul aferent
        :raises: RepoError: Daca id ul nu exista
        """
        return self.__repo.cauta_dupa_id(id_disciplina)

    def get_discipline(self):
        """
        Returneaza lista de discipline
        :return: lista de discipline
        """
        return self.__repo.get_all_discipline()

    def get_numar_discipline(self):
        """
        Returneaa numarul de discipline
        :return:Numarul de discipline
        """
        return self.__repo.size()







