import numpy as np


def get_net(vp, i,p,mq):
    # maq de 1 a 3 (visa, master, elo)
          
    def cal_tx():
        op = []
        op1=[1.55,1.65,1.70]
        op2=[2.15,2.20,2.60]
        
        if mq in range(1,4):
            for q in range(3):
                op.append(op1[q])
        else:
            for q in range(3):
                op.append(op2[q])
            
                
        valores = []
        for n in range(1,13):
            if n == 1:
                tarifa_mq = op[0]
                res = i
                res1 = (((np.mean(res) + tarifa_mq)))
                valores.append(res1)  

            elif n in range(2,7):
                res = []
                for d in range(30,30*p+30,30):
                    tarifa_mq = op[1]
                    for w in range(1,n+1):
                        res.append(w*i)
                valores.append(((np.mean(res) + tarifa_mq))) 

            elif n in range(6,13):
                res = []
                for d in range(30,30*p+30,30):
                    tarifa_mq = op[2]
                    for w in range(1,n+1):
                        res.append(w*i)
                valores.append(((np.mean(res) + tarifa_mq)))
        
        return valores[0:p]
     
                  
    tx = cal_tx()
    valor = [(vp + (vp*tx[i]/100)) for i in range(p)]
    desc =  [(vp*tx[i]/100) for i in range(p)]
    #juros_em =  [((valor[i]/vp)-1)*100 for i in range(p)]  
    parcela = [i+1 for i in range(p)]
    valor_p = [("R$ "+"%.2f" %(valor[i]/parcela[i])).replace(".",",") for i in range(p)]
    
    
    dados = [[("R$ "+"%.2f" %(valor[i])).replace(".",","),parcela[i],valor_p[i],("%.2f" %(tx[i]))+" %",("R$ "+"%.2f" %(desc[i])).replace(".",",")] for i in range(p)]	
    #df = pd.DataFrame(dados, columns=['Valor','Parcelas','Valor da Parcela', 'Taxa Getnet','Desconto'])
    
    return dados