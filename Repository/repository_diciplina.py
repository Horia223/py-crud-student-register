from Domain.Disciplina import Disciplina
from Repository.repository_errors import RepoError
class DisciplinaRepository:
    """

    """
    def __init__(self):
        self.__discipline = {}
        self.__id_contor = 0

    def adauga(self, disciplina: Disciplina):
        """
        Adauga o disciplina in dictionar
        :param disciplina:
        :return:
        """
        """
        if disciplina.get_id_disciplina() in self.__discipline:
            raise RepoError("Exista disciplina cu acest id")
        """
        id_existent = disciplina.get_id_disciplina()
        if id_existent is None:
            self.__id_contor += 1
            disciplina.set_id_disciplina(self.__id_contor)
            self.__discipline[self.__id_contor] = disciplina
        else:
            if id_existent in self.__discipline:
                raise RepoError("ID duplicat!")
            self.__discipline[id_existent] = disciplina
            if id_existent > self.__id_contor:
                self.__id_contor = id_existent




    def cauta_dupa_id(self, id_disciplina: int):
        """
        Cauta daca exista un obiuect cu ID ul existent
        :param id_disciplina:
        :return: Disciplina gasita cu acel ID
        :raises: RepoError: Daca disciplina cu ID-ul dat nu exista
        """
        if id_disciplina not in self.__discipline:
            raise RepoError(f"Disciplina cu ID-ul {id_disciplina} nu a fost gasit!")
        return self.__discipline[id_disciplina]

    def sterge_dupa_id(self, id_disciplina):
        """
        Sterge un obiect existent cu ID-ul specificat
        :param id_disciplina:
        :raises: RepoError: Din functia cauta_dupa_id daca nu exista obiectul cu ID ul specificat
        :return:
        """
        self.cauta_dupa_id(id_disciplina)
        disciplina_stearsa = self.__discipline[id_disciplina]
        del self.__discipline[id_disciplina]
        return disciplina_stearsa

    def modifica(self, disciplina_modificat: Disciplina):
        """
        Modifica o disciplina existenta
        :param disciplina_modificat: Obiectul de tip Disciplina cu datele noi
        :return:
        :raises: RepoError: Apare atunci nu este un obiect cu ID-ul specificat
        """
        id_disciplina = disciplina_modificat.get_id_disciplina()
        self.cauta_dupa_id(id_disciplina)
        disciplina_veche =  self.__discipline[id_disciplina]
        self.__discipline[id_disciplina] = disciplina_modificat
        return disciplina_veche


    def get_all_discipline(self):
        """
        Returneaza o lista cu toate obiectele
        :return:
        """
        return list(self.__discipline.values())

    def size(self):
        """
        Returneaza numarul de discipline in dictionar
        :return:
        """
        return len(self.__discipline)


class DisciplinaRepositoryFile(DisciplinaRepository):
    def __init__(self, filename):
        super().__init__()
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Incara datele din fisier
        :return:
        :raises: RepoError daca exista probleme la citirea datelor din fisier
        """
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if line:
                        id_disc, nume, profesor = line.split(",")
                        id_disc = int(id_disc)
                        disciplina = Disciplina(id_disc, nume.strip(), profesor.strip())
                        super().adauga(disciplina)
        except IOError:
            raise RepoError("Datele din fisier nu au putut sa fie citite")

    def adauga(self, disciplina: Disciplina):
        super().adauga(disciplina)
        self.__save_to_file()

    def sterge_dupa_id(self, id_disciplina):
        disciplina_stearsa = super().sterge_dupa_id(id_disciplina)
        self.__save_to_file()
        return disciplina_stearsa

    def modifica(self, disciplina_modificat: Disciplina):
        disciplina_veche = super().modifica(disciplina_modificat)
        self.__save_to_file()
        return disciplina_veche

    def __save_to_file(self):
        """
        Salveaza datele in fisier
        :return:
        :raises: RepoError daca exista
        """
        try:
            with open(self.__filename, "w", encoding="utf-8") as file:
                discipline = super().get_all_discipline()
                for disciplina in discipline:
                    disciplina_str = str(disciplina.get_id_disciplina()) + ","+ disciplina.get_nume() + "," + disciplina.get_profesor()

                    disciplina_str += "\n"
                    file.write(disciplina_str)
        except IOError:
            raise RepoError("Nu s-au putut salva datele in fisierul"+ self.__filename)









