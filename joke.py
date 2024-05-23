"""this function create a joke and tells us"""
import pyjokes
def joke():
    return pyjokes.get_joke()

joke = joke()
print(joke)