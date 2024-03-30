import npyscreen


class myEmployeeForm(npyscreen.Form):
    '''Se crea un Form que va a contener todos los widgets.'''
    def create(self):
        self.myName = self.add(npyscreen.TitleText, name='Name')
        self.myDepartment = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=3, name='Department', values=[
                                     'Department 1', 'Department 2', 'Department 3'])
        self.myDate = self.add(npyscreen.TitleDateCombo, name='Date Employed')


class MyApplication(npyscreen.NPSAppManaged):
    '''Ahora se crea la app, o bueno, prefiero entenderlo como el rootframe que contiene los widgets.'''
    def onStart(self):
        self.addForm('MAIN', myEmployeeForm, name='New Employee')


if __name__ == '__main__':
    '''Y en vez de usar el basic_wrapper() para ejecutar la aplicación se usa el MyApplication().run'''
    TestApp = MyApplication().run()
    print("All objects, baby.")

    print("yolo")
