from Repository.repository_student import StudentRepository
from Controller_Service.service_studenti import ServiceStudenti
from Domain.validator import StudentValidator
import random
import unittest


class TestServiceStudenti(unittest.TestCase):

    def setUp(self):

        self.repo = StudentRepository()
        self.val = StudentValidator()
        self.service = ServiceStudenti(self.repo, self.val)

    def test_adaugare_service(self):
        self.service.adaugare_student("Mihai Eminescu")
        self.assertEqual(self.service.get_numar_studenti(), 1)


        self.assertRaises(ValueError, self.service.adaugare_student, "")


        self.assertRaises(ValueError, self.service.adaugare_student, "H0ria Istrate")

    def test_stergere_service(self):
        self.service.adaugare_student("Mihai Eminescu")
        self.assertEqual(self.service.get_numar_studenti(), 1)

        student_sters = self.service.sterge_student(1)
        self.assertEqual(self.service.get_numar_studenti(), 0)
        self.assertEqual(student_sters.get_nume(), "Mihai Eminescu")

    def test_modificare(self):
        self.service.adaugare_student("Mihai Eminescu")
        self.assertEqual(self.service.get_numar_studenti(), 1)

        student_vechi = self.service.modifica_student(1, "Ion Creanga")
        self.assertEqual(student_vechi.get_nume(), "Mihai Eminescu")

        student_actualizat = self.repo.cauta_dupa_id(1)
        self.assertEqual(student_actualizat.get_nume(), "Ion Creanga")

    def test_adaugare_studenti_random(self):
        numar = 3
        random.seed(100)
        self.service.adaugare_studenti_random(numar)

        s1 = self.repo.cauta_dupa_id(1)
        self.assertEqual(s1.get_nume(), "dlustlu nclbyyi")

        s2 = self.repo.cauta_dupa_id(2)
        self.assertEqual(s2.get_nume(), "itfeejq zfyoxve")

        s3 = self.repo.cauta_dupa_id(3)
        self.assertEqual(s3.get_nume(), "qdakuof vxglqxd")

if __name__ == "__main__":
    unittest.main()

def test_adaugare_service():
    test_repo = StudentRepository()
    test_val = StudentValidator()
    test_service = ServiceStudenti(test_repo, test_val)
    test_service.adaugare_student("Mihai Eminescu")
    assert test_service.get_numar_studenti() == 1

    """
    Daca scot id ul automat
    try:
        test_service.adaugare_student(1,"Mihai Eminescu")
        assert False
    except ValueError as e:
        assert True
    """
    try:
        test_service.adaugare_student("")
        assert False
    except ValueError as e:
        assert True
    try:
        test_service.adaugare_student("H0ria Istrate")
        assert False
    except ValueError as e:
        assert True
def test_stergere_service():
    test_repo = StudentRepository()
    test_val = StudentValidator()
    test_service = ServiceStudenti(test_repo, test_val)
    test_service.adaugare_student("Mihai Eminescu")
    assert test_service.get_numar_studenti() == 1

    student_sters = test_service.sterge_student(1)
    assert test_service.get_numar_studenti() == 0
    assert student_sters.get_nume() == "Mihai Eminescu"

def test_modificare():
    test_repo = StudentRepository()
    test_val = StudentValidator()
    test_service = ServiceStudenti(test_repo, test_val)
    test_service.adaugare_student("Mihai Eminescu")
    assert test_service.get_numar_studenti() == 1
    student_vechi = test_service.modifica_student(1, "Ion Creanga")
    assert student_vechi.get_nume() == "Mihai Eminescu"
    student_actualizat = test_repo.cauta_dupa_id(1)
    assert student_actualizat.get_nume() == "Ion Creanga"

def test_adaugare_studenti_random():
    test_repo = StudentRepository()
    test_val = StudentValidator()
    test_service = ServiceStudenti(test_repo, test_val)
    numar = 3
    random.seed(100)
    test_service.adaugare_studenti_random(numar)
    """
    for s in test_service.get_studenti():
        print (s)
        (
        ID:1 Nume: dlustlu nclbyyi
        ID:2 Nume: itfeejq zfyoxve
        ID:3 Nume: qdakuof vxglqxd
        
    """
    s1 = test_repo.cauta_dupa_id(1)
    assert s1.get_nume() == "dlustlu nclbyyi"
    s2 = test_repo.cauta_dupa_id(2)
    assert s2.get_nume() == "itfeejq zfyoxve"
    s3 = test_repo.cauta_dupa_id(3)
    assert s3.get_nume() == "qdakuof vxglqxd"











if __name__ == "__main__":
    test_adaugare_service()
    test_stergere_service()
    test_modificare()
    test_adaugare_studenti_random()


