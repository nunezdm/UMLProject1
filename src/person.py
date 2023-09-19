from abc import ABC
from typing import List

class Persona(ABC):

    def __init__(self, nombre : str, cedula: int ) -> None:
        self._nombre = nombre #Protegido, un solo _
        self._cedula = cedula #Protegido, un solo _

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._cedula}, {self._nombre!r})" #!r le pone comillas al str
    
    
class Autor(Persona):

    def __init__(self, nombre: str, cedula: int) -> None:
        super().__init__(nombre, cedula)
        self.__libros: List["Libro"] = [] #Privado, doss _

