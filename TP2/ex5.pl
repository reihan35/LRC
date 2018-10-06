et(0,0,0). 
et(1,0,0).
et(0,1,0).
et(1,1,1).
ou(0,0,0).
ou(1,0,1).
ou(0,1,1).
ou(1,1,1).
non(0,1).
non(1,0).
circuit(0,0,1).
circuit(1,0,0).
circuit(0,1,1).
circuit(1,1,1).
/* 2.
?- et(X,Y,1).
X = Y, Y = 1.

?- et(0,0,R).
R = 0 .

?- et(X,Y,R).
X = Y, Y = R, R = 0 .

*/
