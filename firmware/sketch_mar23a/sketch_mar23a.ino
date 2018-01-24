void setup() {
  Serial.begin(9600);
  // define as portas como saida
  pinMode(13, OUTPUT);
 
 
}
void loop() {
  // testa se a porta serial está disponível
  if (Serial.available() > 0) {
    // le os dados da porta serial armazena na variavel 'entrada'
    char entrada = Serial.read();
    switch (entrada) {
    case 'A':
      digitalWrite(13, HIGH); //acende led_A
      break;
    case 'D':
      digitalWrite(13, LOW); // apaga led_A
      break;

    }
  }
}
