from Domain.Student import Student
from Domain.Disciplina import Disciplina
from Domain.Nota import Nota
from Repository.repository_errors import RepoError
from Repository.repository_nota import NotaRepository
import unittest



class TestRepoNota(unittest.TestCase):

    def test_adaugare_repo(self):
        test_repo = NotaRepository()

        s = Student(1, "Mihai Eminescu")
        d = Disciplina(1, "Literatura", "Profesor X")

        n = Nota(None, s, d, 10)
        test_repo.adauga(n)
        self.assertEqual(test_repo.size(), 1)

        s2 = Student(2, "Ion Creanga")
        n2 = Nota(None, s2, d, 9)
        test_repo.adauga(n2)
        self.assertEqual(test_repo.size(), 2)

    def test_stergere(self):
        test_repo = NotaRepository()

        s1 = Student(1, "Ion Creanga")
        d1 = Disciplina(1, "Matematica", "Prof")

        n3 = Nota(None, s1, d1, 5)
        test_repo.adauga(n3)
        self.assertEqual(test_repo.size(), 1)

        s2 = Student(2, "Mihai Eminescu")
        n = Nota(None, s2, d1, 10)
        test_repo.adauga(n)
        self.assertEqual(test_repo.size(), 2)

        nota_stearsa = test_repo.sterge_dupa_id(2)
        self.assertEqual(test_repo.size(), 1)
        self.assertEqual(nota_stearsa.get_nota(), 10)
        self.assertEqual(nota_stearsa.get_student(), s2)

    def test_modificare(self):
        test_repo = NotaRepository()

        s = Student(1, "Istrate Horia")
        d = Disciplina(1, "Informatica", "Prof")

        n = Nota(None, s, d, 8)
        test_repo.adauga(n)
        self.assertEqual(test_repo.size(), 1)

        n_modif = Nota(1, s, d, 10)

        nota_veche = test_repo.modifica(n_modif)
        self.assertEqual(test_repo.size(), 1)
        self.assertEqual(nota_veche.get_nota(), 8)

        nota_actualizata = test_repo.cauta_dupa_id(1)
        self.assertEqual(nota_actualizata.get_nota(), 10)

    def test_cauta_dupa_id(self):
        test_repo = NotaRepository()

        s = Student(1, "Istrate Horia")
        d = Disciplina(1, "Fizica", "Prof A")

        n = Nota(None, s, d, 7)
        test_repo.adauga(n)

        self.assertEqual(test_repo.cauta_dupa_id(1), n)
        n_cautat = test_repo.cauta_dupa_id(1)
        self.assertEqual(n_cautat.get_nota(), 7)

        self.assertRaises(RepoError, test_repo.cauta_dupa_id, 2)

    def test_size(self):
        test_repo = NotaRepository()

        s = Student(1, "Istrate Horia")
        d = Disciplina(1, "Sport", "Prof")
        n = Nota(None, s, d, 10)

        self.assertEqual(test_repo.size(), 0)
        test_repo.adauga(n)
        self.assertEqual(test_repo.size(), 1)

if __name__ == "__main__":
    unittest.main()


def test_adaugare_repo():
    test_repo = NotaRepository()

    s = Student(1, "Mihai Eminescu")
    d = Disciplina(1, "Literatura", "Profesor X")

    n = Nota(None, s, d, 10)
    test_repo.adauga(n)
    assert test_repo.size() == 1

    """
    try:
        # Verificare comportament daca ID-ul s-ar seta manual
        test_repo.adauga(n)
    except ValueError:
        assert True
    """

    s2 = Student(2, "Ion Creanga")
    n2 = Nota(None, s2, d, 9)
    test_repo.adauga(n2)
    assert test_repo.size() == 2


def test_stergere():
    test_repo = NotaRepository()

    s1 = Student(1, "Ion Creanga")
    d1 = Disciplina(1, "Matematica", "Prof")

    n3 = Nota(None, s1, d1, 5)
    test_repo.adauga(n3)
    assert test_repo.size() == 1

    s2 = Student(2, "Mihai Eminescu")
    n = Nota(None, s2, d1, 10)
    test_repo.adauga(n)
    assert test_repo.size() == 2

    nota_stearsa = test_repo.sterge_dupa_id(2)
    assert test_repo.size() == 1
    assert nota_stearsa.get_nota() == 10
    assert nota_stearsa.get_student() == s2


def test_modificare():
    test_repo = NotaRepository()

    s = Student(1, "Istrate Horia")
    d = Disciplina(1, "Informatica", "Prof")

    n = Nota(None, s, d, 8)
    test_repo.adauga(n)
    assert test_repo.size() == 1

    # Modificam nota: pastram studentul si materia, schimbam valoarea notei
    # ID-ul este 1 deoarece a fost prima nota adaugata
    n_modif = Nota(1, s, d, 10)

    nota_veche = test_repo.modifica(n_modif)
    assert test_repo.size() == 1
    assert nota_veche.get_nota() == 8

    nota_actualizata = test_repo.cauta_dupa_id(1)
    assert nota_actualizata.get_nota() == 10


def test_cauta_dupa_id():
    test_repo = NotaRepository()

    s = Student(1, "Istrate Horia")
    d = Disciplina(1, "Fizica", "Prof A")

    n = Nota(None, s, d, 7)
    test_repo.adauga(n)

    assert test_repo.cauta_dupa_id(1) == n
    n_cautat = test_repo.cauta_dupa_id(1)
    assert n_cautat.get_nota() == 7

    try:
        test_repo.cauta_dupa_id(2)
        assert False
    except RepoError:
        assert True


def test_size():
    test_repo = NotaRepository()

    s = Student(1, "Istrate Horia")
    d = Disciplina(1, "Sport", "Prof")
    n = Nota(None, s, d, 10)

    assert test_repo.size() == 0
    test_repo.adauga(n)
    assert test_repo.size() == 1


if __name__ == "__main__":
    test_adaugare_repo()
    test_stergere()
    test_modificare()
    test_cauta_dupa_id()
    test_size()