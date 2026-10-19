
from Domain.Student import Student
from Repository.repository_errors import RepoError
from Repository.repository_student import StudentRepository
import unittest


class TestRepoStudenti(unittest.TestCase):

    def setUp(self) -> None:
        print("setup called")
        self.__test_repo = StudentRepository()

    def test_adaugare_repo(self):
        test_repo = StudentRepository()
        s = Student(None, "Mihai Eminescu")
        test_repo.adauga(s)
        self.assertEqual(test_repo.size(), 1)
        """
        try:
        Daca scot id ul automat
            test_repo.adauga(s)
            assert False
        except ValueError:
            assert True
        """
        s2 = Student(None, "Istrate Horia")
        test_repo.adauga(s2)
        self.assertEqual(test_repo.size(), 2)

    def test_stergere(self):
        test_repo = StudentRepository()
        s3 = Student(None, "Ion Creanga")
        test_repo.adauga(s3)
        self.assertEqual(test_repo.size(), 1)
        s = Student(None, "Mihai Eminescu")
        test_repo.adauga(s)
        self.assertEqual(test_repo.size(), 2)

        student_stearsa = test_repo.sterge_dupa_id(2)

        self.assertEqual(test_repo.size(), 1)
        self.assertEqual(student_stearsa.get_nume(), "Mihai Eminescu")

    def test_modificare(self):
        test_repo = StudentRepository()
        s = Student(None, "Istrate Horia")
        test_repo.adauga(s)
        self.assertEqual(test_repo.size(), 1)

        s_modif = Student(1, "Istrate Paul")

        student_vechi = test_repo.modifica(s_modif)
        self.assertEqual(test_repo.size(), 1)
        self.assertEqual(student_vechi.get_nume(), "Istrate Horia")

        student_actualizat = test_repo.cauta_dupa_id(1)
        self.assertEqual(student_actualizat.get_nume(), "Istrate Paul")

    def test_cauta_dupa_id(self):
        test_repo = StudentRepository()
        s = Student(None, "Istrate Horia")
        test_repo.adauga(s)

        self.assertEqual(test_repo.cauta_dupa_id(1), s)

        s_cautat = test_repo.cauta_dupa_id(1)
        self.assertEqual(s_cautat.get_nume(), "Istrate Horia")


        self.assertRaises(RepoError, self.__test_repo.cauta_dupa_id,2)

    def test_size(self):
        test_repo = StudentRepository()
        s = Student(None, "Istrate Horia")
        self.assertEqual(test_repo.size(), 0)
        test_repo.adauga(s)
        self.assertEqual(test_repo.size(), 1)

    def tearDown(self) -> None:
        print("tearDown")
        del self.__test_repo


if __name__ == '__main__':
    unittest.main()

def test_adaugare_repo():
    test_repo = StudentRepository()
    s = Student(None, "Mihai Eminescu")
    test_repo.adauga(s)
    assert test_repo.size() == 1
    """
    try:
    
    Daca scot id ul automat
        test_repo.adauga(s)
        assert False
    except ValueError:
        assert True
    """
    s2 = Student(None, "Istrate Horia")
    test_repo.adauga(s2)
    assert test_repo.size() == 2

def test_stergere():
    test_repo = StudentRepository()
    s3 = Student(None, "Ion Creanga")
    test_repo.adauga(s3)
    assert test_repo.size() == 1
    s = Student(None, "Mihai Eminescu")
    test_repo.adauga(s)
    assert test_repo.size() == 2

    student_stearsa =  test_repo.sterge_dupa_id(2)
    assert test_repo.size() == 1
    assert student_stearsa.get_nume() == "Mihai Eminescu"

def test_modificare():
    test_repo = StudentRepository()
    s = Student(None, "Istrate Horia")
    test_repo.adauga(s)
    assert test_repo.size() == 1
    s_modif = Student(1, "Istrate Paul")
    student_vechi = test_repo.modifica(s_modif)
    assert test_repo.size() == 1
    assert student_vechi.get_nume() == "Istrate Horia"
    student_actualizat =  test_repo.cauta_dupa_id(1)
    assert student_actualizat.get_nume() == "Istrate Paul"

def test_cauta_dupa_id():
    test_repo = StudentRepository()
    s = Student(None, "Istrate Horia")
    test_repo.adauga(s)
    assert test_repo.cauta_dupa_id(1) == s
    s_cautat = test_repo.cauta_dupa_id(1)
    assert s_cautat.get_nume() == "Istrate Horia"
    try:
        test_repo.cauta_dupa_id(2)
        assert False
    except RepoError:
        assert True

def test_size():
    test_repo = StudentRepository()
    s = Student(None, "Istrate Horia")
    assert test_repo.size() == 0
    test_repo.adauga(s)
    assert test_repo.size() == 1












if __name__ == "__main__":
    test_adaugare_repo()
    test_stergere()
    test_modificare()
    test_cauta_dupa_id()
    test_size()

