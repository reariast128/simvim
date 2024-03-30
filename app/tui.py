'''Esta primera versión de la TUI crea una ventana con un input titulado "First Widget" en el que uno puede poner texto.'''

import npyscreen


class myEmployeeForm(npyscreen.Form):
    def create(self):
        # Al parecer este super().create no es necesario, pero uno nunca sabe.
        # La descripción del método sugiere que se sobreescriba para crear los widgets ahí. NPI.
        super(myEmployeeForm, self).create()

        # Este crea un label con input con nombre 'Name'
        self.myName = self.add(npyscreen.TitleText, name='Name')

        # Este crea un label con input con nombre 'Department'
        self.myDepartment = self.add(npyscreen.TitleText, name='Department')

        # Este crea un input con calendario llamado 'Date Employed'
        self.myDate = self.add(npyscreen.TitleDateCombo, name='Date Employed')

# Se crea una función, que se encarga de hacer toda la magia con las ventanas y tal. Como si fuera el main(), más o menos.
# Este *args no se puede remover, crashea.
def myFunction(*args):
    F = myEmployeeForm(name = 'New Employee')
    F.edit()
    return f'Created record for {F.myName.value}'

if __name__ == '__main__':
    # Y se llama usando el wrapper_basic este.
    print(npyscreen.wrapper_basic(myFunction))