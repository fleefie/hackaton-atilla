#include "affichage.h"





void ecran(){
    // Affichage d'un message
    mvprintw(5, 10, "Salut, bienvenue dans le mode ncurses !");
    mvprintw(7, 10, "Appuyez sur une touche pour quitter.");

    // Rafraîchit l'écran pour afficher le texte
    refresh();

    // Attendre que l'utilisateur appuie sur une touche
    getch();

    // Fermer ncurses
    endwin();


}
