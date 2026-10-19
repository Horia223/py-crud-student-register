from Domain.Nota import Nota
from Repository.repository_errors import RepoError
class NotaRepository:
    def __init__(self):
        """
        Cream un dictionar pentru accesarea notelor cu id
        Cream un contor simplu care va fi incrementat cu 1 la fiecare nota adaguata
        """
        self.__id_contor = 0
        self.__note = {}

    def adauga(self, nota: Nota ):
        """
        Adauga o nota de tip nota in dictionar cheia fiind id ul
        Contorul este incrementat
        :param nota:
        :return:
        :raises:-
        """
        id_existent = nota.get_id_nota()
        if id_existent is None:
            self.__id_contor += 1
            nota.set_id_nota(self.__id_contor)
            self.__note[nota.get_id_nota()] = nota
        else:
            if id_existent in self.__note:
                raise RepoError("ID duplicat")
            self.__note[id_existent] = nota
            if id_existent > self.__id_contor:
                self.__id_contor = id_existent


    def cauta_dupa_id(self, id_nota):
        """
        Cauta dupa id daca exista nota in dictionar si o afiseaza, daca nu da raise RepoError
        :param id_nota:
        :return: nota (cu id ul aferent)
        :raises: RepoError
        """
        if id_nota not in self.__note:
            raise RepoError(f"Nota cu id ul {id_nota} nu a fost gasit!")

        return self.__note[id_nota]

    def sterge_dupa_id (self, id_nota):
        """
        Vom sterge dupa id nota, daca exista, daca nu va dat raise RepoError
        :param id_nota:
        :return: nota stearsa
        :raises: RepoError
        """
        self.cauta_dupa_id(id_nota)
        nota_sters = self.__note[id_nota]
        del self.__note[id_nota]
        return nota_sters

    def modifica(self, nota_modificata: Nota):
        """
        Modifica nota exista cu alt nota modificata, daca nu exista nota cu acel id, se va da raise la RepoError
        :param nota_modificata:
        :return: nota_veche
        :raises: RepoError
        """

        nota_veche = self.cauta_dupa_id(nota_modificata.get_id_nota())
        self.__note[nota_modificata.get_id_nota()] = nota_modificata
        return nota_veche

    def get_all_note(self):
        """
        :return: lista cu toate notele
        """

        return list(self.__note.values())
    #daca nu am fi converit cu list am fi returnat un obiect special numit dict_values
    #list converteste toate intr o lista standard, iar values() ne da toate valorile din dictionar, adica obiectele de tip Nota

    def size(self):
        """
        :return: returneaza numarul de note
        """
        return len(self.__note)

class NotaRepositoryFile(NotaRepository):
    def __init__(self, filename, repo_studenti, repo_discipline):
        """
        Avem nevoie de repo studenti si repo discipline pentru a putea
        cauta obiectele pe baza ID-urilor citite din fisier.
        """
        super().__init__()
        self.__filename = filename
        self.__repo_studenti = repo_studenti
        self.__repo_discipline = repo_discipline
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if line:

                        parti = line.split(",")
                        id_nota = int(parti[0])


                        id_student = int(parti[1])
                        id_disciplina = int(parti[2])
                        valoare_nota = float(parti[3])




                        student_obiect = self.__repo_studenti.cauta_dupa_id(id_student)
                        disciplina_obiect = self.__repo_discipline.cauta_dupa_id(id_disciplina)


                        nota = Nota(id_nota, student_obiect, disciplina_obiect, valoare_nota)


                        super().adauga(nota)
        except IOError:
            raise RepoError("Nu s-a putut citi fisierul de note.")
        except RepoError:
            # Daca un student sau o disciplina din fisier nu mai exista, dam eroare
            print(f"Eroare la incarcarea unei note")

    def __save_to_file(self):
        try:
            with open(self.__filename, "w", encoding="utf-8") as file:
                note = super().get_all_note()
                for nota in note:

                    line = str(nota.get_id_nota()) + "," + str(nota.get_student().get_id_student()) + "," + str(nota.get_disciplina().get_id_disciplina()) + "," + str(nota.get_nota()) + "\n"
                    file.write(line)
        except IOError:
            raise RepoError("Nu s-a putut scrie in fisierul de note.")

    def adauga(self, nota: Nota):
        super().adauga(nota)
        self.__save_to_file()

    def sterge_dupa_id(self, id_nota):
        nota_stearsa = super().sterge_dupa_id(id_nota)
        self.__save_to_file()
        return nota_stearsa

    def modifica(self, nota_modificata: Nota):
        nota_veche = super().modifica(nota_modificata)
        self.__save_to_file()
        return nota_veche







