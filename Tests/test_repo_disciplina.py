from Domain.Disciplina import Disciplina
from Repository.repository_errors import RepoError
from Repository.repository_diciplina import DisciplinaRepository
import unittest

class TestRepoDisciplina(unittest.TestCase):

    def test_adaugare_repo(self):
        test_repo = DisciplinaRepository()
        d = Disciplina(None, "Matematica", "Popescu Ion")
        test_repo.adauga(d)
        self.assertEqual(test_repo.size(), 1)

        """
        Daca ai avea nevoie sa testezi o eroare la adaugare pe o singura linie, ar arata asa:
        self.assertRaises(ValueError, test_repo.adauga, d)
        """

        d2 = Disciplina(None, "Informatica", "Ionescu Maria")
        test_repo.adauga(d2)
        self.assertEqual(test_repo.size(), 2)

    def test_stergere(self):
        test_repo = DisciplinaRepository()
        d3 = Disciplina(None, "Fizica", "Vasilescu Dan")
        test_repo.adauga(d3)
        self.assertEqual(test_repo.size(), 1)

        d = Disciplina(None, "Matematica", "Popescu Ion")
        test_repo.adauga(d)
        self.assertEqual(test_repo.size(), 2)


        disciplina_stearsa = test_repo.sterge_dupa_id(2)
        self.assertEqual(test_repo.size(), 1)
        self.assertEqual(disciplina_stearsa.get_nume(), "Matematica")

    def test_modificare(self):
        test_repo = DisciplinaRepository()
        d = Disciplina(None, "Istorie", "Georgescu Vlad")
        test_repo.adauga(d)
        self.assertEqual(test_repo.size(), 1)


        d_modif = Disciplina(1, "Matematica", "Vlad M")
        disciplina_veche = test_repo.modifica(d_modif)

        self.assertEqual(test_repo.size(), 1)
        self.assertEqual(disciplina_veche.get_nume(), "Istorie")

        disciplina_actualizata = test_repo.cauta_dupa_id(1)
        self.assertEqual(disciplina_actualizata.get_nume(), "Matematica")

    def test_cauta_dupa_id(self):
        test_repo = DisciplinaRepository()
        d = Disciplina(None, "Chimie", "Ana M")
        test_repo.adauga(d)

        self.assertEqual(test_repo.cauta_dupa_id(1), d)
        d_cautat = test_repo.cauta_dupa_id(1)
        self.assertEqual(d_cautat.get_nume(), "Chimie")


        self.assertRaises(RepoError, test_repo.cauta_dupa_id, 2)

    def test_size(self):
        test_repo = DisciplinaRepository()
        d = Disciplina(None, "Sport", "Vlad M")
        self.assertEqual(test_repo.size(), 0)
        test_repo.adauga(d)
        self.assertEqual(test_repo.size(), 1)


if __name__ == '__main__':
    unittest.main()

def test_adaugare_repo():
    test_repo = DisciplinaRepository()

    d = Disciplina(None, "Matematica", "Popescu Ion")
    test_repo.adauga(d)
    assert test_repo.size() == 1

    """
    try:
        # Verificare comportament daca ID-ul s-ar seta manual (in acest repo se face auto-increment)
        test_repo.adauga(d)
    except ValueError:
        assert True
    """

    d2 = Disciplina(None, "Informatica", "Ionescu Maria")
    test_repo.adauga(d2)
    assert test_repo.size() == 2


def test_stergere():
    test_repo = DisciplinaRepository()
    d3 = Disciplina(None, "Fizica", "Vasilescu Dan")
    test_repo.adauga(d3)
    assert test_repo.size() == 1

    d = Disciplina(None, "Matematica", "Popescu Ion")
    test_repo.adauga(d)
    assert test_repo.size() == 2


    disciplina_stearsa = test_repo.sterge_dupa_id(2)
    assert test_repo.size() == 1
    assert disciplina_stearsa.get_nume() == "Matematica"


def test_modificare():
    test_repo = DisciplinaRepository()
    d = Disciplina(None, "Istorie", "Georgescu Vlad")
    test_repo.adauga(d)
    assert test_repo.size() == 1


    d_modif = Disciplina(1, "Matematica", "Vlad M")
    disciplina_veche = test_repo.modifica(d_modif)

    assert test_repo.size() == 1
    assert disciplina_veche.get_nume() == "Istorie"

    disciplina_actualizata = test_repo.cauta_dupa_id(1)
    assert disciplina_actualizata.get_nume() == "Matematica"


def test_cauta_dupa_id():
    test_repo = DisciplinaRepository()
    d = Disciplina(None, "Chimie", "Ana M")
    test_repo.adauga(d)

    assert test_repo.cauta_dupa_id(1) == d
    d_cautat = test_repo.cauta_dupa_id(1)
    assert d_cautat.get_nume() == "Chimie"

    try:
        test_repo.cauta_dupa_id(2)
        assert False
    except RepoError:
        assert True


def test_size():
    test_repo = DisciplinaRepository()
    d = Disciplina(None, "Sport", "Vlad M")
    assert test_repo.size() == 0
    test_repo.adauga(d)
    assert test_repo.size() == 1


if __name__ == "__main__":
    test_adaugare_repo()
    test_stergere()
    test_modificare()
    test_cauta_dupa_id()
    test_size()