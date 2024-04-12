import PySimpleGUI as sg
import zipper
label1 = sg.Text("Choose files to compress: ")
files_input = sg.Input(tooltip="Enter files", key="files")
choose_file_btn = sg.FilesBrowse("Choose")

label2 = sg.Text("Choose destination folder: ")
folder_input = sg.Input(tooltip="Enter destination folder", key="folder")
choose_folder_btn = sg.FolderBrowse("Choose")

compress_btn = sg.Button("Compress")

result = sg.Text(key="result", text_color="green")
window = sg.Window("File Zipper",
                   layout=[[label1, files_input, choose_file_btn],
                           [label2, folder_input, choose_folder_btn],
                           [compress_btn, result]])

while True:
    event, values = window.read()
    filepaths = values["files"].split(";")
    folder = values["folder"]
    match event:
        case "Compress":
            zipper.make_archive(filepaths=filepaths, dest=folder)
            window["result"].update(value="Files compressed successfully!")
        case sg.WINDOW_CLOSED:
            break

window.close()
