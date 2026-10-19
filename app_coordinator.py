from Controller_Service.service_studenti import ServiceStudenti
from Repository.repository_student import StudentRepository, StudentRepositoryFile
from Repository.repository_diciplina import DisciplinaRepository, DisciplinaRepositoryFile
from Repository.repository_nota import NotaRepository, NotaRepositoryFile
from UI.console import Console
from Domain.validator import StudentValidator
from Domain.validator import DisciplinaValidator
from Domain.validator import NotaValidator
from Controller_Service.service_disciplina import ServiceDisciplina
from Controller_Service.service_nota import ServiceNota
repo = StudentRepositoryFile("data/studenti.txt")
repo_d = DisciplinaRepositoryFile("data/discipline.txt")
repo_student = StudentRepository()
repo_discipline = DisciplinaRepository()
repo_n = NotaRepositoryFile("data/note.txt", repo_student, repo_discipline)
val = StudentValidator()
val_d = DisciplinaValidator()
val_n = NotaValidator()
service = ServiceStudenti( repo, val)
service_disciplina = ServiceDisciplina(repo_d, val_d)
service_nota = ServiceNota(repo_n, val_n, repo, repo_d)
Console = Console(service, service_disciplina, service_nota

                  )
Console.run()


"""
DE TERMINAT PANA SAMBATA:
CERINTA LABORATOR,OK
TESTE STATISTICA OK
TESTE PT CLASA STUDENT, DISCIPLINA, NOTA OK
FIX BUGS DE SCRIERE ETC, INFRUMUSETARE OK
==========================================
UNITY TESTS?
CITIRE DIN FISIER OK
GTO?
"""