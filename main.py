import random


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.up = None
        self.down = None


class DLL:

    def __init__(self):
        self.head = Node(0)

    def crearMatriz(self, n):
        current = self.head
        i = 1
        while i < n:
            curd = current
            j = 1
            while j < n:
                # valor = random.randint(0,1)
                # if valor == 0:
                #   nodo = Node(j)
                #   current.down = nodo
                # else:
                jos = curd.down = Node(j)
                jos.up = curd
                curd = jos
                j += 1
            #   valorf = random.randint(0,1)
            #   if valorf == 0:
            #       nodo = Node(i)
            #   else:
            aj = current.next = Node(i)
            aj.prev = current

            current = aj
            i += 1

    def Unir_next(self):
        unir = self.head

        while unir.next != None:
            print("unir")
            unir2 = unir.down
            unir_frente = unir.next.down
            while unir2 != None:
                if unir_frente != None:
                    unir2.next = unir_frente
                    unir2 = unir2.down
                    unir_frente = unir_frente.down

                else:
                    break

            unir = unir.next

    def unir_prev(self):

        unir = self.head

        while unir.next != None:

            unir2 = unir.down
            unir_izq = unir.next.down

            while unir2 != None:
                if unir_izq != None:

                    unir_izq.prev = unir2
                    unir_izq = unir_izq.down
                    unir2 = unir2.down

                else:
                    break

            unir = unir.next

    def traverse2(self):
        current = self.head
        col = current
        row = current
        for i in range(0, self.n):
            while current != None:
                print(current.value, ", ", end=" ")
                current = current.right
            row = row.down
            current = row
            print("\n")


