import pytermgui as ptg

with ptg.WindowManager() as manager:
    app = ptg.Window(
        ptg.Label('[bold]SimVIM'),
        ptg.InputField(prompt='Insert your note here')
    )

    manager.add(app)
    manager.run()