#pragma once

#define FRAME(x) x * 3 + arduboy.currentPlane()
#define MAX_FPS 10

struct Player {
  uint8_t x, y;
  uint24_t sprite;
  uint8_t frames;
  bool up;
  bool down;
  bool left;
  bool right;
  bool big;
};


enum class Screen : uint8_t {
  Title,
  Game,
  Gallery,
  Gameover
};

struct Light {
  int centerX;
  int centerY;
  int radius;
 
};
Light light = {64, 64, 5};
Player player = {64, 0, idlefsmall, 7, false, true, false, false, true};
Screen screen = {Screen::Title};
uint8_t currentframe = 0;

uint8_t firstframe = 0;
int last_frame = -1;
uint8_t framewait = 2;
int prevTime=0;
int startcounter=0;
uint8_t gamestate =0;

uint8_t framecount = 7; //1 less than actual number of frames, first frame = 0