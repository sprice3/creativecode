let x;
let y;

let xspeed; 
let yspeed;

let logo;

function preload() {
  logo = loadImage ("netflix-logo-circle-png-5.png");
}

function setup() {
  createCanvas(800, 600);
  x = 400;
  y = 300;
  xspeed = 3;
  yspeed = 3;
}

function draw() {
  background(0);
  // rect(x, y, 80, 60);
  image(logo, x, y, 200, 150);
  
  x = x + xspeed + 1;
  y = y + yspeed + 1;
  
  if (x + 200 == width || x == 0) {
    xspeed = xspeed * -1;
  }
  
  if (y + 120 == height || y == 0){
    yspeed = yspeed * -1;
  }

}
