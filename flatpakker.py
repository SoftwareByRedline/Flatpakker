from tkinter import *

mw = Tk()
mw.title("Flatpakker")

DirPath = StringVar()
AppId = StringVar()
runtime = StringVar()
RuntimeVersion = StringVar()
sdk = StringVar()
command = StringVar()
ModuleBuildsystem = StringVar()


def AddModule():
    ModuleName = StringVar()

    AddModuleWindow = Toplevel(mw)
    AddModuleWindow.title("Add module")

    ModuleNameLabel = Label(AddModuleWindow, text="Module name:")
    ModuleNameLabel.pack()
    ModuleNameEntry = Entry(AddModuleWindow, textvariable=ModuleName)
    ModuleNameEntry.pack()

    BuildsystemLabel = Label(AddModuleWindow, text="Build system:")  # TODO: add "simple" as default
    BuildsystemLabel.pack()
    BuildsystemEntry = Entry(AddModuleWindow, textvariable=ModuleBuildsystem)
    BuildsystemEntry.pack()

    BuildCommandsLabel = Label(AddModuleWindow, text="Build commands:")
    BuildCommandsLabel.pack()


EnterPathLabel = Label(mw, text="Build directory path:")
EnterPathLabel.pack()
DirectoryPathEntry = Entry(mw, textvariable=DirPath)
DirectoryPathEntry.pack()

AppIdLabel = Label(mw, text="App ID:")
AppIdLabel.pack()
AppIdEntry = Entry(mw, textvariable=AppId)
AppIdEntry.pack()

RuntimeLabel = Label(mw, text="Runtime:")
RuntimeLabel.pack()
RuntimeEntry = Entry(mw, textvariable=runtime)  # TODO: add org.freedesktop.Platform as default
RuntimeEntry.pack()

RuntimeVersionLabel = Label(mw, text="Runtime version:")
RuntimeVersionLabel.pack()
RuntimeVersionEntry = Entry(mw, textvariable=RuntimeVersion)
RuntimeVersionEntry.pack()

SdkLabel = Label(mw, text="SDK:")
SdkLabel.pack()
SdkEntry = Entry(mw, textvariable=sdk)
SdkEntry.pack()

CommandLabel = Label(mw, text="Command to execute:")
CommandLabel.pack()
CommandEntry = Entry(mw, textvariable=command)
CommandEntry.pack()

ModulesLabel = Label(mw, text="Modules:")
ModulesLabel.pack()

AddModuleButton = Button(mw, text="Add Module", command=AddModule)
AddModuleButton.pack()

mw.mainloop()
