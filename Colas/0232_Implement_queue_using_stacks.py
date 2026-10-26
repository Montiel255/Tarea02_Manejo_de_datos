class MyQueue:

    def __init__(self):
        #pila para meter 
        self.in_stack = []
        #pila para sacar
        self.out_stack = []

    def push(self, x: int) -> None:
        #creamos la instruccion de meter numeros
        self.in_stack.append(x)

    def pop(self) -> int:
        #creamos la instruccion de sacar numeros
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        # añadimos el return para que devuelva el elemento eliminado
        return self.out_stack.pop()

    def peek(self) -> int:
        #si la pila de los que quitamos esta vacia, pasamos los elementos
        if not self.out_stack:
            while self.in_stack:
                #mete el elemento en la otra pila(saca el ultimo elemento que se metio)
                self.out_stack.append(self.in_stack.pop())
        # esto va a regresar el ultimo elemento
        return self.out_stack[-1] 
        
    def empty(self) -> bool:
        #si la cola esta vacia entonces las 2 pilas anteriores estaban vacias 
        return not self.in_stack and not self.out_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
