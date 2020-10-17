import numpy as np            

V = np.array(([35,-6],[-6,30]))
a = np.array(([V[0,0]],[V[1,0]]))
b = np.array(([V[0,1]],[V[1,1]]))
u_1 = a
e_1 = u_1/np.sqrt(u_1[0]**2 + u_1[1]**2)
u_2 = b - np.dot(np.transpose(b),e_1)*e_1
e_2 = u_2/np.sqrt(u_2[0]**2 + u_2[1]**2)
q = np.array(([e_1[0,0],e_2[0,0]],[e_1[1,0],e_2[1,0]]))
r = np.array(([np.dot(np.transpose(a),e_1)[0],np.dot(np.transpose(b),e_1)[0]],[0,np.dot(np.transpose(b),e_2)[0]]))

print("Q")
print(q)
print("R")
print(r)
