import npyscreen
from typing import List

class NoteApp(npyscreen.Form):
    '''Form principal que va a contener todos los elementos'''

    def afterEditing(self) -> None:
        '''Se sobreescribe este método para poder salir de la aplicación con el botón "Ok"'''
        self.parentApp.setNextForm(None)

    def create(self) -> None:
        self.myName = self.add(npyscreen.TitleText, name='Name')
        self.myDepartment = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=3, name='Cuadernos', values=[
                                     'Department 1', 'Department 2', 'Department 3'])
        self.myDate = self.add(npyscreen.TitleDateCombo, name='Date Employed')


class MyApplication(npyscreen.NPSAppManaged):
    '''Ahora se crea la app, o bueno, prefiero entenderlo como el rootframe que contiene los widgets.'''
    def onStart(self) -> None:
        self.addForm('MAIN', NoteApp, name='New Employee')


if __name__ == '__main__':
    '''Y en vez de usar el basic_wrapper() para ejecutar la aplicación se usa el MyApplication().run'''
    TestApp = MyApplication()
    TestApp.run()
