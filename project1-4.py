# Making the results using h (timestep) of .01 instead of 1:
import xarray as xr
import numpy as np
import sys
import seaborn as sns
import matplotlib.pyplot as plt


ds = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210101.nc')
ds1 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210102.nc')
ds2 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210103.nc')
ds3 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210104.nc')
ds4 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210105.nc')
ds5 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210106.nc')
ds6 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210107.nc')
ds7 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210108.nc')
ds8 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210109.nc')
ds9 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210110.nc')
ds10 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210111.nc')
ds11 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210112.nc')
ds12 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210113.nc')
ds13 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210114.nc')
ds14 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210115.nc')
ds15 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210116.nc')
ds16 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210117.nc')
ds17 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210118.nc')
ds18 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210119.nc')
ds19 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210120.nc')
ds20 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210121.nc')
ds21 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210122.nc')
ds22 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210123.nc')
ds23 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210124.nc')
ds24 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210125.nc')
ds25 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210126.nc')
ds26 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210127.nc')
ds27 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210128.nc')
ds28 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210129.nc')
ds29 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210130.nc')
ds30 = xr.open_dataset('/workspaces/179963577/MATH 460/oscar_currents_nrt_20210131.nc')

#Initialize matrices containing the entire sets of U and V values from dataset
UOGmatrix = ds['u'].values
VOGmatrix = ds['v'].values

UOG1matrix = ds1['u'].values
VOG1matrix = ds1['v'].values

UOG2matrix = ds2['u'].values
VOG2matrix = ds2['v'].values

UOG3matrix = ds3['u'].values
VOG3matrix = ds3['v'].values

UOG4matrix = ds4['u'].values
VOG4matrix = ds4['v'].values

UOG5matrix = ds5['u'].values
VOG5matrix = ds5['v'].values

UOG6matrix = ds6['u'].values
VOG6matrix = ds6['v'].values

UOG7matrix = ds7['u'].values
VOG7matrix = ds7['v'].values

UOG8matrix = ds8['u'].values
VOG8matrix = ds8['v'].values

UOG9matrix = ds9['u'].values
VOG9matrix = ds9['v'].values

UOG10matrix = ds10['u'].values
VOG10matrix = ds10['v'].values

UOG11matrix = ds11['u'].values
VOG11matrix = ds11['v'].values

UOG12matrix = ds12['u'].values
VOG12matrix = ds12['v'].values

UOG13matrix = ds13['u'].values
VOG13matrix = ds13['v'].values

UOG14matrix = ds14['u'].values
VOG14matrix = ds14['v'].values

UOG15matrix = ds15['u'].values
VOG15matrix = ds15['v'].values

UOG16matrix = ds16['u'].values
VOG16matrix = ds16['v'].values

UOG17matrix = ds17['u'].values
VOG17matrix = ds17['v'].values

UOG18matrix = ds18['u'].values
VOG18matrix = ds18['v'].values

UOG19matrix = ds19['u'].values
VOG19matrix = ds19['v'].values

UOG20matrix = ds20['u'].values
VOG20matrix = ds20['v'].values

UOG21matrix = ds21['u'].values
VOG21matrix = ds21['v'].values

UOG22matrix = ds22['u'].values
VOG22matrix = ds22['v'].values

UOG23matrix = ds23['u'].values
VOG23matrix = ds23['v'].values

UOG24matrix = ds24['u'].values
VOG24matrix = ds24['v'].values

UOG25matrix = ds25['u'].values
VOG25matrix = ds25['v'].values

UOG26matrix = ds26['u'].values
VOG26matrix = ds26['v'].values

UOG27matrix = ds27['u'].values
VOG27matrix = ds27['v'].values

UOG28matrix = ds28['u'].values
VOG28matrix = ds28['v'].values

UOG29matrix = ds29['u'].values
VOG29matrix = ds29['v'].values

UOG30matrix = ds30['u'].values
VOG30matrix = ds30['v'].values


print(UOGmatrix[0, 1360, 359])
print(VOGmatrix[0, 1360, 359])

#Putting them into same sized matrices corresponding to the desired area


#INITIAL MATRIX
Umatrix0 = np.zeros((41,41))
Vmatrix0 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix0[40-row,column] = UOGmatrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix0[40-row,column] = VOGmatrix[0, column+1360, row+319]

print(Umatrix0)
print(Vmatrix0)
Umatrix1 = np.zeros((41,41))
Vmatrix1 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix1[40-row,column] = UOG1matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix1[40-row,column] = VOG1matrix[0, column+1360, row+319]

print(Umatrix1)
print(Vmatrix1)

#two timesteps
Umatrix2 = np.zeros((41,41))
Vmatrix2 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix2[40-row,column] = UOG2matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix2[40-row,column] = VOG2matrix[0, column+1360, row+319]

#three timesteps
Umatrix3 = np.zeros((41,41))
Vmatrix3 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix3[40-row,column] = UOG3matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix3[40-row,column] = VOG3matrix[0, column+1360, row+319]

#4 timesteps
Umatrix4 = np.zeros((41,41))
Vmatrix4 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix4[40-row,column] = UOG4matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix4[40-row,column] = VOG4matrix[0, column+1360, row+319]


#Five Timesteps
Umatrix5 = np.zeros((41,41))
Vmatrix5 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix5[40-row,column] = UOG5matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix5[40-row,column] = VOG5matrix[0, column+1360, row+319]

#Six Timesteps

Umatrix6 = np.zeros((41,41))
Vmatrix6 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix6[40-row,column] = UOG6matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix6[40-row,column] = VOG6matrix[0, column+1360, row+319]

#Seven Timesteps
Umatrix7 = np.zeros((41,41))
Vmatrix7 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix7[40-row,column] = UOG7matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix7[40-row,column] = VOG7matrix[0, column+1360, row+319]

#Eight Timesteps
Umatrix8 = np.zeros((41,41))
Vmatrix8 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix8[40-row,column] = UOG8matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix8[40-row,column] = VOG8matrix[0, column+1360, row+319]
#Nine Timesteps
Umatrix9 = np.zeros((41,41))
Vmatrix9 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix9[40-row,column] = UOG9matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix9[40-row,column] = VOG9matrix[0, column+1360, row+319]

#Ten Timesteps
Umatrix10 = np.zeros((41,41))
Vmatrix10 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix10[40-row,column] = UOG10matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix10[40-row,column] = VOG10matrix[0, column+1360, row+319]
#Eleven Timesteps
Umatrix11 = np.zeros((41,41))
Vmatrix11 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix11[40-row,column] = UOG11matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix11[40-row,column] = VOG11matrix[0, column+1360, row+319]

#Twelve Timesteps
Umatrix12 = np.zeros((41,41))
Vmatrix12 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix12[40-row,column] = UOG12matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix12[40-row,column] = VOG12matrix[0, column+1360, row+319]

#Thirteen Timesteps
Umatrix13 = np.zeros((41,41))
Vmatrix13 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix13[40-row,column] = UOG13matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix13[40-row,column] = VOG13matrix[0, column+1360, row+319]

#Fourteen Timesteps
Umatrix14 = np.zeros((41,41))
Vmatrix14 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix14[40-row,column] = UOG14matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix14[40-row,column] = VOG14matrix[0, column+1360, row+319]

#Fifteen Timesteps
Umatrix15 = np.zeros((41,41))
Vmatrix15 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix15[40-row,column] = UOG15matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix15[40-row,column] = VOG15matrix[0, column+1360, row+319]
#Sixteen Timesteps
Umatrix16 = np.zeros((41,41))
Vmatrix16 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix16[40-row,column] = UOG16matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix16[40-row,column] = VOG16matrix[0, column+1360, row+319]

#Seventeen Timesteps
Umatrix17 = np.zeros((41,41))
Vmatrix17 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix17[40-row,column] = UOG17matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix17[40-row,column] = VOG17matrix[0, column+1360, row+319]
#Eighteen Timesteps
Umatrix18 = np.zeros((41,41))
Vmatrix18 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix18[40-row,column] = UOG18matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix18[40-row,column] = VOG18matrix[0, column+1360, row+319]

#Nineteen Timesteps
Umatrix19 = np.zeros((41,41))
Vmatrix19 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix19[40-row,column] = UOG19matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix19[40-row,column] = VOG19matrix[0, column+1360, row+319]
#Twenty Timesteps
Umatrix20 = np.zeros((41,41))
Vmatrix20 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix20[40-row,column] = UOG20matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix20[40-row,column] = VOG20matrix[0, column+1360, row+319]

#Twenty-One Timesteps
Umatrix21 = np.zeros((41,41))
Vmatrix21 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix21[40-row,column] = UOG21matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix21[40-row,column] = VOG21matrix[0, column+1360, row+319]

#Twenty Two Timesteps
Umatrix22 = np.zeros((41,41))
Vmatrix22 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix22[40-row,column] = UOG22matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix22[40-row,column] = VOG22matrix[0, column+1360, row+319]

#23 Timesteps
Umatrix23 = np.zeros((41,41))
Vmatrix23 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix23[40-row,column] = UOG23matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix23[40-row,column] = VOG23matrix[0, column+1360, row+319]
#24 Timesteps
Umatrix24 = np.zeros((41,41))
Vmatrix24 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix24[40-row,column] = UOG24matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix24[40-row,column] = VOG24matrix[0, column+1360, row+319]

#25 Timesteps
Umatrix25 = np.zeros((41,41))
Vmatrix25 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix25[40-row,column] = UOG25matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix25[40-row,column] = VOG25matrix[0, column+1360, row+319]

#26 Timesteps
Umatrix26 = np.zeros((41,41))
Vmatrix26 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix26[40-row,column] = UOG26matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix26[40-row,column] = VOG26matrix[0, column+1360, row+319]
#27 Timesteps
Umatrix27 = np.zeros((41,41))
Vmatrix27 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix27[40-row,column] = UOG27matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix27[40-row,column] = VOG27matrix[0, column+1360, row+319]

#28 Timesteps
Umatrix28 = np.zeros((41,41))
Vmatrix28 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix28[40-row,column] = UOG28matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix28[40-row,column] = VOG28matrix[0, column+1360, row+319]

#29 Timesteps
Umatrix29 = np.zeros((41,41))
Vmatrix29 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix29[40-row,column] = UOG29matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix29[40-row,column] = VOG29matrix[0, column+1360, row+319]

#30 Timesteps
Umatrix30 = np.zeros((41,41))
Vmatrix30 = np.zeros((41,41))

for row in range(0, 41):
    for column in range(0, 41):
        Umatrix30[40-row,column] = UOG30matrix[0, column+1360, row+319]

for row in range(0, 41):
    for column in range(0, 41):
        Vmatrix30[40-row,column] = VOG30matrix[0, column+1360, row+319]


#Diffusion constant
d = 1.0001

#Timestep
h = .01;

#Spatial Step
k = 7;


#MODEL IMPLEMENTATION
#initial zero state
concentrationM0 = np.zeros((41,41))
concentrationM0[20, 20] = .2;
concentrationM0[19, 20] = .2;
concentrationM0[21, 20] = .2;
concentrationM0[20, 19] = .2;
concentrationM0[20, 21] = .2;

concentrationM1 = np.zeros((41,41))

concentrationM2 = np.zeros((41,41))

concentrationM3 = np.zeros((41,41))

concentrationM4 = np.zeros((41,41))

concentrationM5 = np.zeros((41,41))

concentrationM6 = np.zeros((41,41))

concentrationM7 = np.zeros((41,41))

concentrationM8 = np.zeros((41,41))

concentrationM9 = np.zeros((41,41))

concentrationM10 = np.zeros((41,41))

concentrationM11 = np.zeros((41,41))

concentrationM12 = np.zeros((41,41))

concentrationM13 = np.zeros((41,41))

concentrationM14 = np.zeros((41,41))

concentrationM15 = np.zeros((41,41))

concentrationM16 = np.zeros((41,41))

concentrationM17 = np.zeros((41,41))

concentrationM18 = np.zeros((41,41))

concentrationM19 = np.zeros((41,41))

concentrationM20 = np.zeros((41,41))

concentrationM21 = np.zeros((41,41))

concentrationM22 = np.zeros((41,41))

concentrationM23 = np.zeros((41,41))

concentrationM24 = np.zeros((41,41))

concentrationM25 = np.zeros((41,41))

concentrationM26 = np.zeros((41,41))

concentrationM27 = np.zeros((41,41))

concentrationM28 = np.zeros((41,41))

concentrationM29 = np.zeros((41,41))

concentrationM30 = np.zeros((41,41))





for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM0[row-1, column]
            concXPlus1 = concentrationM0[row+1, column]

            concXY = concentrationM0[row, column]

            concYMinus1 = concentrationM0[row, column-1]
            concYPlus1 = concentrationM0[row, column+1]

            Uvelocity1 = -1*(Umatrix0[row, column])
            Vvelocity1 = -1*(Vmatrix0[row, column])

            concentrationM1[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM1[row-1, column]
            concXPlus1 = concentrationM1[row+1, column]

            concXY = concentrationM1[row, column]

            concYMinus1 = concentrationM1[row, column-1]
            concYPlus1 = concentrationM1[row, column+1]

            Uvelocity1 = -1*(Umatrix0[row, column])
            Vvelocity1 = -1*(Vmatrix0[row, column])

            concentrationM1[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY
#Concentration 2
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM1[row-1, column]
            concXPlus1 = concentrationM1[row+1, column]

            concXY = concentrationM1[row, column]

            concYMinus1 = concentrationM1[row, column-1]
            concYPlus1 = concentrationM1[row, column+1]

            Uvelocity1 = -1*(Umatrix1[row, column])
            Vvelocity1 = -1*(Vmatrix1[row, column])

            concentrationM2[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM2[row-1, column]
            concXPlus1 = concentrationM2[row+1, column]

            concXY = concentrationM2[row, column]

            concYMinus1 = concentrationM2[row, column-1]
            concYPlus1 = concentrationM2[row, column+1]

            Uvelocity1 = -1*(Umatrix1[row, column])
            Vvelocity1 = -1*(Vmatrix1[row, column])

            concentrationM2[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY



#concentration 3
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM2[row-1, column]
            concXPlus1 = concentrationM2[row+1, column]

            concXY = concentrationM2[row, column]

            concYMinus1 = concentrationM2[row, column-1]
            concYPlus1 = concentrationM2[row, column+1]

            Uvelocity1 = -1*(Umatrix2[row, column])
            Vvelocity1 = -1*(Vmatrix2[row, column])

            concentrationM3[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM3[row-1, column]
            concXPlus1 = concentrationM3[row+1, column]

            concXY = concentrationM3[row, column]

            concYMinus1 = concentrationM3[row, column-1]
            concYPlus1 = concentrationM3[row, column+1]

            Uvelocity1 = -1*(Umatrix2[row, column])
            Vvelocity1 = -1*(Vmatrix2[row, column])

            concentrationM3[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY



#concentration 4

for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM3[row-1, column]
            concXPlus1 = concentrationM3[row+1, column]

            concXY = concentrationM3[row, column]

            concYMinus1 = concentrationM3[row, column-1]
            concYPlus1 = concentrationM3[row, column+1]

            Uvelocity1 = -1*(Umatrix3[row, column])
            Vvelocity1 = -1*(Vmatrix3[row, column])

            concentrationM4[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM4[row-1, column]
            concXPlus1 = concentrationM4[row+1, column]

            concXY = concentrationM4[row, column]

            concYMinus1 = concentrationM4[row, column-1]
            concYPlus1 = concentrationM4[row, column+1]

            Uvelocity1 = -1*(Umatrix3[row, column])
            Vvelocity1 = -1*(Vmatrix3[row, column])

            concentrationM4[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY


#Concentration 5
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM4[row-1, column]
            concXPlus1 = concentrationM4[row+1, column]

            concXY = concentrationM4[row, column]

            concYMinus1 = concentrationM4[row, column-1]
            concYPlus1 = concentrationM4[row, column+1]

            Uvelocity1 = -1*(Umatrix4[row, column])
            Vvelocity1 = -1*(Vmatrix4[row, column])

            concentrationM5[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM5[row-1, column]
            concXPlus1 = concentrationM5[row+1, column]

            concXY = concentrationM5[row, column]

            concYMinus1 = concentrationM5[row, column-1]
            concYPlus1 = concentrationM5[row, column+1]

            Uvelocity1 = -1*(Umatrix4[row, column])
            Vvelocity1 = -1*(Vmatrix4[row, column])

            concentrationM5[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY



#concentration 6
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM5[row-1, column]
            concXPlus1 = concentrationM5[row+1, column]

            concXY = concentrationM5[row, column]

            concYMinus1 = concentrationM5[row, column-1]
            concYPlus1 = concentrationM5[row, column+1]

            Uvelocity1 = -1*(Umatrix5[row, column])
            Vvelocity1 = -1*(Vmatrix5[row, column])

            concentrationM6[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM6[row-1, column]
            concXPlus1 = concentrationM6[row+1, column]

            concXY = concentrationM6[row, column]

            concYMinus1 = concentrationM6[row, column-1]
            concYPlus1 = concentrationM6[row, column+1]

            Uvelocity1 = -1*(Umatrix5[row, column])
            Vvelocity1 = -1*(Vmatrix5[row, column])

            concentrationM6[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY



#concentration 7
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM6[row-1, column]
            concXPlus1 = concentrationM6[row+1, column]

            concXY = concentrationM6[row, column]

            concYMinus1 = concentrationM6[row, column-1]
            concYPlus1 = concentrationM6[row, column+1]

            Uvelocity1 = -1*(Umatrix6[row, column])
            Vvelocity1 = -1*(Vmatrix6[row, column])

            concentrationM7[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY
for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM7[row-1, column]
            concXPlus1 = concentrationM7[row+1, column]

            concXY = concentrationM7[row, column]

            concYMinus1 = concentrationM7[row, column-1]
            concYPlus1 = concentrationM7[row, column+1]

            Uvelocity1 = -1*(Umatrix6[row, column])
            Vvelocity1 = -1*(Vmatrix6[row, column])

            concentrationM7[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY


#concentration 8
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM7[row-1, column]
            concXPlus1 = concentrationM7[row+1, column]

            concXY = concentrationM7[row, column]

            concYMinus1 = concentrationM7[row, column-1]
            concYPlus1 = concentrationM7[row, column+1]

            Uvelocity1 = -1*(Umatrix7[row, column])
            Vvelocity1 = -1*(Vmatrix7[row, column])

            concentrationM8[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY
for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM8[row-1, column]
            concXPlus1 = concentrationM8[row+1, column]

            concXY = concentrationM8[row, column]

            concYMinus1 = concentrationM8[row, column-1]
            concYPlus1 = concentrationM8[row, column+1]

            Uvelocity1 = -1*(Umatrix7[row, column])
            Vvelocity1 = -1*(Vmatrix7[row, column])

            concentrationM8[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY


#concentration 9
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM8[row-1, column]
            concXPlus1 = concentrationM8[row+1, column]

            concXY = concentrationM8[row, column]

            concYMinus1 = concentrationM8[row, column-1]
            concYPlus1 = concentrationM8[row, column+1]

            Uvelocity1 = -1*(Umatrix8[row, column])
            Vvelocity1 = -1*(Vmatrix8[row, column])

            concentrationM9[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM9[row-1, column]
            concXPlus1 = concentrationM9[row+1, column]

            concXY = concentrationM9[row, column]

            concYMinus1 = concentrationM9[row, column-1]
            concYPlus1 = concentrationM9[row, column+1]

            Uvelocity1 = -1*(Umatrix8[row, column])
            Vvelocity1 = -1*(Vmatrix8[row, column])

            concentrationM9[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY



#concentration 10
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM9[row-1, column]
            concXPlus1 = concentrationM9[row+1, column]

            concXY = concentrationM9[row, column]

            concYMinus1 = concentrationM9[row, column-1]
            concYPlus1 = concentrationM9[row, column+1]

            Uvelocity1 = -1*(Umatrix9[row, column])
            Vvelocity1 = -1*(Vmatrix9[row, column])

            concentrationM10[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY
for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM10[row-1, column]
            concXPlus1 = concentrationM10[row+1, column]

            concXY = concentrationM10[row, column]

            concYMinus1 = concentrationM10[row, column-1]
            concYPlus1 = concentrationM10[row, column+1]

            Uvelocity1 = -1*(Umatrix9[row, column])
            Vvelocity1 = -1*(Vmatrix9[row, column])

            concentrationM10[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY



#concentration 11
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM10[row-1, column]
            concXPlus1 = concentrationM10[row+1, column]

            concXY = concentrationM10[row, column]

            concYMinus1 = concentrationM10[row, column-1]
            concYPlus1 = concentrationM10[row, column+1]

            Uvelocity1 = -1*(Umatrix10[row, column])
            Vvelocity1 = -1*(Vmatrix10[row, column])

            concentrationM11[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY
for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM11[row-1, column]
            concXPlus1 = concentrationM11[row+1, column]

            concXY = concentrationM11[row, column]

            concYMinus1 = concentrationM11[row, column-1]
            concYPlus1 = concentrationM11[row, column+1]

            Uvelocity1 = -1*(Umatrix10[row, column])
            Vvelocity1 = -1*(Vmatrix10[row, column])

            concentrationM11[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY


#concentration 12
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM11[row-1, column]
            concXPlus1 = concentrationM11[row+1, column]

            concXY = concentrationM11[row, column]

            concYMinus1 = concentrationM11[row, column-1]
            concYPlus1 = concentrationM11[row, column+1]

            Uvelocity1 = -1*(Umatrix11[row, column])
            Vvelocity1 = -1*(Vmatrix11[row, column])

            concentrationM12[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM12[row-1, column]
            concXPlus1 = concentrationM12[row+1, column]

            concXY = concentrationM12[row, column]

            concYMinus1 = concentrationM12[row, column-1]
            concYPlus1 = concentrationM12[row, column+1]

            Uvelocity1 = -1*(Umatrix11[row, column])
            Vvelocity1 = -1*(Vmatrix11[row, column])

            concentrationM12[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY


#concentration 13
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM12[row-1, column]
            concXPlus1 = concentrationM12[row+1, column]

            concXY = concentrationM12[row, column]

            concYMinus1 = concentrationM12[row, column-1]
            concYPlus1 = concentrationM12[row, column+1]

            Uvelocity1 = -1*(Umatrix12[row, column])
            Vvelocity1 = -1*(Vmatrix12[row, column])

            concentrationM13[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM13[row-1, column]
            concXPlus1 = concentrationM13[row+1, column]

            concXY = concentrationM13[row, column]

            concYMinus1 = concentrationM13[row, column-1]
            concYPlus1 = concentrationM13[row, column+1]

            Uvelocity1 = -1*(Umatrix12[row, column])
            Vvelocity1 = -1*(Vmatrix12[row, column])

            concentrationM13[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY



#concentration 14
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM13[row-1, column]
            concXPlus1 = concentrationM13[row+1, column]

            concXY = concentrationM13[row, column]

            concYMinus1 = concentrationM13[row, column-1]
            concYPlus1 = concentrationM13[row, column+1]

            Uvelocity1 = -1*(Umatrix13[row, column])
            Vvelocity1 = -1*(Vmatrix13[row, column])

            concentrationM14[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY
for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM14[row-1, column]
            concXPlus1 = concentrationM14[row+1, column]

            concXY = concentrationM14[row, column]

            concYMinus1 = concentrationM14[row, column-1]
            concYPlus1 = concentrationM14[row, column+1]

            Uvelocity1 = -1*(Umatrix13[row, column])
            Vvelocity1 = -1*(Vmatrix13[row, column])

            concentrationM14[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY


#concentration 15
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM14[row-1, column]
            concXPlus1 = concentrationM14[row+1, column]

            concXY = concentrationM14[row, column]

            concYMinus1 = concentrationM14[row, column-1]
            concYPlus1 = concentrationM14[row, column+1]

            Uvelocity1 = -1*(Umatrix14[row, column])
            Vvelocity1 = -1*(Vmatrix14[row, column])

            concentrationM15[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY
for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM15[row-1, column]
            concXPlus1 = concentrationM15[row+1, column]

            concXY = concentrationM15[row, column]

            concYMinus1 = concentrationM15[row, column-1]
            concYPlus1 = concentrationM15[row, column+1]

            Uvelocity1 = -1*(Umatrix14[row, column])
            Vvelocity1 = -1*(Vmatrix14[row, column])

            concentrationM15[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY


#concentration 16
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM15[row-1, column]
            concXPlus1 = concentrationM15[row+1, column]

            concXY = concentrationM15[row, column]

            concYMinus1 = concentrationM15[row, column-1]
            concYPlus1 = concentrationM15[row, column+1]

            Uvelocity1 = -1*(Umatrix15[row, column])
            Vvelocity1 = -1*(Vmatrix15[row, column])

            concentrationM16[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY
for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM16[row-1, column]
            concXPlus1 = concentrationM16[row+1, column]

            concXY = concentrationM16[row, column]

            concYMinus1 = concentrationM16[row, column-1]
            concYPlus1 = concentrationM16[row, column+1]

            Uvelocity1 = -1*(Umatrix15[row, column])
            Vvelocity1 = -1*(Vmatrix15[row, column])

            concentrationM16[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY


#concentration 17
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM16[row-1, column]
            concXPlus1 = concentrationM16[row+1, column]

            concXY = concentrationM16[row, column]

            concYMinus1 = concentrationM16[row, column-1]
            concYPlus1 = concentrationM16[row, column+1]

            Uvelocity1 = -1*(Umatrix16[row, column])
            Vvelocity1 = -1*(Vmatrix16[row, column])

            concentrationM17[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY
for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM17[row-1, column]
            concXPlus1 = concentrationM17[row+1, column]

            concXY = concentrationM17[row, column]

            concYMinus1 = concentrationM17[row, column-1]
            concYPlus1 = concentrationM17[row, column+1]

            Uvelocity1 = -1*(Umatrix16[row, column])
            Vvelocity1 = -1*(Vmatrix16[row, column])

            concentrationM17[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY


#concentration 18
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM17[row-1, column]
            concXPlus1 = concentrationM17[row+1, column]

            concXY = concentrationM17[row, column]

            concYMinus1 = concentrationM17[row, column-1]
            concYPlus1 = concentrationM17[row, column+1]

            Uvelocity1 = -1*(Umatrix17[row, column])
            Vvelocity1 = -1*(Vmatrix17[row, column])

            concentrationM18[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM18[row-1, column]
            concXPlus1 = concentrationM18[row+1, column]

            concXY = concentrationM18[row, column]

            concYMinus1 = concentrationM18[row, column-1]
            concYPlus1 = concentrationM18[row, column+1]

            Uvelocity1 = -1*(Umatrix17[row, column])
            Vvelocity1 = -1*(Vmatrix17[row, column])

            concentrationM18[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY




#concentration 19
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM18[row-1, column]
            concXPlus1 = concentrationM18[row+1, column]

            concXY = concentrationM18[row, column]

            concYMinus1 = concentrationM18[row, column-1]
            concYPlus1 = concentrationM18[row, column+1]

            Uvelocity1 = -1*(Umatrix18[row, column])
            Vvelocity1 = -1*(Vmatrix18[row, column])

            concentrationM19[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY
for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM19[row-1, column]
            concXPlus1 = concentrationM19[row+1, column]

            concXY = concentrationM19[row, column]

            concYMinus1 = concentrationM19[row, column-1]
            concYPlus1 = concentrationM19[row, column+1]

            Uvelocity1 = -1*(Umatrix18[row, column])
            Vvelocity1 = -1*(Vmatrix18[row, column])

            concentrationM19[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY



#concentration 20
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM19[row-1, column]
            concXPlus1 = concentrationM19[row+1, column]

            concXY = concentrationM19[row, column]

            concYMinus1 = concentrationM19[row, column-1]
            concYPlus1 = concentrationM19[row, column+1]

            Uvelocity1 = -1*(Umatrix19[row, column])
            Vvelocity1 = -1*(Vmatrix19[row, column])

            concentrationM20[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM20[row-1, column]
            concXPlus1 = concentrationM20[row+1, column]

            concXY = concentrationM20[row, column]

            concYMinus1 = concentrationM20[row, column-1]
            concYPlus1 = concentrationM20[row, column+1]

            Uvelocity1 = -1*(Umatrix19[row, column])
            Vvelocity1 = -1*(Vmatrix19[row, column])

            concentrationM20[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY


#concentration 21
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM20[row-1, column]
            concXPlus1 = concentrationM20[row+1, column]

            concXY = concentrationM20[row, column]

            concYMinus1 = concentrationM20[row, column-1]
            concYPlus1 = concentrationM20[row, column+1]

            Uvelocity1 = -1*(Umatrix20[row, column])
            Vvelocity1 = -1*(Vmatrix20[row, column])

            concentrationM21[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY
for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM21[row-1, column]
            concXPlus1 = concentrationM21[row+1, column]

            concXY = concentrationM21[row, column]

            concYMinus1 = concentrationM21[row, column-1]
            concYPlus1 = concentrationM21[row, column+1]

            Uvelocity1 = -1*(Umatrix20[row, column])
            Vvelocity1 = -1*(Vmatrix20[row, column])

            concentrationM21[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY


#concentration 22
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM21[row-1, column]
            concXPlus1 = concentrationM21[row+1, column]

            concXY = concentrationM21[row, column]

            concYMinus1 = concentrationM21[row, column-1]
            concYPlus1 = concentrationM21[row, column+1]

            Uvelocity1 = -1*(Umatrix21[row, column])
            Vvelocity1 = -1*(Vmatrix21[row, column])

            concentrationM22[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY
for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM22[row-1, column]
            concXPlus1 = concentrationM22[row+1, column]

            concXY = concentrationM22[row, column]

            concYMinus1 = concentrationM22[row, column-1]
            concYPlus1 = concentrationM22[row, column+1]

            Uvelocity1 = -1*(Umatrix21[row, column])
            Vvelocity1 = -1*(Vmatrix21[row, column])

            concentrationM22[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

#concentration 23
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM22[row-1, column]
            concXPlus1 = concentrationM22[row+1, column]

            concXY = concentrationM22[row, column]

            concYMinus1 = concentrationM22[row, column-1]
            concYPlus1 = concentrationM22[row, column+1]

            Uvelocity1 = -1*(Umatrix22[row, column])
            Vvelocity1 = -1*(Vmatrix22[row, column])

            concentrationM23[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY
for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM23[row-1, column]
            concXPlus1 = concentrationM23[row+1, column]

            concXY = concentrationM23[row, column]

            concYMinus1 = concentrationM23[row, column-1]
            concYPlus1 = concentrationM23[row, column+1]

            Uvelocity1 = -1*(Umatrix22[row, column])
            Vvelocity1 = -1*(Vmatrix22[row, column])

            concentrationM22[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

#concentration 24
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM23[row-1, column]
            concXPlus1 = concentrationM23[row+1, column]

            concXY = concentrationM23[row, column]

            concYMinus1 = concentrationM23[row, column-1]
            concYPlus1 = concentrationM23[row, column+1]

            Uvelocity1 = -1*(Umatrix23[row, column])
            Vvelocity1 = -1*(Vmatrix23[row, column])

            concentrationM24[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM24[row-1, column]
            concXPlus1 = concentrationM24[row+1, column]

            concXY = concentrationM24[row, column]

            concYMinus1 = concentrationM24[row, column-1]
            concYPlus1 = concentrationM24[row, column+1]

            Uvelocity1 = -1*(Umatrix23[row, column])
            Vvelocity1 = -1*(Vmatrix23[row, column])

            concentrationM24[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

#concentration 25
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM24[row-1, column]
            concXPlus1 = concentrationM24[row+1, column]

            concXY = concentrationM24[row, column]

            concYMinus1 = concentrationM24[row, column-1]
            concYPlus1 = concentrationM24[row, column+1]

            Uvelocity1 = -1*(Umatrix24[row, column])
            Vvelocity1 = -1*(Vmatrix24[row, column])

            concentrationM25[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM25[row-1, column]
            concXPlus1 = concentrationM25[row+1, column]

            concXY = concentrationM25[row, column]

            concYMinus1 = concentrationM25[row, column-1]
            concYPlus1 = concentrationM25[row, column+1]

            Uvelocity1 = -1*(Umatrix24[row, column])
            Vvelocity1 = -1*(Vmatrix24[row, column])

            concentrationM25[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

#concentration 26
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM25[row-1, column]
            concXPlus1 = concentrationM25[row+1, column]

            concXY = concentrationM25[row, column]

            concYMinus1 = concentrationM25[row, column-1]
            concYPlus1 = concentrationM25[row, column+1]

            Uvelocity1 = -1*(Umatrix25[row, column])
            Vvelocity1 = -1*(Vmatrix25[row, column])

            concentrationM26[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY
for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM26[row-1, column]
            concXPlus1 = concentrationM26[row+1, column]

            concXY = concentrationM26[row, column]

            concYMinus1 = concentrationM26[row, column-1]
            concYPlus1 = concentrationM26[row, column+1]

            Uvelocity1 = -1*(Umatrix25[row, column])
            Vvelocity1 = -1*(Vmatrix25[row, column])

            concentrationM26[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

#concentration 27
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM26[row-1, column]
            concXPlus1 = concentrationM26[row+1, column]

            concXY = concentrationM26[row, column]

            concYMinus1 = concentrationM26[row, column-1]
            concYPlus1 = concentrationM26[row, column+1]

            Uvelocity1 = -1*(Umatrix26[row, column])
            Vvelocity1 = -1*(Vmatrix26[row, column])

            concentrationM27[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM27[row-1, column]
            concXPlus1 = concentrationM27[row+1, column]

            concXY = concentrationM27[row, column]

            concYMinus1 = concentrationM27[row, column-1]
            concYPlus1 = concentrationM27[row, column+1]

            Uvelocity1 = -1*(Umatrix26[row, column])
            Vvelocity1 = -1*(Vmatrix26[row, column])

            concentrationM27[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

#concentration 28
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM27[row-1, column]
            concXPlus1 = concentrationM27[row+1, column]

            concXY = concentrationM27[row, column]

            concYMinus1 = concentrationM27[row, column-1]
            concYPlus1 = concentrationM27[row, column+1]

            Uvelocity1 = -1*(Umatrix27[row, column])
            Vvelocity1 = -1*(Vmatrix27[row, column])

            concentrationM28[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY
for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM28[row-1, column]
            concXPlus1 = concentrationM28[row+1, column]

            concXY = concentrationM28[row, column]

            concYMinus1 = concentrationM28[row, column-1]
            concYPlus1 = concentrationM28[row, column+1]

            Uvelocity1 = -1*(Umatrix27[row, column])
            Vvelocity1 = -1*(Vmatrix27[row, column])

            concentrationM28[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

#concentration 29
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM28[row-1, column]
            concXPlus1 = concentrationM28[row+1, column]

            concXY = concentrationM28[row, column]

            concYMinus1 = concentrationM28[row, column-1]
            concYPlus1 = concentrationM28[row, column+1]

            Uvelocity1 = -1*(Umatrix28[row, column])
            Vvelocity1 = -1*(Vmatrix28[row, column])

            concentrationM29[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY
for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM29[row-1, column]
            concXPlus1 = concentrationM29[row+1, column]

            concXY = concentrationM29[row, column]

            concYMinus1 = concentrationM29[row, column-1]
            concYPlus1 = concentrationM29[row, column+1]

            Uvelocity1 = -1*(Umatrix28[row, column])
            Vvelocity1 = -1*(Vmatrix28[row, column])

            concentrationM29[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY

#concentration 30
for row in range(1,40):
    for column in range(1,40):
        #if ((row != 0 or row != 40) and (column != 0 or column != 40)):
            concXMinus1 = concentrationM29[row-1, column]
            concXPlus1 = concentrationM29[row+1, column]

            concXY = concentrationM29[row, column]

            concYMinus1 = concentrationM29[row, column-1]
            concYPlus1 = concentrationM29[row, column+1]

            Uvelocity1 = -1*(Umatrix29[row, column])
            Vvelocity1 = -1*(Vmatrix29[row, column])

            concentrationM30[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))
                                              -(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY
for i in range(0,99):
    for row in range(1,40):
        for column in range(1,40):

            concXMinus1 = concentrationM30[row-1, column]
            concXPlus1 = concentrationM30[row+1, column]

            concXY = concentrationM30[row, column]

            concYMinus1 = concentrationM30[row, column-1]
            concYPlus1 = concentrationM30[row, column+1]

            Uvelocity1 = -1*(Umatrix29[row, column])
            Vvelocity1 = -1*(Vmatrix29[row, column])

            concentrationM30[row, column] = h*(Uvelocity1*((concXPlus1 - concXMinus1)/(2*k)) + Vvelocity1*((concYPlus1-concYMinus1)/(2*k))-(d*(((concXPlus1 - 2*concXY + concYMinus1)/(k*k))+((concYPlus1 - 2*concXY + concYMinus1)/(k*k)))))+ concXY



np.set_printoptions(threshold=sys.maxsize)
sns.heatmap(concentrationM30, annot=False, cmap="viridis")
plt.savefig("heatmap2_1.png")
plt.close()

sns.heatmap(concentrationM1, annot=False, cmap="viridis")
plt.savefig("heatmap2-2.png")
plt.close()
