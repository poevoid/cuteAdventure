#pragma once

/**** FX data header generated by fxdata-build.py tool version 1.15 ****/

using uint24_t = __uint24;

// Initialize FX hardware using  FX::begin(FX_DATA_PAGE); in the setup() function.

constexpr uint16_t FX_DATA_PAGE  = 0xfcdb;
constexpr uint24_t FX_DATA_BYTES = 201824;

constexpr uint16_t FX_SAVE_PAGE  = 0xfff0;
constexpr uint24_t FX_SAVE_BYTES = 2;

constexpr uint24_t dpad = 0x000000;
constexpr uint24_t abutton = 0x000182;
constexpr uint24_t bbutton = 0x0001E4;
constexpr uint24_t catg = 0x000246;
constexpr uint24_t graylsmall = 0x000848;
constexpr uint24_t grayusmall = 0x00204A;
constexpr uint24_t grayfsmall = 0x00384C;
constexpr uint24_t graywalkfsmall = 0x00504E;
constexpr uint24_t grayrsmall = 0x006E50;
constexpr uint24_t graywalkleftsmall = 0x008652;
constexpr uint24_t grayl = 0x00A454;
constexpr uint24_t grayu = 0x010456;
constexpr uint24_t graywalkf = 0x016458;
constexpr uint24_t graywalkleft = 0x01DC5A;
constexpr uint24_t grayr = 0x02545C;
constexpr uint24_t grayf = 0x02B45E;