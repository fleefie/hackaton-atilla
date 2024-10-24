class Character {
public:
  Character(int x, int y) : _posx(x), _posy(y) {}

  int getx() { return _posx; };
  int gety() { return _posy; };
  void setx(int x) { _posx = x; };
  void sety(int y) { _posy = y; };

private:
  int _posx;
  int _posy;
};
