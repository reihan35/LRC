concatene([],L,L).
concatene(L,[],L).
concatene([X | L],Y,[X | Z]) :- concatene(L,Y,Z).

inverse([],[]).
/*inverse([X|L], Lr) :- inverse(L, concatene(Lr,X,)).
*/
inverse([X|L], Lr) :- inverse(L,Lt), concatene(Lt,[X],Lr).


supprime([], _, []).
supprime([X|L], X, Lr) :- supprime(L, X, Lr).
supprime([X|L], Y, Lr) :- supprime(L, Y, Lt), concatene([X],Lt,Lr).

filtre([],_,[]).
filtre(L, [Y|L2], Lr) :- supprime(L, Y, Lt), filtre(Lt, L2, Lr).
