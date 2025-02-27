import unittest
import pytest
import inspect
import math
from src.external_service import Shape, Circle

# class TestShape(unittest.TestCase):
#     def test_shape_is_abstract(self):
#         """Verifica che Shape sia una classe astratta non istanziabile"""
#         with self.assertRaises(TypeError):
#             Shape()
            
# class TestCircle(unittest.TestCase):
#     def setUp(self):
#         self.circle = Circle(5)
        
#     def test_circle_initialization(self):
#         """Verifica che Circle venga inizializzato correttamente"""
#         self.assertEqual(self.circle.radius, 5)
        
#     def test_circle_area(self):
#         """Verifica che il metodo area di Circle funzioni correttamente"""
#         expected_area = math.pi * 5 ** 2
#         self.assertAlmostEqual(self.circle.area(), expected_area)
        
#     def test_circle_perimeter(self):
#         """Verifica che il metodo perimeter di Circle funzioni correttamente"""
#         expected_perimeter = 2 * math.pi * 5
#         self.assertAlmostEqual(self.circle.perimeter(), expected_perimeter)
        
#     def test_circle_with_zero_radius(self):
#         """Verifica il comportamento con raggio zero"""
#         circle = Circle(0)
#         self.assertEqual(circle.area(), 0)
#         self.assertEqual(circle.perimeter(), 0)
        
#     def test_circle_with_negative_radius(self):
#         """Verifica il comportamento con raggio negativo"""
#         with self.assertRaises(ValueError):
#             Circle(-1)

# Implementazione pytest (alternativa)
def test_circle_pytest():
    """Test con pytest per Circle"""
    circle = Circle(10)
    assert circle.radius == 10
    assert circle.area() == pytest.approx(math.pi * 100)
    assert circle.perimeter() == pytest.approx(2 * math.pi * 10)

# def test_circle_implements_shape_interface():
#     """Verifica che Circle implementi correttamente l'interfaccia Shape"""
#     # Verifica che Circle sia una sottoclasse di Shape
#     assert issubclass(Circle, Shape)
    
#     # Verifica che Circle abbia implementato tutti i metodi astratti
#     circle = Circle(5)
    
#     # Verifica che i metodi dell'interfaccia esistano e siano chiamabili
#     assert hasattr(circle, "area") and callable(getattr(circle, "area"))
#     assert hasattr(circle, "perimeter") and callable(getattr(circle, "perimeter"))
    
#     # Verifica che i metodi funzionino come previsto
#     assert circle.area() == pytest.approx(math.pi * 25)
#     assert circle.perimeter() == pytest.approx(2 * math.pi * 5)





# # def test_shape_is_abstract():
# #     """Verifica che Shape sia una classe astratta"""
# #     assert inspect.isabstract(Shape)

# def test_shape_abstract_methods():
#     """Verifica la presenza dei metodi astratti e il loro contenuto"""
#     # Ottieni i metodi astratti
#     abstract_methods = {name for name, method in inspect.getmembers(Shape, predicate=inspect.isfunction)
#                        if getattr(method, '__isabstractmethod__', False)}
    
#     # Verifica che ci siano esattamente i metodi area e perimeter
#     assert abstract_methods == {'area', 'perimeter'}
    
#     # Verifica il contenuto dei metodi (che contengono pass)
#     # Questo è un po' hacky ma funziona per la copertura
#     area_source = inspect.getsource(Shape.area)
#     perimeter_source = inspect.getsource(Shape.perimeter)
    
#     assert "pass" in area_source
#     assert "pass" in perimeter_source

# def test_cannot_instantiate_shape():
#     """Verifica che non si possa istanziare direttamente Shape"""
#     with pytest.raises(TypeError) as exc_info:
#         Shape()
    
#     # Verifica che l'errore sia dovuto al fatto che Shape è astratta
#     assert "abstract" in str(exc_info.value).lower()

# def test_concrete_subclass_must_implement_methods():
#     """Verifica che una sottoclasse concreta debba implementare i metodi"""
#     # Definisci una classe incompleta che eredita da Shape
#     class IncompleteShape(Shape):
#         pass
    
#     # Verifica che non si possa istanziare perché mancano i metodi
#     with pytest.raises(TypeError) as exc_info:
#         IncompleteShape()
    
#     # Verifica che l'errore menzioni i metodi mancanti
#     error_message = str(exc_info.value).lower()
#     assert "abstract" in error_message
#     assert "area" in error_message or "perimeter" in error_message
