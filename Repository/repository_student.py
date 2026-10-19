from Domain.Student import Student
from Repository.repository_errors import RepoError


class StudentRepository:
    """
    Gestioneaza stocarea datelor despre studenti in memorie.
    Aici vom genera ID-urile automat (daca nu sunt furnizate),
    si vom salva, modifica, sterge si cauta studenti.
    """

    def __init__(self):
        """
        Cream un dictionar pentru a accesa rapid studentii dupa id.
        Cream un contor simplu, care va functiona prin incrementarea cu 1.
        """
        self.__studenti = {}
        self.__id_contor = 0

    def adauga(self, student: Student):
        """
        Adauga un student in dictionar.

        """
        id_existent = student.get_id_student()

        if id_existent is None:
            self.__id_contor += 1
            student.set_id_student(self.__id_contor)
            self.__studenti[self.__id_contor] = student
        else:
            if id_existent in self.__studenti:
                raise RepoError("ID duplicat")
            self.__studenti[id_existent] = student
            if id_existent > self.__id_contor:
                self.__id_contor = id_existent

    def cauta_dupa_id(self, id_student: int):
        """
        Verifica daca exista id-ul studentului in dictionar.
        Daca nu exista, se ridica RepoError.
        Daca exista, returneaza obiectul Student aferent id-ului.
        """
        if id_student not in self.__studenti:
            raise RepoError(f"Studentul cu id-ul {id_student} nu a fost gasit!")

        return self.__studenti[id_student]

    def sterge_dupa_id(self, id_student: int):
        """
        Folosind un id_student, sterge studentul aferent id-ului din dictionar.
        :return: studentul sters
        :raises: RepoError daca ID-ul nu exista
        """
        self.cauta_dupa_id(id_student)
        student_sters = self.__studenti[id_student]
        del self.__studenti[id_student]
        return student_sters

    def modifica(self, student_modificat: Student):
        """
        Modifica un student existent.
        :param student_modificat: obiectul Student cu datele noi
        :return: studentul vechi (inainte de modificare)
        :raises: RepoError, daca ID-ul nu exista
        """
        id_student = student_modificat.get_id_student()
        student_vechi = self.cauta_dupa_id(id_student)
        self.__studenti[id_student] = student_modificat
        return student_vechi

    def get_all_studenti(self):
        """
        Returneaza o lista cu toti studentii de tip obiect Student.
        """
        # daca nu am fi convertit cu list am fi returnat un obiect special dict_values
        # list converteste toate intr-o lista standard, iar values() ne da toate valorile din dictionar (Student)
        return list(self.__studenti.values())

    def size(self):
        """
        Returneaza numarul de studenti.
        """
        return len(self.__studenti)


class StudentRepositoryFile(StudentRepository):


    def __init__(self, filename):
        """
        :param filename: numele fisierului in care se salveaza
        """
        super().__init__()
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Incarca datele din fisier.
        Fisierul trebuie sa aiba cate un student pe linie
        :raises: RepoError daca exista probleme la citirea datelor
        """
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if line:
                        id_student, nume = line.split(",")
                        id_student = int(id_student)
                        student = Student(id_student, nume.strip())
                        super().adauga(student)
        except IOError:
            raise RepoError("Datele din fisier nu au putut sa fie citite")

    def adauga(self, student: Student):
        """
        Adauga un student si salveaza imediat modificarile in fisier.
        """
        super().adauga(student)
        self.__save_to_file()

    def sterge_dupa_id(self, id_student: int):
        """
        Sterge un student dupa ID si salveaza modificarile .
        """
        student_sters = super().sterge_dupa_id(id_student)
        self.__save_to_file()
        return student_sters

    def modifica(self, student_modificat: Student):
        """
        Modifica un student existent si salveaza modificarile
        """
        student_vechi = super().modifica(student_modificat)
        self.__save_to_file()
        return student_vechi

    def __save_to_file(self):
        """
        Salveaza toti studentii in fisier, cate unul pe linie.
        Format linie: id_student, nume
        :raises: RepoError daca exista probleme la scrierea in fisier
        """
        try:
            with open(self.__filename, "w", encoding="utf-8") as file:
                studenti = super().get_all_studenti()
                for student in studenti:
                    student_str = (
                        str(student.get_id_student()) + ","+ student.get_nume())
                    student_str += "\n"
                    file.write(student_str)
        except IOError:
            raise RepoError("Nu s-au putut salva datele in fisierul" + self.__filename)

