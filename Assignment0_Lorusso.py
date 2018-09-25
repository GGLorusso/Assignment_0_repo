# -*- coding: utf-8 -*-
#Assignment 0
#exemple B
wall_height= 0.8 #m
wall_wide= 1.5 #m
k_glass= 0.78 #W/(m*°C)

T_in= 20 #°C
T_out= -10 #°C
L= 0.008 #m
h_in= 10 #W/((m^2)*°C)
h_out= 40 #W/((m^2)*°C)

#Determine the steady rate of heat transfer throgh the glass
#Determine the temperature of its inner surface

R_in= 1/(h_in*wall_height*wall_wide)
R_glass= L/(k_glass*wall_height*wall_wide)
R_out= 1/(h_out*wall_height*wall_wide)
R_tot= R_in + R_glass + R_out
Q= (T_in - T_out)/R_tot

T1=T_in-Q*R_in
T2=T1-Q*R_glass

print"R_tot [°C/W] value: "+str (R_tot)
print"Q [W] value : "+str (Q)
print"T1 [°C] inner surface value: "+str (T1)
print"T2 [°C] outside surface value: "+str (T2)