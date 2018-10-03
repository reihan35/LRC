pere(morteza,fati).
pere(parviz,homeira).
pere(morteza,laura).
mere(homeira,fati).
parent(X,Y):- mere(X,Y); pere(X,Y).
parent(X,Y,Z):- mere(Y,Z), pere(X,Z).
grandPere(X,Y) :-  (pere(Z,Y), pere(X,Z));(mere(Z,Y), pere(X,Z)).
frereOuSoeur(X,Y) :- pere(Z,X),pere(Z,Y);mere(Z,X),mere(Z,Y).
ancetre(X,Y) :- pere(X,Y); grandPere(X,Y).
/*
?- parent(homeira,fati).
true [print]
true .

?- parent(morteza,fati).
true.

?- parent(Laura,fati).
Laura = homeira .

?- parent(laura,fati).
false.

*/

/*?- grandPere(parviz,fati).
true.
*/
/*?- frereOuSoeur(laura,fati).
true .
*/
