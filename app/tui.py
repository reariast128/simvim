'''Esta primera versión de la TUI crea una ventana con un input titulado "First Widget" en el que uno puede poner texto.'''

import npyscreen

def myFunction(*args) -> str:
    # name='My Test Application' es el título de la ventana.
    F = npyscreen.Form(name='SimVIM')

    title_text = F.add(npyscreen.TitleText, name="First Widget")
    
    # Con esto lo hacemos editable. También se pudiera usar F.display, pero el comportamiento que deseamos es que este form sea editable.
    F.edit()

    return title_text.value

if __name__ == '__main__':
    print(npyscreen.wrapper_basic(myFunction))