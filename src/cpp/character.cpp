#include "character.hpp"
#include "../c/classes.h"

#include <stdlib.h>

extern "C" {

Character_c *Character_new(int x, int y) {
  Character *obj = new Character(x, y);
  Character_c *c_obj = (Character_c *)malloc(sizeof(Character_c));
  c_obj->x = obj->getx();
  c_obj->y = obj->gety();
  return c_obj;
}

void Character_delete(Character_c *c_obj) {
  if (c_obj) {
    free(c_obj);
  }
}

int Character_getx(const Character_c *c_obj) {
  if (c_obj) {
    return c_obj->x;
  }
  exit(-1); // or some error value
}

void Character_setx(Character_c *c_obj, int x) {
  if (c_obj) {
    c_obj->x = x;
  }
}

int Character_gety(const Character_c *c_obj) {
  if (c_obj) {
    return c_obj->y;
  }
  exit(-1);
}

void Character_sety(Character_c *c_obj, int y) {
  if (c_obj) {
    c_obj->y = y;
  }
  exit(-1);
}
}
