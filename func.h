#include "Arduino.h"
#include "Arduboy2Core.h"
#include "vars.h"

void playerInput() {
  if (arduboy.pressed(LEFT_BUTTON)){
        player.right = false;
        player.down = false;
        player.up = false;
        player.left = true;
      } if (arduboy.pressed(DOWN_BUTTON)) {
        player.right = false;
        player.down = true;
        player.up = false;
        player.left = false;
      } if (arduboy.pressed(RIGHT_BUTTON)){
        player.right = true;
        player.down = false;
        player.up = false;
        player.left = false;
      } if (arduboy.pressed(UP_BUTTON)){
        player.right = false;
        player.down = false;
        player.up = true;
        player.left = false;
      }
}
void animate(){
  framecount = player.frames;
  if (startcounter %(framewait*5)==0){
    if (currentframe < framecount){
      currentframe++;
    } else {
      currentframe = firstframe;
    }
  }
  startcounter++;
}
void updateSprite(){
  if (arduboy.pressed(A_BUTTON)){
    player.big = false;
  } else {
    player.big =true;
  }
  if (player.left && !arduboy.pressed(LEFT_BUTTON)){
    if (player.big) {player.sprite =idlel;}
    else {
    player.sprite = idlelsmall;
    }
  } else if (player.left && arduboy.pressed(LEFT_BUTTON)){
    if (player.big) {player.sprite =walkleft;}
    else {
      player.sprite = walkleftsmall;
    }
  }
  if (player.right && !arduboy.pressed(RIGHT_BUTTON)){
    if (player.big) {player.sprite =idler;}
    else {
    player.sprite = idlersmall;
    }
  } else if (player.right && arduboy.pressed(RIGHT_BUTTON)){
    if (player.big) {player.sprite =walkright;}
    else {
      player.sprite = walkrightsmall;
    }
  }
  if (player.down && !arduboy.pressed(DOWN_BUTTON)){
    if (player.big) {player.sprite =idlef;}
    else {
    player.sprite = idlefsmall;
    }
  } else if (player.down && arduboy.pressed(DOWN_BUTTON)){
    if (player.big) {player.sprite =walkf;}
    else {
    player.sprite = walkfsmall;
    }
  }
  if (player.sprite == walkfsmall || player.sprite == walkf || player.sprite == walkleft || player.sprite == walkleftsmall || player.sprite == walkright || player.sprite ==walkrightsmall){
    player.frames = 9;
  } else {
    player.frames =7;
  }
  if (player.up==true){
    if (player.big) {player.sprite =idleu;}
    else {
    player.sprite = idleusmall;
    }
  }
}
void update() {
  switch (screen) {
    case Screen::Title:
      animate();
      playerInput();
      updateSprite();
      


      break;

    case Screen::Game:
      
      break;

   
    case Screen::Gallery:

      break;

    
    case Screen::Gameover:
      
      if (arduboy.justPressed(A_BUTTON)) {
        screen = Screen::Title;
      }
      if (arduboy.justPressed(B_BUTTON)) {
        screen = Screen::Game;
      }
      break;
  }
}


void render() {
  uint16_t currentPlane = arduboy.currentPlane();

  switch (screen) {
    case Screen::Title:
      arduboy.fillScreen(WHITE);

      if (currentPlane <= 0) {  //dark gray
      }

      if (currentPlane <= 1) {  //gray
      }

      if (currentPlane <= 2) {  //white
        arduboy.setCursor(0, 0);
        //arduboy.println("cutecat");
        
      }

      SpritesU::drawOverwriteFX(0, 0, test, FRAME(0));
      SpritesU::drawPlusMaskFX(player.x, player.y, player.sprite, FRAME(currentframe));
      
      break;

    case Screen::Game:
      

      
      break;

    
    case Screen::Gallery:

      break;

    case Screen::Gameover:

      break;
  }
}