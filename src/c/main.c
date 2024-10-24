#include "main.h"
#include "classes.h"

void c_main() {
  printf("test\n");
  Character_c *a_character_test = Character_new(5, 5);
  printf("%i\n", Character_getx(a_character_test));
  Character_setx(a_character_test, 10);
  printf("%i\n", Character_getx(a_character_test));
  // Implementation of the function
}
