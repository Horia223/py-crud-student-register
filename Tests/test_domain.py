from Domain.Student import Student
from Domain.validator import StudentValidator
from Domain.Disciplina import Disciplina
from Domain.validator import DisciplinaValidator
from Domain.Nota import Nota
from Domain.validator import NotaValidator
import unittest
class TestRepoStundeti(unittest.TestCase):

    def test_student(self):
        student = Student(100, "Nume")
        self.assertEqual(student.get_id_student(),100)
        self.assertEqual(student.get_nume(), "Nume")
        student.set_id_student(1)
        self.assertEqual(student.get_id_student(), 1)
        student.set_nume("Horia")
        self.assertEqual(student.get_nume(), "Horia")

    def test_equal_student(self):
        student1 = Student(1, "Nume")
        student2 = Student(1, "Marian")
        student3 = Student(2, "Nume")
        self.assertEqual(student1, student2)
        self.assertNotEqual(student1, student3)

    def test_disciplina(self):
        d1 = Disciplina(1, "Matematica", "Nume Profesor")
        self.assertEqual(d1.get_id_disciplina(), 1)
        self.assertEqual(d1.get_nume(),"Matematica")
        self.assertEqual(d1.get_profesor(), "Nume Profesor")
        d1.set_id_disciplina(2)
        self.assertEqual(d1.get_id_disciplina(), 2)
        d1.set_nume("Informatica")
        self.assertEqual(d1.get_nume(), "Informatica")
        d1.set_profesor("Profesor Nume")
        self.assertEqual(d1.get_profesor(), "Profesor Nume")


    def test_equal_disciplina(self):
        d1 = Disciplina(1, "Matematica", "Nume Profesor")
        d2 = Disciplina(1, "S", "P")
        d3 = Disciplina(2, "Matematica", "Nume Profesor")
        self.assertEqual(d1, d2)
        self.assertNotEqual(d2, d3)

    def test_nota(self):
        s1 = Student(1, "Istrate Horia")
        d1 = Disciplina(1, "Mate", "Profesor")
        s = Nota(1, s1, d1, 10)
        self.assertEqual(s.get_id_nota(), 1)
        self.assertEqual(s.get_student(), s1)
        self.assertEqual(s.get_disciplina(), d1)

    def test_equal_nota(self):
        s1 = Student(1, None)
        s2 = Student(2, None)
        d1 = Disciplina(1, None, None)
        d2 = Disciplina(2, None, None)
        n = Nota(1, s1, d1, 10)
        n1 = Nota(2, s2, d2, 9)
        n2 = Nota(2, s1, d1, 2)
        self.assertNotEqual(n, n1)
        self.assertNotEqual(n2, n)

    def test_validator_student(self):
        s = Student(123, "Istrate Horia")
        val = StudentValidator()
        val.validate(s)

        s1 = Student(12321, "Constantin")

        self.assertRaises(ValueError,val.validate, s1)
        s2 = Student(123, "Miha1 Eminescu")
        self.assertRaises(ValueError,val.validate, s2)
        s3 = Student(123, "")
        self.assertRaises(ValueError, val.validate, s3)

    def test_validator_disciplina(self):
        d1 = Disciplina(1, "", "")
        val = DisciplinaValidator()
        ms = "Numele disciplinei nu poate sa fie vid\nNumele profesorului nu poate sa fie vid\nNumele profesorului trebuie sa contina Numele de familie si Prenumele"
        with self.assertRaises(ValueError) as msj:
            val.validate(d1)
        self.assertEqual(ms, str(msj.exception))

        d1 = Disciplina(2, "Matematica", "Horia")
        ms = "Numele profesorului trebuie sa contina Numele de familie si Prenumele"
        with self.assertRaises(ValueError) as e:
            val.validate(d1)
        self.assertEqual(ms, str(e.exception))

        d1 = Disciplina(3, "Matematica", "H0ria Istrate")
        ms = "Numele profesorului trebuie sa contina doar litere"
        with self.assertRaises(ValueError) as e:
            val.validate(d1)
        self.assertEqual(ms, str(e.exception))


    def test_validator_nota(self):
        val = NotaValidator()
        s1 = Student(1, "Istrate Horia")
        d1 = Disciplina(1, "Mate", "Ispasoiu Dorel")
        n = Nota(1, s1, d1, 0)
        self.assertRaises(ValueError, val.validate, n)

        n = Nota(1, s1, d1, 11)
        msj = "Nota trebuie sa fie intre 1 si 10!"
        with self.assertRaises(ValueError) as e:
            val.validate(n)
        self.assertEqual(msj, str(e.exception))

        n = Nota(1, None, None, 10)
        msj = "Studentul lipseste\nDisciplina lipseste"
        with self.assertRaises(ValueError) as e:
            val.validate(n)
        self.assertEqual(msj, str(e.exception))


def test_student():
    student = Student(100, "Nume")
    assert student.get_id_student() == 100
    assert student.get_nume() == "Nume"
    student.set_id_student(1)
    assert student.get_id_student() == 1
    student.set_nume("Horia")
    assert student.get_nume() == "Horia"

def test_equal_student():
    student1 = Student(1,"Nume")
    student2 = Student(1, "Marian")
    student3 = Student(2, "Nume")
    assert student1 == student2
    assert not student1 == student3

def test_disciplina():
    d1= Disciplina(1, "Matematica", "Nume Profesor")
    assert d1.get_id_disciplina() == 1
    assert d1.get_nume() == "Matematica"
    assert d1.get_profesor() == "Nume Profesor"
    d1.set_id_disciplina(2)
    assert d1.get_id_disciplina() == 2
    d1.set_nume("Informatica")
    assert d1.get_nume() == "Informatica"
    d1.set_profesor("Profesor Nume")
    assert d1.get_profesor() == "Profesor Nume"

def test_equal_disciplina():
    d1 = Disciplina(1, "Matematica", "Nume Profesor")
    d2 = Disciplina(1, "S", "P")
    d3 = Disciplina(2, "Matematica", "Nume Profesor")
    assert d1 == d2
    assert not d2 == d3
def test_nota():
    s1 = Student(1, "Istrate Horia")
    d1 = Disciplina(1, "Mate", "Profesor")
    s = Nota(1, s1, d1, 10 )
    assert s.get_id_nota() == 1
    assert s.get_student() == s1
    assert s.get_disciplina() == d1


def test_equal_nota():
    s1 = Student(1, None)
    s2 = Student(2, None)
    d1 = Disciplina(1, None, None)
    d2 = Disciplina(2, None, None)
    n = Nota(1, s1, d1, 10)
    n1 = Nota(2, s2, d2, 9)
    n2= Nota(2, s1, d1, 2)
    assert not n == n1
    assert not n2 == n



if __name__ == "__main__":
    test_student()
    test_equal_student()
    test_disciplina()
    test_equal_disciplina()
    test_nota()
    test_equal_nota()
    test_validator_student()
    test_validator_disciplina()
    test_validator_nota()