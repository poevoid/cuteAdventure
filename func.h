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
    if (player.big) {player.sprite =grayl;}
    else {
    player.sprite = graylsmall;
    }
  } else if (player.left && arduboy.pressed(LEFT_BUTTON)){
    if (player.big) {player.sprite =graywalkleft;}
    else {
      player.sprite = graywalkleftsmall;
    }
  }
  if (player.right){
    if (player.big) {player.sprite =grayr;}
    else {
    player.sprite = grayrsmall;
    }
  }
  if (player.down && !arduboy.pressed(DOWN_BUTTON)){
    if (player.big) {player.sprite =grayf;}
    else {
    player.sprite = grayfsmall;
    }
  } else if (player.down && arduboy.pressed(DOWN_BUTTON)){
    if (player.big) {player.sprite =graywalkf;}
    else {
    player.sprite = graywalkfsmall;
    }
  }
  if (player.sprite == graywalkfsmall || player.sprite == graywalkf || player.sprite == graywalkleft || player.sprite == graywalkleftsmall){
    player.frames = 9;
  } else {
    player.frames =7;
  }
  if (player.up==true){
    if (player.big) {player.sprite =grayu;}
    else {
    player.sprite = grayusmall;
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
        arduboy.println("cutecat");
        
      }

      
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