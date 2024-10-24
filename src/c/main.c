#include "main.h"
#include "affichage.h"

void my_c_function() {
  initscr();            // Démarre le mode ncurses
  cbreak();             // Désactive la mise en tampon d'entrée
  noecho();             // Empêche l'affichage des touches pressées
  curs_set(FALSE);      // Cache le curseur
  
  // Implementation of the function
}
