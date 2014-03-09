/*
Programa que gera solos de arduino de acordo com o acorde enviado via serial...
O sinal é gerado no pino 8 com a função tone().
Conexões:
pino GND -> GND do falante.
pino 8   -> Positivo do falante.
*/

String valor_recebido = "AMajor";
boolean onoff = false;

void setup(){
  Serial.begin(9600);
}

void loop(){
    switch(valor_recebido){
    case "AMajor":
        break;
    case "A#Major":
        break;
    case "BMajor":
        break;
    case "CMajor":
        break;
    case "C#Major":
        break;
    case "DMajor":
        break;
    case "D#Major":
        break;
    case "EMajor":
        break;
    case "FMajor":
        break;
    case "F#Major":
        break;
    case "GMajor":
        break;
    case "G#Major":
        break;
    case "True":
        break;
    case "False":
        break;
    default:
        break;
    }
    delay(100);
}

void serialEvent (){
    while (Serial.available()) {
        char inChar = (char)Serial.read();
            valor_recebido += inChar;
    }

    if (valor_recebido == "onoff") {
        onoff = !onoff;
    }
}
