//------------------------------------------------------------------------
// OpenSCAD models of miscellaneous components and devices:
// various berry Pi models, SainSmart Relays, PCD8544 LCD, etc.
//
// Author:      Niccolo Rigacci <niccolo@rigacci.org>
// Version:     1.0 2017-12-14
// License:     GNU General Public License v3.0
//------------------------------------------------------------------------

include <misc_parts.scad>;

// Interference for 3D union(), difference() and intersection();
// used to avoid the manifold problem.
interf = 0.1;

//------------------------------------------------------------------------
// Matrix of 2.54 mm pins.
//------------------------------------------------------------------------
module pin_headers(cols, rows) {
    w = 2.54; h = 2.54; p = 0.65;
    for(x = [0 : (cols -1)]) {
        for(y = [0 : (rows  - 1)]) {
            translate([w * x, w * y, 0]) {
                union() {
                    color("black") cube([w, w, h]);
                    color("gold")  translate([(w - p) / 2, (w - p) / 2, -3]) cube([p, p, 11.54]);
                }
            }
        }
    }
}

//------------------------------------------------------------------------
// Sub-models for the Raspberry Pi Models
//------------------------------------------------------------------------
module video_rca() {
    x = 10; y = 9.8; z = 13;
    d = 8.3; h = 9.5;
    color("yellow") cube([x, y, z]);
    translate([-h, y / 2, (d / 2) + 4])
        rotate(a=90, v=[0, 1, 0])
            color("silver") cylinder(r=(d / 2), h=h);
}
module audio_jack() {
    x = 11.4; y = 12; z = 10.2;
    d = 6.7; h = 3.4;
    color("blue") cube([x, y, z]);
    translate([-h, y / 2, (d / 2) + 3])
        rotate(a=90, v=[0, 1, 0])
            color("blue") cylinder(r=(d / 2), h=h);
}
module ethernet_connector(x, y, z) {
    color("silver") cube([x, y, z]);
}
module usb_connector(x, y, z) {
    f = 0.6; // Flange
    color("silver") cube([x, y, z]);
    translate([-f, y - f, -f])
        color("silver") cube([x + f * 2, f, z + f * 2]);
}
module hdmi_connector(x, y, z) {
    color("silver") cube([x, y, z]);
}
module microusb_connector(x, y, z) {
    color("silver") cube([x, y, z]);
}
module capacitor(d, h) {
    color("silver") cylinder(r=(d / 2), h=h);
}
module micro_sd_card() {
    color("silver")   translate([0,  0.0, -1.5]) cube([14, 13, 1.5]);
    color("darkblue") translate([2, -3.2, -1.0]) cube([11, 15, 1.0]);
}
module audio_video(size_x) {
    color([58/255, 58/255, 58/255]) {
        cube([size_x, 7, 5.6]);
        translate([size_x, 7 / 2, 5.6 / 2]) rotate([0,90,0]) cylinder(d=5.6, h=2.6);
    }
}



//------------------------------------------------------------------------
// Raspberry Pi 3 Model B v.1.2.
//------------------------------------------------------------------------
module board_raspberrypi_3_model_b() {
    x  = 56;     y = 85;    z = 1.60;  // Measured PCB size
    ex = 15.9; ey = 21.5; ez = 13.5;   // Ethernet measure
    ux = 13.1; uy = 17.1; uz = 15.5;   // Measured USB connector size
    hx = 11.40; hy = 15.1; hz = 6.15;  // Measured HDMI connector size
    mx =  5.60; my =  7.6; mz = 2.40;  // Measured micro USB power connector size
    // The origin is the lower face of PCB.
    translate([0, 0, z]) {
        translate([1.0, 7.1, 0])                    pin_headers(2, 20);
        translate([x - ex - 2.3, y - ey + 2.1, 0])  ethernet_connector(ex, ey, ez);
        translate([ 2.5, 85 - uy + 2.1, 0])         usb_connector(ux, uy, uz);
        translate([20.5, 85 - uy + 2.1, 0])         usb_connector(ux, uy, uz);
        translate([x - hx + 1.8, 25, 0])            hdmi_connector(hx, hy, hz);
        translate([x - 12.8, 50, 0])                audio_video(12.8);
        translate([20.5, 0.8, -z])                  micro_sd_card();
        translate([x - mx + 1, 7, 0])               microusb_connector(mx, my, mz);
        translate([x + 2.2, 10.55, 1.2])            rotate(a=270, v=[0, 0, 1]) usb_male_micro_b_connector();
        translate([0, 0, -z]) {
            color("green") linear_extrude(height=z)
                difference() {
                    hull() {
                        translate([  3,   3]) circle(r=3);
                        translate([x-3,   3]) circle(r=3);
                        translate([x-3, y-3]) circle(r=3);
                        translate([  3, y-3]) circle(r=3);
                    }
                    raspberrypi_3_model_b_holes();
                }
        }
    }
}

//------------------------------------------------------------------------
// Holes for Raspberry Pi 3 Model B v.1.2.
//------------------------------------------------------------------------
module raspberrypi_3_model_b_holes() {
    x = 56;
    translate([3.5, 3.5])            circle(r=(2.75 / 2), $fn=16);
    translate([(x - 3.5), 3.5])      circle(r=(2.75 / 2), $fn=16);
    translate([3.5, 3.5 + 58])       circle(r=(2.75 / 2), $fn=16);
    translate([(x - 3.5), 3.5 + 58]) circle(r=(2.75 / 2), $fn=16);
}

module network(){
    // 114 x 86 x 26 mm
    // https://www.amazon.com/NETGEAR-Ethernet-Unmanaged-Internet-Splitter/dp/B00KFD0SEA/ref=pd_cp_147_1?_encoding=UTF8&pd_rd_i=B00KFD0SEA&pd_rd_r=07d8d6d0-6545-11e8-884b-f548ab926653&pd_rd_w=twuai&pd_rd_wg=KWnuX&pf_rd_i=desktop-dp-sims&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=80460301815383741&pf_rd_r=7HRPGYWCB196SF54SYQV&pf_rd_s=desktop-dp-sims&pf_rd_t=40701&psc=1&refRID=7HRPGYWCB196SF54SYQV&dpID=316sFs-UFNL&preST=_SX300_QL70_&dpSrc=detail
    color("silver") cube([114,86,26]);
}

module pibank (x,y){
for (j=[0:y-1]) {
    for (i=[0:x-1]) {
         translate([i*(56 + 25), 0, j*20]) board_raspberrypi_3_model_b();
    }
}
}

// for (b=[0:4]) {

//translate([0,0, (5 * 20 + 20) * b]) pibank(5, 5);

//}

module powerplug() {
    color("grey") cube(10 * 2.54 * [3.9, 2.8, 1]);
}
network();
translate ([0,0, 40]) powerplug();
translate ([0,0, 80]) board_raspberrypi_3_model_b();