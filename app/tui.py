import pytermgui as ptg

notes = ['Pyt', 'hon']

with ptg.WindowManager() as manager:
    notebooks = ptg.containers(
        
    )

    input_content = ptg.Window(
        ptg.Label('[bold]SimVIM'),
        ptg.InputField(prompt='Insert your note here')
    )

    manager.add(app)
    manager.run()