#!/bin/bash

GRAFANA_CONFIG_FILE="/etc/grafana/grafana.ini"
GRAFANA_SERVICE_NAME="grafana-server"

# Vérifier si le fichier de configuration existe
if [ -f "$GRAFANA_CONFIG_FILE" ]; then
    # Modifier la configuration Grafana
    cat <<EOL >> "$GRAFANA_CONFIG_FILE"
[paths]
data = /var/lib/grafana
temp_data_lifetime = 24h
logs = /var/log/grafana
plugins = /var/lib/grafana/plugins
provisioning = conf/provisioning

[server]
protocol = http
;min_tls_version = ""
http_addr = 192.168.33.12
http_port = 3000
domain = 192.168.33.12
enforce_domain = false
EOL

    # Redémarrer le service Grafana pour appliquer les changements
    systemctl restart "$GRAFANA_SERVICE_NAME"

    echo "Configuration de Grafana mise à jour. Le service Grafana a été redémarré."
else
    echo "Le fichier de configuration de Grafana ($GRAFANA_CONFIG_FILE) n'existe pas. Veuillez vérifier le chemin du fichier."
fi