/* exercice 1 */

subs(chat, felin).
subs(lion, felin).
subs(chien, canide).
subs(canide, chien).
subs(souris, mammifere).
subs(felin, mammifere).
subs(canide, mammifere).
subs(mammifere, animal).
subs(canari, animal).
subs(and(animal,plante),nothing).
subs(animal, etreVivant).
subs(animal, some(mange)).
subs(humain, mammifere).
subs(lion, carnivoreExc).
/*subs(A,B) :- equiv(A,B) .
subs(B,A) :- equiv(A,B) .*/
equiv(A,B) :- subs(A,B), subs(B,A) .
equiv(carnivoreExc, all(mange,animal)).
equiv(herbivoreExc, all(mange,plante)).


/* exercice 2 */

subsS1(C,C). /* C est subsumé par lui-même */ 
subsS1(C,D) :- subs(C,D), C\==D. /* C est subsumé par D et C est différent de D */
subsS1(C,D) :- subs(C,E), subsS1(E,D). /* transitivité de la subsomption */

/* 2.

?- subsS1(canari, animal).
true .

?- subsS1(chat, etreVivant).
true .

*/

/* 
3. chien est subsumé par canide et vice-versa : on a une boucle infinie.
*/

subsS(C,D) :- subsS(C,D,[C]).
subsS(C,C,_).
subsS(C,D,_) :- subs(C,D), C\==D.
subsS(C,D,L) :- subs(C,E),not(member(E,L)),subsS(E,D,[E|L]),E\==D.

/* 4.
?- subsS(canari, animal).
true .

?- subsS(chat, etreVivant).
true .

?- subsS(chien, canide).
true .

?- subsS(chien, chien).
true .

5.
?- subsS1(souris, some(mange)).
true .

Comme on est en FL-, "il existe" est comme un concept simple pour prolog, il unifie sans problème. 

6. 
?- subsS(chat, humain).
false.

?- subsS(chien, souris).
false.

7.
?- subsS(chat,X).
X = chat ;
X = felin ;
X = mammifere ;
X = animal ;
X = etreVivant ;
X = some(mange) ;
false.

?- subsS(X, mammifere).
X = mammifere ;
X = souris ;
X = felin ;
X = canide ;
X = humain ;
X = chat ;
X = lion ;
X = chien ;
false.
*/

