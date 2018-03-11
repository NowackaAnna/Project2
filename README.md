Krótki opis projektu.


Będzie to program (może przerodzić się w aplikację) w typie kalulatora biegowego. Będzie on działał w dwie strony.
Po pierwsze, będzie wyznaczyał między czasy poszczególnych odcinków po podaniu zakładanego czasu, jaki chcemy uzyskać na całym dystansie i wybraniu typu tempa biegu.
Np. zakładamy, że chcemu uzyskać 40min na 10 km. Następnie wybieramy rodzaj tempa.
Tempo biegu będzie wybiareane najpawdopodobniej z 4: regresywnego, stałego, negativ split i progresywnego.  
Wtedy program poda nam, jakie międzyczasy powinniśmy mieć na każdym kilometrze.
Po drugie, po wpisaniu średniej prędkości (min/km) z jaką chcemy biec, program wygeneruje nam w jakim czasie powinniśmy przebiegać kolejne odcinki
Np. biegając 10 000m. na stadionie 400m. dostaniemy w jakie czasy powiniśmy mieć na kolejnych okrążeniach razem z międzyczasami.

W wersji rozszerzonej programu (jeśli taka dojedzie do skutku), będą do uzupełnienia także dane użytkownika (imię, nazwisko i data urodzenia).
Po wypełnieniu tych pól, będzie można wpisać swoje PB,SB oraz czasu uzyskiwane na zawodach, które będą zapisywane do pliku.
Jeśli użytkownik o podanych danych istnieje, to wyniki będą dopisywane, a PB i SB aktualizowane, jeśli nie, to zostanie stworzony.
Dzięki temu można będzie mieć wgląd na swoje czasy oraz program będzie mógł rysować wykres progresji danego zawodnika. 

Program będzie działał tylko dla danych dystansów, ponieważ każdy z nich ma inny, unikalny algorytm przeliczeń i nie można np. tempem na 100m przebiec maratonu.
Dystanse: 1000m., 3000m., 5000., 10 000., półmaraton, maraton 

Biblioteki: Datatime, Numpy, PyQt5 (aplikacja okienkowa) 
