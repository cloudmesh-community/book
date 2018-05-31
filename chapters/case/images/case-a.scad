module base(x,y,h, pos) {
       translate([0,0,pos])
          cube([x,y,h], 0);
}

module case_a(){
       x=20;
       y=10;
       h=1;

       base (x,y,h,0);
       base (x,y,h,2);
       base (x,y,h,10);
}

case_a();

