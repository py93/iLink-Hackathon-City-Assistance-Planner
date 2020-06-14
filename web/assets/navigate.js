let mx = 100;
let my = 100;
let dx = 300;
let dy = 300;
let list = [
  // {a: [100, 100], b:[150, 100]},
  // {a: [150, 100], b:[90, 200]},
  // {a: [90, 200], b:[300, 250]},
  // {a: [300, 250], b:[300, 300]},
  {a: [100, 100], b:[300, 300]}
];
let img;

function setup() {
  createCanvas(400, 400);
  img = loadImage('assets/map.png');
}

function draw() {
  background(220);
  image(img, 0, 0);
  plotMarker(mx, my);
  plotMarker(dx, dy);

  stroke(0, 0, 250);
  for (el of list) {
    line(el.a[0], el.a[1], el.b[0], el.b[1]);
  }
}

function plotMarker(x, y) {
    stroke(0, 0, 0);
    fill(255, 0, 0);
    circle(x, y - 21, 10);
    line(x, y - 16, x, y);
}

function updateView(data) {
  if (data != null)
  {
    mx = data["dest"][0];
    my = data["dest"][1];
    dx = data["orig"][0];
    dy = data["orig"][1];
    list = data["path"];

    console.log("Updating Nav view");
    console.log(data);
  }
  console.log("null Nav data");
}
