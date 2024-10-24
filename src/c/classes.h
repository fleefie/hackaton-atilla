#ifndef CLASS_C_H
#define CLASS_C_H

#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
  int x;
  int y;
  void (*method_test)();
} Character_c;

// Create a new instance of MyClass
Character_c *Character_new(int x, int y);

// Destroy an instance of MyClass
void Character_delete(Character_c *obj);

// Getters and setters for the fields
int Character_getx(const Character_c *obj);
void Character_setx(Character_c *obj, int x);

int Character_gety(const Character_c *obj);
void Character_sety(Character_c *obj, int y);

#ifdef __cplusplus
}
#endif

#endif // CLASS_C_H
