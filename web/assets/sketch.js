let mx = 0;
let my = 0;
let img;

function getUrlVars()
{
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++)
    {
        hash = hashes[i].split('=');
        //vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}

function setup() {
  createCanvas(400, 400);
  src = "assets/map.png";
  origsrc = src;
  
  param = getUrlVars();
  // alert(param['keyword']);
  if ('keyword' in  param)
    src = "assets/" + param['keyword'] + ".png";

  console.log(src);
  img = loadImage(src);
  // if (img.pixels.length == 0) {
  //   img = loadImage(origsrc);
  //   console.log("Loading backup image");
  // }
}

function draw() {
  background(220);
  image(img, 0, 0);
  fill(255, 0, 0);
  circle(mx, my - 21, 10);
  line(mx, my - 16, mx, my);
}

function doubleClicked() {
  mx = mouseX;
  my = mouseY;

  httpPost("setOrigin", 'json', {mx: mx, my: my}, function(data) {
    console.log("setGrid");
    console.log(data);
  });
}
