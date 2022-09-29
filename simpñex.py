import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
c = np.array([-5.0, -4.0]) # Coeficientes de la funcion costo
A = np.array([[6,4],[1,2],[-1,1],[0,1]]) # coeficientes de la matriz de inequalities
b = np.array([24, 6, 1, 2]) # coeficientes libres
res = linprog(c, A, b, method="revised simplex")
print(res)  # mostramos la estrucutra OptimizedResult
con: array([], dtype=float64)
    fun: -21.0
message: 'Optimization terminated successfully.'
    nit: 2
  slack: array([0. , 0. , 2.5, 0.5])
 status: 0
success: True
      x: array([3. , 1.5])
      def plot_constr(c,A,b,limites,zz):
    """Author Stephen Krol 2020 <stephendata.science.blog>"""
    N = A.shape[0]
    print("Number of contraints inequalities: ", N)
    plt.figure()
    plt.title("Cost:  z = "+ " + ".join([str(x)+" x"+str(i+1) for i,x in enumerate(c)]))
    X = np.linspace(0,15)
    for i in range(0,N):
        c_txt = " + ".join([str(x)+" x"+str(i+1) for i,x in enumerate(A[i,:])]) + " <= " + str(b[i])
        plt.plot(X, -X*(A[i,0]/A[i,1]) + b[i]/A[i,1] ,label = c_txt ) 
 
    for j in range(zz[0],zz[1], zz[2]):
        c_txt = "z = " + str(j)
        plt.plot(X, -X*(c[0]/c[1]) + (j/c[1]), "--" ,label = c_txt ) 
         
    res = linprog(c, A, b, method="revised simplex")
    plt.plot(res.x[0],res.x[1],"ro", label="Solucion")
     
    plt.xlim(0,limites[0])
    plt.ylim(0,limites[1])
    plt.legend()
    plt.grid()
    plt.show()
    np.dot(res.x.T , -c)
    plot_constr(c,A,b,[6,6],[-21,0,5])