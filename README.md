Toutes les VMs en UTC+1 : Europe/Paris

Prometheus :  Récupère automatiquement la dernière version stable ("Latest") sur le Git Prometheus.
              Scrape automatiquement : Prometheus, Apache2_exporter, apache_node_exporter, nginx_exporter, nginx_node_exporter
              
Nginx :       Envoi des logs à Graylog en Syslog UDP sur les ports 5514 (Syslogs), 5515 (Nginx_Access), 5516 (Nginx_Errors)

Grafana:      Configuration de la datasource Prometheus
              ## Reste à configurer l'intégration d'Opensearch pour récupérer les logs

Graylog v5.2, OpenSearch v2 Latest, MongoDB v6 Latest:
              Création des certificats et clés privée & publique automatiquement
              ## Reste à automatiser l'ajout d'inputs

Apache2 :    Envoi des logs à Graylog en GELF UDP sur le port 5510
