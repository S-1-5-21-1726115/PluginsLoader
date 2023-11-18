#依赖7z.exe,请自行下载

from tkinter import messagebox
import os

def StartUpDisk(Disk):
    if os.path.exists("{}:\StartUpFolder".format(Disk)):
        try:
            headerfile=open("{}:\StartUpFolder".format(Disk),"r+")
        except Exception as e:
            messagebox.showerror("错误","{},对了，你是不是想创建一个文件夹糊弄？有没有这么一种可能，你的权限不够？".format(e))
        if headerfile.read()=="[StartUpFolder][/StartUpFolder]":
            return True
        else:
            return False
        headerfile.close()
    else:
        return False


NotFound=True
for i in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
    disk=StartUpDisk(i)
    if disk:
        if not os.path.exists(f"{i}:\Plugins"):
            os.mkdir(f"{i}:\Plugins")
            messagebox.showinfo("信息","已创建存放插件的目录，请注销后重新登录")
        else:
            plugin=os.listdir(f"{i}:\Plugins")
            if plugin==[]:
                messagebox.showinfo("信息","没有发现插件")
            else:
                for j in plugin:
                    if j.endswith(".7z"):
                        os.system("7z.exe x {}:\Plugins\{} -oX:\Plugins\{}".format(i,j,j.rstrip(".7z")))
                        os.system("start X:\Plugins\{}\Install.bat".format(j.rstrip(".7z")))
                        messagebox.showinfo("信息","已加载插件：{}".format(j.rstrip(".7z")))
        NotFound=False
    else:
        if i=="Z" and NotFound:
            messagebox.showinfo("信息","没有发现合法启动盘，请重新创建")

