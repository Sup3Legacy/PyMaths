class ObjectType :
    id = 0

    def __init__(self, str = "NullType", base = True):
        self.str = str
        self.base = base
        self.id = ObjectType.id
        ObjectType.id += 1

    def __repr__(self):
        return self.str

    def combine(types):
        str = "("
        n = len(types)
        for i in range(n):
            str += types[i].str
            if i < n - 1:
                str += "*"
        str += ")"
        res = ObjectType(str = str, base = False)
        return res

    def function(type1, type2):
        res = ObjectType()
        res.str = type1.str + "->" + type2.str
        res.base = False
        return res

    def egalite(type1, type2):
        return type1.str == type2.str #On raisonne sur le str, là, pas sur l'id! Evite des erreurs de types qui sont équivalents mais non égaux


ObjectType.NullType = ObjectType()


intType = ObjectType(str = "int")

class Object :
    def __init__(self, type = ObjectType.NullType, value = None):
        self.type = type
        self.value = value

    def delete(self):
        del self

    def tuple(objects):
        types = [t.type for t in objects]
        values = [t.value for t in objects]
        return Object(type = ObjectType.combine(types), value = values)



class Set :
    def __init__(self, arbitrary = False, values = None, constructionFunction = None, dimensions = 1, type = intType):
        self.arbitrary = arbitrary
        self.values = values
        self.function = constructionFunction
        self.type = type
        self.dimensions = dimensions

    def empty():
        return Set(arbitrary = True, values = {})



    def cartesien(set1, set2):
        res = Set(arbitrary = set1.arbitrary and set2.arbitrary, values = [set1.values, set2.values], dimensions = set1.dimensions * set2.dimensions)
        return res

    def fill(self):
        pass

Set.emptySet = Set.empty()

class Function :
    def __init__(self, setIn = Set.emptySet, setOut = Set.emptySet, functionValue = None, typeIn = ObjectType.NullType, typeOut = ObjectType.NullType, str = "Undefined function"):
        self.setIn = setIn
        self.setOut = setOut
        self.functionValue = functionValue
        self.typeIn = typeIn
        self.typeOut = typeOut
        self.str = str

    def __call__(self, arg): #Normalement pas de kvargs
        if not ObjectType.egalite(arg.type, self.typeIn):
            print("Erreur de type dans " + self.str)
            print("Arguent donné: " + arg.type)
            print("Argument attendu: " + self.typeIn)
            return None
        res = Object(type = self.typeOut)
        res.value = self.functionValue(*arg.value)
        return res

    def __repr__(self):
        return self.str


def succ(n):
    return n + 1
def succD(n):
    return (- n - 1, n + 1)

N_Set = Set(arbitrary = False, values = {0}, constructionFunction = succ, type = intType, dimensions = 1)
Z_Set = Set(arbitrary = False, values = {0}, constructionFunction = succD, type = intType)










a = Object(type = intType, value = 1)
b = Object(type = intType, value = 2)
c = Object.tuple([a, b])

IntTupleType = ObjectType.combine([intType, intType])

add = Function(setIn = Set.cartesien(N_Set, N_Set), setOut = N_Set, typeIn = IntTupleType, typeOut = intType, functionValue = lambda a, b: a + b)

d = add(c) #On applique add sur le tuple c = (a, b)
print(d.value)
