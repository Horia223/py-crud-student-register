from Repository.repository_diciplina import DisciplinaRepository
from Domain.validator import DisciplinaValidator
from Controller_Service.service_disciplina import ServiceDisciplina
from Repository.repository_errors import RepoError
import unittest


class TestServiceDisciplina(unittest.TestCase):

    def setUp(self):
        self.repo = DisciplinaRepository()
        self.val = DisciplinaValidator()
        self.service = ServiceDisciplina(self.repo, self.val)

    def test_adaugare_service_d(self):
        self.service.adaugare_disciplina("Mate", "Ioan Stefan")
        self.assertEqual(self.service.get_numar_discipline(), 1)

        self.assertRaises(ValueError, self.service.adaugare_disciplina, "", "")
        self.assertRaises(ValueError, self.service.adaugare_disciplina, "m0te", "Ioan Stefan")
        self.assertRaises(ValueError, self.service.adaugare_disciplina, "Mate", "Ioan")

    def test_stergere_service(self):
        self.service.adaugare_disciplina("FP", "Ioan Stefan")
        self.assertEqual(self.service.get_numar_discipline(), 1)

        disciplina_stearsa = self.service.sterge_disciplina(1)
        self.assertEqual(self.service.get_numar_discipline(), 0)
        self.assertEqual(disciplina_stearsa.get_nume(), "FP")
        self.assertEqual(disciplina_stearsa.get_profesor(), "Ioan Stefan")

        self.assertRaises(RepoError, self.service.sterge_disciplina, 1)

    def test_modifica_service(self):
        self.service.adaugare_disciplina("FP", "Ioan Stefan")
        self.assertEqual(self.service.get_numar_discipline(), 1)

        disciplina_veche = self.service.modifica_disciplina(1, "Mate", "Ioan Stefan")
        self.assertEqual(disciplina_veche.get_nume(), "FP")

        disciplina_actualizata = self.repo.cauta_dupa_id(1)
        self.assertEqual(disciplina_actualizata.get_nume(), "Mate")

if __name__ == "__main__":
    unittest.main()

def test_adaugare_service_d():
    test_repo = DisciplinaRepository()
    test_val = DisciplinaValidator()
    test_service =  ServiceDisciplina(test_repo, test_val)
    test_service.adaugare_disciplina("Mate", "Ioan Stefan")
    assert test_service.get_numar_discipline() == 1
    try:
        test_service.adaugare_disciplina("", "")
        assert False
    except ValueError as e:
        assert True

    try:
        test_service.adaugare_disciplina("m0te", "Ioan Stefan")
        assert False
    except ValueError as e:
        assert True

    try:
        test_service.adaugare_disciplina("Mate", "Ioan")
        assert False
    except ValueError as e:
        assert True

def test_stergere_service():
    test_repo = DisciplinaRepository()
    test_val = DisciplinaValidator()
    test_service = ServiceDisciplina(test_repo, test_val)
    test_service.adaugare_disciplina("FP", "Ioan Stefan")
    assert test_service.get_numar_discipline() == 1

    disciplina_stearsa = test_service.sterge_disciplina(1)
    assert test_service.get_numar_discipline() == 0
    assert disciplina_stearsa.get_nume() == "FP"
    assert disciplina_stearsa.get_profesor() == "Ioan Stefan"

    try:
        test_service.sterge_disciplina(1)
        assert False
    except RepoError as e:
        assert True

def test_modifica_service():
    test_repo = DisciplinaRepository()
    test_val = DisciplinaValidator()
    test_service = ServiceDisciplina(test_repo, test_val)
    test_service.adaugare_disciplina("FP", "Ioan Stefan")
    assert test_service.get_numar_discipline() == 1

    disciplina_veche =  test_service.modifica_disciplina(1, "Mate", "Ioan Stefan")
    assert disciplina_veche.get_nume() == "FP"

    disciplina_actualizata = test_repo.cauta_dupa_id(1)
    assert disciplina_actualizata.get_nume() == "Mate"





if __name__ == "__main__":
    test_adaugare_service_d()
    test_stergere_service()
    test_modifica_service()



