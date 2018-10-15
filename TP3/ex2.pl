concatene([],L,L).
concatene(L,[],L).
concatene([X | L],Y,[X | Z]) :- concatene(L,Y,Z).

/* 
?- concatene([], [1, 2, 3], L).
L = [1, 2, 3] ;

?- concatene([1, 2, 3], [], L).
L = [1, 2, 3] ;

?- concatene([], [1, 2, 3], L).
L = [1, 2, 3] ;

*/

inverse([],[]).
inverse([X|L], Lr) :- inverse(L,Lt), concatene(Lt,[X],Lr).

/* 
?- inverse([], L).
L = [].

?- inverse([1, 2, 3], L).
L = [3, 2, 1] ;
*/

supprime([], _, []).
supprime([X|L], X, Lr) :- supprime(L, X, Lr).
supprime([X|L], Y, Lr) :- supprime(L, Y, Lt), concatene([X],Lt,Lr).

/*
?- supprime([], 1, L).
L = [].

?- supprime([1, 5, 1, 9], 1, L).
L = [5, 9] .

?- supprime([1, 5, 1, 9], 5, L).
L = [1, 1, 9] .
*/

filtre(L,[],L).
filtre(L, [Y|L2], Lr) :- supprime(L, Y, Lt), filtre(Lt, L2, Lr).

/*
?- filtre([1, 5, 1, 9], [], L).
L = [1, 5, 1, 9] .

?- filtre([1, 5, 1, 9, 5, 8], [1, 5], L).
L = [9, 8] .

?- filtre([1, 5, 1, 9, 5, 8], [8, 9], L).
L = [1, 5, 1, 5] .
*/

palindrome(L) :- inverse(L,L).

/*
?- palindrome([k,a,y,a,k]).
true .

?- palindrome([k,a,y,k,k]).
false.
*/

/* récupère le dernier élément d'une liste */
fin([], []).
fin([X],X).
fin([X|L],Z) :- fin(L,Z).

/* supprime le dernier élément d'une liste */
supprimefin([], _, []).
supprimefin([X,Y], [X]).
supprimefin([X|L], Lr) :- supprimefin(L, Lt),concatene([X],Lt,Lr).


palindrome2([]).
palindrome2([X,Y,X]).
palindrome2([X|L]) :-  fin(L,X), supprimefin(L, Lr), palindrome2(Lr).

/*
?- palindrome2([]).
true.

?- palindrome2([x]).
false.

?- palindrome2([k,a,y,a,k]).
true.

?- palindrome2([k,a,y,k,k]).
false.*/
