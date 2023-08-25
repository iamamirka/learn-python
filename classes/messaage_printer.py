class MessagePrinter:
    name = ''

    def __init__(self, name):
        self.name = name

    def print_hello(self):
        print("hello " + self.name)

    def print_hello_custom(self, custom_name):
        print("hello " + custom_name)

printer_1 = MessagePrinter('Amir')
printer_2 = MessagePrinter('Foo')

printer_1.print_hello()
printer_2.print_hello()
printer_2.print_hello_custom('Baz')