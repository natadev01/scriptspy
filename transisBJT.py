
def trEstabEmisor(Rb,Rc,Re,hFe,E):
    IB = (E-0.7)/(Rb+(Re*(hFe+1)))
    IC = IB * hFe
    IE = IB + IC
    VE = Re * IE
    VC = E - ( IC * Rc) 
    VCE = VC - VE
    VB = 0.7 + VE
    return print(f'Ib es: {IB:.3}A \nIc es: {IC:.3}A \nIe es: {IE:.3} \nel Vce es: {VCE:.3} \nVc es: {VC:.3}\nVe es: {VE:.3}\nVb es:{VB:.3}')

trEstabEmisor(510000,2400,1500,100,20)

def trEmisorCom(Rb,Rc,hFe,E):
    ib=(E-0.7)/Rb
    vb=0.7
    ic=ib*hFe
    vRc=ic*Rc
    vce=E-vRc
    vc=vce
    ie=ib+ic
    ve=0
    return print(f'Ib es: {ib:.3}A \nIc es: {ic:.3}A \nIe es: {ie:.3} \nel Vce es: {vce:.3} \nVc es: {vc:.3}\nVe es: {ve:.3}\nVb es:{vb:.3}')

def trDivVolt(R1,R2,RC,RE,hFe,E):
    RB=(R1*R2)/(R1+R2)
    VBB=(E*R2)/(R1+R2)
    IB = (VBB-0.7)/(RB+(RE*(hFe+1)))
    IC = IB * hFe
    IE = IB + IC
    VE = RE * IE
    VC = E - ( IC * RC) 
    VCE = VC - VE
    VB = 0.7 + VE
    return print(f'Ib es: {IB:.3}A \nIc es: {IC:.3}A \nIe es: {IE:.3} \nel Vce es: {VCE:.3} \nVc es: {VC:.3}\nVe es: {VE:.3}\nVb es:{VB:.3}')

