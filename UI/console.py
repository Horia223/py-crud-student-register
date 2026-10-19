from Repository.repository_errors import RepoError
from Controller_Service.service_studenti import ServiceStudenti
from Controller_Service.service_disciplina import  ServiceDisciplina
from Controller_Service.service_nota import ServiceNota
class Console:
    def __init__(self, service: ServiceStudenti, service_disciplina: ServiceDisciplina, service_nota: ServiceNota):
        self.__service = service
        self.__service_disciplina = service_disciplina
        self.__service_nota = service_nota

    @staticmethod
    def __print_menu():
        print("1.Adauga.")
        print("2.Modifica.")
        print("3.Sterge.")
        print("4.Cautare.")
        print("5.Asignare nota.")
        print("6.Statistici.")
        print("R.Random.")
        print("P.Afisare.")
        print("I.Iesire.")
    @staticmethod
    def __print_menu_adaugare():
        print("1.Adauga Student.")
        print("2.Adauga Disciplina.")
        print("I.Iesire.")

    @staticmethod
    def __print_menu_modificare():
        print("1.Modifica Student.")
        print("2.Modifica Disciplina.")
        print("I.Iesire.")
    @staticmethod
    def __print_menu_stergere():
        print("1.Sterge Student.")
        print("2.Sterge disciplina.")
        print("I.Iesire.")
    @staticmethod
    def __print_menu_afisare():
        print("1.Afisare Studenti.")
        print("2.Afisare Discipline.")
    @staticmethod
    def __print_menu_cautare():
        print("1.Cautare Student.")
        print("2.Cautare Disciplina.")
    @staticmethod
    def __print_menu_statistica():
        print("1.Statistica studenti si notele lor la o disciplina data, ordonat: alfabetic dupa nume, dupa nota.")
        print("2.Statistica primi 20% din studenti ordonat dupa media notelor la toate disciplinele.")
        print("3.Statistica top k studenti si legaturile sale cu top k discipline.")
    def __adaugare_student_ui(self):
        #id_student = input("ID student:")
        nume_student = input("Nume Student:")

        try:
            self.__service.adaugare_student(nume_student)
        except (ValueError, RepoError) as e:
            print(e)
        else:
            print(f"Studentul {nume_student} a fost adaugat cu succes.")
    def __adaugare_disciplina_ui(self):
        nume_disciplina = input("Nume Disciplina:")
        nume_profesor = input("Nume Profesor:")

        try:
            self.__service_disciplina.adaugare_disciplina(nume_disciplina, nume_profesor)
        except ValueError as e:
            print(e)
        else:
            print(f"Disciplina {nume_disciplina} tinuta de profesorul/profesoara {nume_profesor} a fost adaugate cu succes")



    def __stergere_student_ui(self):
        id_student = input("ID-ul studentului care este sters:")
        try:
            id_student = int(id_student)
            student_sters = self.__service.sterge_student(id_student)
            print(f"{student_sters} a fost sters")
        except (RepoError, ValueError) as e:
            print(e)



    def __stergere_disciplina_ui(self):
        id_disciplina = input("ID-ul disciplinei cara urmeaza sa fie sters:")
        try:
            id_disciplina = int(id_disciplina)
            disciplina_stearsa = self.__service_disciplina.sterge_disciplina(id_disciplina)
            print(f"{disciplina_stearsa} a fost sters")
        except (RepoError, ValueError) as e:
            print(e)


    def __cauta_student_ui(self):
        id_student = input("ID-ul studentului care va fi cautat:")
        try:
            id_student = int(id_student)
            student_cautat = self.__service.cauta_dupa_id(id_student)
            print(f"Studentul a fost gasit:\n {student_cautat}")
        except (ValueError, RepoError) as e:
            print(e)

    def __cauta_disciplina_ui(self):
        id_disciplina = input("ID-ul disciplina care va fi cautat:")
        try:
            id_disciplina = int(id_disciplina)
            disciplina_cautat = self.__service_disciplina.cauta_dupa_id(id_disciplina)
            print(f"Disciplina a fost gasita:\n {disciplina_cautat}")
        except (ValueError, RepoError) as e:
            print(e)
    def __random_studenti(self):
        numar = input("Numarul de studenti sa fie random: ")
        try:
            numar = int(numar)
            self.__service.adaugare_studenti_random(numar)
        except (ValueError, RepoError) as e:
            print(e)



    def __modifica_student_ui(self):
        id_student = input("ID-ul studentului care este modificat:")
        nume_nou = input("Numele nou: ")
        try:
            id_student = int(id_student)
            student_vechi = self.__service.modifica_student(id_student, nume_nou)
            print(f"{student_vechi} a fost modificat")
        except (ValueError, RepoError) as e:
            print(e)

    def __modifica_disciplina_ui(self):
        id_disciplina_nou = input("ID-ul disciplinei care va fi modificat:")
        nume_disciplina_nou = input("Nume nou a disciplinei:")
        nume_profesor_nou = input("Nume profesor nou:")
        try:
            id_disciplina_nou = int(id_disciplina_nou)
            disciplina_veche = self.__service_disciplina.modifica_disciplina(id_disciplina_nou, nume_disciplina_nou, nume_profesor_nou)
            print(f"{disciplina_veche} a fost modificat")
        except (ValueError, RepoError) as e:
            print(e)

    def __asignare_note_ui(self):
        id_student = input("Introdu ID-ul studentului care va primi nota:")
        id_disciplina = input("Introdu ID-ul disciplinei la care va primi nota:")
        nota = input("Introdu nota:")
        try:
            id_disciplina = int(id_disciplina)
            id_student = int(id_student)
            nota = float(nota)
            self.__service_nota.adaugare_nota(id_student, id_disciplina,nota)
            print(f"Nota a fost asignata cu succes!")
        except (ValueError, RepoError) as e:
            print(e)
    def __ui_statistica_disciplina(self):
        id_disciplina = input("Introdu ID ul disciplinei:")
        try:
            id_disciplina = int(id_disciplina)
            lista = self.__service_nota.get_statistica_note_disciplina(id_disciplina)
            if len(lista) == 0:
                print("Nu exista note la aceasta disciplina.")
            else:
                print(f"Statistica Disciplina {id_disciplina}")
                for nota in lista:
                    print(f"Student:{nota.get_student().get_nume()} Nota: {nota.get_nota()}")
        except ValueError as e:
            print(e)

    def __ui_statistica_top_20(self):
        lista = self.__service_nota.get_statistica_top_studenti()
        if len(lista) == 0:
            print("Nu exista studenti cu note.")
        else:
            print("Top 20% Studenti:")
            for obiect in lista:
                student = obiect["student"]
                medie = obiect["medie"]
                print(f"Student:{student} Media:{medie}")

    def __ui_statistica_top_K_leg(self):
        k = input("Introdu numarul de studenti/discipline cu care se va face top ul:")
        try:
            k = int(k)
            raport = self.__service_nota.top_k_studenti_discipline_legatura(k)
            if len(raport) == 0:
                print("Nu exista date pentru afisare a statisticii.")
            else:
                i = 1
                for nume_student, lista_mesaje in raport.items():
                    print(f"{i}.{nume_student}")
                    print("\n".join(lista_mesaje))
                    print()
                    i += 1

        except ValueError as e:
            print(e)


    @staticmethod
    def __print_studenti(lista_studenti):
        if not lista_studenti:
            print("Nu exista studenti")
        else:
            print("Lista studenti:")
            for student in lista_studenti:
                print(student)
    @staticmethod
    def __print_discipline(lista_discipline):
        if not lista_discipline:
            print("Nu exista discipline")
        else:
            print("Lista discipline:")
            for disciplina in lista_discipline:
                print(disciplina)

    def run(self):
        while True:
            Console.__print_menu()
            optiune = input(">>>")
            if optiune == "1":

                while True:
                    Console.__print_menu_adaugare()
                    optiune1 = input(">>>")
                    if optiune1 == "1":
                        self.__adaugare_student_ui()
                    elif optiune1 == "2":
                        self.__adaugare_disciplina_ui()
                    elif optiune1 == "i" or optiune1 == "I":
                        break
                    else:
                        print("Comanda invalida")
                    input("Apasa enter sa continui...")
            elif optiune == "2":
                while True:
                    Console.__print_menu_modificare()
                    optiune1 = input(">>>")
                    if optiune1 == "1":
                        self.__modifica_student_ui()
                    elif optiune1 == "2":
                        self.__modifica_disciplina_ui()
                    elif optiune1 == "i" or optiune1 == "I":
                        break
                    else:
                        print("Comanda invalida")
                    input("Apasa enter sa continui...")
            elif optiune == "3":
                while True:
                    Console.__print_menu_stergere()
                    optiune1 = input(">>>")
                    if optiune1 == "1":
                        self.__stergere_student_ui()
                    elif optiune1 == "2":
                        self.__stergere_disciplina_ui()
                    elif optiune1 == "i" or optiune1 == "I":
                        break
                    else:
                        print("Comanda invalida")
                    input("Apasa enter sa continui...")

            elif optiune == "4":
                while True:
                    Console.__print_menu_cautare()
                    optiune1 = input(">>>")
                    if optiune1 == "1":
                        self.__cauta_student_ui()
                    elif optiune1 == "2":
                        self.__cauta_disciplina_ui()
                    elif optiune1 == "i" or optiune1 == "I":
                        break
                    else:
                        print("Comanda invalida")
                    input("Apasa enter sa continui...")

            elif optiune == "5":
                self.__asignare_note_ui()
            elif optiune == "6":
                while True:
                    Console.__print_menu_statistica()
                    optiune1 = input(">>>")
                    if optiune1 == "1":
                        self.__ui_statistica_disciplina()
                    elif optiune1 == "2":
                        self.__ui_statistica_top_20()
                    elif optiune1 == "3":
                        self.__ui_statistica_top_K_leg()
                    elif optiune1 == "i" or optiune1 == "I":
                        break
            elif optiune == "R" or optiune == "r":
                self.__random_studenti()
            elif optiune == "p" or optiune == "P":
                Console.__print_menu_afisare()
                optiune1 = input(">>>")
                if optiune1 == "1":
                    Console.__print_studenti(self.__service.get_studenti())
                if optiune1 == "2":
                    Console.__print_discipline(self.__service_disciplina.get_discipline())
                input("Apasa enter sa continui...")

            elif optiune == "i" or optiune =="I":
                print("Iesire din program...")
                break
            else:
                print("Comanda invalida")









