# CookieClickBot
## Opis projektu
Projekt Cookie Click Bot to automatyczny skrypt napisany w języku Python przy użyciu biblioteki Selenium, który umożliwia automatyczne granie w popularną grę przeglądarkową "Cookie Clicker". Główne funkcje skryptu to klikanie w ciasteczko, zbieranie pieniędzy i dokonywanie zakupów w sklepie gry

## Jak działa program?

1. **Inicjalizacja przeglądarki**: Skrypt inicjalizuje przeglądarkę Google Chrome, korzystając z Selenium, i otwiera stronę gry Cookie Clicker [Cookie Clicker](https://orteil.dashnet.org/experiments/cookie/).

2. **Pobieranie elementów**: Skrypt identyfikuje główne elementy gry, takie jak ciasteczko (cookie) i dostępne produkty w sklepie.

3. **Główna pętla**: Skrypt uruchamia główną pętlę, która działa przez zdefiniowany czas (w tym przypadku 5 minut), klikając w ciasteczko oraz monitorując dostępne produkty w sklepie.

4. **Zakupy**: Jeśli stan konta gracza pozwala na zakup produktu, skrypt kliknie na odpowiednią opcję w sklepie. Zakupy są dokonywane tylko wtedy, gdy wystarczająco dużo pieniędzy jest dostępne.

5. **Optymalizacja zakupów**: Skrypt próbuje optymalizować zakupy, przechodząc przez dostępne produkty od najdroższego w dół, kupując je, jeśli tylko gracz ma wystarczającą ilość pieniędzy.

6. **Zarządzanie czasem zakupów**: Skrypt kontroluje czas między zakupami, aby nie kupować produktów zbyt często. W tym przypadku zakupy są dokonywane co najmniej co 5 sekund (możesz dostosować ten interwał według własnych preferencji).

7. **Zakończenie pracy**: Po upływie zdefiniowanego czasu (5 minut), skrypt kończy działanie i zamyka przeglądarkę.
