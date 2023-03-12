class Categorias:
    pass
    categoria1="Accion"
    categoria2="Terror"
    categoria3="Comedia"
    
    from Categorias import Categorias

class Peliculas(Categorias):
    pass
    
    def __init__(self,Pelicula1,Pelicula2,pelicula3):
        
        self.Pelicula1=Pelicula1
        self.Pelicula2=Pelicula2
        self.Pelicula3=pelicula3
        

    def CategoriaAccion(self):
        return"Las siguiente Peliculas son de la categoria: {}  \n {} \n {}  \n {}".format(Categorias.categoria1,self.Pelicula1,self.Pelicula2,self.Pelicula3)
    
    def CategoriaTerror(self):
        return"\nLas siguiente Peliculas son de la categoria: {}  \n {} \n {}  \n {}".format(Categorias.categoria2,self.Pelicula1,self.Pelicula2,self.Pelicula3)

    def CategoriaComedia(self):
        return"\nLas siguiente Peliculas son de la categoria: {}  \n {} \n {}  \n {}".format(Categorias.categoria3,self.Pelicula1,self.Pelicula2,self.Pelicula3)

    
verCategoria1 = Peliculas("Rapidos y furiosos","Iron Man","The Batman")
print(verCategoria1.CategoriaAccion())
verCategoria2 = Peliculas("La luz del Diablo","La abuela","El Conjuro 3")
print(verCategoria2.CategoriaTerror())
verCategoria3 = Peliculas("Que paso ayer","Super Cool","Ted")
print(verCategoria3.CategoriaComedia())

from Peliculas import Peliculas
from Peliculas import verCategoria1

class Cliente (Peliculas):
      
    def __init__(self, Peli1):
        
        self.Peli1=Peli1
        
 
    def ValidarPeli(self):
        Validacion1=verCategoria1.Pelicula1

        if Validacion1 ==self.Peli1:
            print("\n/////////////////////////////////////////////////////////////////////////////////////////////")
            print(" Usted a elegido una pelicula de accion y la pelicula que usted eligio es: Rapidos y furiosos" )
            print("////////////////////////////////////////////////////////////////////////////////////////////////")
        else:
            print("Error")

Progra1 = Cliente("Rapidos y furiosos")
print(Progra1.ValidarPeli())
