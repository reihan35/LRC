pere(morteza,fati).
pere(parviz,homeira).
pere(morteza,laura).
mere(homeira,fati).
parent(X,Y):- mere(X,Y); pere(X,Y).
parent(X,Y,Z):- mere(Y,Z), pere(X,Z).
grandPere(X,Y) :-  (pere(Z,Y), pere(X,Z));(mere(Z,Y), pere(X,Z)).
frereOuSoeur(X,Y) :- pere(Z,X),pere(Z,Y);mere(Z,X),mere(Z,Y).

/* V1
ancetre(X,Y) :- parent(X,Y).
ancetre(X,Y) :- parent(X,Z), ancetre(Z,Y). */

/* V2
ancetre(X,Y) :- parent(X,Z), ancetre(Z,Y).
ancetre(X,Y) :- parent(X,Y). */

/* V3 */
ancetre(X,Y) :- parent(X,Y).
ancetre(X,Y) :- ancetre(Z,Y),parent(X,Z).

/* 2.
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

/* 4.
?- parent(morteza,homeira,fati).
true .

?- parent(homeira,morteza,fati).
false
*/

/* 5.
?- grandPere(parviz,fati).
true.
*/
/*?- frereOuSoeur(laura,fati).
true .
*/

/* 6. Mêmes résultats pour toutes les versions
?- ancetre(parviz,fati).
true .

?- ancetre(homeira,fati).
true .
*/
