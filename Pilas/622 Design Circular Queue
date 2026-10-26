class MyCircularQueue:

    def __init__(self, k: int):
        # Guardamos el tamaño máximo que tendrá nuestra cola
        self.capacity = k
        # Creamos una lista fija con ceros del tamaño k (nuestro carrusel)
        self.queue = [0] * k
        # Apuntador para saber dónde está el frente (el que va a salir primero)
        self.head = 0
        # Apuntador para saber dónde está el último elemento que entró
        self.tail = -1
        # Un contador para saber cuántos elementos hay adentro ahora mismo
        self.size = 0

    def enQueue(self, value: int) -> bool:
        # Si la cola ya está llena, no podemos meter nada
        if self.isFull():
            return False
        
        # Movemos el tail a la siguiente posición dando la vuelta con el módulo (%)
        self.tail = (self.tail + 1) % self.capacity
        # Guardamos el valor nuevo en esa posición del carrusel
        self.queue[self.tail] = value
        # Aumentamos en 1 el contador de elementos
        self.size += 1
        return True

    def deQueue(self) -> bool:
        # Si la cola está vacía, no podemos sacar nada
        if self.isEmpty():
            return False
        
        # Movemos el head a la siguiente posición dando la vuelta con el módulo (%)
        self.head = (self.head + 1) % self.capacity
        # Reducimos en 1 el contador porque acabamos de sacar un elemento
        self.size -= 1
        return True

    def Front(self) -> int:
        # Si está vacía, devolvemos -1 como pide el problema
        if self.isEmpty():
            return -1
        # Devolvemos el número que está mero adelante
        return self.queue[self.head]

    def Rear(self) -> int:
        # Si está vacía, devolvemos -1
        if self.isEmpty():
            return -1
        # Devolvemos el último número que entró (el que marca tail)
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        # Si el tamaño es 0, significa que no hay nada
        return self.size == 0

    def isFull(self) -> bool:
        # Si el tamaño llegó al límite (capacity), está lleno
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
