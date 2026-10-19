from Domain.Student import Student
from Domain.Disciplina import Disciplina
from Domain.Nota import Nota
from Repository.repository_student import StudentRepositoryFile, StudentRepository
from Repository.repository_diciplina import DisciplinaRepositoryFile, DisciplinaRepository
from Repository.repository_nota import NotaRepositoryFile

from Repository.repository_errors import RepoError
import unittest
import os


class TestStudentRepoFile(unittest.TestCase):
    def setUp(self):
        self.filename = "test.studenti_temp.txt"
        with open(self.filename, "w") as f:
            f.write("")
            #sau pass ca nu ai voie sa nu pui nimic intr un bloc with


    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_salvare_in_fisier(self):
        test_repo_file = StudentRepositoryFile(self.filename)
        student = Student(2, "Mihai Eminescu")
        test_repo_file.adauga(student)

        with open(self.filename, "r") as f:
            continut = f.read().strip()
        self.assertEqual(continut, "2,Mihai Eminescu" )

        s2 = Student(None,"Istrate Horia")
        test_repo_file.adauga(s2)

        with open(self.filename, "r") as f:
            continut = f.read().strip()
        self.assertEqual(continut, "2,Mihai Eminescu\n3,Istrate Horia")

    def test_incarcare_din_fisier(self):
        with open(self.filename, "w") as f:
            f.write("10,Ion Creanga\n20,Mihai Eminescu")

        repo = StudentRepositoryFile(self.filename)

        self.assertEqual(repo.size(), 2)
        s = repo.cauta_dupa_id(10)
        self.assertEqual(s.get_nume(), "Ion Creanga")

    def test_stergere(self):
        repo = StudentRepositoryFile(self.filename)
        repo.adauga(Student(1, "Sters Da"))
        self.assertEqual(repo.size(), 1)

        repo.sterge_dupa_id(1)
        self.assertEqual(repo.size(), 0)

        with open(self.filename, "r") as f:
            continut = f.read().strip()

        self.assertEqual(continut, "")



class TestDisciplinaRepoFile(unittest.TestCase):
    def setUp(self):
        self.__filename = "test.disciplina_temp.txt"
        with open(self.__filename, "w") as file:
            file.write("")
    def test_load_from_file(self):
        with open(self.__filename, "w") as file:
            file.write("1,Mate,Profesor Unu\n")
            file.write("2,Info,Profesor Doi")

        repo  =  DisciplinaRepositoryFile(self.__filename)

        self.assertEqual(repo.size(), 2)

        d = Disciplina(1, "Mate", "Profesor Unu")
        d_test = repo.cauta_dupa_id(1)
        self.assertEqual(d_test.get_nume(), d.get_nume() )
        self.assertEqual(d_test.get_id_disciplina(), d.get_id_disciplina())
        self.assertEqual(d_test.get_profesor(), d.get_profesor())


    def test_save_to_file(self):
        d = Disciplina(None, "Mate", "Profesor Unu")
        repo = DisciplinaRepositoryFile(self.__filename)
        repo.adauga(d)

        with open(self.__filename, "r")as file:
            line = file.read()
            line = line.strip()

        self.assertEqual(line, "1,Mate,Profesor Unu")

        repo.sterge_dupa_id(1)

        with open(self.__filename,"r") as file:
            line = file.read()
            line = line.strip()
        self.assertEqual(line, "")

    def tearDown(self):
        if os.path.exists(self.__filename):
            os.remove(self.__filename)


class TestNotaRepoFile(unittest.TestCase):
    def setUp(self):
        self.__filename = "test_nota_temp.txt"
        with open(self.__filename, "w") as file:
            file.write("")

    def tearDown(self):
        if os.path.exists(self.__filename):
            os.remove(self.__filename)

    def test_load_from_file(self):
        repo_s = StudentRepository()
        repo_d = DisciplinaRepository()

        s = Student(None, "Student Unu")
        d = Disciplina(None, "Disciplina Unu", "Profesor Unu")

        repo_s.adauga(s)
        repo_d.adauga(d)


        with open(self.__filename, "w") as file:
            file.write("1,1,1,9.5")

        repo_n = NotaRepositoryFile(self.__filename, repo_s, repo_d)

        self.assertEqual(repo_n.size(), 1)

        nota = repo_n.cauta_dupa_id(1)

        s_test = nota.get_student()
        d_test = nota.get_disciplina()

        self.assertEqual(nota.get_id_nota(), 1)
        self.assertEqual(nota.get_nota(), 9.5)

        self.assertEqual(s_test.get_id_student(), s.get_id_student())
        self.assertEqual(s_test.get_nume(), s.get_nume())

        self.assertEqual(d_test.get_id_disciplina(), d.get_id_disciplina())
        self.assertEqual(d_test.get_nume(), d.get_nume())
        self.assertEqual(d_test.get_profesor(), d.get_profesor())



        pass

    def test_save_to_file(self):
        s = Student(None, "Student Unu")
        repo_s = StudentRepository()
        repo_s.adauga(s)

        d = Disciplina(None, "Disciplina Unu", "Profesor Unu")
        repo_d = DisciplinaRepository()
        repo_d.adauga(d)

        n = Nota(None, s, d , 10)
        repo = NotaRepositoryFile(self.__filename, repo_s, repo_d)
        repo.adauga(n)

        with open(self.__filename, "r") as file:
            line = file.read()
            line = line.strip()

        self.assertEqual(line, "1,1,1,10")

        repo.sterge_dupa_id(1)

        with open(self.__filename, "r") as file:
            line = file.read()
            line = line.strip()

        self.assertEqual(line, "")




        pass









if __name__ == '__main__':
    unittest.main()








