var py = 0
var d = 0
var ps = 0
var x = 250
var y = 250
var pu, pd, cy = 70
var xa = (Math.random() + 0.3) * 10
var ya = (Math.random() + 0.3) * 10
var intel = Math.floor(Math.random() * 100)
var t = 400
function physics(){
  if (collideRectCircle(5, py, 10, 140, x, y, 20)){
    x = 26
    xa *= -1
    intel = Math.floor(Math.random() * 100)
    console.log(intel)
  }
  if (collideRectCircle(485, cy, 10, 140, x, y, 20)){
    x = 474
    xa *= -1
    t = 400
  }
  if (x > t){

    if (intel > 60){
      cy = y
    }
    
  }
  if (x > 500 || x < 0){xa *= -1}
  if (y > 500 || y < 0){ya *= -1}

}
function setup(){
  createCanvas(500, 500)
}
function draw(){
  physics()
  background(0)
  var c = color(255)
  fill(c)
  noStroke()
  if (keyIsDown(DOWN_ARROW)){
    pd = true
    pu = false
  }
  else if (keyIsDown(UP_ARROW)){
    pu = true
    pd = false
  }
  else{pu = false; pd = false}
  if(pu){py -= 10}
  else if (pd){py += 10}
  
  rect(5, py, 10, 140) //Player's paddle
  c = color(255)
  fill(c)
  noStroke()
  ellipse(x, y, 20, 20) //Ball
  c = color(255)
  fill(c)
  noStroke()
  rect(485, cy - 70, 10, 140) //computer's paddle
  x += xa
  y += ya
}