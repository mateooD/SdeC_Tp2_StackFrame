#include <WiFi.h>
#include <WebServer.h>
#include <ArduinoJson.h>


const char* ssid = "ssid"; // Reemplaza con tu SSID de red Wi-Fi
const char* password = "password"; // Reemplaza con tu contraseña de red Wi-Fi
// Reemplaza con tu SSID y contraseña de red Wi-Fi

WebServer server(80);

// Variables para guardar los últimos datos
String ultimoPais = "N/A";
float ultimoGini = 0.0;
int ultimoAnio = 0;


void handleRoot() {
  server.send(200, "text/plain", "Servidor ESP32 OK");
}

// Función para manejar la solicitud de datos

void loop() {
  server.handleClient();
}

void handlePostDatos() {
  if (server.hasArg("plain")) {
    String body = server.arg("plain");

    DynamicJsonDocument doc(256);
    DeserializationError error = deserializeJson(doc, body);

    if (error) {
      server.send(400, "text/plain", "JSON inválido");
      return;
    }

    // Leer los campos
    ultimoPais = doc["pais"].as<String>();
    ultimoGini = doc["gini"].as<float>();
    ultimoAnio = doc["anio"].as<int>();

    Serial.printf("✅ Datos recibidos: País = %s, GINI = %.2f, Año = %d\n", ultimoPais.c_str(), ultimoGini, ultimoAnio);

    server.send(200, "text/plain", "✅ Datos recibidos correctamente");
  } else {
    server.send(400, "text/plain", "Falta cuerpo en el POST");
  }
}


void handleVer() {
  String html = "<html><head>";
  html += "<style>"
          "body { font-family: Arial, sans-serif; background-color: #f4f4f9; margin: 0; padding: 20px; }"
          "h2 { color: #333; }"
          "table { width: 100%; border-collapse: collapse; margin-top: 20px; }"
          "th, td { padding: 8px 12px; text-align: left; border-bottom: 1px solid #ddd; }"
          "th { background-color: #4CAF50; color: white; }"
          "tr:nth-child(even) { background-color: #f2f2f2; }"
          "tr:hover { background-color: #ddd; }"
          "button { padding: 10px 15px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer; }"
          "button:hover { background-color: #45a049; }"
          "</style>";
  html += "</head><body>";

  html += "<h2>Ultimos Datos Recibidos</h2>";

  // Si los datos existen, mostrarlos en una tabla
  if (ultimoPais != "N/A") {
    html += "<table>";
    html += "<tr><th>Pais</th><th>Indice de Gini</th></tr>";
    html += "<tr><td>" + ultimoPais + "</td><td>" + String(ultimoGini, 2) + "</td></tr>";
    html += "</table>";
  } else {
    html += "<p>No se han recibido datos aún.</p>";
  }


  server.send(200, "text/html", html);
}
// Función para manejar la solicitud de datos

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando...");
  }

  Serial.println("Conectado:");
  Serial.println(WiFi.localIP());

  server.on("/", handleRoot);
  server.on("/datos", HTTP_POST, handlePostDatos);
  server.on("/ver", handleVer);

  server.begin();
}

void loop() {
  server.handleClient();
}