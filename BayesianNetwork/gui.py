# Varun Gupta
# 2016A7PS0087P

from tkinter import *
from network import *

bayesian_network = create_bayesian_network("input.txt")
root = Tk()
bg = root.cget("background")


def create_expression(query_vars, cond_vars):
    if len(query_vars) == 0:
        root.destroy()
        raise ValueError("There must be at least one query variable")

    if len(cond_vars) > 10:
        root.destroy()
        raise ValueError("Number of conditional variables is limited to 10")

    query_var_list = query_vars.split(',')
    if cond_vars == '':
        cond_var_list = []
    else:
        cond_var_list = cond_vars.split(',')

    for var in cond_var_list:
        if var[0] == '~':
            if var in query_var_list or var[1:] in query_var_list:
                root.destroy()
                raise ValueError("Same variables cannot appear in both query and conditions")
        else:
            if var in query_var_list or ('~' + var) in query_var_list:
                root.destroy()
                raise ValueError("Same variables cannot appear in both query and conditions")
    return query_var_list, cond_var_list


def find_value(event):
    query_vars = Query_variables_entry.get()
    cond_vars = Cond_variables_entry.get()
    print("Markov blanket of variable A is", compute_markov_blanket(bayesian_network, 'A'))
    query_vars, cond_vars = create_expression(query_vars[:-1], cond_vars[:-1])
    prob = compute_probability(query_vars, cond_vars, bayesian_network)
    Value_entry.delete(0, "end")
    Value_entry.insert(0, "{:.20f}".format(prob))


#####################################################################
def add_query_var_A(event): Query_variables_entry.insert(END, "A,")


def add_query_var_notA(event): Query_variables_entry.insert(END, "~A,")


def add_query_var_B(event): Query_variables_entry.insert(END, "B,")


def add_query_var_notB(event): Query_variables_entry.insert(END, "~B,")


def add_query_var_C(event): Query_variables_entry.insert(END, "C,")


def add_query_var_notC(event): Query_variables_entry.insert(END, "~C,")


def add_query_var_D(event): Query_variables_entry.insert(END, "D,")


def add_query_var_notD(event): Query_variables_entry.insert(END, "~D,")


def add_query_var_F(event): Query_variables_entry.insert(END, "F,")


def add_query_var_notF(event): Query_variables_entry.insert(END, "~F,")


def add_query_var_G(event): Query_variables_entry.insert(END, "G,")


def add_query_var_notG(event): Query_variables_entry.insert(END, "~G,")


def add_query_var_H(event): Query_variables_entry.insert(END, "H,")


def add_query_var_notH(event): Query_variables_entry.insert(END, "~H,")


def add_query_var_N(event): Query_variables_entry.insert(END, "N,")


def add_query_var_notN(event): Query_variables_entry.insert(END, "~N,")


def add_query_var_L(event): Query_variables_entry.insert(END, "L,")


def add_query_var_notL(event): Query_variables_entry.insert(END, "~L,")


def add_query_var_O(event): Query_variables_entry.insert(END, "O,")


def add_query_var_notO(event): Query_variables_entry.insert(END, "~O,")


def add_query_var_P(event): Query_variables_entry.insert(END, "P,")


def add_query_var_notP(event): Query_variables_entry.insert(END, "~P,")


def add_query_var_R(event): Query_variables_entry.insert(END, "R,")


def add_query_var_notR(event): Query_variables_entry.insert(END, "~R,")


def add_query_var_T(event): Query_variables_entry.insert(END, "T,")


def add_query_var_notT(event): Query_variables_entry.insert(END, "~T,")


def add_query_var_X(event): Query_variables_entry.insert(END, "X,")


def add_query_var_notX(event): Query_variables_entry.insert(END, "~X,")


def add_query_var_Y(event): Query_variables_entry.insert(END, "Y,")


def add_query_var_notY(event): Query_variables_entry.insert(END, "~Y,")


#####################################################################

#####################################################################
def add_cond_var_A(event): Cond_variables_entry.insert(END, "A,")


def add_cond_var_notA(event): Cond_variables_entry.insert(END, "~A,")


def add_cond_var_B(event): Cond_variables_entry.insert(END, "B,")


def add_cond_var_notB(event): Cond_variables_entry.insert(END, "~B,")


def add_cond_var_C(event): Cond_variables_entry.insert(END, "C,")


def add_cond_var_notC(event): Cond_variables_entry.insert(END, "~C,")


def add_cond_var_D(event): Cond_variables_entry.insert(END, "D,")


def add_cond_var_notD(event): Cond_variables_entry.insert(END, "~D,")


def add_cond_var_F(event): Cond_variables_entry.insert(END, "F,")


def add_cond_var_notF(event): Cond_variables_entry.insert(END, "~F,")


def add_cond_var_G(event): Cond_variables_entry.insert(END, "G,")


def add_cond_var_notG(event): Cond_variables_entry.insert(END, "~G,")


def add_cond_var_H(event): Cond_variables_entry.insert(END, "H,")


def add_cond_var_notH(event): Cond_variables_entry.insert(END, "~H,")


def add_cond_var_N(event): Cond_variables_entry.insert(END, "N,")


def add_cond_var_notN(event): Cond_variables_entry.insert(END, "~N,")


def add_cond_var_L(event): Cond_variables_entry.insert(END, "L,")


def add_cond_var_notL(event): Cond_variables_entry.insert(END, "~L,")


def add_cond_var_O(event): Cond_variables_entry.insert(END, "O,")


def add_cond_var_notO(event): Cond_variables_entry.insert(END, "~O,")


def add_cond_var_P(event): Cond_variables_entry.insert(END, "P,")


def add_cond_var_notP(event): Cond_variables_entry.insert(END, "~P,")


def add_cond_var_R(event): Cond_variables_entry.insert(END, "R,")


def add_cond_var_notR(event): Cond_variables_entry.insert(END, "~R,")


def add_cond_var_T(event): Cond_variables_entry.insert(END, "T,")


def add_cond_var_notT(event): Cond_variables_entry.insert(END, "~T,")


def add_cond_var_X(event): Cond_variables_entry.insert(END, "X,")


def add_cond_var_notX(event): Cond_variables_entry.insert(END, "~X,")


def add_cond_var_Y(event): Cond_variables_entry.insert(END, "Y,")


def add_cond_var_notY(event): Cond_variables_entry.insert(END, "~Y,")


#####################################################################


canvas_width = 600
canvas_height = 600

back_g = Canvas(root, width=canvas_width, height=canvas_height)
back_g.grid(row=0, rowspan=30, column=0, columnspan=8, sticky=(N, W, E, S))

Label(root, text="Query Variables", font=("Times", 10, "bold")).grid(row=0, column=0, columnspan=3, sticky=(E, W))

Label(root, text="Condition Variables", font=("Times", 10, "bold")).grid(row=0, column=5, columnspan=3, sticky=(E, W))

# A_button
A_Query_Button = Button(root, text="A", font=("Times", 10, "bold"), padx=40,
                        command=lambda: A_Query_Button.config(bg="green"))
A_Query_Button.grid(row=3, column=0, columnspan=1, rowspan=1, sticky=E)
A_Query_Button.bind("<Button-1>", add_query_var_A)

notA_Query_Button = Button(root, text="~A", font=("Times", 10, "bold"), padx=40,
                           command=lambda: notA_Query_Button.config(bg="green"))
notA_Query_Button.grid(row=3, column=1, columnspan=1, rowspan=1, sticky=E)
notA_Query_Button.bind("<Button-1>", add_query_var_notA)

# B_button
B_Query_Button = Button(root, text="B", font=("Times", 10, "bold"), padx=40,
                        command=lambda: B_Query_Button.config(bg="green"))
B_Query_Button.grid(row=4, column=0, columnspan=1, rowspan=1, sticky=E)
B_Query_Button.bind("<Button-1>", add_query_var_B)

notB_Query_Button = Button(root, text="~B", font=("Times", 10, "bold"), padx=40,
                           command=lambda: notB_Query_Button.config(bg="green"))
notB_Query_Button.grid(row=4, column=1, columnspan=1, rowspan=1, sticky=E)
notB_Query_Button.bind("<Button-1>", add_query_var_notB)

# C_button
C_Query_Button = Button(root, text="C", font=("Times", 10, "bold"), padx=40,
                        command=lambda: C_Query_Button.config(bg="green"))
C_Query_Button.grid(row=5, column=0, columnspan=1, rowspan=1, sticky=E)
C_Query_Button.bind("<Button-1>", add_query_var_C)

notC_Query_Button = Button(root, text="~C", font=("Times", 10, "bold"), padx=40,
                           command=lambda: notC_Query_Button.config(bg="green"))
notC_Query_Button.grid(row=5, column=1, columnspan=1, rowspan=1, sticky=E)
notC_Query_Button.bind("<Button-1>", add_query_var_notC)

# D_button
D_Query_Button = Button(root, text="D", font=("Times", 10, "bold"), padx=40,
                        command=lambda: D_Query_Button.config(bg="green"))
D_Query_Button.grid(row=6, column=0, columnspan=1, rowspan=1, sticky=E)
D_Query_Button.bind("<Button-1>", add_query_var_D)

notD_Query_Button = Button(root, text="~D", font=("Times", 10, "bold"), padx=40,
                           command=lambda: notD_Query_Button.config(bg="green"))
notD_Query_Button.grid(row=6, column=1, columnspan=1, rowspan=1, sticky=E)
notD_Query_Button.bind("<Button-1>", add_query_var_notD)

# F_button
F_Query_Button = Button(root, text="F", font=("Times", 10, "bold"), padx=40,
                        command=lambda: F_Query_Button.config(bg="green"))
F_Query_Button.grid(row=7, column=0, columnspan=1, rowspan=1, sticky=E)
F_Query_Button.bind("<Button-1>", add_query_var_F)

notF_Query_Button = Button(root, text="~F", font=("Times", 10, "bold"), padx=40,
                           command=lambda: notF_Query_Button.config(bg="green"))
notF_Query_Button.grid(row=7, column=1, columnspan=1, rowspan=1, sticky=E)
notF_Query_Button.bind("<Button-1>", add_query_var_notF)

# G_button
G_Query_Button = Button(root, text="G", font=("Times", 10, "bold"), padx=40,
                        command=lambda: G_Query_Button.config(bg="green"))
G_Query_Button.grid(row=8, column=0, columnspan=1, rowspan=1, sticky=E)
G_Query_Button.bind("<Button-1>", add_query_var_G)

notG_Query_Button = Button(root, text="~G", font=("Times", 10, "bold"), padx=40,
                           command=lambda: notG_Query_Button.config(bg="green"))
notG_Query_Button.grid(row=8, column=1, columnspan=1, rowspan=1, sticky=E)
notG_Query_Button.bind("<Button-1>", add_query_var_notG)

# H_button
H_Query_Button = Button(root, text="H", font=("Times", 10, "bold"), padx=40,
                        command=lambda: H_Query_Button.config(bg="green"))
H_Query_Button.grid(row=9, column=0, columnspan=1, rowspan=1, sticky=E)
H_Query_Button.bind("<Button-1>", add_query_var_H)

notH_Query_Button = Button(root, text="~H", font=("Times", 10, "bold"), padx=40,
                           command=lambda: notH_Query_Button.config(bg="green"))
notH_Query_Button.grid(row=9, column=1, columnspan=1, rowspan=1, sticky=E)
notH_Query_Button.bind("<Button-1>", add_query_var_notH)

# N_button
N_Query_Button = Button(root, text="N", font=("Times", 10, "bold"), padx=40,
                        command=lambda: N_Query_Button.config(bg="green"))
N_Query_Button.grid(row=11, column=0, columnspan=1, rowspan=1, sticky=E)
N_Query_Button.bind("<Button-1>", add_query_var_N)

notN_Query_Button = Button(root, text="~N", font=("Times", 10, "bold"), padx=40,
                           command=lambda: notN_Query_Button.config(bg="green"))
notN_Query_Button.grid(row=11, column=1, columnspan=1, rowspan=1, sticky=E)
notN_Query_Button.bind("<Button-1>", add_query_var_notN)

# L_button
L_Query_Button = Button(root, text="L", font=("Times", 10, "bold"), padx=40,
                        command=lambda: L_Query_Button.config(bg="green"))
L_Query_Button.grid(row=10, column=0, columnspan=1, rowspan=1, sticky=E)
L_Query_Button.bind("<Button-1>", add_query_var_L)

notL_Query_Button = Button(root, text="~L", font=("Times", 10, "bold"), padx=40,
                           command=lambda: notL_Query_Button.config(bg="green"))
notL_Query_Button.grid(row=10, column=1, columnspan=1, rowspan=1, sticky=E)
notL_Query_Button.bind("<Button-1>", add_query_var_notL)

# O_button
O_Query_Button = Button(root, text="O", font=("Times", 10, "bold"), padx=40,
                        command=lambda: O_Query_Button.config(bg="green"))
O_Query_Button.grid(row=12, column=0, columnspan=1, rowspan=1, sticky=E)
O_Query_Button.bind("<Button-1>", add_query_var_O)

notO_Query_Button = Button(root, text="~O", font=("Times", 10, "bold"), padx=40,
                           command=lambda: notO_Query_Button.config(bg="green"))
notO_Query_Button.grid(row=12, column=1, columnspan=1, rowspan=1, sticky=E)
notO_Query_Button.bind("<Button-1>", add_query_var_notO)

# P_button
P_Query_Button = Button(root, text="P", font=("Times", 10, "bold"), padx=40,
                        command=lambda: P_Query_Button.config(bg="green"))
P_Query_Button.grid(row=13, column=0, columnspan=1, rowspan=1, sticky=E)
P_Query_Button.bind("<Button-1>", add_query_var_P)

notP_Query_Button = Button(root, text="~P", font=("Times", 10, "bold"), padx=40,
                           command=lambda: notP_Query_Button.config(bg="green"))
notP_Query_Button.grid(row=13, column=1, columnspan=1, rowspan=1, sticky=E)
notP_Query_Button.bind("<Button-1>", add_query_var_notP)

# R_button
R_Query_Button = Button(root, text="R", font=("Times", 10, "bold"), padx=40,
                        command=lambda: R_Query_Button.config(bg="green"))
R_Query_Button.grid(row=14, column=0, columnspan=1, rowspan=1, sticky=E)
R_Query_Button.bind("<Button-1>", add_query_var_R)

notR_Query_Button = Button(root, text="~R", font=("Times", 10, "bold"), padx=40,
                           command=lambda: notR_Query_Button.config(bg="green"))
notR_Query_Button.grid(row=14, column=1, columnspan=1, rowspan=1, sticky=E)
notR_Query_Button.bind("<Button-1>", add_query_var_notR)

# T_button
T_Query_Button = Button(root, text="T", font=("Times", 10, "bold"), padx=40,
                        command=lambda: T_Query_Button.config(bg="green"))
T_Query_Button.grid(row=15, column=0, columnspan=1, rowspan=1, sticky=E)
T_Query_Button.bind("<Button-1>", add_query_var_T)

notT_Query_Button = Button(root, text="~T", font=("Times", 10, "bold"), padx=40,
                           command=lambda: notT_Query_Button.config(bg="green"))
notT_Query_Button.grid(row=15, column=1, columnspan=1, rowspan=1, sticky=E)
notT_Query_Button.bind("<Button-1>", add_query_var_notT)

# X_button
X_Query_Button = Button(root, text="X", font=("Times", 10, "bold"), padx=40,
                        command=lambda: X_Query_Button.config(bg="green"))
X_Query_Button.grid(row=16, column=0, columnspan=1, rowspan=1, sticky=E)
X_Query_Button.bind("<Button-1>", add_query_var_X)

notX_Query_Button = Button(root, text="~X", font=("Times", 10, "bold"), padx=40,
                           command=lambda: notX_Query_Button.config(bg="green"))
notX_Query_Button.grid(row=16, column=1, columnspan=1, rowspan=1, sticky=E)
notX_Query_Button.bind("<Button-1>", add_query_var_notX)

# Y_button
Y_Query_Button = Button(root, text="Y", font=("Times", 10, "bold"), padx=40,
                        command=lambda: Y_Query_Button.config(bg="green"))
Y_Query_Button.grid(row=17, column=0, columnspan=1, rowspan=1, sticky=E)
Y_Query_Button.bind("<Button-1>", add_query_var_Y)

notY_Query_Button = Button(root, text="~Y", font=("Times", 10, "bold"), padx=40,
                           command=lambda: notY_Query_Button.config(bg="green"))
notY_Query_Button.grid(row=17, column=1, columnspan=1, rowspan=1, sticky=E)
notY_Query_Button.bind("<Button-1>", add_query_var_notY)

Label(root, text="Query Expression : ", font=("Times", 10, "bold")).grid(row=20, column=0, columnspan=1, sticky=(E, W))

Query_variables_entry = Entry(root)
Query_variables_entry.grid(row=20, column=1, columnspan=3, sticky=(E, W))

###################################################################################

# A_button
A_Cond_Button = Button(root, text="A", font=("Times", 10, "bold"), padx=40,
                       command=lambda: A_Cond_Button.config(bg="yellow"))
A_Cond_Button.grid(row=3, column=5, columnspan=1, rowspan=1, sticky=E)
A_Cond_Button.bind("<Button-1>", add_cond_var_A)

notA_Cond_Button = Button(root, text="~A", font=("Times", 10, "bold"), padx=40,
                          command=lambda: notA_Cond_Button.config(bg="yellow"))
notA_Cond_Button.grid(row=3, column=6, columnspan=1, rowspan=1, sticky=E)
notA_Cond_Button.bind("<Button-1>", add_cond_var_notA)

# B_button
B_Cond_Button = Button(root, text="B", font=("Times", 10, "bold"), padx=40,
                       command=lambda: B_Cond_Button.config(bg="yellow"))
B_Cond_Button.grid(row=4, column=5, columnspan=1, rowspan=1, sticky=E)
B_Cond_Button.bind("<Button-1>", add_cond_var_B)

notB_Cond_Button = Button(root, text="~B", font=("Times", 10, "bold"), padx=40,
                          command=lambda: notB_Cond_Button.config(bg="yellow"))
notB_Cond_Button.grid(row=4, column=6, columnspan=1, rowspan=1, sticky=E)
notB_Cond_Button.bind("<Button-1>", add_cond_var_notB)

# C_button
C_Cond_Button = Button(root, text="C", font=("Times", 10, "bold"), padx=40,
                       command=lambda: C_Cond_Button.config(bg="yellow"))
C_Cond_Button.grid(row=5, column=5, columnspan=1, rowspan=1, sticky=E)
C_Cond_Button.bind("<Button-1>", add_cond_var_C)

notC_Cond_Button = Button(root, text="~C", font=("Times", 10, "bold"), padx=40,
                          command=lambda: notC_Cond_Button.config(bg="yellow"))
notC_Cond_Button.grid(row=5, column=6, columnspan=1, rowspan=1, sticky=E)
notC_Cond_Button.bind("<Button-1>", add_cond_var_notC)

# D_button
D_Cond_Button = Button(root, text="D", font=("Times", 10, "bold"), padx=40,
                       command=lambda: D_Cond_Button.config(bg="yellow"))
D_Cond_Button.grid(row=6, column=5, columnspan=1, rowspan=1, sticky=E)
D_Cond_Button.bind("<Button-1>", add_cond_var_D)

notD_Cond_Button = Button(root, text="~D", font=("Times", 10, "bold"), padx=40,
                          command=lambda: notD_Cond_Button.config(bg="yellow"))
notD_Cond_Button.grid(row=6, column=6, columnspan=1, rowspan=1, sticky=E)
notD_Cond_Button.bind("<Button-1>", add_cond_var_notD)

# F_button
F_Cond_Button = Button(root, text="F", font=("Times", 10, "bold"), padx=40,
                       command=lambda: F_Cond_Button.config(bg="yellow"))
F_Cond_Button.grid(row=7, column=5, columnspan=1, rowspan=1, sticky=E)
F_Cond_Button.bind("<Button-1>", add_cond_var_F)

notF_Cond_Button = Button(root, text="~F", font=("Times", 10, "bold"), padx=40,
                          command=lambda: notF_Cond_Button.config(bg="yellow"))
notF_Cond_Button.grid(row=7, column=6, columnspan=1, rowspan=1, sticky=E)
notF_Cond_Button.bind("<Button-1>", add_cond_var_notF)

# G_button
G_Cond_Button = Button(root, text="G", font=("Times", 10, "bold"), padx=40,
                       command=lambda: G_Cond_Button.config(bg="yellow"))
G_Cond_Button.grid(row=8, column=5, columnspan=1, rowspan=1, sticky=E)
G_Cond_Button.bind("<Button-1>", add_cond_var_G)

notG_Cond_Button = Button(root, text="~G", font=("Times", 10, "bold"), padx=40,
                          command=lambda: notG_Cond_Button.config(bg="yellow"))
notG_Cond_Button.grid(row=8, column=6, columnspan=1, rowspan=1, sticky=E)
notG_Cond_Button.bind("<Button-1>", add_cond_var_notG)

# H_button
H_Cond_Button = Button(root, text="H", font=("Times", 10, "bold"), padx=40,
                       command=lambda: H_Cond_Button.config(bg="yellow"))
H_Cond_Button.grid(row=9, column=5, columnspan=1, rowspan=1, sticky=E)
H_Cond_Button.bind("<Button-1>", add_cond_var_H)

notH_Cond_Button = Button(root, text="~H", font=("Times", 10, "bold"), padx=40,
                          command=lambda: notH_Cond_Button.config(bg="yellow"))
notH_Cond_Button.grid(row=9, column=6, columnspan=1, rowspan=1, sticky=E)
notH_Cond_Button.bind("<Button-1>", add_cond_var_notH)

# N_button
N_Cond_Button = Button(root, text="N", font=("Times", 10, "bold"), padx=40,
                       command=lambda: N_Cond_Button.config(bg="yellow"))
N_Cond_Button.grid(row=11, column=5, columnspan=1, rowspan=1, sticky=E)
N_Cond_Button.bind("<Button-1>", add_cond_var_N)

notN_Cond_Button = Button(root, text="~N", font=("Times", 10, "bold"), padx=40,
                          command=lambda: notN_Cond_Button.config(bg="yellow"))
notN_Cond_Button.grid(row=11, column=6, columnspan=1, rowspan=1, sticky=E)
notN_Cond_Button.bind("<Button-1>", add_cond_var_notN)

# L_button
L_Cond_Button = Button(root, text="L", font=("Times", 10, "bold"), padx=40,
                       command=lambda: L_Cond_Button.config(bg="yellow"))
L_Cond_Button.grid(row=10, column=5, columnspan=1, rowspan=1, sticky=E)
L_Cond_Button.bind("<Button-1>", add_cond_var_L)

notL_Cond_Button = Button(root, text="~L", font=("Times", 10, "bold"), padx=40,
                          command=lambda: notL_Cond_Button.config(bg="yellow"))
notL_Cond_Button.grid(row=10, column=6, columnspan=1, rowspan=1, sticky=E)
notL_Cond_Button.bind("<Button-1>", add_cond_var_notL)

# O_button
O_Cond_Button = Button(root, text="O", font=("Times", 10, "bold"), padx=40,
                       command=lambda: O_Cond_Button.config(bg="yellow"))
O_Cond_Button.grid(row=12, column=5, columnspan=1, rowspan=1, sticky=E)
O_Cond_Button.bind("<Button-1>", add_cond_var_O)

notO_Cond_Button = Button(root, text="~O", font=("Times", 10, "bold"), padx=40,
                          command=lambda: notO_Cond_Button.config(bg="yellow"))
notO_Cond_Button.grid(row=12, column=6, columnspan=1, rowspan=1, sticky=E)
notO_Cond_Button.bind("<Button-1>", add_cond_var_notO)

# P_button
P_Cond_Button = Button(root, text="P", font=("Times", 10, "bold"), padx=40,
                       command=lambda: P_Cond_Button.config(bg="yellow"))
P_Cond_Button.grid(row=13, column=5, columnspan=1, rowspan=1, sticky=E)
P_Cond_Button.bind("<Button-1>", add_cond_var_P)

notP_Cond_Button = Button(root, text="~P", font=("Times", 10, "bold"), padx=40,
                          command=lambda: notP_Cond_Button.config(bg="yellow"))
notP_Cond_Button.grid(row=13, column=6, columnspan=1, rowspan=1, sticky=E)
notP_Cond_Button.bind("<Button-1>", add_cond_var_notP)

# R_button
R_Cond_Button = Button(root, text="R", font=("Times", 10, "bold"), padx=40,
                       command=lambda: R_Cond_Button.config(bg="yellow"))
R_Cond_Button.grid(row=14, column=5, columnspan=1, rowspan=1, sticky=E)
R_Cond_Button.bind("<Button-1>", add_cond_var_R)

notR_Cond_Button = Button(root, text="~R", font=("Times", 10, "bold"), padx=40,
                          command=lambda: notR_Cond_Button.config(bg="yellow"))
notR_Cond_Button.grid(row=14, column=6, columnspan=1, rowspan=1, sticky=E)
notR_Cond_Button.bind("<Button-1>", add_cond_var_notR)

# T_button
T_Cond_Button = Button(root, text="T", font=("Times", 10, "bold"), padx=40,
                       command=lambda: T_Cond_Button.config(bg="yellow"))
T_Cond_Button.grid(row=15, column=5, columnspan=1, rowspan=1, sticky=E)
T_Cond_Button.bind("<Button-1>", add_cond_var_T)

notT_Cond_Button = Button(root, text="~T", font=("Times", 10, "bold"), padx=40,
                          command=lambda: notT_Cond_Button.config(bg="yellow"))
notT_Cond_Button.grid(row=15, column=6, columnspan=1, rowspan=1, sticky=E)
notT_Cond_Button.bind("<Button-1>", add_cond_var_notT)

# X_button
X_Cond_Button = Button(root, text="X", font=("Times", 10, "bold"), padx=40,
                       command=lambda: X_Cond_Button.config(bg="yellow"))
X_Cond_Button.grid(row=16, column=5, columnspan=1, rowspan=1, sticky=E)
X_Cond_Button.bind("<Button-1>", add_cond_var_X)

notX_Cond_Button = Button(root, text="~X", font=("Times", 10, "bold"), padx=40,
                          command=lambda: notX_Cond_Button.config(bg="yellow"))
notX_Cond_Button.grid(row=16, column=6, columnspan=1, rowspan=1, sticky=E)
notX_Cond_Button.bind("<Button-1>", add_cond_var_notX)

# Y_button
Y_Cond_Button = Button(root, text="Y", font=("Times", 10, "bold"), padx=40,
                       command=lambda: Y_Cond_Button.config(bg="yellow"))
Y_Cond_Button.grid(row=17, column=5, columnspan=1, rowspan=1, sticky=E)
Y_Cond_Button.bind("<Button-1>", add_cond_var_Y)

notY_Cond_Button = Button(root, text="~Y", font=("Times", 10, "bold"), padx=40,
                          command=lambda: notY_Cond_Button.config(bg="yellow"))
notY_Cond_Button.grid(row=17, column=6, columnspan=1, rowspan=1, sticky=E)
notY_Cond_Button.bind("<Button-1>", add_cond_var_notY)

Label(root, text="Cond Expression : ", font=("Times", 10, "bold")).grid(row=20, column=4, columnspan=1, sticky=(E, W))
Cond_variables_entry = Entry(root)
Cond_variables_entry.grid(row=20, column=5, columnspan=2, sticky=(E, W))

Find_Value_Button = Button(root, text="Find Value", font=("Times", 10, "bold"), padx=40)
Find_Value_Button.grid(row=25, column=1, columnspan=4, sticky=(E, W))
Find_Value_Button.bind("<Button-1>", find_value)

Value_entry = Entry(root)
Value_entry.grid(row=25, column=5, columnspan=2, sticky=(E, W))


def clear_entry(event):
    Query_variables_entry.delete(0, "end")
    Cond_variables_entry.delete(0, "end")
    Value_entry.delete(0, "end")
    A_Cond_Button.config(bg=bg)
    notA_Cond_Button.config(bg=bg)
    B_Cond_Button.config(bg=bg)
    notB_Cond_Button.config(bg=bg)
    C_Cond_Button.config(bg=bg)
    notC_Cond_Button.config(bg=bg)
    D_Cond_Button.config(bg=bg)
    notD_Cond_Button.config(bg=bg)
    F_Cond_Button.config(bg=bg)
    notF_Cond_Button.config(bg=bg)
    G_Cond_Button.config(bg=bg)
    notG_Cond_Button.config(bg=bg)
    H_Cond_Button.config(bg=bg)
    notH_Cond_Button.config(bg=bg)
    N_Cond_Button.config(bg=bg)
    notN_Cond_Button.config(bg=bg)
    L_Cond_Button.config(bg=bg)
    notL_Cond_Button.config(bg=bg)
    O_Cond_Button.config(bg=bg)
    notO_Cond_Button.config(bg=bg)
    P_Cond_Button.config(bg=bg)
    notP_Cond_Button.config(bg=bg)
    R_Cond_Button.config(bg=bg)
    notR_Cond_Button.config(bg=bg)
    T_Cond_Button.config(bg=bg)
    notT_Cond_Button.config(bg=bg)
    X_Cond_Button.config(bg=bg)
    notX_Cond_Button.config(bg=bg)
    Y_Cond_Button.config(bg=bg)
    notY_Cond_Button.config(bg=bg)

    A_Query_Button.config(bg=bg)
    notA_Query_Button.config(bg=bg)
    B_Query_Button.config(bg=bg)
    notB_Query_Button.config(bg=bg)
    C_Query_Button.config(bg=bg)
    notC_Query_Button.config(bg=bg)
    D_Query_Button.config(bg=bg)
    notD_Query_Button.config(bg=bg)
    F_Query_Button.config(bg=bg)
    notF_Query_Button.config(bg=bg)
    G_Query_Button.config(bg=bg)
    notG_Query_Button.config(bg=bg)
    H_Query_Button.config(bg=bg)
    notH_Query_Button.config(bg=bg)
    N_Query_Button.config(bg=bg)
    notN_Query_Button.config(bg=bg)
    L_Query_Button.config(bg=bg)
    notL_Query_Button.config(bg=bg)
    O_Query_Button.config(bg=bg)
    notO_Query_Button.config(bg=bg)
    P_Query_Button.config(bg=bg)
    notP_Query_Button.config(bg=bg)
    R_Query_Button.config(bg=bg)
    notR_Query_Button.config(bg=bg)
    T_Query_Button.config(bg=bg)
    notT_Query_Button.config(bg=bg)
    X_Query_Button.config(bg=bg)
    notX_Query_Button.config(bg=bg)
    Y_Query_Button.config(bg=bg)
    notY_Query_Button.config(bg=bg)


New_Query_Button = Button(root, text="New Query", font=("Times", 10, "bold"), padx=40)
New_Query_Button.grid(row=27, column=1, columnspan=4, sticky=(E, W))
New_Query_Button.bind("<Button-1>", clear_entry)

root.mainloop()
