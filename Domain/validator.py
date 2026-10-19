from Domain.Student import  Student
from Domain.Disciplina import Disciplina
from Domain.Nota import Nota
class StudentValidator:
    @staticmethod
    def validate( student: Student):
        errors = []
        if student.get_nume() == "":
            errors.append("Numele nu poate sa fie vid")
        nume = student.get_nume()
        nume = nume.strip()
        if not all(c.isalpha() or c.isspace() for c in nume):
            errors.append("Numele trebuie sa fie format doar din litere!")
        if " " not in nume:
            errors.append("Numele trebuie sa contina Numele de familie si Prenumele")

        #if bool(re.fullmatch(r"[A-Za-z]+(?: [A-Za-z]+)+", name)):

        if len(errors) > 0:
            raise ValueError('\n'.join(errors))

class DisciplinaValidator:
    @staticmethod
    def validate(disciplina: Disciplina):
        errors = []
        if disciplina.get_nume() == "":
            errors.append("Numele disciplinei nu poate sa fie vid")
        elif not all(parte.isalpha() for parte in disciplina.get_nume().split()):
            errors.append("Numele disciplinei trebuie sa fie format doar din litere si spatiu")
        if disciplina.get_profesor() == "":
            errors.append("Numele profesorului nu poate sa fie vid")
        elif not all(parte.isalpha() for parte in disciplina.get_profesor().split()):
            errors.append("Numele profesorului trebuie sa contina doar litere")
        nume_profesor = disciplina.get_profesor()
        nume_profesor = nume_profesor.strip()
        if " " not in nume_profesor:
            errors.append("Numele profesorului trebuie sa contina Numele de familie si Prenumele")
        if len(errors) > 0:
            raise ValueError(('\n'.join(errors)))
class NotaValidator:
    @staticmethod
    def validate(nota: Nota):
        errors = []
        if nota.get_nota()< 1 or nota.get_nota() > 10:
            errors.append("Nota trebuie sa fie intre 1 si 10!")

        if nota.get_student() is None:
            errors.append("Studentul lipseste") #s ar putea sa fie redundant

        if nota.get_disciplina() is None:
            errors.append("Disciplina lipseste") # reduntant?

        if len(errors) > 0:
            raise ValueError(('\n'.join(errors)))








