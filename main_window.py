import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import pickle

class Win1:
    
    def __init__(self, master):
        self.master = master
        self.master.geometry("530x550")

        self.frame = tk.Frame(self.master)
        

        label = Label(master, text="Enter your Symptons", fg='blue', font=("Algerian", 30, "bold")).pack()
        
        label = tk.Label(master).pack()
        
        label = tk.Label(master, text="Enter Fever Value:", fg='#6200ee', font=("Arial", 16)).pack()
        fever=Entry(master, bd = 2)
        fever.pack()
        
        label = tk.Label(master).pack()
        
        label = tk.Label(master, text="Body Pain:", fg='#6200ee', font=("Arial", 16)).pack()
        bodyPain=("No Pain", "Severe Pain")
        cb_bp=Combobox(master, values=bodyPain)
        cb_bp.pack()
        
        label = tk.Label(master).pack()

        label = tk.Label(master, text="Enter Age Value:", fg='#6200ee', font=("Arial", 16)).pack()
        age=Entry(master, bd = 2)
        age.pack()
        label = tk.Label(master).pack()

        label = tk.Label(master, text="Cough:", fg='#6200ee', font=("Arial", 16)).pack()
        cough=("No Cough", "Dry Cough")
        cb_c=Combobox(master, values=cough)
        cb_c.pack()
        label = tk.Label(master).pack()
        
        label = tk.Label(master, text="Runny Nose:", fg='#6200ee', font=("Arial", 16)).pack()
        runnyNose=("No", "Yes")
        cb_rn=Combobox(master, values=runnyNose)
        cb_rn.pack()
        label = tk.Label(master).pack()
        
        label = tk.Label(master, text="Breathing Difficulty:", fg='#6200ee', font=("Arial", 16)).pack()
        diffBreadth=("No Difficulty", "Little Difficulty", "Severe Diffculty")
        cb_db=Combobox(master, values=diffBreadth)
        cb_db.pack()
        
        file = open('model.pkl','rb')
        clf = pickle.load(file)
        file.close()

        
        label = tk.Label(master).pack()

        tk.Button(self.frame, text = "Submit", command = lambda: self.new_window(clf, fever, cb_bp, age, cb_c, cb_rn, cb_db, Win2)).pack()
        

        self.frame.pack()

        


    def new_window(self, clf, fever, cb_bp, age, cb_c, cb_rn, cb_db, _class):

        #code for inference
        inputFeatures = [int(fever.get()), int(cb_bp.current()), int(age.get()), int(cb_c.current()), int(cb_rn.current()), int(cb_db.current() - 1)]
        
        infProb = clf.predict_proba([inputFeatures])[0][1]
        probability=str(infProb * 100)
    
        self.new = tk.Toplevel(self.master)
        _class(self.new, probability)
        

class Win2:
    def __init__(self, master, probability):
        self.master = master
        self.master.geometry("500x350+200+200")
        self.frame = tk.Frame(self.master)


        label = tk.Label(master, text="Thank you for taking this assessment.", wraplength = 450,fg='black', font=("Arial Black", 20, "bold")).pack()
        label = tk.Label(master).pack()

        if (int(float(probability)) > 60):
            assessment = "you are either unwell or at risk. We recommand that you should go for a Novel Coronavirus test."
        elif(int(float(probability)) > 40 & int(float(probability)) < 60):
            assessment = "your infection is low. We recommend that you stay at home to avoid any chance of exposure to Novel Coronavirus."
        else:
            assessment = "your are safe. We recommend that you stay at home to avoid any chance of exposure to Novel Coronavirus."
        
        label = tk.Label(master, text=f"If the information provided by you is accurate, it indicates that {assessment}", fg='black', wraplength=460, font=("Arial", 16)).pack()

        label = tk.Label(master).pack()

        self.quit = tk.Button(self.frame, text = "Quit", command = self.close_window)
        self.quit.pack()
        self.frame.pack()

    def close_window(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Win1(root)
    root.wm_title("CoVid-19 Probability Detector")
    root.mainloop()
