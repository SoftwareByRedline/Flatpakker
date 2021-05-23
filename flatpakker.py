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

modules = []

runtime.set("org.freedesktop.Platform")
RuntimeVersion.set("19.08")
sdk.set("org.freedesktop.Sdk")


def AddModule():
    ModuleBuildCommands = []
    ModuleSources = []
    ModuleBuildsystem.set("simple")

    def AddModuleEnter():
        modules.append([ModuleBuildCommands, ModuleSources])

    def AddBuildCommand():
        def EnterBuildCommand():
            ModuleBuildCommands.append(BuildCommand.get())
            BuildCommand.set("")
            AddBuildCommandWindow.destroy()

        BuildCommand = StringVar()

        AddBuildCommandWindow = Toplevel(AddModuleWindow)
        AddBuildCommandWindow.title("Add build command")
        AddBuildCommandLabel = Label(AddBuildCommandWindow, text="Build command:")
        AddBuildCommandLabel.pack()
        AddBuildCommandEntry = Entry(AddBuildCommandWindow, textvariable=BuildCommand)
        AddBuildCommandEntry.pack()

        BuildCommandNoFeedbackNoticeLabel = Label(AddBuildCommandWindow, text="Note: Added commands won't show on "
                                                                              "module screen yet.")
        BuildCommandNoFeedbackNoticeLabel.pack()

        EnterBuildCommandButton = Button(AddBuildCommandWindow, text="Done", command=EnterBuildCommand)
        EnterBuildCommandButton.pack()

    def AddSource():
        def EnterSource():
            ModuleSources.append([ModuleName.get(), ModuleBuildsystem.get(), SourceType.get(), SourcePath.get()])

        SourceType = StringVar()
        SourceType.set("file")

        SourcePath = StringVar()
        SourcePath.set("")

        AddSourceWindow = Toplevel(AddModuleWindow)
        AddSourceWindow.title("Add source")

        AddSourceTypeLabel = Label(AddSourceWindow, text="Source type:")
        AddSourceTypeLabel.pack()
        AddSourceTypeEntry = Entry(AddSourceWindow, textvariable=SourceType)
        AddSourceTypeEntry.pack()

        AddSourcePathLabel = Label(AddSourceWindow, text="Source path:")
        AddSourcePathLabel.pack()
        AddSourcePathEntry = Entry(AddSourceWindow, textvariable=SourcePath)
        AddSourcePathEntry.pack()

        AddSourceEnterButton = Button(AddSourceWindow, text="Done", command=EnterSource)
        AddSourceEnterButton.pack()

    ModuleName = StringVar()

    AddModuleWindow = Toplevel(mw)
    AddModuleWindow.title("Add module")

    ModuleNameLabel = Label(AddModuleWindow, text="Module name:")
    ModuleNameLabel.pack()
    ModuleNameEntry = Entry(AddModuleWindow, textvariable=ModuleName)
    ModuleNameEntry.pack()

    BuildsystemLabel = Label(AddModuleWindow, text="Build system:")
    BuildsystemLabel.pack()
    BuildsystemEntry = Entry(AddModuleWindow, textvariable=ModuleBuildsystem)
    BuildsystemEntry.pack()

    BuildCommandsLabel = Label(AddModuleWindow, text="Build commands:")
    BuildCommandsLabel.pack()

    AddModuleBuildCommandButton = Button(AddModuleWindow, text="Add build command", command=AddBuildCommand)
    AddModuleBuildCommandButton.pack()

    SourcesLabel = Label(AddModuleWindow, text="Sources:")
    SourcesLabel.pack()
    AddSourceButton = Button(AddModuleWindow, text="Add source", command=AddSource)
    AddSourceButton.pack()

    AddModuleEnterButton = Button(AddModuleWindow, text="Done", command=AddModuleEnter)
    AddModuleEnterButton.pack()


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
RuntimeEntry = Entry(mw, textvariable=runtime)
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


def BuildFlatpak():
    yml_file_out = open(DirPath.get() + "/" + AppId.get() + ".yml", "w")
    print("app-id: %s\nruntime: %s\nruntime-version: \'%s\'\nsdk: %s\ncommand: %s\nmodules:" % (
    AppId.get(), runtime.get(), RuntimeVersion.get(), sdk.get(), command.get()), file=yml_file_out)

    for module in modules:
        print("\t- name: %s\n\t  buildsystem: %s\n\t  build-commands:" % (module[0], module[1]), file=yml_file_out)

        for buildCommand in module[2]:
            print("\t    - %s" % buildCommand, file=yml_file_out)

        print("\t  sources:", file=yml_file_out)

        for source in module[3]:
            print("\t    - type: %s\n\t      path: %s" % (source[0], source[1]))

    yml_file_out.close()


BuildButton = Button(mw, text="Build", command=BuildFlatpak)
BuildButton.pack()

mw.mainloop()
