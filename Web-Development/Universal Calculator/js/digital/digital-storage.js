/*Elements */
/*
1 byte = 8 bits
1 kilobyte (K / Kb) = 2^10 bytes = 1,024 bytes
1 megabyte (M / MB) = 2^20 bytes = 1,048,576 bytes
1 gigabyte (G / GB) = 2^30 bytes = 1,073,741,824 bytes
1 terabyte (T / TB) = 2^40 bytes = 1,099,511,627,776 bytes
1 petabyte (P / PB) = 2^50 bytes = 1,125,899,906,842,624 bytes
1 exabyte (E / EB) = 2^60 bytes = 1,152,921,504,606,846,976 bytes

*/
var bit_element = document.getElementById("bit");
var byte_element = document.getElementById("byte");
var kb_element = document.getElementById("kb");
var mb_element = document.getElementById("mb");
var gb_element = document.getElementById("gb");
var tb_element = document.getElementById("tb");
var pt_element = document.getElementById("pb");
var exa_element = document.getElementById("eb");
var zb_element = document.getElementById("zb");
var yb_element = document.getElementById("yb");
function FromBitToOther(bit){
    bit = parseFloat(bit);
    byte_element.value = bit*0.125;
    kb_element.value = bit*0.0001220703125;
    mb_element.value = bit*1.1920928955078125e-7;
    gb_element.value = bit*1.1641532182693481e-10;
    tb_element.value = bit*1.1368683772161603e-13;
    pt_element.value = bit*1.1102230246251565e-16;
    exa_element.value = bit* 6.938893903907228e-18;
    zb_element.value = bit*6.776263578034403e-21;
    yb_element.value = bit*6.617444900424222e-24;
}

function FromByteToOther(byte){
    byte = parseFloat(byte);
    bit_element.value = byte*8;
    kb_element.value =  byte*0.0009765625;
    mb_element.value =  byte*9.5367431640625e-7;
    gb_element.value =  byte*9.313225746154785e-10;
    tb_element.value =  byte*9.094947017729282e-13;
    pt_element.value =  byte*8.881784197001252e-16;
    exa_element.value = byte*8.673617379884035e-19;
    zb_element.value = byte*8.470329472543003e-22;
    yb_element.value = byte*8.271806125530277e-25;
}
function fromKbToOther(kb){
    kb = parseFloat(kb);
    byte_element.value =kb*8192;
    bit_element.value = kb*1024;
    mb_element.value =  kb*0.0009765625;
    gb_element.value =  kb*9.5367431640625e-7;
    tb_element.value =  kb*9.313225746154785e-10;
    pt_element.value =  kb*9.094947017729282e-13;
    exa_element.value = kb*8.881784197001252e-16;
    zb_element.value = kb*8.673617379884035e-19;
    yb_element.value = kb*8.470329472543003e-22;
}
function fromMbToOthers(mb){
    mb = parseFloat(mb);
    kb_element.value =   mb*1024;
    byte_element.value = mb*1048576;
    bit_element.value =  mb* 8388608;
    
    gb_element.value =  mb*0.0009765625;
    tb_element.value =  mb*9.5367431640625e-7;
    pt_element.value =  mb*9.313225746154785e-10;
    exa_element.value = mb*9.094947017729282e-13;
    zb_element.value = mb*8.881784197001252e-16;
    yb_element.value = mb*8.673617379884035e-19;
}
function fromGbToOther(gb){
    gb = parseFloat(gb);
    mb_element.value =  gb*1024;
    kb_element.value =  gb*1048576;
    byte_element.value =gb*1073741824;
    bit_element.value = gb*85899345592;
    tb_element.value =  gb*0.0009765625;
    pt_element.value =  gb*9.5367431640625e-7;
    exa_element.value = gb*9.313225746154785e-10;
    zb_element.value = gb*9.094947017729282e-13;
    yb_element.value = gb*8.881784197001252e-16;
}

function fromTbToOther(tb){
    tb = parseFloat(tb);
    mb_element.value =  tb*1048576;
    kb_element.value =  tb*1073741824;
    byte_element.value =tb*1099511627776;
    bit_element.value = tb*8796093022208;
    gb_element.value =  tb*1024;
    pt_element.value =  tb*0.0009765625;
    exa_element.value = tb*9.5367431640625e-7;
    zb_element.value = tb*9.313225746154785e-10;
    yb_element.value = tb*9.094947017729282e-13;
}
function fromPbToOthers(pb){
    pb = parseFloat(pb);
    tb_element.value =  pb*1024;
    mb_element.value =  pb*1073741824;
    kb_element.value =  pb*1099511627776;
    byte_element.value =pb*1125899906842624;
    bit_element.value = pb*9007199254740992;
    gb_element.value =  pb*1048576;
    exa_element.value = pb*0.0009765625;
    zb_element.value = pb*9.5367431640625e-7;
    yb_element.value = pb*9.313225746154785e-10;
}
function fromEbToOthers(eb){
    eb = parseFloat(eb);
    tb_element.value =  eb*1048576;
    mb_element.value =  eb*1099511627776;
    kb_element.value =  eb*1125899906842624;
    byte_element.value =eb*1152921504606847000;
    bit_element.value = eb*9223372036854776000;
    gb_element.value =  eb*1073741824;
    pt_element.value =  eb*1024;
    zb_element.value = eb*0.0009765625;
    yb_element.value = eb*9.5367431640625e-7;
}
function fromZbToOthers(zb){
    zb = parseFloat(zb);
    tb_element.value =  zb*1073741824;
    mb_element.value =  zb*1125899906842624;
    kb_element.value =  zb*1152921504606847000;
    byte_element.value =zb*1.1805916207174113e+21;
    bit_element.value = zb*9.44473296573929e+21;
    gb_element.value =  zb*1099511627776;
    pt_element.value =  zb*1048576;
    exa_element.value =  zb*1024;
    yb_element.value =  zb*0.0009765625;
}
function fromYbToOthers(yb){
    yb = parseFloat(yb);
    tb_element.value =  yb*1099511627776;
    mb_element.value =  yb*1152921504606847000;
    kb_element.value =  yb*1.1805916207174113e+21;
    byte_element.value =yb*1.2089258196146292e+24;
    bit_element.value = yb*9.671406556917033e+24;
    gb_element.value =  yb*1125899906842624;
    pt_element.value =  yb*1073741824;
    exa_element.value =  yb*1048576;
    zb_element.value =  yb*1024;
}