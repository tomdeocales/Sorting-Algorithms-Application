from tkinter import *
import tkinter as tk
import subprocess
Sorting = ["Insertion", "Selection","Radix","Quick", "Merge"]

def SORT():
    if x.get()==0:
        subprocess.Popen('C:\\Users\\deoca\\Desktop\\project\\sortingalgorithms\\Insertion.exe')
    elif x.get()==1: 
        subprocess.Popen('C:\\Users\\deoca\\Desktop\\project\\sortingalgorithms\\Selection.exe')
    elif x.get()==2:
        subprocess.Popen('C:\\Users\\deoca\\Desktop\\project\\sortingalgorithms\\Radix.exe')
    elif x.get()==3:
        subprocess.Popen('C:\\Users\\deoca\\Desktop\\project\\sortingalgorithms\\Quick.exe')
    else:
        subprocess.Popen('C:\\Users\\deoca\\Desktop\\project\\sortingalgorithms\\Merge.exe')
#Color1='#fdcddd'
window = Tk()
window.geometry("500x538")
window.title('Sort Types')
#window.configure(background=Color1) 

tk.Label(window, 
         text="""Choose your favourite 
Sorting Algorithm:""",
        #background='#fdcddd',
         justify = tk.CENTER,
         padx = 20).pack()

InsertionImage = PhotoImage(file='icons/Insertion.png')
SelectionImage = PhotoImage(file='icons/Selection.png')
RadixImage = PhotoImage(file='icons/Radix.png')
QuickImage = PhotoImage(file='icons/Quick.png')
MergeImage = PhotoImage(file='icons/Merge.png')
SortImages = [InsertionImage,SelectionImage,RadixImage,QuickImage,MergeImage]

x = IntVar()
myColor = '#d8c7db'
for index in range(len(Sorting)):#nagcreate kame ng for loop para maiterate o mabasa yung mga list at kapag nalagyan ng radiobutton ay magkakaroon ng limang button dahil 5 yung nasa list natin
    radiobutton = Radiobutton(window,
                              text=Sorting[index], #lalabas sa radiobutton yung string array na dineclare naten
                              variable=x, #groups radiobuttons together if they share the same variable
                              bg=myColor,
                              value=index, #assigns each radiobutton a different value
                              padx = 25, #adds padding on x-axis
                              font=("Impact",45),
                              image = SortImages[index], #image sa radiobutton
                              compound = 'left', #adds image sa text sa left
                              indicatoron=0, #mas malapad yung button
                              width = 1300, #width
                              command=SORT #define Sort para magfunction yung bawat pagclick ng button na nakabase don sa if else-if statement
                              )
    radiobutton.pack(anchor=W)
    
window.mainloop()