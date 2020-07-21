function setup() {
  createCanvas(400, 400);
  angleMode(DEGREES);
}

function draw() {
  background(255,200,200);
  translate(200, 200);
  rotate(-90);


  let hr = hour();
  let mn = minute();
  let sc = second();
  

  strokeWeight(8);
  stroke(255, 100, 150);
  noFill();
  let secondAngle = map(sc, 0, 60, 0, 360);

  stroke(150, 100, 255);
  let minuteAngle = map(mn, 0, 60, 0, 360);

  stroke(150, 255, 100);
  let hourAngle = map(hr % 12, 0, 12, 0, 360);

  push();
  rotate(secondAngle);
  strokeWeight (3)
  stroke('hsb(160, 100%, 50%)');
  line(0, 0, 140, 0);
  pop();
  

  push();
  rotate(minuteAngle);
  strokeWeight (8)
  stroke(50, 55, 100);
  line(0, 0, 100, 0);
  pop();

  push();
  rotate(hourAngle);
  strokeWeight (12)
  stroke(2255, 204, 0);
  line(0, 0, 80, 0);
  pop();

  stroke(255);
  point(0, 0);

  strokeWeight (10);
  stroke (255);
  noFill();
  ellipse (0,0,325,325);
  
}
