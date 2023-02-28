import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class FileOrganizerGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("file organizer")
        self.geometry("400x200")

        self.dir_path = tk.StringVar()
        self.dir_path.set("")

        tk.Label(self, text="Specify the folder path for organizing the files:").pack()
        tk.Entry(self, textvariable=self.dir_path).pack()

        tk.Button(self, text="Folder selection",
                  command=self.choose_directory).pack()
        tk.Button(self, text="Organizing files",
                  command=self.organize_files).pack()

    def choose_directory(self):
        self.dir_path.set(filedialog.askdirectory())

    def organize_files(self):
        dir_path = self.dir_path.get()
        if dir_path:
            # قائمة بامتدادات الملفات التي يجب تنظيمها
            file_exts = {
                'mp4': 'mp4',
                'aif': 'aif',
                'cda': 'cda',
                'mid': 'mid',
                'midi': 'midi',
                'mp3': 'mp3',
                'mpa': 'mpa',
                'ogg': 'ogg',
                'wav': 'wav',
                'wma': 'wma',
                'wpl': 'wpl',
                '7z': '7z',
                'arj': 'arj',
                'deb': 'deb',
                'pkg': 'pkg',
                'rar': 'rar',
                'rpm': 'rpm',
                'zip': 'zip',
                'Z': 'Z',
                'bin': 'bin',
                'dmg': 'dmg',
                'iso': 'iso',
                'toast': 'toast',
                'vcd': 'vcd',
                'csv': 'csv',
                'apk': 'apk',
                'bat': 'bat',
                'exe': 'exe',
                'gadget': 'gadget',
                'jar': 'jar',
                'msi': 'msi',
                'py': 'py',
                'wsf': 'wsf',
                'fnt': 'fnt',
                'ai': 'ai',
                'bmp': 'bmp',
                'gif': 'gif',
                'ico': 'ico',
                'jpg': 'jpg',
                'jpeg': 'jpeg',
                'png': 'png',
                'ps': 'ps',
                'psd': 'psd',
                'svg': 'svg',
                'asp': 'asp',
                'aspx': 'aspx',
                'css': 'css',
                'pl': 'pl',
                'html': 'html',
                'htm': 'htm',
                'js': 'js',
                'jsp': 'jsp',
                'part': 'part',
                'php': 'php',
                'xhtml': 'xhtml',
                'vb': 'vb',
                'sh': 'sh',
                'xls': 'xls',
                'xlsm': 'xlsm',
                'xlsx': 'xlsx',
                'ods': 'ods',
                'bak': 'bak',
                'cab': 'cab',
                'msi': 'msi',
                '3gp': '3gp',
                'avi': 'avi',
                'flv': 'flv',
                'h264': 'h264',
                'm4v': 'm4v',
                'mkv': 'mkv',
                'mov': 'mov',
                'mpeg': 'mpeg',
                'mpg': 'mpg',
                'rm': 'rm',
                'swf': 'swf',
                'vob': 'vob',
                'wmv': 'wmv',
                'docx': 'docx',
                'doc': 'doc',
                'odt': 'odt',
                'vob': 'vob',
                'pdf': 'pdf',
                'rtf': 'rtf',
                'tex': 'tex',
                'txt': 'txt',
                'wpd': 'wpd'
            }

            # الانتقال إلى المجلد المحدد
            os.chdir(dir_path)

            # الحصول على جميع الملفات في المجلد وتنظيمها حسب الامتداد
            for file in os.listdir():
                if os.path.isfile(file):
                    file_ext = file.split('.')[-1].lower()
                    if file_ext in file_exts.keys():
                        # إنشاء مجلد جديد إذا لم يكن موجوداً
                        if not os.path.exists(file_exts[file_ext]):
                            os.mkdir(file_exts[file_ext])
                        # نقل الملف إلى المجلد المناسب
                        shutil.move(file, file_exts[file_ext])
            tk.messagebox.showinfo("Completed", "Files organized successfully.")
        else:
            tk.messagebox.showerror("Error", "The folder path must be specified.") 

if __name__ == "__main__":
    app = FileOrganizerGUI()
    app.mainloop()

