import os
import numpy as np
from generate_att import generate_Att_from_img_threebythree
Name=os.listdir('D:\\zsk\\SRAN-master\\I-RAVEN\\distribute_nine')
k=0
for name_ind in range (0,10000):
        #for name_ind in [0,1]:
    length=len('RAVEN_'+str(name_ind)+'_')
    for n in Name:
        if n[0:length]=='RAVEN_'+str(name_ind)+'_' and n[-3:]=='npz':
            Exist0=np.zeros((3,3,9))
            A=np.load('D:\\zsk\\SRAN-master\\I-RAVEN\\distribute_nine\\'+n)
            data=A['image']
            answer=A['target']
            Exist,Type,Color,Size,Angle,Exist_panel,Angle_panel,Color_panel,Size_panel,Type_panel=generate_Att_from_img_threebythree(data)
            Exist0[:,:,0:8]=Exist[:,:,0:8]
            Exist0[:,:,8]=Exist[:,:,answer+8]
            Exist1=Exist[:,:,8:16]
            np.save('D:\\zsk\\RAVEN\\position9_3\\'+str(k)+'.npy',Exist0)
            np.save('D:\\zsk\\RAVEN\\pselection9_3\\'+str(k)+'.npy',Exist1)
            k+=1