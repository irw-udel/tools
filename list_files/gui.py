import tkinter as tk
from tkinter import filedialog
from list_files import list_files

def select_folder(entry):
    folder_path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, folder_path)

def run():
    # Check file input
    input_path = entry_input.get()
    project_path = entry_output.get()

    if (not input_path):
        msg = 'Note: Please select a folder for input'
        bar_status.config(text = msg)
        return
    # elif (not project_path):
    #     msg = 'Note: Please select a folder for output'
    #     bar_status.config(text = msg)
    #     return
    else:
        # Run
        bar_status.config(text = "Running...")
        root.update()
        list_files(input_path, project_path)
        bar_status.config(text = "Done!")
        return

if __name__ == '__main__':
    # Set up window
    root = tk.Tk()
    root.title('App')
    root.geometry('300x210+200+200')
    root.minsize(200, 160)
    root.columnconfigure(0,weight=1)
    
    # Set frames for layout
    frame_paths = tk.Frame(root)
    frame_paths.grid(sticky = tk.EW)
    frame_paths.columnconfigure(1, weight=1)

    frame_run = tk.Frame(root)
    frame_run.grid(sticky=tk.EW)
    frame_run.columnconfigure(0, weight=1)

    frame_stdout = tk.Frame(root)
    frame_stdout.grid(sticky=tk.NSEW)
    frame_stdout.columnconfigure(0, weight=1)
    frame_stdout.rowconfigure(0,weight=1)
    root.rowconfigure(2, weight=1)

    frame_info = tk.Frame(root)
    frame_info.grid(sticky=(tk.S, tk.EW))
    frame_info.columnconfigure(0, weight=1)


    # Path input fields
    button_input = tk.Button(frame_paths, text = 'Input Folder', command = lambda:select_folder(entry_input))
    button_input.grid(row = 0, column = 0, padx=5, pady=5, sticky=tk.EW)
    entry_input = tk.Entry(frame_paths)
    entry_input.grid(row=0, column=1, padx = 5, pady=5, sticky=tk.EW)

    button_output = tk.Button(frame_paths, text = '.git Parent\n(optional)', command = lambda:select_folder(entry_output))
    entry_output = tk.Entry(frame_paths)
    button_output.grid(row = 1, column = 0, padx=5, pady=5, sticky=tk.EW)
    entry_output.grid(row=1, column=1, padx = 5, pady=5, sticky=tk.EW)

    # Run options
    button_run = tk.Button(frame_run, text = 'Run', command = run, padx=10, pady=10)
    button_run.grid(column=0, row = 0, padx=10, pady=10, sticky=tk.EW)

    # Bottom info
    bar_status = tk.Label(frame_info, text=(f"Software v0.1.0"), bd=1, relief=tk.SUNKEN, anchor='w')
    bar_status.grid(sticky=(tk.S, tk.EW))

    # Run GUI
    root.mainloop()