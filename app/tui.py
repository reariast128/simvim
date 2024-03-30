'''Esta primera versión de la TUI crea una ventana con un input titulado "First Widget" en el que uno puede poner texto.'''

import npyscreen


class myEmployeeForm(npyscreen.Form):
    def create(self):
        # Al parecer este super().create no es necesario, pero uno nunca sabe.
        # La descripción del método sugiere que se sobreescriba para crear los widgets ahí. NPI.
        super(myEmployeeForm, self).create()

        # Este crea un label con input con nombre 'Name'
        self.myName = self.add(npyscreen.TitleText, name='Name')

        # Ahora esto es una lista de selección.
        self.myDepartment = self.add(npyscreen.TitleSelectOne, max_height=3,
                                     name='Department',
                                     values=['Department 1',
                                             'Department 2', 'Department 3'],
                                     scroll_exit=True  # Esto permite que el usuario se pueda salir del widget.
                                     )

        # Este crea un input con calendario llamado 'Date Employed'
        self.myDate = self.add(npyscreen.TitleDateCombo, name='Date Employed')

def myFunction(*args):
    '''Se crea una función, que se encarga de hacer toda la magia con las ventanas y tal. Como si fuera el main(), más o menos.
        Este *args no se puede remover, crashea.'''
    F = myEmployeeForm(name='New Employee')
    F.edit()
    return f'Created record for {F.myName.value}'


if __name__ == '__main__':
    # Y se llama usando el wrapper_basic este.
    print(npyscreen.wrapper_basic(myFunction))
