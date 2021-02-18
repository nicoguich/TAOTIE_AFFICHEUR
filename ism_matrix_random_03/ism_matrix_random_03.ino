// Demo the quad alphanumeric display LED backpack kit
// scrolls through every character, then scrolls Serial
// input onto the display


//"perio/", "petro/", "phallo/", "phantasma/", "photo/", "pico/", "pluri/", "politico/", "poly/", "posterio/", "pan/", 
//"pana/", "porno/", "post/", "pre/", "pro/", "proto/", "pseudo/", "psycho/", "pyro/" , "radio/", "retro/", "rhizo/", "russo/" , "sacro/", "scato/", "schyzo/", "seleno/", 
//"semi/", "semio/", "sexo/", "sidero/", "sino/", "slavo/", "socio/", "sono/", "sovieto/", "spatio/", "spectro/", "speleo/", "sphero/", "stereo/", "super/", "subordi/",
//"tauto/", "tele/", "techno/", "telo/", "tera/", "terato/", "theo/", "toxico/", "topo/", "trans/", "traumato/", "troglo/", "typo/", "tyranno/", "ultra/" , "uni/" ,
//"utero/" , "veloci/", "vita/" , "xeno/" ,"zoo/"

//"Capitalism/1","economism/2","evolutionnism/1","Commercialism/1","Consumerism/1","Toyotism/1","Pointillism/1","Populism/1","Primitivism/1",
//"Purism/1", "Rayonnism/","Realism/1","Regionalism/","Romantism/1","Spatialism/1","Suprematism/1","Surrealism/","Symbolism/1","Ultraism/1",
//"Vedutism/1","Academism/1", "Brutalism/1" ,"Classicism/1", "Confessionnalism/",
//"Constructivism/1", "Conism/","Cubism/1",  "Dadaism/1","Doudouism/","Elginism/","Esthetism/1", "Exotism/1","Expressionnism/","Facadism/","Fauvism/1","Futurism/2",
//"Graphism/","Imagism/","Impressionnism/1","Indigenism/","Jdanovism/","Lettrism/","Lyrism/1","Manierism/1", "Minimalism/1", "Modernism/1","Muralism/","Naturalism/1",
//"logism/", "plasticism/","Objectivism/","Orientalism/1","Orphism/"








#include <Wire.h>
#include <Adafruit_GFX.h>
#include "Adafruit_LEDBackpack.h"
#include <ctype.h>

Adafruit_AlphaNum4 alpha4_1 = Adafruit_AlphaNum4();
Adafruit_AlphaNum4 alpha4_2 = Adafruit_AlphaNum4();
Adafruit_AlphaNum4 alpha4_3 = Adafruit_AlphaNum4();
Adafruit_AlphaNum4 alpha4_4 = Adafruit_AlphaNum4();
Adafruit_AlphaNum4 alpha4_5 = Adafruit_AlphaNum4();
Adafruit_AlphaNum4 alpha4_6 = Adafruit_AlphaNum4();
Adafruit_AlphaNum4 alpha4_7 = Adafruit_AlphaNum4();
int index_pre=0,index_post=0,limit_pre, limit_post, total_pre, total_post;

String prefix[]={"afro/1", "alter/2", "andro/1", "ante/1", "anthropo/1", "anti/1", "apo/1", "archeo/1", "archi/1", "auto/1", 
"anarcho/1", "aristo/1", "bi/1", "chromato/1", "chrono/1", "claustro/1", "cosmo/1", "cranio/1", "crypto/1", "demi/1", "demono/1",
"dys/1", "deca/1", "electro/1", "eroto/1", "ethno/1", "ex/1", "exa/1", "exo/1", "extra/1", "euro/1", "franco/1" , "galacto/1", "gallo/1",
"genito/1", "geo/1", "germano/1", "geronto/1", "giga/1", "grapho/1", "greco/1", "gyneco/1","hagio/1", "hetero/1", "hexa/1", "hira/1", "hispano/1",
"histo/1", "historio/1", "holo/1", "homeo/1", "horo/1", "hyper/1", "hypo/1", "hypso/1", "hystero/1","icono/1", "ideo/1", "infra/1", "inter/1", "intra/1", "iso/1", 
 "maxi/1", "mecano/", "medico/", "megalo/1", "meta/", "micro/1", "mini/1", 
 "miso/1", "mono/1", "morpho/", "multi/1", "museo/1", "mytho/1" ,"nano/1", "necro/1", "neuro/1", "nippo/1", "nympho/1", "neo/1","oligo/", "omni/1", "oniro/1", "onto/1", "organo/1",
"para/1", "parasito/1", "patho/1", "pedo/1"};

String postfix[]={"Capitalism/1","economism/1","evolutionnism/1","Commercialism/1","Consumerism/1","Toyotism/1","Pointillism/1","Populism/1","Primitivism/1",
"Purism/1","Realism/1","Regionalism/","Romantism/1","Spatialism/1","Suprematism/1","Surrealism/","Symbolism/1","Ultraism/1",
"Vedutism/1","Academism/1", "Brutalism/1" ,"Classicism/1",
"Constructivism/1", "Cubism/1",  "Dadaism/1","Esthetism/1", "Exotism/1","Expressionnism/","Fauvism/1","Futurism/2",
"Impressionnism/1","Lyrism/1","Manierism/1", "Minimalism/1", "Modernism/1","Naturalism/1",
"Orientalism/1"};





int prefix_prob[sizeof(prefix) / sizeof(prefix[0])];
int postfix_prob[sizeof(postfix) / sizeof(postfix[0])];

String newprefix[1000];
String newpostfix[1000];

int ;

void setup() {
  Serial.begin(9600);

 
 alpha4_1.begin(0x70);  // pass in the address
 alpha4_2.begin(0x71);  // pass in the address
 alpha4_3.begin(0x72);  // pass in the address
 alpha4_4.begin(0x73);  // pass in the address
 alpha4_5.begin(0x74);  // pass in the address
 alpha4_6.begin(0x75);  // pass in the address
 alpha4_7.begin(0x76);  // pass in the address




for (int x=0;x<sizeof(prefix) / sizeof(prefix[0]);x++){
  int index_prob=0;
  int temp_prob[6];
  for (int i=0;i<6;i++){
    temp_prob[i]=0;
  }
  prefix_prob[x]=0;
for (int y=0;y<sizeof(prefix[x]) / sizeof(prefix[x][0]);y++){
if (isDigit(prefix[x][y])) {

temp_prob[index_prob]= int(prefix[x][y])-'0';
index_prob++;
}

}
int index_pow=0;
for (int j=index_prob-1;j>-1;j--){
  if (j!=index_prob-1){
prefix_prob[x]=prefix_prob[x]+((temp_prob[j]*(pow(10,index_pow))));}
else{

  prefix_prob[x]=temp_prob[j];
}
index_pow++;

}


}


total_pre=0;
int index_newpre=0;
for (int x=0;x < sizeof(prefix) / sizeof(prefix[0]);x++){


if (prefix_prob[x]>0){
for (int y=0;y<prefix_prob[x];y++){

newprefix[index_newpre]= prefix[x];
  index_newpre++;
  total_pre++;
}
  
}

  
}





for (int x=0;x<sizeof(postfix) / sizeof(postfix[0]);x++){
  int index_prob=0;
  int temp_prob[6];
  for (int i=0;i<6;i++){
    temp_prob[i]=0;
  }
  postfix_prob[x]=0;
for (int y=0;y<sizeof(postfix[x]) / sizeof(postfix[x][0]);y++){
if (isDigit(postfix[x][y])) {

temp_prob[index_prob]= int(postfix[x][y])-'0';
index_prob++;
}

}
int index_pow=0;
for (int j=index_prob-1;j>-1;j--){
  if (j!=index_prob-1){
postfix_prob[x]=postfix_prob[x]+((temp_prob[j]*(pow(10,index_pow))));}
else{

  postfix_prob[x]=temp_prob[j];
}
index_pow++;

}


}


total_post=0;
int index_newpost=0;
for (int x=0;x < sizeof(postfix) / sizeof(postfix[0]);x++){


if (postfix_prob[x]>0){
for (int y=0;y<postfix_prob[x];y++){

newpostfix[index_newpost]= postfix[x];
  index_newpost++;
  total_post++;
}
  
}

  
}











for (int x=0;x<total_post;x++){
  Serial.print (x);
    Serial.print ("  ");
Serial.println(newpostfix[x]);
}
Serial.println();Serial.println();Serial.println();Serial.println();Serial.println();
for (int x=0;x<total_pre;x++){
  Serial.print (x);
    Serial.print ("  ");
Serial.println(newprefix[x]);



}



}




void loop() {



  alpha4_1.clear();
    alpha4_2.clear();
      alpha4_3.clear();
        alpha4_4.clear();
          alpha4_5.clear();
            alpha4_6.clear();
              alpha4_7.clear();




index_pre=int(random(total_pre));
index_post=int(random(total_post));




for (int x=0;x<sizeof(newprefix[index_pre]) / sizeof(newprefix[index_pre][0]);x++){
  

if (newprefix[index_pre][x]=='/'){

limit_pre=x;

break;
  
}
}


switch (limit_pre){

case 0:
alpha4_1.writeDigitRaw(0, 0x0);
alpha4_1.writeDigitRaw(1, 0x0);
alpha4_1.writeDigitRaw(2, 0x0);
alpha4_1.writeDigitRaw(3, 0x0);
alpha4_2.writeDigitRaw(0, 0x0);
alpha4_2.writeDigitRaw(1, 0x0);
alpha4_2.writeDigitRaw(2, 0x0);
alpha4_2.writeDigitRaw(3, 0x0);
break;


case 1:
alpha4_1.writeDigitRaw(0, 0x0);
alpha4_1.writeDigitRaw(1, 0x0);
alpha4_1.writeDigitRaw(2, 0x0);
alpha4_1.writeDigitRaw(3, 0x0);
alpha4_2.writeDigitRaw(0, 0x0);
alpha4_2.writeDigitRaw(1, 0x0);
alpha4_2.writeDigitRaw(2, 0x0);
alpha4_2.writeDigitAscii(3, toupper(newprefix[index_pre][0]));
break;


case 2:
alpha4_1.writeDigitRaw(0, 0x0);
alpha4_1.writeDigitRaw(1, 0x0);
alpha4_1.writeDigitRaw(2, 0x0);
alpha4_1.writeDigitRaw(3, 0x0);
alpha4_2.writeDigitRaw(0, 0x0);
alpha4_2.writeDigitRaw(1, 0x0);
alpha4_2.writeDigitAscii(2, toupper(newprefix[index_pre][0]));
alpha4_2.writeDigitAscii(3, toupper(newprefix[index_pre][1]));
break;



case 3:
alpha4_1.writeDigitRaw(0, 0x0);
alpha4_1.writeDigitRaw(1, 0x0);
alpha4_1.writeDigitRaw(2, 0x0);
alpha4_1.writeDigitRaw(3, 0x0);
alpha4_2.writeDigitRaw(0, 0x0);
alpha4_2.writeDigitAscii(1, toupper(newprefix[index_pre][0]));
alpha4_2.writeDigitAscii(2, toupper(newprefix[index_pre][1]));
alpha4_2.writeDigitAscii(3, toupper(newprefix[index_pre][2]));
break;



case 4:
alpha4_1.writeDigitRaw(0, 0x0);
alpha4_1.writeDigitRaw(1, 0x0);
alpha4_1.writeDigitRaw(2, 0x0);
alpha4_1.writeDigitRaw(3, 0x0);
alpha4_2.writeDigitAscii(0, toupper(newprefix[index_pre][0]));
alpha4_2.writeDigitAscii(1, toupper(newprefix[index_pre][1]));
alpha4_2.writeDigitAscii(2, toupper(newprefix[index_pre][2]));
alpha4_2.writeDigitAscii(3,toupper( newprefix[index_pre][3]));
break;


case 5:
alpha4_1.writeDigitRaw(0, 0x0);
alpha4_1.writeDigitRaw(1, 0x0);
alpha4_1.writeDigitRaw(2, 0x0);
alpha4_1.writeDigitAscii(3, toupper(newprefix[index_pre][0]));
alpha4_2.writeDigitAscii(0, toupper(newprefix[index_pre][1]));
alpha4_2.writeDigitAscii(1, toupper(newprefix[index_pre][2]));
alpha4_2.writeDigitAscii(2, toupper(newprefix[index_pre][3]));
alpha4_2.writeDigitAscii(3, toupper(newprefix[index_pre][4]));
break;



case 6:
alpha4_1.writeDigitRaw(0, 0x0);
alpha4_1.writeDigitRaw(1, 0x0);
alpha4_1.writeDigitAscii(2, toupper(newprefix[index_pre][0]));
alpha4_1.writeDigitAscii(3, toupper(newprefix[index_pre][1]));
alpha4_2.writeDigitAscii(0, toupper(newprefix[index_pre][2]));
alpha4_2.writeDigitAscii(1, toupper(newprefix[index_pre][3]));
alpha4_2.writeDigitAscii(2, toupper(newprefix[index_pre][4]));
alpha4_2.writeDigitAscii(3, toupper(newprefix[index_pre][5]));
break;



case 7:
alpha4_1.writeDigitRaw(0, 0x0);
alpha4_1.writeDigitAscii(1, toupper(newprefix[index_pre][0]));
alpha4_1.writeDigitAscii(2, toupper(newprefix[index_pre][1]));
alpha4_1.writeDigitAscii(3, toupper(newprefix[index_pre][2]));
alpha4_2.writeDigitAscii(0, toupper(newprefix[index_pre][3]));
alpha4_2.writeDigitAscii(1, toupper(newprefix[index_pre][4]));
alpha4_2.writeDigitAscii(2, toupper(newprefix[index_pre][5]));
alpha4_2.writeDigitAscii(3, toupper(newprefix[index_pre][6]));
break;



case 8:
alpha4_1.writeDigitAscii(0, toupper(newprefix[index_pre][0]));
alpha4_1.writeDigitAscii(1, toupper(newprefix[index_pre][1]));
alpha4_1.writeDigitAscii(2, toupper(newprefix[index_pre][2]));
alpha4_1.writeDigitAscii(3, toupper(newprefix[index_pre][3]));
alpha4_2.writeDigitAscii(0, toupper(newprefix[index_pre][4]));
alpha4_2.writeDigitAscii(1, toupper(newprefix[index_pre][5]));
alpha4_2.writeDigitAscii(2, toupper(newprefix[index_pre][6]));
alpha4_2.writeDigitAscii(3, toupper(newprefix[index_pre][7]));
break;
}









for (int x=0;x<sizeof(newpostfix[index_post]) / sizeof(newpostfix[index_post][0]);x++){

if (newpostfix[index_post][x]=='/'){
 
limit_post=x;

break;

}
}


switch (limit_post){

case 0:
alpha4_3.writeDigitRaw(0, 0x0);
alpha4_3.writeDigitRaw(1, 0x0);
alpha4_3.writeDigitRaw(2, 0x0);
alpha4_3.writeDigitRaw(3, 0x0);
alpha4_4.writeDigitRaw(0, 0x0);
alpha4_4.writeDigitRaw(1, 0x0);
alpha4_4.writeDigitRaw(2, 0x0);
alpha4_4.writeDigitRaw(3, 0x0);
alpha4_5.writeDigitRaw(0, 0x0);
alpha4_5.writeDigitRaw(1, 0x0);
alpha4_5.writeDigitRaw(2, 0x0);
alpha4_5.writeDigitRaw(3, 0x0);
alpha4_6.writeDigitRaw(0, 0x0);
alpha4_6.writeDigitRaw(1, 0x0);
alpha4_6.writeDigitRaw(2, 0x0);
alpha4_6.writeDigitRaw(3, 0x0);
break;


case 1:
alpha4_3.writeDigitAscii(0, toupper(newpostfix[index_post][0]));
alpha4_3.writeDigitRaw(1, 0x0);
alpha4_3.writeDigitRaw(2, 0x0);
alpha4_3.writeDigitRaw(3, 0x0);
alpha4_4.writeDigitRaw(0, 0x0);
alpha4_4.writeDigitRaw(1, 0x0);
alpha4_4.writeDigitRaw(2, 0x0);
alpha4_4.writeDigitRaw(3, 0x0);
alpha4_5.writeDigitRaw(0, 0x0);
alpha4_5.writeDigitRaw(1, 0x0);
alpha4_5.writeDigitRaw(2, 0x0);
alpha4_5.writeDigitRaw(3, 0x0);
alpha4_6.writeDigitRaw(0, 0x0);
alpha4_6.writeDigitRaw(1, 0x0);
alpha4_6.writeDigitRaw(2, 0x0);
alpha4_6.writeDigitRaw(3, 0x0);
break;


case 2:
alpha4_3.writeDigitAscii(0, toupper(newpostfix[index_post][0]));
alpha4_3.writeDigitAscii(1, toupper(newpostfix[index_post][1]));
alpha4_3.writeDigitRaw(2, 0x0);
alpha4_3.writeDigitRaw(3, 0x0);
alpha4_4.writeDigitRaw(0, 0x0);
alpha4_4.writeDigitRaw(1, 0x0);
alpha4_4.writeDigitRaw(2, 0x0);
alpha4_4.writeDigitRaw(3, 0x0);
alpha4_5.writeDigitRaw(0, 0x0);
alpha4_5.writeDigitRaw(1, 0x0);
alpha4_5.writeDigitRaw(2, 0x0);
alpha4_5.writeDigitRaw(3, 0x0);
alpha4_6.writeDigitRaw(0, 0x0);
alpha4_6.writeDigitRaw(1, 0x0);
alpha4_6.writeDigitRaw(2, 0x0);
alpha4_6.writeDigitRaw(3, 0x0);
break;



case 3:
alpha4_3.writeDigitAscii(0, toupper(newpostfix[index_post][0]));
alpha4_3.writeDigitAscii(1, toupper(newpostfix[index_post][1]));
alpha4_3.writeDigitAscii(2, toupper(newpostfix[index_post][2]));
alpha4_3.writeDigitRaw(3, 0x0);
alpha4_4.writeDigitRaw(0, 0x0);
alpha4_4.writeDigitRaw(1, 0x0);
alpha4_4.writeDigitRaw(2, 0x0);
alpha4_4.writeDigitRaw(3, 0x0);
alpha4_5.writeDigitRaw(0, 0x0);
alpha4_5.writeDigitRaw(1, 0x0);
alpha4_5.writeDigitRaw(2, 0x0);
alpha4_5.writeDigitRaw(3, 0x0);
alpha4_6.writeDigitRaw(0, 0x0);
alpha4_6.writeDigitRaw(1, 0x0);
alpha4_6.writeDigitRaw(2, 0x0);
alpha4_6.writeDigitRaw(3, 0x0);
break;



case 4:
alpha4_3.writeDigitAscii(0, toupper(newpostfix[index_post][0]));
alpha4_3.writeDigitAscii(1, toupper(newpostfix[index_post][1]));
alpha4_3.writeDigitAscii(2, toupper(newpostfix[index_post][2]));
alpha4_3.writeDigitAscii(3, toupper(newpostfix[index_post][3]));
alpha4_4.writeDigitRaw(0, 0x0);
alpha4_4.writeDigitRaw(1, 0x0);
alpha4_4.writeDigitRaw(2, 0x0);
alpha4_4.writeDigitRaw(3, 0x0);
alpha4_5.writeDigitRaw(0, 0x0);
alpha4_5.writeDigitRaw(1, 0x0);
alpha4_5.writeDigitRaw(2, 0x0);
alpha4_5.writeDigitRaw(3, 0x0);
alpha4_6.writeDigitRaw(0, 0x0);
alpha4_6.writeDigitRaw(1, 0x0);
alpha4_6.writeDigitRaw(2, 0x0);
alpha4_6.writeDigitRaw(3, 0x0);
break;


case 5:
alpha4_3.writeDigitAscii(0, toupper(newpostfix[index_post][0]));
alpha4_3.writeDigitAscii(1, toupper(newpostfix[index_post][1]));
alpha4_3.writeDigitAscii(2, toupper(newpostfix[index_post][2]));
alpha4_3.writeDigitAscii(3, toupper(newpostfix[index_post][3]));
alpha4_4.writeDigitAscii(0, toupper(newpostfix[index_post][4]));
alpha4_4.writeDigitRaw(1, 0x0);
alpha4_4.writeDigitRaw(2, 0x0);
alpha4_4.writeDigitRaw(3, 0x0);
alpha4_5.writeDigitRaw(0, 0x0);
alpha4_5.writeDigitRaw(1, 0x0);
alpha4_5.writeDigitRaw(2, 0x0);
alpha4_5.writeDigitRaw(3, 0x0);
alpha4_6.writeDigitRaw(0, 0x0);
alpha4_6.writeDigitRaw(1, 0x0);
alpha4_6.writeDigitRaw(2, 0x0);
alpha4_6.writeDigitRaw(3, 0x0);
break;



case 6:
alpha4_3.writeDigitAscii(0, toupper(newpostfix[index_post][0]));
alpha4_3.writeDigitAscii(1, toupper(newpostfix[index_post][1]));
alpha4_3.writeDigitAscii(2, toupper(newpostfix[index_post][2]));
alpha4_3.writeDigitAscii(3, toupper(newpostfix[index_post][3]));
alpha4_4.writeDigitAscii(0, toupper(newpostfix[index_post][4]));
alpha4_4.writeDigitAscii(1, toupper(newpostfix[index_post][5]));
alpha4_4.writeDigitRaw(2, 0x0);
alpha4_4.writeDigitRaw(3, 0x0);
alpha4_5.writeDigitRaw(0, 0x0);
alpha4_5.writeDigitRaw(1, 0x0);
alpha4_5.writeDigitRaw(2, 0x0);
alpha4_5.writeDigitRaw(3, 0x0);
alpha4_6.writeDigitRaw(0, 0x0);
alpha4_6.writeDigitRaw(1, 0x0);
alpha4_6.writeDigitRaw(2, 0x0);
alpha4_6.writeDigitRaw(3, 0x0);
break;



case 7:
alpha4_3.writeDigitAscii(0, toupper(newpostfix[index_post][0]));
alpha4_3.writeDigitAscii(1, toupper(newpostfix[index_post][1]));
alpha4_3.writeDigitAscii(2, toupper(newpostfix[index_post][2]));
alpha4_3.writeDigitAscii(3, toupper(newpostfix[index_post][3]));
alpha4_4.writeDigitAscii(0, toupper(newpostfix[index_post][4]));
alpha4_4.writeDigitAscii(1, toupper(newpostfix[index_post][5]));
alpha4_4.writeDigitAscii(2, toupper(newpostfix[index_post][6]));
alpha4_4.writeDigitRaw(3, 0x0);
alpha4_5.writeDigitRaw(0, 0x0);
alpha4_5.writeDigitRaw(1, 0x0);
alpha4_5.writeDigitRaw(2, 0x0);
alpha4_5.writeDigitRaw(3, 0x0);
alpha4_6.writeDigitRaw(0, 0x0);
alpha4_6.writeDigitRaw(1, 0x0);
alpha4_6.writeDigitRaw(2, 0x0);
alpha4_6.writeDigitRaw(3, 0x0);
break;



case 8:
alpha4_3.writeDigitAscii(0, toupper(newpostfix[index_post][0]));
alpha4_3.writeDigitAscii(1, toupper(newpostfix[index_post][1]));
alpha4_3.writeDigitAscii(2, toupper(newpostfix[index_post][2]));
alpha4_3.writeDigitAscii(3, toupper(newpostfix[index_post][3]));
alpha4_4.writeDigitAscii(0, toupper(newpostfix[index_post][4]));
alpha4_4.writeDigitAscii(1, toupper(newpostfix[index_post][5]));
alpha4_4.writeDigitAscii(2, toupper(newpostfix[index_post][6]));
alpha4_4.writeDigitAscii(3, toupper(newpostfix[index_post][7]));
alpha4_5.writeDigitRaw(0, 0x0);
alpha4_5.writeDigitRaw(1, 0x0);
alpha4_5.writeDigitRaw(2, 0x0);
alpha4_5.writeDigitRaw(3, 0x0);
alpha4_6.writeDigitRaw(0, 0x0);
alpha4_6.writeDigitRaw(1, 0x0);
alpha4_6.writeDigitRaw(2, 0x0);
alpha4_6.writeDigitRaw(3, 0x0);
break;





case 9:
alpha4_3.writeDigitAscii(0, toupper(newpostfix[index_post][0]));
alpha4_3.writeDigitAscii(1, toupper(newpostfix[index_post][1]));
alpha4_3.writeDigitAscii(2, toupper(newpostfix[index_post][2]));
alpha4_3.writeDigitAscii(3, toupper(newpostfix[index_post][3]));
alpha4_4.writeDigitAscii(0, toupper(newpostfix[index_post][4]));
alpha4_4.writeDigitAscii(1, toupper(newpostfix[index_post][5]));
alpha4_4.writeDigitAscii(2, toupper(newpostfix[index_post][6]));
alpha4_4.writeDigitAscii(3, toupper(newpostfix[index_post][7]));
alpha4_5.writeDigitAscii(0, toupper(newpostfix[index_post][8]));
alpha4_5.writeDigitRaw(1, 0x0);
alpha4_5.writeDigitRaw(2, 0x0);
alpha4_5.writeDigitRaw(3, 0x0);
alpha4_6.writeDigitRaw(0, 0x0);
alpha4_6.writeDigitRaw(1, 0x0);
alpha4_6.writeDigitRaw(2, 0x0);
alpha4_6.writeDigitRaw(3, 0x0);
break;





case 10:
alpha4_3.writeDigitAscii(0, toupper(newpostfix[index_post][0]));
alpha4_3.writeDigitAscii(1, toupper(newpostfix[index_post][1]));
alpha4_3.writeDigitAscii(2, toupper(newpostfix[index_post][2]));
alpha4_3.writeDigitAscii(3, toupper(newpostfix[index_post][3]));
alpha4_4.writeDigitAscii(0, toupper(newpostfix[index_post][4]));
alpha4_4.writeDigitAscii(1, toupper(newpostfix[index_post][5]));
alpha4_4.writeDigitAscii(2, toupper(newpostfix[index_post][6]));
alpha4_4.writeDigitAscii(3, toupper(newpostfix[index_post][7]));
alpha4_5.writeDigitAscii(0, toupper(newpostfix[index_post][8]));
alpha4_5.writeDigitAscii(1, toupper(newpostfix[index_post][9]));
alpha4_5.writeDigitRaw(2, 0x0);
alpha4_5.writeDigitRaw(3, 0x0);
alpha4_6.writeDigitRaw(0, 0x0);
alpha4_6.writeDigitRaw(1, 0x0);
alpha4_6.writeDigitRaw(2, 0x0);
alpha4_6.writeDigitRaw(3, 0x0);
break;





case 11:
alpha4_3.writeDigitAscii(0, toupper(newpostfix[index_post][0]));
alpha4_3.writeDigitAscii(1, toupper(newpostfix[index_post][1]));
alpha4_3.writeDigitAscii(2, toupper(newpostfix[index_post][2]));
alpha4_3.writeDigitAscii(3, toupper(newpostfix[index_post][3]));
alpha4_4.writeDigitAscii(0, toupper(newpostfix[index_post][4]));
alpha4_4.writeDigitAscii(1, toupper(newpostfix[index_post][5]));
alpha4_4.writeDigitAscii(2, toupper(newpostfix[index_post][6]));
alpha4_4.writeDigitAscii(3, toupper(newpostfix[index_post][7]));
alpha4_5.writeDigitAscii(0, toupper(newpostfix[index_post][8]));
alpha4_5.writeDigitAscii(1, toupper(newpostfix[index_post][9]));
alpha4_5.writeDigitAscii(2, toupper(newpostfix[index_post][10]));
alpha4_5.writeDigitRaw(3, 0x0);
alpha4_6.writeDigitRaw(0, 0x0);
alpha4_6.writeDigitRaw(1, 0x0);
alpha4_6.writeDigitRaw(2, 0x0);
alpha4_6.writeDigitRaw(3, 0x0);
break;





case 12:
alpha4_3.writeDigitAscii(0, toupper(newpostfix[index_post][0]));
alpha4_3.writeDigitAscii(1, toupper(newpostfix[index_post][1]));
alpha4_3.writeDigitAscii(2, toupper(newpostfix[index_post][2]));
alpha4_3.writeDigitAscii(3, toupper(newpostfix[index_post][3]));
alpha4_4.writeDigitAscii(0, toupper(newpostfix[index_post][4]));
alpha4_4.writeDigitAscii(1, toupper(newpostfix[index_post][5]));
alpha4_4.writeDigitAscii(2, toupper(newpostfix[index_post][6]));
alpha4_4.writeDigitAscii(3, toupper(newpostfix[index_post][7]));
alpha4_5.writeDigitAscii(0, toupper(newpostfix[index_post][8]));
alpha4_5.writeDigitAscii(1, toupper(newpostfix[index_post][9]));
alpha4_5.writeDigitAscii(2, toupper(newpostfix[index_post][10]));
alpha4_5.writeDigitAscii(3, toupper(newpostfix[index_post][11]));
alpha4_6.writeDigitRaw(0, 0x0);
alpha4_6.writeDigitRaw(1, 0x0);
alpha4_6.writeDigitRaw(2, 0x0);
alpha4_6.writeDigitRaw(3, 0x0);
break;


case 13:
alpha4_3.writeDigitAscii(0, toupper(newpostfix[index_post][0]));
alpha4_3.writeDigitAscii(1, toupper(newpostfix[index_post][1]));
alpha4_3.writeDigitAscii(2, toupper(newpostfix[index_post][2]));
alpha4_3.writeDigitAscii(3, toupper(newpostfix[index_post][3]));
alpha4_4.writeDigitAscii(0, toupper(newpostfix[index_post][4]));
alpha4_4.writeDigitAscii(1, toupper(newpostfix[index_post][5]));
alpha4_4.writeDigitAscii(2, toupper(newpostfix[index_post][6]));
alpha4_4.writeDigitAscii(3, toupper(newpostfix[index_post][7]));
alpha4_5.writeDigitAscii(0, toupper(newpostfix[index_post][8]));
alpha4_5.writeDigitAscii(1, toupper(newpostfix[index_post][9]));
alpha4_5.writeDigitAscii(2, toupper(newpostfix[index_post][10]));
alpha4_5.writeDigitAscii(3, toupper(newpostfix[index_post][11]));
alpha4_6.writeDigitAscii(0, toupper(newpostfix[index_post][12]));
alpha4_6.writeDigitRaw(1, 0x0);
alpha4_6.writeDigitRaw(2, 0x0);
alpha4_6.writeDigitRaw(3, 0x0);
break;



case 14:
alpha4_3.writeDigitAscii(0, toupper(newpostfix[index_post][0]));
alpha4_3.writeDigitAscii(1, toupper(newpostfix[index_post][1]));
alpha4_3.writeDigitAscii(2, toupper(newpostfix[index_post][2]));
alpha4_3.writeDigitAscii(3, toupper(newpostfix[index_post][3]));
alpha4_4.writeDigitAscii(0, toupper(newpostfix[index_post][4]));
alpha4_4.writeDigitAscii(1, toupper(newpostfix[index_post][5]));
alpha4_4.writeDigitAscii(2, toupper(newpostfix[index_post][6]));
alpha4_4.writeDigitAscii(3, toupper(newpostfix[index_post][7]));
alpha4_5.writeDigitAscii(0, toupper(newpostfix[index_post][8]));
alpha4_5.writeDigitAscii(1, toupper(newpostfix[index_post][9]));
alpha4_5.writeDigitAscii(2, toupper(newpostfix[index_post][10]));
alpha4_5.writeDigitAscii(3, toupper(newpostfix[index_post][11]));
alpha4_6.writeDigitAscii(0, toupper(newpostfix[index_post][12]));
alpha4_6.writeDigitAscii(1, toupper(newpostfix[index_post][13]));
alpha4_6.writeDigitRaw(2, 0x0);
alpha4_6.writeDigitRaw(3, 0x0);
break;



case 15:
alpha4_3.writeDigitAscii(0, toupper(newpostfix[index_post][0]));
alpha4_3.writeDigitAscii(1, toupper(newpostfix[index_post][1]));
alpha4_3.writeDigitAscii(2, toupper(newpostfix[index_post][2]));
alpha4_3.writeDigitAscii(3, toupper(newpostfix[index_post][3]));
alpha4_4.writeDigitAscii(0, toupper(newpostfix[index_post][4]));
alpha4_4.writeDigitAscii(1, toupper(newpostfix[index_post][5]));
alpha4_4.writeDigitAscii(2, toupper(newpostfix[index_post][6]));
alpha4_4.writeDigitAscii(3, toupper(newpostfix[index_post][7]));
alpha4_5.writeDigitAscii(0, toupper(newpostfix[index_post][8]));
alpha4_5.writeDigitAscii(1, toupper(newpostfix[index_post][9]));
alpha4_5.writeDigitAscii(2, toupper(newpostfix[index_post][10]));
alpha4_5.writeDigitAscii(3, toupper(newpostfix[index_post][11]));
alpha4_6.writeDigitAscii(0, toupper(newpostfix[index_post][12]));
alpha4_6.writeDigitAscii(1, toupper(newpostfix[index_post][13]));
alpha4_6.writeDigitAscii(2, toupper(newpostfix[index_post][14]));
alpha4_6.writeDigitRaw(3, 0x0);
break;




case 16:
alpha4_3.writeDigitAscii(0, toupper(newpostfix[index_post][0]));
alpha4_3.writeDigitAscii(1, toupper(newpostfix[index_post][1]));
alpha4_3.writeDigitAscii(2, toupper(newpostfix[index_post][2]));
alpha4_3.writeDigitAscii(3, toupper(newpostfix[index_post][3]));
alpha4_4.writeDigitAscii(0, toupper(newpostfix[index_post][4]));
alpha4_4.writeDigitAscii(1, toupper(newpostfix[index_post][5]));
alpha4_4.writeDigitAscii(2, toupper(newpostfix[index_post][6]));
alpha4_4.writeDigitAscii(3, toupper(newpostfix[index_post][7]));
alpha4_5.writeDigitAscii(0, toupper(newpostfix[index_post][8]));
alpha4_5.writeDigitAscii(1, toupper(newpostfix[index_post][9]));
alpha4_5.writeDigitAscii(2, toupper(newpostfix[index_post][10]));
alpha4_5.writeDigitAscii(3, toupper(newpostfix[index_post][11]));
alpha4_6.writeDigitAscii(0, toupper(newpostfix[index_post][12]));
alpha4_6.writeDigitAscii(1, toupper(newpostfix[index_post][13]));
alpha4_6.writeDigitAscii(2, toupper(newpostfix[index_post][14]));
alpha4_6.writeDigitAscii(3, toupper(newpostfix[index_post][15]));
break;

















}


Serial.print(limit_post);
Serial.print(" ");
Serial.print(newprefix[index_pre]);

Serial.println(newpostfix[index_post]);
    alpha4_1.writeDisplay();
    alpha4_2.writeDisplay();
    alpha4_3.writeDisplay();
    alpha4_4.writeDisplay();
    alpha4_5.writeDisplay();
    alpha4_6.writeDisplay();

    delay(3000);




}
