/* c(p).
c(z). */
rv(X) :- s(X).
/* d(X) :- c(X). */
re(X) :- rv(X).
s(X) :- d(X).

