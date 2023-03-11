class Estudiantes:
    
        estudiante1="Martha Cruz"
        estudiante2="Pablo Giron"
        
        
class Materias:

    materia1="POO"
    materia2="Etica"
    
from Estudiantes import Estudiantes
from Materias import Materias


class Notas(Estudiantes,Materias):
        pass
        LabEstud1POO=10       #Nota laboratorio de Poo de  el estudiante 1
        LabEstud1Etica=10     #Nota laboratorio de Etica de  el estudiante 1
        LabEstud2POO=10       #Nota laboratorio de POO de  el estudiante 2
        LabEstud2Etica=9      #Nota laboratorio de Etica de  el estudiante2
        ParEstud1POO=10       #Nota parcial de POO de el estudiante 1
        ParEstud1Etica=9.50   #Nota Parcialde  de Etica de el estudiante1
        ParEstud2POO=9.50     #Nota parcial de Poo de el estudiante2
        ParEstud2Etica=8      #Nota Parcial de Etica de el estudiante2
         
        def VerNotas():
          return "La estudiante {}  obtuvo las siguientes calificaciones en las materias: \n Materia: {} \n Nota Laboratorio:{} \n Nota Parcial:{} \n\n Materia: {} \n Nota Laboratorio: {} \n Nota Parcial: {}".format(Estudiantes.estudiante1,Materias.materia1,Notas.LabEstud1POO,Notas.ParEstud1POO,Materias.materia2,Notas.LabEstud1Etica,Notas.ParEstud1Etica)

MostrarNotas = Notas()
print(Notas.VerNotas())
