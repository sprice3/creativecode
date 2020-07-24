let x;
let y;

let xspeed;
let yspeed;

let dvd;

let r, g, b;

function preload() {
  dvd = loadImage("hulu.png");
}


function setup() {
  createCanvas(800, 600);
  x = random(width);
  y = random(height);
  xspeed = 3;
  yspeed = 3;
  pickColor();
}

function pickColor() {
  r = random(100, 256);
  g = random(100, 256);
  b = random(100, 256);

}

function draw() {
  background(0);
  // rect(x, y, 80, 60);
  // Draw the DVD logo
  tint(r, g, b);
  image(dvd, x, y);


  x = x + xspeed;
  y = y + yspeed;

  if (x + dvd.width >= width) {
    xspeed = -xspeed;
    x = width - dvd.width;
    pickColor();
  } else if (x <= 0) {
    xspeed = -xspeed;
    x = 0;
    pickColor();
  }

  if (y + dvd.height >= height) {
    yspeed = -yspeed;
    y = height - dvd.height;
    pickColor();
  } else if (y <= 0) {
    yspeed = -yspeed;
    y = 0;
    pickColor();
  }
}
