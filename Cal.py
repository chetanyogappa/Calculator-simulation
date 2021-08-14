# Calculator simulation
from tkinter import Tk , Label , Entry , Button , messagebox
import math
def   disp(x):  #  It  is  executed when  any  button  is  clicked  except  but[7]  and  x  is  0  to 6  depending  on  the  button
        try:
                a = eval(ent1 . get())  # values  of  ent1   and  ent2  are  copied  to  variables  a  and  b
                b = eval(ent2 . get())
                ent3 . delete(0 , 'end') #  deletes  value of ent3  before  displaying  the   new  result
                if  x == 0:  # display a + b in ent3  when but[0] is clicked
                        ent3 . insert(0 , a + b)
                elif  x == 1:  # display a - b in ent3  when but[1] is clicked
                        ent3 . insert(0 , a - b)
                elif  x == 2:  # display a * b in ent3  when but[2] is clicked
                        ent3 . insert(0 , a * b)
                elif  x == 3:  # display a / b in ent3  when but[3] is clicked
                        try:
                                ent3 . insert(0 , a / b)
                        except:
                                ent3 . insert(0 , 'Division  by 0 is not allowed')
                elif  x == 4:  # display sqrt(a)  in ent3  when but[4] is clicked
                        ent3 . insert(0 , math . sqrt(a))
                elif x == 5:  # display a ^ b in ent3  when but[5] is clicked
                        ent3 . insert(0 , a ** b)
                elif  x == 6:  # display largest  of  a  and  b   in ent3  when but[6] is clicked
                        ent3 . insert(0 , max(a , b))
        except:
                messagebox . showinfo('Hello  Srinivas' , 'Type inputs')

#end of the function

win = Tk()  #  Tk  window  object  is  created
win . geometry('400x500') # Dimensions of  the window are 400(width) and  500(Height)
win . title('CALCULATOR') # Title  of  the  window  is  modified (Default title  is  Tk)

lab1 = Label(text = 'Number 1' , fg = 'Red') # 3  labels  are  created  and labels  are  used  for  identification   of  the  objects
lab2 = Label(text = 'Number 2' , fg = 'Red')
lab3 = Label(text = 'Result' , fg = 'Red')

ent1 = Entry(fg = 'Green' , width = 25)  # 3  entry  boxes  are  created  with   width = 25
ent2 = Entry(fg = 'Green' , width = 25)
ent3 = Entry(fg = 'Green' , width = 25)

lab1 . grid(row = 0 , column = 0)   #  6  objects  are  displayed on the window
ent1 . grid(row = 0 , column = 1)
lab2 . grid(row = 1 , column = 0)
ent2 . grid(row = 1 , column = 1)
lab3 . grid(row = 2 , column = 0)
ent3 . grid(row = 2 , column = 1)

s = ['+' ,  '-' ,  '*'  ,  '/'  ,  'Sqrt'  ,  'Power'  ,  'Max'  ,  'Exit']  # list of strings
but = []  # Empty  list
for  i  in  range(8):  # Loop  is  executed  8  times  becoz  there  are  8  buttons
        button = Button(text = s[i] ,  fg = 'Blue' , height = 1 ,  width = 10 ,  command = lambda  x = i   : disp(x) ) #  Button  is  created
        but . append(button)  # Each button is  appended  to  the list  but
# End of  for  lopp
but[7] . configure(command = win . destroy)  #  window  is  closed  when  but[7] is  clicked  and  disp(7)  is  not  executed  becoz  it  is  configured

but[0] . grid(row = 3 , column = 0)  #  8  buttons  are  displayed  on the  window
but[1] . grid(row = 3 , column = 1)
but[2] . grid(row = 4 , column = 0)
but[3] . grid(row = 4 , column = 1)
but[4] . grid(row = 5 , column = 0)
but[5] . grid(row = 5 , column = 1)
but[6] . grid(row = 6 , column = 0)
but[7] . grid(row = 6 , column = 1)

ent1 . focus()  # cursor  moves  to  ent1
ent3 . bind('<Key>' ,  lambda a : 'break')  # ent3  can not  be  edited
win . mainloop()  # window  is  displayed





'''
1) disp(0) is executed when but[0] is clicked
    disp(1) is executed when but[1] is clicked
    disp(2) is executed when but[2] is clicked
     .  .  .  .
    disp(6) is executed when but[6] is clicked
    win . destroy is executed when but[7] is clicked becoz it is configured

2) config  or configure method is used to modify property of an  object like command property
    Eg: but[7] . config(command = win . destroy)  ----> command property of bu[7] is modified

3)  To  display  an object on window ,  There are 3 options
     a) obj . pack()  ----> obj is displayed at an arbitary location on the window
     b) obj . place(x = 10 , y = 20)   ----> obj is displayed at the specified co-ordinates
     c) obj . grid(row = 10 , column = 20)  ----> obj is displayed at 10th row and 20th column

'''