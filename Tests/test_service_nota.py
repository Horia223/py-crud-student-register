from Domain.Student import Student
from Domain.Disciplina import Disciplina
from Domain.Nota import Nota
from Controller_Service.service_nota import ServiceNota
from Repository.repository_nota import NotaRepository
from Repository.repository_student import StudentRepository
from Repository.repository_diciplina import DisciplinaRepository
from Domain.validator import NotaValidator
from Repository.repository_errors import RepoError
import unittest




class TestServiceNota(unittest.TestCase):

    def setUp(self):
        self.repo_nota = NotaRepository()
        self.repo_student = StudentRepository()
        self.repo_disciplina = DisciplinaRepository()
        self.val_nota = NotaValidator()
        self.test_service = ServiceNota(self.repo_nota, self.val_nota, self.repo_student, self.repo_disciplina)

    def test_adaugare_nota(self):
        s = Student(1, "Istrate Horia")
        d = Disciplina(1, "Matematica", "Prof")
        self.repo_student.adauga(s)
        self.repo_disciplina.adauga(d)

        self.assertEqual(self.test_service.get_numar_note(), 0)
        self.test_service.adaugare_nota(1, 1, 10)
        self.assertEqual(self.test_service.get_numar_note(), 1)

        self.assertRaises(RepoError, self.test_service.adaugare_nota, 2, 1, 10)
        self.assertRaises(ValueError, self.test_service.adaugare_nota, 1, 1, 11)

    def test_sterge_nota(self):
        s = Student(1, "Istrate Horia")
        d = Disciplina(1, "Matematica", "Prof")
        self.repo_student.adauga(s)
        self.repo_disciplina.adauga(d)

        self.assertEqual(self.test_service.get_numar_note(), 0)
        self.test_service.adaugare_nota(1, 1, 10)
        self.assertEqual(self.test_service.get_numar_note(), 1)
        self.test_service.sterge_nota(1)
        self.assertEqual(self.test_service.get_numar_note(), 0)

    def test_modifica_nota(self):
        s = Student(1, "Istrate Horia")
        d = Disciplina(1, "Matematica", "Prof")
        self.repo_student.adauga(s)
        self.repo_disciplina.adauga(d)

        self.assertEqual(self.test_service.get_numar_note(), 0)
        self.test_service.adaugare_nota(1, 1, 10)
        self.assertEqual(self.test_service.get_numar_note(), 1)

        nota_veche = self.test_service.cauta_dupa_id(1)
        self.assertEqual(self.test_service.modifica_nota(1, 9), nota_veche)
        self.assertEqual(self.test_service.cauta_dupa_id(1).get_nota(), 9)

    def test_get_note_student_la_disciplina(self):
        s = Student(1, "Istrate Horia")
        d = Disciplina(1, "Matematica", "Prof")
        s1 = Student(2, "Max N")
        d1 = Disciplina(2, "Sport", "Prof S")

        self.repo_student.adauga(s)
        self.repo_student.adauga(s1)
        self.repo_disciplina.adauga(d)
        self.repo_disciplina.adauga(d1)

        self.test_service.adaugare_nota(1, 1, 10)
        self.test_service.adaugare_nota(1, 1, 9)
        self.test_service.adaugare_nota(1, 1, 10)
        self.test_service.adaugare_nota(1, 1, 1)
        self.test_service.adaugare_nota(1, 2, 6)
        self.test_service.adaugare_nota(1, 1, 7)
        self.test_service.adaugare_nota(2, 1, 10)
        self.test_service.adaugare_nota(2, 1, 3)
        self.test_service.adaugare_nota(2, 2, 10)
        self.test_service.adaugare_nota(2, 2, 10)

        lista = self.test_service.get_note_student_la_disciplina(1, 1)
        lista_test = [10, 9, 10, 1, 7]
        self.assertEqual(len(lista), 5)

        for i in range(len(lista)):
            self.assertEqual(lista[i].get_nota(), lista_test[i])

        lista = self.test_service.get_note_student_la_disciplina(1, 2)
        self.assertEqual(len(lista), 1)
        self.assertEqual(lista[0].get_nota(), 6)

        lista = self.test_service.get_note_student_la_disciplina(2, 1)
        self.assertEqual(len(lista), 2)
        self.assertEqual(lista[0].get_nota(), 10)
        self.assertEqual(lista[1].get_nota(), 3)

    def test_get_statistica_note_disciplina(self):
        s = Student(1, "Istrate Horia")
        d = Disciplina(1, "Matematica", "Prof")
        s1 = Student(2, "Max N")
        d1 = Disciplina(2, "Sport", "Prof S")
        s2 = Student(3, "Max N")

        self.repo_student.adauga(s)
        self.repo_student.adauga(s1)
        self.repo_student.adauga(s2)
        self.repo_disciplina.adauga(d)
        self.repo_disciplina.adauga(d1)

        self.test_service.adaugare_nota(1, 1, 10)
        self.test_service.adaugare_nota(1, 1, 9)
        self.test_service.adaugare_nota(1, 1, 10)
        self.test_service.adaugare_nota(1, 1, 1)
        self.test_service.adaugare_nota(1, 2, 6)
        self.test_service.adaugare_nota(1, 1, 7)
        self.test_service.adaugare_nota(2, 1, 10)
        self.test_service.adaugare_nota(2, 1, 3)
        self.test_service.adaugare_nota(2, 2, 10)
        self.test_service.adaugare_nota(2, 2, 10)
        self.test_service.adaugare_nota(3, 2, 10)
        self.test_service.adaugare_nota(3, 1, 10)
        self.test_service.adaugare_nota(3, 1, 7)
        self.test_service.adaugare_nota(3, 1, 9)

        note_lista = self.test_service.get_statistica_note_disciplina(1)
        note_lista_test = []
        note_lista_test.append(self.test_service.cauta_dupa_id(4))
        note_lista_test.append(self.test_service.cauta_dupa_id(6))
        note_lista_test.append(self.test_service.cauta_dupa_id(2))
        note_lista_test.append(self.test_service.cauta_dupa_id(1))
        note_lista_test.append(self.test_service.cauta_dupa_id(3))
        note_lista_test.append(self.test_service.cauta_dupa_id(8))
        note_lista_test.append(self.test_service.cauta_dupa_id(13))
        note_lista_test.append(self.test_service.cauta_dupa_id(14))
        note_lista_test.append(self.test_service.cauta_dupa_id(7))
        note_lista_test.append(self.test_service.cauta_dupa_id(12))

        self.assertEqual(note_lista, note_lista_test)

    def test_get_statistica_top_studenti(self):
        s1 = Student(1, "Eminescu Mihai")
        s2 = Student(2, "Creanga Ion")
        s3 = Student(3, "Caragiale I.L.")
        s4 = Student(4, "Slavici Ioan")
        s5 = Student(5, "Rebreanu Liviu")

        d1 = Disciplina(1, "Matematica", "Prof X")
        d2 = Disciplina(2, "Informatica", "Prof Y")

        self.repo_student.adauga(s1)
        self.repo_student.adauga(s2)
        self.repo_student.adauga(s3)
        self.repo_student.adauga(s4)
        self.repo_student.adauga(s5)

        self.repo_disciplina.adauga(d1)
        self.repo_disciplina.adauga(d2)

        self.test_service.adaugare_nota(1, 1, 10)
        self.test_service.adaugare_nota(1, 2, 10)
        self.test_service.adaugare_nota(2, 1, 9)
        self.test_service.adaugare_nota(2, 2, 9)
        self.test_service.adaugare_nota(3, 1, 8)
        self.test_service.adaugare_nota(3, 2, 8)
        self.test_service.adaugare_nota(4, 1, 7)
        self.test_service.adaugare_nota(4, 2, 7)
        self.test_service.adaugare_nota(5, 1, 6)
        self.test_service.adaugare_nota(5, 2, 6)

        lista = self.test_service.get_statistica_top_studenti()
        lista_test = []
        lista_test.append({"student": s1, "medie": 10.0})

        self.assertEqual(lista, lista_test)

    def test_numar_note_student_si_disciplina(self):
        s1 = Student(1, "Elev unu")
        s2 = Student(2, "Elev doi")
        d1 = Disciplina(1, "Mate", "Prof MAte")
        d2 = Disciplina(2, "Info", "Prof Info")

        self.repo_student.adauga(s1)
        self.repo_student.adauga(s2)
        self.repo_disciplina.adauga(d1)
        self.repo_disciplina.adauga(d2)

        self.test_service.adaugare_nota(1, 1, 10)
        self.test_service.adaugare_nota(1, 2, 9)
        self.test_service.adaugare_nota(2, 2, 8)

        self.assertEqual(self.test_service.numar_note_student(1), 2)
        self.assertEqual(self.test_service.numar_note_student(2), 1)
        self.assertEqual(self.test_service.numar_note_disciplina(1), 1)
        self.assertEqual(self.test_service.numar_note_disciplina(2), 2)

    def test_top_k_studenti_discipline_legatura(self):
        s1 = Student(1, "Elev unu")
        s2 = Student(2, "Elev doi")
        d1 = Disciplina(1, "Mate", "Prof Mate")
        d2 = Disciplina(2, "Info", "Prof Info")

        self.repo_student.adauga(s1)
        self.repo_student.adauga(s2)
        self.repo_disciplina.adauga(d1)
        self.repo_disciplina.adauga(d2)

        self.test_service.adaugare_nota(1, 1, 10)
        self.test_service.adaugare_nota(1, 2, 9)
        self.test_service.adaugare_nota(2, 1, 8)

        raport = self.test_service.top_k_studenti_discipline_legatura(2)

        self.assertEqual(len(raport), 2)


        self.assertEqual(raport["Elev unu"][0], "DA - are nota la disciplina Mate cu id ul 1 si profesorul Prof Mate")
        self.assertEqual(raport["Elev unu"][1], "DA - are nota la disciplina Info cu id ul 2 si profesorul Prof Info")
        self.assertEqual(raport["Elev doi"][0], "DA - are nota la disciplina Mate cu id ul 1 si profesorul Prof Mate")
        self.assertEqual(raport["Elev doi"][1],
                         "NU - nu are nota la disciplina Info cu id ul 2 si profesorul Prof Info")


if __name__ == "__main__":
    unittest.main()


def test_adaugare_nota():
    s = Student(1, "Istrate Horia")
    d = Disciplina(1, "Matematica", "Prof")
    repo_nota = NotaRepository()
    repo_student = StudentRepository()
    repo_student.adauga(s)
    repo_disciplina = DisciplinaRepository()
    repo_disciplina.adauga(d)
    val_nota = NotaValidator()
    test_service = ServiceNota(repo_nota, val_nota, repo_student, repo_disciplina)
    assert test_service.get_numar_note() == 0
    test_service.adaugare_nota(1, 1, 10)
    assert test_service.get_numar_note() == 1
    try:
        test_service.adaugare_nota(2, 1, 10)
        assert False
    except RepoError:
        assert True

    try:
        test_service.adaugare_nota(1, 1, 11)
        assert False
    except ValueError:
        assert True

def test_sterge_nota():
    s = Student(1, "Istrate Horia")
    d = Disciplina(1, "Matematica", "Prof")
    repo_nota = NotaRepository()
    repo_student = StudentRepository()
    repo_student.adauga(s)
    repo_disciplina = DisciplinaRepository()
    repo_disciplina.adauga(d)
    val_nota = NotaValidator()
    test_service = ServiceNota(repo_nota, val_nota, repo_student, repo_disciplina)
    assert test_service.get_numar_note() == 0
    test_service.adaugare_nota(1, 1, 10)
    assert test_service.get_numar_note() == 1
    test_service.sterge_nota(1)
    assert test_service.get_numar_note() == 0

def test_modifica_nota():
    s = Student(1, "Istrate Horia")
    d = Disciplina(1, "Matematica", "Prof")
    n = Nota(None, s, d, 10)
    repo_nota = NotaRepository()
    repo_student = StudentRepository()
    repo_student.adauga(s)
    repo_disciplina = DisciplinaRepository()
    repo_disciplina.adauga(d)
    val_nota = NotaValidator()
    test_service = ServiceNota(repo_nota, val_nota, repo_student, repo_disciplina)
    assert test_service.get_numar_note() == 0
    test_service.adaugare_nota(1, 1, 10)
    assert test_service.get_numar_note() == 1
    nota_veche = test_service.cauta_dupa_id(1)
    assert test_service.modifica_nota(1, 9) == nota_veche
    assert test_service.cauta_dupa_id(1).get_nota() == 9

def test_get_note_student_la_disciplina():
    s = Student(1, "Istrate Horia")
    d = Disciplina(1, "Matematica", "Prof")
    s1 = Student(2,"Max N")
    d1 = Disciplina(2, "Sport", "Prof S")
    repo_nota = NotaRepository()
    repo_student = StudentRepository()
    repo_student.adauga(s)
    repo_student.adauga(s1)
    repo_disciplina = DisciplinaRepository()
    repo_disciplina.adauga(d)
    repo_disciplina.adauga(d1)
    val_nota = NotaValidator()
    test_service = ServiceNota(repo_nota, val_nota, repo_student, repo_disciplina)
    test_service.adaugare_nota(1, 1, 10)
    test_service.adaugare_nota(1, 1, 9)
    test_service.adaugare_nota(1, 1, 10)
    test_service.adaugare_nota(1, 1, 1)
    test_service.adaugare_nota(1, 2, 6)
    test_service.adaugare_nota(1, 1, 7)
    test_service.adaugare_nota(2, 1, 10)
    test_service.adaugare_nota(2, 1, 3)
    test_service.adaugare_nota(2, 2, 10)
    test_service.adaugare_nota(2, 2, 10)
    lista = test_service.get_note_student_la_disciplina(1,1)
    lista_test = [10,9,10,1,7]
    assert len(lista) == 5
    i = 0
    for nota in lista:
        assert nota.get_nota() == lista_test[i]
        i += 1
    lista = test_service.get_note_student_la_disciplina(1, 2)
    assert len(lista) == 1
    assert lista[0].get_nota() == 6
    lista = test_service.get_note_student_la_disciplina(2,1)
    assert len(lista) == 2
    assert lista[0].get_nota() == 10
    assert lista[1].get_nota() == 3

def test_get_statistica_note_disciplina():
    s = Student(1, "Istrate Horia")
    d = Disciplina(1, "Matematica", "Prof")
    s1 = Student(2, "Max N")
    d1 = Disciplina(2, "Sport", "Prof S")
    s2 = Student(3, "Max N")

    repo_nota = NotaRepository()
    repo_student = StudentRepository()

    repo_student.adauga(s)
    repo_student.adauga(s1)
    repo_student.adauga(s2)

    repo_disciplina = DisciplinaRepository()

    repo_disciplina.adauga(d)
    repo_disciplina.adauga(d1)

    val_nota = NotaValidator()
    test_service = ServiceNota(repo_nota, val_nota, repo_student, repo_disciplina)

    test_service.adaugare_nota(1, 1, 10)
    test_service.adaugare_nota(1, 1, 9)
    test_service.adaugare_nota(1, 1, 10)
    test_service.adaugare_nota(1, 1, 1)
    test_service.adaugare_nota(1, 2, 6)
    test_service.adaugare_nota(1, 1, 7)

    test_service.adaugare_nota(2, 1, 10)
    test_service.adaugare_nota(2, 1, 3)
    test_service.adaugare_nota(2, 2, 10)
    test_service.adaugare_nota(2, 2, 10)

    test_service.adaugare_nota(3, 2, 10)
    test_service.adaugare_nota(3, 1, 10)
    test_service.adaugare_nota(3, 1, 7)
    test_service.adaugare_nota(3, 1, 9)

    note_lista = test_service.get_statistica_note_disciplina(1)

    note_lista_test = []

    note_lista_test.append(test_service.cauta_dupa_id(4))
    note_lista_test.append(test_service.cauta_dupa_id(6))
    note_lista_test.append(test_service.cauta_dupa_id(2))
    note_lista_test.append(test_service.cauta_dupa_id(1))
    note_lista_test.append(test_service.cauta_dupa_id(3))
    note_lista_test.append(test_service.cauta_dupa_id(8))
    note_lista_test.append(test_service.cauta_dupa_id(13))
    note_lista_test.append(test_service.cauta_dupa_id(14))
    note_lista_test.append(test_service.cauta_dupa_id(7))
    note_lista_test.append(test_service.cauta_dupa_id(12))

    assert note_lista == note_lista_test

def test_get_statistica_top_studenti():

    s1 = Student(1, "Eminescu Mihai")
    s2 = Student(2, "Creanga Ion")
    s3 = Student(3, "Caragiale I.L.")
    s4 = Student(4, "Slavici Ioan")
    s5 = Student(5, "Rebreanu Liviu")

    d1 = Disciplina(1, "Matematica", "Prof X")
    d2 = Disciplina(2, "Informatica", "Prof Y")

    repo_nota = NotaRepository()
    repo_student = StudentRepository()
    repo_student.adauga(s1)
    repo_student.adauga(s2)
    repo_student.adauga(s3)
    repo_student.adauga(s4)
    repo_student.adauga(s5)

    repo_disciplina = DisciplinaRepository()
    repo_disciplina.adauga(d1)
    repo_disciplina.adauga(d2)

    val_nota = NotaValidator()
    test_service = ServiceNota(repo_nota, val_nota, repo_student, repo_disciplina)


    test_service.adaugare_nota(1, 1, 10)
    test_service.adaugare_nota(1, 2, 10)

    test_service.adaugare_nota(2, 1, 9)
    test_service.adaugare_nota(2, 2, 9)

    test_service.adaugare_nota(3, 1, 8)
    test_service.adaugare_nota(3, 2, 8)

    test_service.adaugare_nota(4, 1, 7)
    test_service.adaugare_nota(4, 2, 7)

    test_service.adaugare_nota(5, 1, 6)
    test_service.adaugare_nota(5, 2, 6)

    lista = test_service.get_statistica_top_studenti()


    lista_test = []


    lista_test.append({"student": s1, "medie": 10.0})

    assert lista == lista_test
def test_numar_note_student_si_disciplina():
    repo_disciplina = DisciplinaRepository()
    repo_nota = NotaRepository()
    repo_student = StudentRepository()

    val_nota = NotaValidator()
    test_service = ServiceNota(repo_nota, val_nota, repo_student, repo_disciplina)

    s1 = Student(1, "Elev unu")
    s2 = Student(2, "Elev doi")
    d1 = Disciplina(1, "Mate", "Prof MAte")
    d2 = Disciplina(2, "Info", "Prof Info")
    repo_student.adauga(s1)
    repo_student.adauga(s2)
    repo_disciplina.adauga(d1)
    repo_disciplina.adauga(d2)
    test_service.adaugare_nota(1, 1, 10)
    test_service.adaugare_nota(1, 2, 9)
    test_service.adaugare_nota(2, 2, 8)
    assert test_service.numar_note_student(1) == 2
    assert test_service.numar_note_student(2) == 1
    assert test_service.numar_note_disciplina(1) == 1
    assert test_service.numar_note_disciplina(2) == 2


def test_top_k_studenti_discipline_legatura():
    repo_disciplina = DisciplinaRepository()
    repo_nota = NotaRepository()
    repo_student = StudentRepository()

    val_nota = NotaValidator()
    test_service = ServiceNota(repo_nota, val_nota, repo_student, repo_disciplina)

    s1 = Student(1, "Elev unu")
    s2 = Student(2, "Elev doi")
    d1 = Disciplina(1, "Mate", "Prof Mate")
    d2 = Disciplina(2, "Info", "Prof Info")
    repo_student.adauga(s1)
    repo_student.adauga(s2)
    repo_disciplina.adauga(d1)
    repo_disciplina.adauga(d2)
    test_service.adaugare_nota(1, 1, 10)
    test_service.adaugare_nota(1, 2, 9)
    test_service.adaugare_nota(2, 1, 8)
    raport = test_service.top_k_studenti_discipline_legatura(2)
    assert len(raport) == 2
    #print(raport)
    assert "Elev unu" in raport
    assert "Elev doi" in raport
    assert raport["Elev unu"][0] == "DA - are nota la disciplina Mate cu id ul 1 si profesorul Prof Mate"
    assert raport["Elev unu"][1] == "DA - are nota la disciplina Info cu id ul 2 si profesorul Prof Info"
    assert raport["Elev doi"][0] == "DA - are nota la disciplina Mate cu id ul 1 si profesorul Prof Mate"
    assert raport["Elev doi"][1] == "NU - nu are nota la disciplina Info cu id ul 2 si profesorul Prof Info"



if __name__ == "__main__":
    test_adaugare_nota()
    test_sterge_nota()
    test_modifica_nota()
    test_get_note_student_la_disciplina()
    test_get_statistica_note_disciplina()
    test_numar_note_student_si_disciplina()
    test_top_k_studenti_discipline_legatura()
