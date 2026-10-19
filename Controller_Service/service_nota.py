from Domain.Nota import Nota
from Repository.repository_nota import NotaRepository
from Repository.repository_student import StudentRepository
from Repository.repository_diciplina import DisciplinaRepository
from Domain.validator import NotaValidator


class ServiceNota:
    def __init__(self, repo: NotaRepository, val: NotaValidator, repo_student: StudentRepository,
                 repo_disciplina: DisciplinaRepository):
        self.__repo = repo
        self.__val = val
        self.__repo_student = repo_student
        self.__repo_disciplina = repo_disciplina

    def adaugare_nota(self, id_student, id_disciplina, nota):
        """

        :param id_student:
        :param id_disciplina:
        :param nota:
        :return:
        :raises: ValueError: Daca informatiile sunt incorecte
                 RepoError: Daca nu se gaseste vreun obiect cu acel id
        """
        student = self.__repo_student.cauta_dupa_id(id_student)
        disciplina = self.__repo_disciplina.cauta_dupa_id(id_disciplina)
        nota_o = Nota(None, student, disciplina, nota)
        self.__val.validate(nota_o)
        self.__repo.adauga(nota_o)

    def sterge_nota(self, id_nota):
        """

        :param id_nota:
        :return: Nota stearsa
        :raises: RepoError: Daca nu exista nota cu id ul dat
        """
        return self.__repo.sterge_dupa_id(id_nota)

    def modifica_nota(self, id_nota, nota_noua):
        """
        Modifica o nota existenta
        :param id_nota:
        :param nota_noua:
        :return: Nota veche, care a fost modificata
        :raises:RepoError: daca nu exista nota cu id ul dat
                ValueError: daca informatiile sunt nevalide
        """
        nota_veche = self.__repo.cauta_dupa_id(id_nota)
        student = nota_veche.get_student()
        disciplina = nota_veche.get_disciplina()
        nota_noua_o = Nota(id_nota, student, disciplina, nota_noua)
        self.__val.validate(nota_noua_o)
        self.__repo.modifica(nota_noua_o)
        return nota_veche

    def cauta_dupa_id(self, id_nota):
        """
        Cauta daca exista o nota cu id ul dat
        :param id_nota:
        :return: Nota cu id ul aferent
        :raises: RepoError: Daca id ul nu exista
        """
        return self.__repo.cauta_dupa_id(id_nota)

    def get_numar_note(self):
        """
        :return: Returneaza numarul de note
        """
        return self.__repo.size()

    def get_note_student_la_disciplina(self, id_student, id_disciplina):
        """
        Returneza o lista cu note tip nota afeerente unui student la o disciplina anume
        :param id_student:
        :param id_disciplina:
        :return: note_filtrate
        """
        student = self.__repo_student.cauta_dupa_id(id_student)
        disciplina = self.__repo_disciplina.cauta_dupa_id(id_disciplina)
        toate_notele = self.__repo.get_all_note()
        note_filtrate = []

        for nota in toate_notele:
            if nota.get_student() == student and nota.get_disciplina() == disciplina:
                note_filtrate.append(nota)
        return note_filtrate

    def get__all_note(self):
        """
        :return: Returneaza o lista cu toate obiectele nota
        """

        return self.__repo.get_all_note()

    def get_statistica_note_disciplina(self, id_disciplina):
        """
        Returneaza o lista cu notele la o anumita disciplina.
        Lista este ordonata alfabetic dupa numele studentului,
        iar daca numele este acelasi, dupa valoarea notei
        :param id_disciplina:
        :return:note_filtrate
        """
        toate_notele = self.__repo.get_all_note()
        note_filtrate = []
        for nota in toate_notele:
            if nota.get_disciplina().get_id_disciplina() == id_disciplina:
                note_filtrate.append(nota)

        note_filtrate.sort(key=lambda x: (x.get_student().get_nume(), x.get_nota()))

        return note_filtrate

    def get_statistica_top_studenti(self):
        """
        Returneaza primii 20 la suta studenti ordonati dupa media la toate disciplinele

        :return:lista_finala
        """
        toate_notele = self.__repo.get_all_note()
        studenti_nota = {}
        for nota in toate_notele:
            id_student = nota.get_student().get_id_student()
            if id_student not in studenti_nota:
                studenti_nota[id_student] = {"student": nota.get_student(), "lista_note": []}
            studenti_nota[id_student]["lista_note"].append(nota.get_nota())
        # note organizate frumos la fiecare student de la fiecare disciplina
        lista_medii = []
        for id_student, date in studenti_nota.items():
            note_student = date["lista_note"]

            media = sum(note_student) / len(note_student)
            lista_medii.append({"student": date["student"], "medie": media})

        lista_medii.sort(key=lambda x: x["medie"], reverse=True)

        nr_studenti = len(lista_medii)
        returnare_la_suta_20 = int(nr_studenti * 0.2)

        lista_finala = []
        for i in range(returnare_la_suta_20):
            lista_finala.append(lista_medii[i])

        return lista_finala

    def numar_note_student(self, id_student):
        """
        Returneaza numarul de note pe care le are un student
        :param id_student:
        :return: nr
        """
        lista_toate_note = self.get__all_note()
        nr = 0
        for nota in lista_toate_note:
            if nota.get_student().get_id_student() == id_student:
                nr += 1
        return nr

    def numar_note_disciplina(self, id_disciplina):
        """
        Returneaza nr de note pe care le are o disciplina
        :param id_disciplina:
        :return: nr
        """
        lista_toate_note = self.get__all_note()
        nr = 0
        for nota in lista_toate_note:
            if nota.get_disciplina().get_id_disciplina() == id_disciplina:
                nr += 1
        return nr

    def top_k_studenti_cu_cele_mai_multe_note(self, k):
        """
        Returneaza top k studenti care au cele mai multe note la toate disciplinele
        :param k:
        :return: lista_dict_student_nr_note
        """
        lista_studenti = self.__repo_student.get_all_studenti()
        lista_dict_student_nr_note = []
        for student in lista_studenti:
            lista_dict_student_nr_note.append({"student": student, "nr_note": self.numar_note_student(student.get_id_student())})
        lista_dict_student_nr_note.sort(key = lambda x: x["nr_note"], reverse = True)

        return lista_dict_student_nr_note[:k]

    def top_k_discipline_cu_cele_mai_multe_note(self, k):
        """
                Returneaza top k discipline care au cele mai multe note de la toti studentii
                :param k:
                :return: lista_dict_disp_nr_note
                """
        lista_disciplina = self.__repo_disciplina.get_all_discipline()
        lista_dict_disp_nr_note = []
        for disciplina in lista_disciplina:
            lista_dict_disp_nr_note.append({"disciplina": disciplina, "nr_note": self.numar_note_disciplina(disciplina.get_id_disciplina())})
        lista_dict_disp_nr_note.sort(key = lambda x: x["nr_note"], reverse = True)

        return lista_dict_disp_nr_note[:k]

    def top_k_studenti_discipline_legatura(self, k):
        """
        Returneaza un raport cu top k studenti si legaturile lor cu top k discipline, daca au/nu au nota la una dintre cele top k discipline
        :param k:
        :return: raport
        """
        lista_dict_k_studenti = self.top_k_studenti_cu_cele_mai_multe_note(k)
        lista_dict_k_discipline = self.top_k_discipline_cu_cele_mai_multe_note(k)
        toate_notele = self.get__all_note()
        raport = {}
        for student_dict in lista_dict_k_studenti:
            student = student_dict["student"]
            raport[student.get_nume()] = []

            for disciplina_dict in lista_dict_k_discipline:
                disciplina = disciplina_dict["disciplina"]
                are_nota = False

                for nota in toate_notele:

                    if nota.get_student() == student and nota.get_disciplina() == disciplina:
                        are_nota = True
                        break

                if are_nota:
                    raport[student.get_nume()].append(f"DA - are nota la disciplina {disciplina.get_nume()} cu id ul {disciplina.get_id_disciplina()} si profesorul {disciplina.get_profesor()}")
                else:
                    raport[student.get_nume()].append(f"NU - nu are nota la disciplina {disciplina.get_nume()} cu id ul {disciplina.get_id_disciplina()} si profesorul {disciplina.get_profesor()}")
        return raport










