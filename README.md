# MES-finite-element-method
#### Opis
Jest to program do rozwiązywania jednowymiarowych równań
różniczkowych liniowych cząstkowych metodą elementów skończonych.
#### Background
Projekt został wykonany na przedmiot: Równania różniczkowe i różnicowe prowadzone na 
Akademii Górniczo-Hutniczej im. Stanisława Staszica w Krakowie na Wydziale 
Informatyki,Elektroniki i Telekomiunikacji na keirunku Informatyka.
#### Równanie
(a(x)*u'(x))' + b(x)*u'(x) + c(x)*u(x) = f(x) <br>
Obszar Ω=(u0,un)
#### Warunki brzegowe
-a(u0)*u'(u0) + β*u(u0) = γ <br>
u(un) = Ur
#### Uruchomienie
Plik głowny z któego uruchamiamy to main.py. W tym również pliku ustawiamy funkcje a(x), b(x), c(x),oraz f(x).<br>
W InputData.py ustawiamy paramtey β,γ oraz Ur, oraz Ω=(u0,un)
#### Technologie
Python
#### Twórcy
Radosław Kopeć
